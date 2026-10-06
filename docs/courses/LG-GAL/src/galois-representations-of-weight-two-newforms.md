# Galois representations of weight-two newforms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Jacobian of a modular curve contains the Hecke spectra of many cusp forms. To attach a representation to one newform, we take a quotient that retains its Galois conjugates. Its dimension is the degree of the coefficient field, and its Tate module has rank two over that field after completion. A polarization then supplies the determinant needed to turn the Eichler–Shimura annihilating relation into a characteristic polynomial.

Throughout, \(f\) is a **normalized newform of exact level \(N\) in \(S_2(\Gamma_0(N))\), with trivial character**:
\[
f=\sum_{n\ge1}a_nq^n,\qquad a_1=1,\qquad
K=K_f=\mathbf Q(a_n:n\ge1),\qquad d=[K: \mathbf Q].
\tag{1}
\]
The coefficient field is a number field by the modular-forms prerequisite. We use covariant Tate modules and arithmetic Frobenius \(\mathrm{Fr}_p\). Thus the cyclotomic character satisfies \(\chi_\ell(\mathrm{Fr}_p)=p\) for \(p\ne\ell\). Geometric Frobenius is its inverse; local reciprocity, when used, sends a uniformizer to geometric Frobenius. Our earlier Weil–Deligne convention remains \(r(w)Nr(w)^{-1}=|w|N\). No bad-prime local–global correspondence is used in the proofs below.

## 1. The Jacobian, the Hecke algebra and the coefficient field

Put \(X=X_0(N)\), \(J=J_0(N)\), and \(S=S_2(\Gamma_0(N))\). Abel–Jacobi uniformization identifies
\[
J(\mathbf C)\simeq S^\vee/\Lambda,\qquad
\Lambda=H_1(X(\mathbf C),\mathbf Z),
\tag{2}
\]
where a cycle maps to the functional \(\omega\mapsto\int_\gamma\omega\), and the identification of cusp forms with differentials is from the preceding lesson. The period identification is proved in Lemma 2.0 below. The lattice has rank \(2\dim S\). An algebraic endomorphism of \(J\) acts on its tangent space \(S^\vee\) and preserves \(\Lambda\).

Let \(\mathbf T\subset\operatorname{End}_{\mathbf Q}(J)\) be the integral Hecke algebra, including the operators at primes dividing \(N\). Its action on differentials is the classical Hecke action. It is commutative, and the newform defines a character
\[
\lambda_f: \mathbf T\longrightarrow K,\qquad T_n\longmapsto a_n.
\tag{3}
\]
The usual Hecke recursion expresses the \(T_n\) in the prime operators; at a level prime the operator is often called \(U_p\). Since \(\mathbf T\) acts faithfully on the integral homology lattice, it is a subgroup of a finite-rank free abelian group and is itself finite free over \(\mathbf Z\). Consequently its eigenvalues are algebraic integers. Its image under (3) is an order in \(K\): it is a finite \(\mathbf Z\)-module, is contained in the ring of integers, and spans \(K\) over \(\mathbf Q\). An order need not be the full ring of integers.

We first close the particular newform-theory assertions that are needed here. We use the actually written prime-space, adjoint and cusp calculations in *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, §§2–4; the old/new stability proof in *Oldforms, newforms and the theory of Atkin, Lehner and Li*, Theorem 2.3; and that lesson's Appendix A, Theorem A.1, which proves the one-prime Fourier-support lemma at every level. Only their trivial-character weight-two specializations enter. The following additional proof supplies the auxiliary finite set and the two previously missing lowering formulas. Its free primary reading is Li's original article, printed pp. 286–295.

### 1A. Traces, Fourier support and exact multiplicity

Write \(S(M)=S_2(\Gamma_0(M))\), \(V_ph(z)=h(pz)\), and
\[
E_ph(z)=\frac1p\sum_{a=0}^{p-1}h((z+a)/p)
=\sum_{n\ge1}a_{pn}(h)q^n.
\tag{1A}
\]
We use the determinant-normalized weight-two slash
\(h\Vert A=(\det A)(cz+d)^{-2}h(Az)\); scalar matrices act trivially.

**Lemma 1.0a (the lowering trace).** If \(p^2\mid M\), then \(E_p:S(M)\to S(M/p)\). If \(p\Vert M\), choose
\[
A_p^M=\begin{pmatrix}px&y\\Mz&p\end{pmatrix},
\qquad px-(M/p)yz=1,
\qquad W_p^Mh=h\Vert A_p^M.
\]
Then \(W_p^M\) preserves \(S(M)\), has square one, and
\[
Q_p^M=E_p+W_p^M:S(M)\longrightarrow S(M/p),
\qquad Q_p^MV_ph=(1+p^{-1})h\quad(h\in S(M/p)).
\tag{1B}
\]
For \(t\ne p\) dividing \(M\), the coherent choices of these matrices give
\(Q_p^MV_t=V_tQ_p^{M/t}\). The analogous identity for \(E_p\) holds directly on coefficients.

*Proof.* Put \(L=M/p\) and \(\delta_a=\left(\begin{smallmatrix}1&a\\0&p\end{smallmatrix}\right)\). For \(\gamma=\left(\begin{smallmatrix}\alpha&\beta\\c&d\end{smallmatrix}\right)\in\Gamma_0(L)\), if \(\alpha+ac\ne0\pmod p\), choose
\(b\equiv(\beta+ad)/(\alpha+ac)\pmod p\). Multiplication gives
\[
\delta_a\gamma\delta_b^{-1}
=\begin{pmatrix}
\alpha+ac&(\beta+ad-b(\alpha+ac))/p\\
pc&d-bc
\end{pmatrix}\in\Gamma_0(M).
\tag{1C}
\]
When \(p^2\mid M\), \(c\equiv0\pmod p\), so the exceptional case never occurs, and \(a\mapsto b\) permutes all residues. Summing proves the transformation law of \(E_ph\) at level \(L\).

When \(p\Vert M\), \(p\nmid L\). Add the representative \(A_p^M\). In the exceptional case \(\alpha+ac\equiv0\pmod p\), direct multiplication of \(\delta_a\gamma(A_p^M)^{-1}\) gives integral entries, determinant one and lower-left entry
\(p(c-Lzd)\), divisible by \(M\). Thus it belongs to \(\Gamma_0(M)\). For \(A_p^M\gamma\), the same division by \(\delta_b\) applies when \(c\not\equiv0\pmod p\); when \(c\equiv0\pmod p\), \(\gamma\in\Gamma_0(M)\), and conjugation by \(A_p^M\) preserves that group. This last assertion follows by multiplying the three matrices: every potentially divided numerator is divisible by \(p\), and the resulting lower-left entry is divisible by \(M\). The inverse conjugation has the same property.

The \(p+1\) left cosets represented by \(\delta_a,A_p^M\) are distinct. Modulo \(p\), their nonzero row lines are \((1,a)\) and \((0,1)\); a left factor in \(\Gamma_0(M)\) preserves those lines. Right multiplication by \(\Gamma_0(L)\) consequently permutes the cosets. Their slash sum is exactly \(E_p+W_p^M\), proving its lower-level transformation law. Rational slash operators preserve holomorphy and cusp vanishing by the explicit cusp-scaling calculation in the earlier Hecke lesson, §2 immediately after (2.3). Thus all these transformation statements concern cusp forms.

Different allowed matrices \(A_1,A_2\) have \(A_1A_2^{-1}\in\Gamma_0(M)\); the same multiplication proves this and the preceding normalization assertion. Hence \(W_p^M\) is independent of the choice on this trivial-character space. Also \((A_p^M)^2/p\in\Gamma_0(M)\), giving its square. It is unitary for Petersson: \(\operatorname{Im}(Az)=(\det A)\operatorname{Im}(z)/|cz+d|^2\), the hyperbolic area is invariant, and the normalized slash contributes exactly the corresponding weight-two factor. Since a normalizer carries a fundamental domain to another fundamental domain, changing variables preserves the inner product. For \(B_p=\operatorname{diag}(p,1)\),
\[
B_pA_p^M/p=\begin{pmatrix}px&y\\Lz&1\end{pmatrix}\in\Gamma_0(L).
\]
Since \(V_ph=p^{-1}h\Vert B_p\), this gives \(W_p^MV_ph=p^{-1}h\); \(E_pV_ph=h\) proves (1B). Finally
\(B_tA_p^MB_t^{-1}=\left(\begin{smallmatrix}px&ty\\ (M/t)z&p\end{smallmatrix}\right)\)
is a valid matrix at level \(M/t\). This proves the compatibility, with the choices coherent under conjugation. ∎

**Lemma 1.0b (Fourier support with an auxiliary set).** If \(h\in S(M)\) and \(a_n(h)=0\) whenever \((n,D)=1\), then
\[
h=\sum_{p\mid(M,D)}V_ph_p,
\qquad h_p\in S(M/p).
\tag{1D}
\]

*Proof.* Put \(A_p=1-V_pE_p\). On Fourier series it erases exactly the coefficients whose indices are divisible by \(p\); these operators commute. They send a cusp form of level \(L\) to a cusp form of level dividing \(Lp^2\). Indeed the good-prime formula gives \(E_p=T_p-pV_p\) when \(p\nmid L\), while the bad-prime formula preserves \(S(L)\) when \(p\mid L\); a dilation raises a level by at most \(p\).

First suppose all primes dividing \(D\) lie outside \(M\). Their product of annihilators kills \(h\). Order them as \(p_1,\ldots,p_r\). At the final step the preceding form \(H\) satisfies \(H=V_{p_r}E_{p_r}H\), while its level involves only \(M,p_1,\ldots,p_{r-1}\). The one-prime support theorem, earlier Appendix A, Theorem A.1, therefore gives \(H=0\). Repeat backwards to get \(h=0\). In general apply the annihilators for the primes dividing \((M,D)\) first. Their result has support only at the remaining primes, which still lie outside its raised level. The argument just given makes it zero. Consequently the original \(h\) has no coefficients prime to the product of the primes dividing \((M,D)\). We may therefore discard every other prime from \(D\).

Induct on the number of remaining primes. The empty case gives zero; the one-prime case is the actually proved earlier Theorem A.1. Choose a remaining \(p\). If \(p^2\mid M\), put \(h_p=E_ph\), which has level \(M/p\) by Lemma 1.0a. Then \(h-V_ph_p\) has support at the other primes, so induction finishes.

Suppose \(p\Vert M\), and order the other primes as \(q_1,\ldots,q_{t-1}\), putting \(q_t=p\). The coefficient identity \(\prod_iA_{q_i}h=0\) telescopes to
\[
h=\sum_{i=1}^tV_{q_i}\Phi_i,
\qquad \Phi_i=E_{q_i}A_{q_1}\cdots A_{q_{i-1}}h.
\tag{1E}
\]
Let \(M'=M\prod_{i<t}q_i^2\). For \(i<t\), \(\Phi_i\) has level dividing \(M\prod_{j<i}q_j^2\), and hence lies in \(S(M'/q_i)\). The last equality
\(V_p\Phi_t=A_{q_1}\cdots A_{q_{t-1}}h\)
and the one-prime support theorem place \(\Phi_t\) in \(S(M'/p)\).

The allowed matrix for \(W_p^{M'}\) is also an allowed matrix at level \(M\): absorb \(M'/M\) into its lower-left parameter. Its action on \(h\) is therefore \(W_p^Mh\). Apply \(Q_p^{M'}\) to (1E). Compatibility and (1B) give
\[
G=Q_p^Mh
=\sum_{i<t}V_{q_i}\Psi_i+(1+p^{-1})\Phi_t,
\qquad \Psi_i=Q_p^{M'/q_i}\Phi_i.
\]
Thus
\[
h-\frac{V_pG}{1+p^{-1}}
=\sum_{i<t}V_{q_i}
\left(\Phi_i-\frac{V_p\Psi_i}{1+p^{-1}}\right).
\]
The left side lies in \(S(M)\), because \(G\in S(M/p)\), and its Fourier support lies at the other primes. Induction decomposes it at the correct levels \(M/q_i\), irrespective of the auxiliary levels used in the displayed calculation. Taking \(h_p=G/(1+p^{-1})\) proves (1D). ∎

**Lemma 1.0c (exact-level multiplicity).** If \(f\) is normalized new of exact level \(N\), a vector \(g\in S(N)\) which has its prime eigenvalues outside a finite set is a scalar multiple of \(f\). Conjugating the coefficients by any embedding of \(K\) produces another normalized newform of exact level \(N\).

*Proof.* In a joint good-prime eigenspace of the new space, a vector with first coefficient zero has every coefficient prime to \(N\) zero, by the Hecke recurrences and \(a_1(T_nh)=a_n(h)\). Lemma 1.0b places it in the old space; positivity makes it zero. Thus each such eigenspace is one-dimensional and has a uniquely normalized generator. The bad operators preserve it, by the earlier stability proof, so this generator is a full eigenform.

The same-character cross-level uniqueness deduction is actually written in the earlier newform lesson, Theorem 4.4, §§4.2–4.4: its trace projection, removal of one degeneracy, and positive-norm contradiction prove equality of both the normalized form and its primitive level. Its formerly stated lowering and auxiliary-support premises are precisely Lemmas 1.0a–1.0b above. Its initially different-character Lemma 4.1, which invokes attached Galois representations, is unnecessary here and is not used. Induction on the level now decomposes the whole space into the spans \(V_dh\) of the normalized primitive forms \(h\), as in the written proof of that lesson's Theorem 4.5. Distinct primitive forms have distinct almost-all good-prime systems by its same-character Theorem 4.4. The system of our exact-level \(f\) consequently occurs in the full space at level \(N\) only for \(h=f,d=1\). This proves the assertion for \(g\), including the omission of extra primes.

For conjugation, the rational Fourier structure and rational Hecke matrices are proved in *Modular symbols and the algebraicity of Hecke eigenvalues*, Theorems 2.1, 3.1–3.2 and equations (3.5)–(3.8). Their construction is by finite-dimensional scalar extension; it never applies a discontinuous automorphism to an infinite analytic limit. Degeneracies preserve rational coefficients, so the old space is stable under an automorphism of \(\mathbf C\) and its inverse. A conjugate of \(f\) is therefore a normalized eigenform that is not old. In the decomposition just proved, its full good eigenspace must have primitive level \(N\); a smaller one would be entirely old. Thus it is new of that level. Any embedding of the number field extends to an automorphism of \(\mathbf C\): extend to an algebraic closure, choose a transcendence basis, and extend again over the resulting algebraic extension. This proves the stated embedding version. ∎

The earlier Hecke adjoint proof, Theorem 4.2, makes the commuting good operators self-adjoint in this trivial-character space. Lemma 1.0c, rather than an imported representation theorem, is the multiplicity statement used below.

**Corollary 1.0d (the bad Fourier coefficients).** For our normalized exact-level newform,
\[
p^2\mid N\ \Longrightarrow\ a_p=0,
\qquad p\Vert N\ \Longrightarrow\ a_p=\pm1.
\tag{1F}
\]

*Proof.* The coefficient operator \(E_p=U_p\) preserves the new space by the earlier old/new stability proof. When \(p^2\mid N\), Lemma 1.0a also puts its image in \(S(N/p)\), an old subspace. Positivity gives \(U_pf=0\), hence \(a_p=0\). When \(p\Vert N\), \(W_p^N\) preserves the old space and its orthogonal complement. Indeed it is unitary; for a prime \(t\ne p\), conjugating its matrix preserves the two degeneracy images from level \(N/t\), while at \(p\) it exchanges \(h\) and \(V_ph\) with factors \(p,p^{-1}\), as in (1B). Its inverse has the same property, so it preserves newness. Both \(U_pf\) and \(W_p^Nf\) are new, whereas their sum has level \(N/p\) by (1B). The sum is therefore zero. Since \(U_pf=a_pf\) and \((W_p^N)^2=1\), we obtain \(a_p^2=1\). ∎

**Lemma 1.1.** The good-prime coefficients generate \(K\):
\[
K=\mathbf Q(a_p:p\nmid N).
\tag{4}
\]
Moreover, \(K\) is totally real.

*Proof.* Let \(K_0\) be the field on the right. Two embeddings \(K\hookrightarrow\mathbf C\) with the same restriction to \(K_0\) give conjugate newforms with the same good-prime eigenvalues. Multiplicity one makes the forms scalar multiples; normalization makes them equal. All their coefficients agree, so the embeddings are equal.

If \([K:K_0]>1\), separability gives more than one extension to \(K\) of any fixed embedding of \(K_0\) into \(\mathbf C\), contrary to what was just proved. Hence \(K=K_0\). Every \(\sigma(a_p)\) is an eigenvalue of a self-adjoint good-prime operator and is real. Equation (4) then implies \(\sigma(K)\subset\mathbf R\) for every \(\sigma\). ∎

The exact-level hypothesis is essential. At a larger level, several degeneracy images of a lower-level form can share all its good-prime eigenvalues. Dimension statements for a newform quotient must account for that multiplicity.

## 2. The quotient and its dimension

**Lemma 2.0 (periods and the algebraic Jacobian).** For a smooth projective connected curve \(X/\mathbf C\), the algebraic Jacobian has the uniformization (2). It is natural for pullback and pushforward of finite curve maps.

*Proof.* On the analytic curve the exponential sequence is
\[
0\longrightarrow\mathbf Z\longrightarrow\mathcal O_X
\xrightarrow{u\mapsto\exp(2\pi iu)}\mathcal O_X^\times
\longrightarrow1.
\tag{2A}
\]
Exactness is local: a nonvanishing holomorphic function has a holomorphic logarithm on a small disk, and the kernel consists of locally constant integers. Global holomorphic functions are constant, and every nonzero complex constant has a logarithm. The induced map \(H^1(X,\mathbf Z)\to H^1(X,\mathcal O_X)\) is consequently injective. The connecting map for a line bundle is its integral first Chern class: the logarithms of its transition functions differ by integers on triple overlaps. A positive local parameter has winding number one, so this class in \(H^2(X,\mathbf Z)=\mathbf Z\) is its divisor degree. Exactness gives
\[
\operatorname{Pic}^0(X^{\rm an})
=H^1(X,\mathcal O_X)/H^1(X,\mathbf Z).
\tag{2B}
\]

Here the analytic cohomology and duality assertions have actual earlier proofs: *Dimension formulas for congruence subgroups*, Appendix A.1–A.7, proves the compact-curve cohomology, arbitrary-line-bundle duality and genus comparison; *Group cohomology of \(\Gamma\) and the Eichler–Shimura isomorphism*, Lemma 5.1, Proposition 5.2 and Theorem 5.3, gives the period decomposition for this modular curve. Under duality,
\[
H^1(X,\mathcal O_X)\longrightarrow H^0(X,\Omega^1)^\vee,
\qquad \eta\longmapsto\left(\omega\longmapsto\int_X\eta\wedge\omega\right).
\]
We choose the Poincaré-dual orientation \(\int_X\operatorname{PD}(\gamma)\wedge\omega=\int_\gamma\omega\). Thus the integer subgroup in (2B) is exactly the period lattice in (2), with rank \(2g\), rather than an unspecified commensurable lattice. Here is a direct verification that it is a full real lattice, also for an arbitrary compact curve. A real constant Čech cocycle is represented by a real closed one-form, using a smooth partition of unity; conversely its path integrals recover that cocycle modulo real coboundaries. The earlier Appendix A's Čech–Dolbeault comparison sends that form \(\alpha\) to its \((0,1)\)-part. If this part is \(\bar\partial u\), reality gives
\(\alpha=\bar\partial u+\partial\bar u\). Write \(u=a+ib\) with \(a,b\) real. Closedness implies \(\partial\bar\partial b=0\). Green–Stokes on the compact surface gives zero for the integral of \(\lvert db\rvert^2\), so \(b\) is constant and \(\alpha=da\) is exact. The real projection is therefore injective. Its two real dimensions are both \(2g\), by the integral handle basis and the earlier duality/genus proof, so it is an isomorphism. Projecting that basis gives a discrete cocompact lattice. For this modular curve the same assertion is the holomorphic and antiholomorphic decomposition in the group-cohomology lesson, Theorem 5.3.

The line-bundle comparison proved in the preceding lesson, Lemma 1.2, identifies the algebraic and analytic degree-zero line bundles. The algebraic Picard scheme and its Abel maps are constructed in *The Picard functor and the Picard scheme of a curve*, §§4–7, Theorems 6.2 and 7.2 and Proposition 7.1. To check that the point identification is an analytic isomorphism, choose \(d>2g-2\). That earlier proposition makes \(\operatorname{Sym}^dX\to\operatorname{Pic}^dX\) a surjective projective bundle, hence locally a holomorphic projection with local holomorphic sections. On a divisor \(\sum P_i-dP\), (2B) gives the period functional \(\omega\mapsto\sum_i\int_P^{P_i}\omega\), modulo periods. One can check this equality on logarithmic transition cocycles: cut a path from \(P\) to \(P_i\), trivialize on the two sides, and apply Stokes to the logarithm divided by \(2\pi i\), as prescribed in (2A). Its jump is one, and its duality value is precisely that path integral. Changing the path adds an integer period. This sum is holomorphic in the points, and the local sections of the Abel projective bundle make the induced bijection from \(J(\mathbf C)\) holomorphic. A bijective homomorphism of complex Lie groups is an isomorphism: its differential has zero kernel and equal dimensions, so the inverse function theorem gives a holomorphic inverse. This proves (2).

Finally pullback of transition cocycles and the finite-map norm act on (2A) by pullback and trace. The trace is the sum of values on the sheets and, at a ramification point, their local lengths. Substitution in path integrals identifies them with the respective homology maps. This proves naturality for the two legs of every Hecke correspondence. ∎

Define
\[
I_f=\ker\lambda_f,\qquad
B=I_fJ,\qquad A_f=J/B.
\tag{5}
\]
Here \(I_fJ\) means the abelian subvariety generated by the images \(t(J)\), \(t\in I_f\), rather than a set of points killed by \(I_f\). These are different constructions.

To make (5) concrete, choose finitely many additive generators \(t_1,\ldots,t_r\) of \(I_f\). Then \(B\) is the image of the homomorphism
\[
J^r\longrightarrow J,\qquad
(x_1,\ldots,x_r)\longmapsto\sum_i t_i(x_i).
\tag{6}
\]
The image is closed by properness and is geometrically connected as the image of \(J^r\). Its reduced structure is a subgroup: after algebraic closure every image point lifts, addition and inversion preserve those points, and a morphism from a reduced variety whose image lies in a closed reduced subvariety factors through it, since its defining equations vanish on all closed points. This applies to the product of the reduced images as well. These identities descend to \(\mathbf Q\). The actually proved closed-subgroup theorem in *Abelian varieties*, Theorem 8.8, now makes this reduced connected subgroup an abelian subvariety. In particular it is smooth, and is defined over \(\mathbf Q\).

Here is the algebraic quotient construction, so its existence is also proved. Apply the actually written Poincaré reducibility theorem in that lesson, Theorem 6.20, over \(\mathbf Q\), to obtain a complement \(D\) for \(B\). Addition \(B\times D\to J\) is an isogeny, with finite schematic kernel
\(\{(-k,k):k\in H=B\cap D\}\). The finite-subgroup quotient theorem proved there, Proposition 6.3, constructs \(D/H\) over \(\mathbf Q\). The map \((b,d)\mapsto[d]\) is invariant under the displayed kernel. The isogeny is its kernel torsor, by Theorem 6.4; faithfully flat descent therefore gives a homomorphism
\[
q:J\longrightarrow D/H.
\tag{2C}
\]
Its kernel is \(B\) on every test scheme: locally lift a point of \(J\) to \((b,d)\); its image is zero exactly when \(d\in H\), in which case \(b+d\in B\). This description descends, so it is a schematic equality. The same lifting shows the quotient property. A homomorphism out of \(J\) killing \(B\) is determined by its restriction to \(D\), that restriction kills \(H\), and the finite quotient gives its unique factorization through (2C). We take this quotient as \(A_f\). No algebraization of an arbitrary analytic quotient is being assumed.

We prove the dimension, including the rational projection behind it. Let
\[
R=\mathbf Q[T_p:p\nmid N]\subset\operatorname{End}^0_{\mathbf Q}(J).
\tag{7}
\]
On \(S\), the commuting self-adjoint operators have a simultaneous eigenbasis. Thus \(R\) is a finite-dimensional commutative reduced \(\mathbf Q\)-algebra, hence a product of number fields. For completeness, reduction follows because a nilpotent element acts diagonally and must act as zero; the action on \(S\) is faithful. A finite-dimensional commutative algebra is Artinian; its radical is nilpotent, and its reduced quotient is a product of fields. In characteristic zero those fields are separable.

By Lemma 1.1, \(\lambda_f:R\to K\) is surjective. Let \(e=e_f\in R\) be the identity of this field factor and zero on the other factors:
\[
e^2=e,\qquad eR\simeq K.
\tag{8}
\]
After extension to \(\mathbf C\), its factor splits into the \(d\) characters \(\sigma\circ\lambda_f\). The eigenspace in \(S\) for each such good-prime character is exactly \(\mathbf C f^\sigma\), by multiplicity one. Therefore
\[
eS=\bigoplus_{\sigma:K\hookrightarrow\mathbf C}\mathbf C f^\sigma,
\qquad \dim_{\mathbf C}eS=d.
\tag{9}
\]
Every \(t\in I_f\) acts as zero on these lines, so \(et=0\). The equality on differentials implies the equality in \(\operatorname{End}^0(J)\): over \(\mathbf C\), a homomorphism of complex tori is determined by its tangent map. Also \(1-e\in I_f\otimes\mathbf Q\), since its value under \(\lambda_f\) is zero. Thus, on the tangent space \(L=S^\vee\),
\[
I_fL=(1-e)L.
\tag{10}
\]
The first inclusion uses \(eI_f=0\). The reverse uses \(1-e\in I_f\otimes\mathbf Q\); denominators do not change the span of tangent images.

**Theorem 2.1 (dimension).** The quotient \(A_f\) has
\[
\dim A_f=d=[K: \mathbf Q],
\tag{11}
\]
and its Hecke action factors through \(K\) in \(\operatorname{End}^0_{\mathbf Q}(A_f)\).

*Proof.* In characteristic zero, the tangent space of the image (6) is the sum of the tangent images. Hence (10) gives
\[
\operatorname{Lie}(A_f)_{\mathbf C}=L/I_fL\simeq eL.
\]
Its dimension is \(d\) by (9), proving (11). The ideal \(I_f\) acts trivially on the quotient, and \((\mathbf T/I_f)\otimes\mathbf Q=K\). This gives its \(K\)-action. It is unital; its kernel is an ideal of a field, and cannot contain \(1\), so it is injective. ∎

There is also an abelian subvariety representing the same factor up to isogeny. Choose an integer \(m>0\) with \(me\in\operatorname{End}(J)\), and let \(C_f=(me)J\). Its tangent space is \(eL\). The quotient map \(C_f\to A_f\) has invertible tangent map and is therefore an isogeny by *Abelian varieties*, Theorem 6.25. Its rational Tate-module isomorphism is proved there in Corollary 6.10, using the reverse isogeny of Theorem 6.7. Consequently,
\[
V_\ell A_f\simeq eV_\ell J
\tag{12}
\]
as Galois and Hecke modules. This statement concerns rational Tate modules: integral lattices can differ by finite index.

In (2), the analytic quotient lattice is the image of \(\Lambda\) in \(L/I_fL\). One should not identify it without qualification with \(\Lambda/I_f\Lambda\); that latter group can contain torsion. The tangent quotient and the actual image lattice suffice for the dimension argument.

## 3. Rank two over every coefficient completion

Let
\[
K_\ell=K\otimes_{\mathbf Q}\mathbf Q_\ell
\simeq\prod_{\lambda\mid\ell}K_\lambda.
\tag{13}
\]
This is a product of fields, even when \(\ell\) ramifies in \(K\). In particular it is not generally a field. The notation \(K_\lambda\) denotes the completion at a specified prime of \(K\).

**Theorem 3.1 (rank two).** There is an isomorphism of \(K_\ell\)-modules
\[
V_\ell A_f\simeq K_\ell^2.
\tag{14}
\]
Thus the factor \(V_{f,\lambda}\) cut out by the idempotent of \(K_\lambda\) has dimension two over \(K_\lambda\).

*Proof.* Put \(H=H_1(A_f(\mathbf C),\mathbf Q)\). The rational \(K\)-action on the abelian variety makes \(H\) a \(K\)-vector space. It is faithful, since a nonzero element of \(K\) has an inverse acting on \(H\), and \(1\) acts as the identity. Uniformization gives
\[
\dim_{\mathbf Q}H=2\dim A_f=2d,
\]
so \(\dim_K H=2\). Choose a \(K\)-basis \(h_1,h_2\).

For clarity, the comparison needed here has a direct proof on torsion. Write the complex uniformization of \(A_f\) as \(L_A/\Lambda_A\); it is actually proved for every complex abelian variety in *Abelian varieties*, Theorem 6.23, with homomorphism compatibility in Theorem 6.24. The map
\[
\Lambda_A/n\Lambda_A\longrightarrow A_f[n](\mathbf C),
\qquad v\longmapsto v/n\pmod{\Lambda_A}
\tag{3A}
\]
is bijective: the equation \(nx=0\) means a lift has \(nx\in\Lambda_A\), and its ambiguity is exactly \(n\Lambda_A\). All these torsion points are algebraic over \(\mathbf Q\), since they are points of the finite étale scheme \(A_f[n]\) defined over \(\mathbf Q\); the coordinate algebra splits over \(\overline{\mathbf Q}\) and has the same points after extending to \(\mathbf C\). A complex torus retracts onto its underlying real torus, whose handle loops identify \(H_1(A_f(\mathbf C),\mathbf Z)=\Lambda_A\). More explicitly, its universal cover is the contractible real vector space underlying \(L_A\), and a lattice basis gives the product of \(2d\) circles and their coordinate loops. Under (3A), multiplication by \(\ell\) on \(\ell^{r+1}\)-torsion is reduction \(\Lambda_A/\ell^{r+1}\Lambda_A\to\Lambda_A/\ell^r\Lambda_A\). Taking the inverse limit and tensoring with \(\mathbf Q_\ell\) identifies
\[
V_\ell A_f\simeq H\otimes_{\mathbf Q}\mathbf Q_\ell.
\tag{15}
\]
Every endomorphism lifts to its complex-linear map preserving the lattice, by the actually proved Theorem 6.24; thus (3A) and (15) respect it. Tensoring the \(K\)-basis therefore gives
\[
H\otimes_{\mathbf Q}\mathbf Q_\ell
\simeq (K\otimes_{\mathbf Q}\mathbf Q_\ell)^2.
\]
Projection to each field factor in (13) proves the final assertion. The comparison is an isomorphism of vector spaces with endomorphisms, not a Betti realization of the Galois action. ∎

The last tensor step is indispensable. A vector space of total \(\mathbf Q_\ell\)-dimension \(2d\) with an action of the product (13) need not have rank two on every factor; different factors could have different multiplicities. Here they arise by scalar extension from an actual two-dimensional \(K\)-space, which proves equal ranks.

The action of \(G_{\mathbf Q}\) commutes with the \(K\)-action, because its endomorphisms are defined over \(\mathbf Q\). It therefore gives continuous representations
\[
\rho_{f,\lambda}:G_{\mathbf Q}\longrightarrow
\operatorname{GL}_{K_\lambda}(V_{f,\lambda})
\simeq\operatorname{GL}_2(K_\lambda).
\tag{16}
\]
The final matrix representation depends on a choice of basis; its isomorphism class does not.

## 4. The coefficient-valued pairing and determinant

The degree-one curve cup pairing supplies the polarized Jacobian pairing
\[
b_J:V_\ell J\times V_\ell J\longrightarrow\mathbf Q_\ell(1),
\qquad b_J(gx,gy)=\chi_\ell(g)b_J(x,y).
\tag{17}
\]
Its construction and all properties just asserted are proved in the preceding lesson, Lemma 1.3: Kummer identifies \(T_\ell J\) with \(H^1_{\rm et}(X,\mathbf Z_\ell(1))\), and the perfect curve cup pairing is then twisted into (17). That proof binds to the actual earlier *Poincaré duality for curves*, Theorem 10.1, Corollary 10.2, Theorem 11.1 and §12. Graded commutativity gives alternation after tensoring with \(\mathbf Q_\ell\), including \(\ell=2\); the trace target's Galois action gives multiplier \(\chi_\ell\). The finite-trace projection formula in that earlier lesson, §§2 and 7, makes transposition of a curve correspondence its adjoint. Good-prime Hecke correspondences for trivial character are symmetric by the double-coset adjoint calculation of the earlier Hecke lesson, §4. Thus each \(T_p\) is self-adjoint for (17). The argument needs these proved pairing properties; it does not need to select a particular sign convention for a finite Weil pairing.

Every element of the commutative algebra \(R\), including \(e\), is consequently self-adjoint. Products remain self-adjoint here because their factors commute. The decomposition
\[
V_\ell J=eV_\ell J\oplus(1-e)V_\ell J
\tag{18}
\]
is orthogonal: \(b_J(ex,(1-e)y)=b_J(x,e(1-e)y)=0\). Nondegeneracy of \(b_J\) then makes its restriction to \(eV_\ell J\) nondegenerate. Transport it through (12) to a pairing \(b\) on \(V=V_\ell A_f\).

The field \(eR=K\) consists of self-adjoint operators on this factor. Thus
\[
b(ax,y)=b(x,ay),\qquad a\in K_\ell.
\tag{19}
\]
This balancing property is the information needed to obtain a pairing on each \(K_\lambda\)-component. A total symplectic determinant on a \(2d\)-dimensional space would not, by itself, determine those component determinants.

**Lemma 4.1 (trace construction).** There is a unique nondegenerate alternating \(K_\ell\)-bilinear pairing
\[
B:V\times V\longrightarrow K_\ell\otimes_{\mathbf Q_\ell}\mathbf Q_\ell(1)
\tag{20}
\]
satisfying, for every \(a\in K_\ell\),
\[
\operatorname{Tr}_{K_\ell/\mathbf Q_\ell}\bigl(aB(x,y)\bigr)
=b(ax,y).
\tag{21}
\]
It obeys \(B(gx,gy)=\chi_\ell(g)B(x,y)\).

*Proof.* The trace pairing on a finite product of characteristic-zero fields is perfect. Indeed, for any nonzero element choose a component in which it is nonzero, and multiply by its inverse in that component and by zero in the others. The trace of the product is the nonzero degree of that field. Thus the trace pairing has zero radical; its equal finite dimensions make it perfect. It therefore represents the \(\mathbf Q_\ell\)-linear functional \(a\mapsto b(ax,y)\) by a unique element of the target in (20); the one-dimensional Tate twist does not affect this argument.

For \(c\in K_\ell\), (21) gives \(B(cx,y)=cB(x,y)\). Equation (19) gives \(B(x,cy)=cB(x,y)\). These identities follow by testing against every \(a\) and using perfectness of the trace pairing. Also
\[
b(ax,x)=b(x,ax)=-b(ax,x)=0
\]
in characteristic zero. Thus (21) gives \(B(x,x)=0\), and \(B\) is alternating. If \(B(x,y)=0\) for every \(y\), then \(b(x,y)=0\) for every \(y\), so \(x=0\). On each field factor this gives the required nondegeneracy; distinct factors are orthogonal by bilinearity and their mutually annihilating idempotents.

Finally \(a\) commutes with \(g\), and (17) gives
\[
b(agx,gy)=\chi_\ell(g)b(ax,y).
\]
Testing again against all \(a\) proves the asserted Galois multiplier. ∎

**Theorem 4.2 (determinant and oddness).** For every \(\lambda\mid\ell\),
\[
\det\rho_{f,\lambda}=\chi_\ell,
\tag{22}
\]
where the character on the right is viewed in \(K_\lambda^\times\). In particular the representation is odd.

*Proof.* Restrict \(B\) to the two-dimensional \(K_\lambda\)-space. Choose a basis \(u,v\) with \(B(u,v)\ne0\). For a matrix \(M\) on a two-dimensional space, alternating bilinearity gives
\[
B(Mu,Mv)=\det(M)B(u,v).
\]
For \(M=\rho_{f,\lambda}(g)\), Lemma 4.1 gives the same expression with multiplier \(\chi_\ell(g)\). Cancelling the nonzero value proves (22) for every \(g\).

For complex conjugation \(c\), \(\chi_\ell(c)=-1\), hence \(\det\rho(c)=-1\). Since \(c^2=1\) and the coefficient field has characteristic zero, its two eigenvalues are \(1,-1\). This is oddness. ∎

No assertion that every endomorphism of \(A_f\) is self-adjoint was used. The argument applies to the specified commutative field generated by the good Hecke operators.

## 5. Frobenius traces and Euler factors

For \(p\nmid N\ell\), a good model of \(J\) makes inertia act trivially on \(V_\ell J\), by the preceding lesson's proved torsion-specialization Lemma 1.3, and hence on (12). Thus \(\rho_{f,\lambda}\) is unramified outside \(N\ell\), once the general good-model assertion of that lesson is supplied. This dependence on the actual model is retained in §8. The abelian Néron–Ogg–Shafarevich criterion is an actual earlier proof, *Néron models*, Lemmas 7.1–7.3 and Theorem 7.4, for arbitrary abelian dimension. Choose an auxiliary \(\ell\ne p\). Its rational unramified Tate module has an unramified integral lattice, since the integral module injects into its rationalization. That theorem then gives good reduction of \(A_f\). Its proof counts all invertible torsion in the special Néron fibre, rules out a positive-dimensional affine part by the growth bound \(\ell^{n(2g-d)}\), and proves properness of the model from its proper identity fibre; it applies to this quotient without an elliptic-dimension restriction.

**Theorem 5.1 (the weight-two Frobenius polynomial).** At every \(p\nmid N\ell\),
\[
\det\bigl(X-\rho_{f,\lambda}(\mathrm{Fr}_p)\bigr)
=X^2-a_pX+p.
\tag{23}
\]
In particular \(\operatorname{tr}\rho_{f,\lambda}(\mathrm{Fr}_p)=a_p\).

*Proof.* The Eichler–Shimura relation from the preceding lesson descends through the Hecke and Galois quotient:
\[
F^2-a_pF+pI=0,\qquad F=\rho_{f,\lambda}(\mathrm{Fr}_p).
\tag{24}
\]
Theorem 4.2 gives \(\det F=p\). Cayley–Hamilton on this two-dimensional space gives
\[
F^2-(\operatorname{tr}F)F+pI=0.
\]
Subtracting this identity from (24) yields
\((\operatorname{tr}F-a_p)F=0\). Frobenius is invertible, so its trace is \(a_p\), proving (23).

This also covers scalar Frobenius. If \(F=\alpha I\), its determinant is \(\alpha^2=p\), and (24) forces \(a_p=2\alpha\); both polynomials are \((X-\alpha)^2\). An annihilating quadratic without the determinant calculation would not justify this case. ∎

Taking the norm from the product algebra (13) gives the full Tate-module polynomial
\[
\det(X-\mathrm{Fr}_p\mid V_\ell A_f)
=\prod_{\sigma:K\hookrightarrow\overline{\mathbf Q}}
\bigl(X^2-\sigma(a_p)X+p\bigr),
\tag{25}
\]
with the conjugates embedded in \(\overline{\mathbf Q}_\ell\) for the computation. Thus
\[
\operatorname{tr}(\mathrm{Fr}_p\mid V_\ell A_f)
=\operatorname{Tr}_{K/\mathbf Q}(a_p),\qquad
\det(\mathrm{Fr}_p\mid V_\ell A_f)=p^d.
\tag{26}
\]
The right side of (25) is independent of \(\ell\) and is integral: each coefficient is a symmetric polynomial in conjugate algebraic integers, invariant under every automorphism of \(\overline{\mathbf Q}\). It is therefore a rational algebraic integer.

For one coefficient-field component the good-prime local factor is
\[
L_p(f,s)=\bigl(1-a_pp^{-s}+p^{1-2s}\bigr)^{-1}.
\tag{27}
\]
For the abelian variety over \(\mathbf Q\), take the product over \(\sigma\). A degree-\(d\) coefficient field produces \(d\) quadratic factors on the \(2d\)-dimensional \(\mathbf Q_\ell\)-space, rather than a single two-dimensional representation over \(\mathbf Q_\ell\).

## 6. Rational newforms and the full L-function

**Corollary 6.1.** If \(K=\mathbf Q\), then \(A_f\) is an elliptic curve over \(\mathbf Q\), and
\[
a_p(A_f)=a_p(f)\qquad(p\nmid N).
\tag{28}
\]

*Proof.* Theorem 2.1 gives dimension one. An abelian variety of dimension one, with its rational identity, is an elliptic curve. For any \(p\nmid N\), choose \(\ell\ne p\). It has good reduction there, and the elliptic Tate-module formula identifies its Frobenius trace with
\(p+1-\#A_f(\mathbf F_p)\). Equation (23) identifies the same trace with \(a_p(f)\). ∎

Consequently its good-prime Euler factors agree with those of \(f\). The required full statement retains every bad prime and every coefficient degree:

**Theorem 6.2 (full local factors and conductor).** For every normalized weight-two newform of exact level \(N\) and trivial character, the attached quotient satisfies
\[
L(A_f,s)=\prod_\sigma L(f^\sigma,s),\qquad
\operatorname{cond}(A_f)=N^d.
\tag{29}
\]
At \(p\mid N\), the coefficient-field Euler polynomial is \(1-a_pt\), including the constant polynomial one when \(a_p=0\). In particular, when \(K=\mathbf Q\), the elliptic curve's full Hasse–Weil L-function is \(L(f,s)\) and its geometric conductor is \(N\). The free primary source is Carayol's actual Numdam article, §§0.5–0.8, Theorem (A) and its Corollary, printed pp. 410–411. The theorem remains a required proof obligation in this draft; the following proves the local algebra and the passage to arbitrary coefficient degree, and states exactly the missing geometric step.

**Lemma 6.3 (what a rank-two local parameter can contribute).** Let \(D=(r,N_D)\) be a two-dimensional arithmetic local Weil–Deligne parameter in the convention of the earlier local-factor lessons, with determinant \(|\cdot|^{-1}\). If its conductor is one, it is an unramified quadratic twist of the arithmetic special block and its Euler polynomial is \(1-\epsilon t\), \(\epsilon=\pm1\). If its conductor is at least two, its Euler polynomial is one.

*Proof.* Here \(r(I)\) is finite. If \(N_D=0\), the invariant space is stable under the Weil group, since inertia is normal. If it had dimension one, averaging over the finite inertia image would give an inertia-stable complementary line. Its inertia character would be trivial, because the determinant is trivial on inertia and the fixed line's character is trivial. Thus inertia would act trivially on the whole space, contradicting dimension one. The invariant dimension is therefore zero or two. In the latter case the parameter is unramified and has conductor zero. In the former case its tame codimension is two and its nonnegative Swan term gives conductor at least two, while its Euler polynomial is one.

If \(N_D\ne0\), it has rank one, with image equal to its kernel. Choose a basis in which it sends the second vector to the first. The relation \(r(w)N_Dr(w)^{-1}=|w|N_D\) makes the two diagonal characters \(\eta|\cdot|,\eta\). Their product is \(|\cdot|^{-1}\), so \(\eta^2=|\cdot|^{-2}\). Write \(\eta=\chi|\cdot|^{-1}\); then \(\chi^2=1\). On inertia the two diagonal characters are both \(\chi\). A finite inertia image is semisimple by averaging, so it acts by this scalar character. The two Frobenius diagonal values have ratio \(|\Phi|\ne1\); hence a change of the second basis vector diagonalizes Frobenius while preserving the monodromy kernel. Inertia is scalar and every Weil element is an inertia element times a Frobenius power, so this diagonalizes the whole Weil action. Thus this is precisely the quadratic twist of the special block. In particular, the invariant monodromy kernel is one-dimensional exactly when \(\chi\) is unramified, and is zero otherwise.

In the unramified case the conductor formula proved in the monodromy lesson is \(0+2-1=1\); the character on the kernel is \(\chi\), so the Euler eigenvalue is \(\chi(\Phi)=\epsilon=\pm1\). In the ramified case the monodromy correction is zero, and the ramification-group sum is twice the rank-one character conductor, hence at least two; its invariant kernel is zero. These statements use the actual conductor additivity proof in the earlier conductor lesson, Theorem 2.1, and its nonnegative lower-group Swan sum. They prove every case of the lemma. ∎

*The deductions in Theorem 6.2 and its remaining proof.* At a bad prime use the **dual** of the covariant Tate parameter. The earlier elliptic-local lesson, equation (15), proves this normalization: geometric Frobenius on degree-one cohomology defines the arithmetic Euler factor. At good primes it has the same eigenvalues as arithmetic Frobenius on the covariant module, but taking invariants before dualizing at a monodromy prime would change its linear factor. Its determinant is \(|\cdot|^{-1}\), by Theorem 4.2.

The necessary local comparison has two exact conclusions for every \(\lambda\nmid p\):
\[
a(D_{f,\lambda,p})=v_p(N),\qquad
p\Vert N\ \Longrightarrow\
\chi_p(\Phi)=a_p(f)
\quad\text{in the block of Lemma 6.3}.
\tag{29A}
\]
These are not consequences of the good-prime quadratic. Once (29A) is proved, Lemma 6.3 and Corollary 1.0d give the complete bad coefficient-field factor: for \(p\Vert N\) it is \(1-a_pt\), and for \(p^2\mid N\) it is one and \(a_p=0\). This proves the stated factor shape without restricting the residue characteristic, excluding supercuspidal primes, or ignoring monodromy.

The passage to the whole abelian variety is also explicit. Write \(V_\ell A_f=\bigoplus_{\lambda\mid\ell}V_{f,\lambda}\). Inertia-invariant spaces and monodromy kernels commute with extension of scalars, since they are kernels of linear maps; for the smooth inertia part one can use the finite averaging projector. Their determinants on the \(\mathbf Q_\ell\)-space are therefore the products of all coefficient-field conjugate determinants. At good primes this is (25), and at bad primes it gives
\(\prod_{\sigma}(1-\sigma(a_p)t)\).
For conductors, restriction of scalars multiplies every ramification-group codimension and the monodromy correction by \([K_\lambda:\mathbf Q_\ell]\). Additivity, actually proved in the earlier conductor lesson, Theorem 2.1, consequently gives
\[
a_p(V_\ell A_f)=
\sum_{\lambda\mid\ell}[K_\lambda:\mathbf Q_\ell]\,v_p(N)
=d\,v_p(N).
\tag{29B}
\]
Multiplication over primes yields \(N^d\); equality of every local factor yields the full Euler product in (29), not only equality after deleting finitely many factors.

What remains is an actual proof of (29A). Carayol's freely accessible original proof constructs the local parameter from the special and vanishing-cycle cohomology of integral modular or Shimura curves; §§4–11 establish the ordinary local types and the nonzero special monodromy, and §12 treats primitive local types by cubic base change. I have inspected the actual proof, including its Picard–Lefschetz/dual-graph calculation in §§11.4–11.10 and its tetrahedral and octahedral descent in §§12.1–12.3. Those sections themselves require the integral special-fibre and local fundamental-representation constructions, vanishing-cycle comparison, and automorphic base-change theorem. No written earlier programme proof with this complete scope has been verified for these premises. A free copy of the article supplies reading material, not a proof provider in place of them. The interpretation as the geometric elliptic conductor also retains the general conductor-discriminant theorem's unresolved scope in the earlier elliptic-local lesson. Thus the theorem is retained in full, and its conductor and norm deductions are now proved, but its full proof is not yet closed.

## 7. Two examples

### Level 11 and an explicit isogeny

The preceding lesson identified \(X_0(11)\), with its rational cusp as origin, with
\[
E_1: \quad Y^2+Y=X^3-X^2-10X-20,
\tag{30}
\]
and its unique normalized cusp form with
\[
f_{11}=\eta(z)^2\eta(11z)^2
=q-2q^2-q^3+2q^4+q^5+2q^6-2q^7+\cdots.
\tag{31}
\]
The preceding lesson's Proposition 6.1 writes the analytic cubic-model proof from exact modular functions, using Weston's free conference notes, §4. Its descent to the arithmetic model still requires the rational Tate cusp in that lesson's general-model construction; its proof status is tracked there, rather than inferred from a few equal traces. The eta form and its one-dimensional cusp space have the actual earlier proof in the Hecke lesson, §6. Once that arithmetic identification is established, \(J_0(11)\) has dimension one and its entire differential space is this single rational eigenline. Faithfulness of the tangent action then gives \(I_f=0\), and \(A_f=J_0(11)\simeq E_1\).

Here is a complete point count through \(p=7\). For each \(p\), list the right side of (30) as \(X\) runs through the residues, and the number of \(Y\)-solutions for each entry:

| \(p\) | Right sides | Numbers of \(Y\)-solutions | \(\#E_1(\mathbf F_p)\) | \(a_p\) |
|---:|---|---|---:|---:|
| 2 | \(0,0\) | \(2,2\) | 5 | \(-2\) |
| 3 | \(1,0,0\) | \(0,2,2\) | 5 | \(-1\) |
| 5 | \(0,0,4,3,3\) | \(2,2,0,0,0\) | 5 | \(1\) |
| 7 | \(1,5,6,3,2,2,2\) | \(0,1,2,0,2,2,2\) | 10 | \(-2\) |

Modulo 7, \(Y^2+Y\) has values \(0,2,6,5,6,2,0\), so the right side 5 contributes one solution and the right sides 2 and 6 contribute two each. The trace \(a_7=-2\) also agrees with (31).

The earlier Tate-module example used
\[
E_0: \quad y^2+y=x^3-x^2.
\tag{32}
\]
It is not isomorphic to \(E_1\): their \(j\)-invariants are \(-4096/11\) and \(-496^3/11^5\). They are, however, isogenous over \(\mathbf Q\). We can verify this without identifying curves from a few matching traces.

Define
\[
\mathcal X(x)=x+\frac1{x^2}+\frac{2x-1}{(x-1)^2},\qquad
\mathcal Y(x,y)=\frac{(2y+1)\mathcal X'(x)-1}{2}.
\tag{33}
\]
Then \((x,y)\mapsto(\mathcal X,\mathcal Y)\) is a degree-five isogeny \(E_0\to E_1\). Here are the algebraic and degree checks. Put
\[
\begin{aligned}
D&=x^2(x-1)^2,\\
H&=x^5-2x^4+3x^3-2x+1,\\
M&=(x^3-4x^2+4x-2)(x^3+x^2+x-1).
\end{aligned}
\tag{34}
\]
Combining fractions and differentiating gives
\(\mathcal X=H/D\) and
\(\mathcal X'=M/[x^3(x-1)^3]\). The polynomial identity
\[
M^2(4x^3-4x^2+1)-D^3
=4(H^3-H^2D-10HD^2-20D^3)
\tag{35}
\]
is obtained by expanding the displayed polynomials. Since
\((2y+1)^2=4x^3-4x^2+1\) on \(E_0\), dividing (35) by \(4D^3\) gives
\[
\mathcal Y^2+\mathcal Y
=\mathcal X^3-\mathcal X^2-10\mathcal X-20.
\tag{36}
\]
This verifies the rational map to \(E_1\).

A rational map from a smooth projective curve to this projective elliptic curve extends across its missing points: at a discrete valuation ring scale the projective coordinates so that they are all integral and at least one is a unit; the equation then specializes and the generic map extends uniquely. This is also the valuative extension used in *Abelian varieties*, §2. At infinity, \(\mathcal X=x+O(x^{-1})\), so the map sends the origin to the origin. The actually proved origin-preserving rigidity theorem in that lesson, Corollary 2.3, makes it a group homomorphism. Its pointed-cubic and abelian group laws agree by that lesson's Example 9.12 and Corollary 2.3, exactly as checked in this course's Lesson 01, Lemma 3.3.

There are two points of \(E_0\) over \(x=0\) and two over \(x=1\), with \(y=0,-1\) in both cases. At all four points, \(x\) or \(x-1\) is a local parameter, because \(2y+1\ne0\). The function \(\mathcal X\) has pole order two at each. It also has pole order two at infinity and no other poles. Its total pole order is ten. The target coordinate \(X\) has pole divisor twice the origin, so the morphism has degree \(10/2=5\). It is separable in characteristic zero, with kernel
\[
\{O,(0,0),(0,-1),(1,0),(1,-1)\}.
\tag{37}
\]
Thus the isogeny and its degree are verified. Rational Tate modules of isogenous curves are isomorphic, so their \(a_p\) agree at every common good prime. Their integral 5-adic lattices need not be isomorphic; that finer issue belongs to the residual-representation lesson.

### Level 23 and real multiplication

The genus formula from modular-form theory gives
\[
g(X_0(23))
=1+\frac{24}{12}-\frac{0}{4}-\frac{0}{3}-\frac{2}{2}=2.
\tag{38}
\]
Here the index is \(23+1=24\), the two cusp classes give the last term, and there are no elliptic classes of orders two or three. For order two, \(-1\) is not a square modulo 23; for order three, the roots of \(x^2+x+1\) would give elements of order three in the group of order 22. Since the level is prime and there are no weight-two level-one cusp forms, the whole space is new.

We construct the eigenform and its coefficients, instead of taking a computed expansion as an input. Put
\[
H(z)=\eta(z)^2,\qquad
h(z)=H(z)H(23z)
=q^2\prod_{n\ge1}(1-q^n)^2(1-q^{23n})^2,
\qquad j=T_2h+h.
\tag{38A}
\]

Here is a finite proof of the eta product's modularity. The earlier level-eleven calculation, *Hecke operators for \(\Gamma_0(N)\) and \(\Gamma_1(N)\)*, §6, actually proves from \(H^{12}=\Delta\) that
\(H|_1\gamma=\mu(\gamma)H\), with a character \(\mu\) satisfying
\(\mu(T)=\zeta_{12}\), \(\mu(S)=\zeta_{12}^{-3}\), \(\mu(-I)=\zeta_{12}^6\).
For \(\gamma\in\Gamma_0(23)\), let
\(\gamma'=\operatorname{diag}(23,1)\gamma\operatorname{diag}(23^{-1},1)\). Then
\(h|_2\gamma=\mu(\gamma)\mu(\gamma')h\).
The coset representatives \(I,S,ST,\ldots,ST^{22}\), classified by their lower-row lines modulo 23, give generators
\[
T,\quad U=ST^{23}S^{-1},\quad-I,\quad
A_r=\begin{pmatrix}-s&-1\\rs+1&r\end{pmatrix},
\quad s\equiv-r^{-1}\pmod{23},\ 1\le r,s\le22.
\tag{38B}
\]
This generator assertion follows by telescoping the successive coset transitions of a word in \(S,T\); the transitions for \(T\) are consecutive representatives, and those for \(S\) are the displayed \(A_r\). Their conjugates are
\(A_r'=\left(\begin{smallmatrix}-s&-23\\ (rs+1)/23&r\end{smallmatrix}\right)\).
The exponent of \(\mu(A_r)\) is \(r-s-3\pmod{12}\). To verify every exponent of \(\mu(A_r')\), use the following exact Euclidean recurrence on a determinant-one matrix \(B\). While its lower-left entry \(c\ne0\), put \(u=\lfloor a/c\rfloor\) and replace \(B\) by \(S^{-1}T^{-u}B\). Its new lower-left entry is \(uc-a\), with strictly smaller absolute value, so it terminates. If the last matrix is \(\epsilon T^v\), \(\epsilon=\pm1\), the exponent is
\(\sum u-3\#\{u\}+v+6\mathbf1_{\epsilon=-1}\pmod{12}\).
The following table supplies the entire recurrence data; each row is also a multiplication proof of its word.

| \(r\) | \(s\) | Successive \(u\) | \((\epsilon,v)\) | Exponents of \(\mu(A_r),\mu(A_r')\) |
|---:|---:|:---|:---:|:---:|
|1|22|\(-22\)|\((1,1)\)|\(0,0\)|
|2|11|\(-11\)|\((1,2)\)|\(0,0\)|
|3|15|\(-8,-2\)|\((-1,1)\)|\(9,3\)|
|4|17|\(-6,-3\)|\((-1,1)\)|\(8,4\)|
|5|9|\(-5,-2\)|\((-1,2)\)|\(5,7\)|
|6|19|\(-4,-5\)|\((-1,1)\)|\(8,4\)|
|7|13|\(-4,-2,-2,-2\)|\((-1,1)\)|\(3,9\)|
|8|20|\(-3,-7\)|\((-1,1)\)|\(9,3\)|
|9|5|\(-3,-2\)|\((-1,4)\)|\(1,11\)|
|10|16|\(-3,-2,-2,-3\)|\((-1,1)\)|\(3,9\)|
|11|2|\(-2\)|\((1,11)\)|\(6,6\)|
|12|21|\(-2,-11\)|\((-1,1)\)|\(0,0\)|
|13|7|\(-2,-4\)|\((-1,3)\)|\(3,9\)|
|14|18|\(-2,-3,-4\)|\((1,1)\)|\(5,7\)|
|15|3|\(-2,-2\)|\((-1,7)\)|\(9,3\)|
|16|10|\(-2,-2,-4\)|\((1,2)\)|\(3,9\)|
|17|4|\(-2,-2,-2\)|\((1,5)\)|\(10,2\)|
|18|14|\(-2,-2,-2,-3,-2\)|\((1,1)\)|\(1,11\)|
|19|6|\(-2,-2,-2,-2,-2\)|\((1,3)\)|\(10,2\)|
|20|8|\(-2,-2,-2,-2,-2,-2,-2\)|\((1,2)\)|\(9,3\)|
|21|12|\(\underbrace{-2,\ldots,-2}_{11}\)|\((1,1)\)|\(6,6\)|
|22|1|\(-1\)|\((1,22)\)|\(6,6\)|

Every exponent pair sums to zero modulo 12. For the other generators, the pairs are \(1,23\) for \(T,T'\), \(23,1\) for \(U,U'\), and \(6,6\) for \(-I,(-I)'\). This proves \(h\in M_2(\Gamma_0(23))\) on the entire group. It is nonzero and holomorphic on the upper half-plane. At infinity its order is two. At the other cusp, of width 23,
\[
(h|_2S)(z)=-\frac1{23}H(z)H(z/23)
=-\frac1{23}q_0^2+O(q_0^3),
\qquad q_0=e^{2\pi iz/23}.
\tag{38C}
\]
Indeed the exponent in \(q_0\) is \((23+1)/12=2\). These are the two cusp classes, so \(h\) is a cusp form.

The finite norm proof of the valence formula in the earlier dimension lesson, Theorem 3.1, gives total weighted order four here. A cusp form whose first four coefficients vanish has order at least five at infinity and at least one at zero, so it is zero. Thus checking those four coefficients proves an identity of cusp forms. To compute them in \(T_2j\), only the eta product through \(q^{16}\) is needed. Multiplication gives the following exact table:

|\(n\)|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|\(a_n(h)\)|0|1|−2|−1|2|1|2|−2|0|−2|−2|1|0|0|2|3|

It can be reproduced by starting with the constant polynomial one and multiplying \((1-q^n)^2\) for \(1\le n\le14\), discarding terms of degree greater than fourteen, then multiplying by \(q^2\). The level-23 factors start at \(q^{23}\) and cannot affect this table. The good-prime formula is
\(a_n(T_2u)=a_{2n}(u)+2\mathbf1_{2\mid n}a_{n/2}(u)\).
It gives \(j=q-q^3-q^4+O(q^6)\) and the first four coefficients \((0,1,-2,-1)\) of \(T_2j\), equal to those of \(h\). The valence check proves \(T_2j=h\); the definition gives \(T_2h=j-h\) identically.

The equality \(\dim S_2=g=2\) used here is actually proved in the earlier dimension lesson, Theorem 4.1 and Appendix A.7. Thus the independent \(j,h\) form a basis. Alternatively their two-dimensional cusp sector and its nondegenerate integration pairing are the written finite-symbol calculation in the earlier newform lesson, §6.3 and Lemma 6.1. Set \(\alpha=(\sqrt5-1)/2\). The relation \(\alpha^2=1-\alpha\) now shows that \(j+\alpha h\) is a normalized \(T_2\)-eigenvector. The two eigenvalues of this matrix are distinct; every Hecke operator commutes with it, hence preserves its two eigenlines. This is therefore a normalized full eigenform. All its coefficients lie in \(\mathbf Q(\sqrt5)\), since \(j,h\) have rational coefficients; its second coefficient already generates that field. Since weight-two level-one cusp forms vanish by the level-one valence formula, its prime level is new. We have constructed
\[
f_{23}=q+\frac{\sqrt5-1}{2}q^2-\sqrt5\,q^3
-\frac{1+\sqrt5}{2}q^4+(\sqrt5-1)q^5+O(q^6).
\tag{39}
\]
This agrees with the free author manuscript of Alfes–Mertens, §4.3, but the modularity, eigenform property and exact coefficients have just been proved here.

The coefficient \(a_2=(\sqrt5-1)/2\) has minimal polynomial \(X^2+X-1\). Thus \([K: \mathbf Q]\ge2\). Theorem 2.1 and \(\dim J_0(23)=2\) give \([K: \mathbf Q]\le2\), so
\[
K=\mathbf Q(\sqrt5),\qquad \dim A_f=2.
\tag{40}
\]
Its field action is real multiplication in the precise sense that this real quadratic field embeds in \(\operatorname{End}^0_{\mathbf Q}(A_f)\). This does not assert that it is the complete geometric endomorphism algebra.

We can also express the already constructed Hecke action using its two conjugate eigenforms. Put
\(\alpha=(\sqrt5-1)/2\),
\(h=(f_{23}-f_{23}^\sigma)/\sqrt5\), and
\(j=f_{23}-\alpha h\). Then
\[
h=q^2-2q^3-q^4+2q^5+O(q^6),\qquad
j=q-q^3-q^4+O(q^6).
\tag{41}
\]
They are independent and span the two-dimensional space. The relations
\(T_2f_{23}=\alpha f_{23}\) and their conjugates, together with \(\alpha^2=1-\alpha\), give
\[
T_2j=h,\qquad T_2h=j-h,\qquad
[T_2]_{j,h}=\begin{pmatrix}0&1\\1&-1\end{pmatrix}.
\tag{42}
\]
Its characteristic polynomial is \(X^2+X-1\), verifying the field in this rational basis.

For instance, the four-dimensional arithmetic Frobenius polynomial at 2 is
\[
\begin{aligned}
&(X^2-\alpha X+2)(X^2-\alpha^\sigma X+2)\\
&\hspace{12mm}=X^4+X^3+3X^2+2X+4.
\end{aligned}
\tag{43}
\]
Indeed \(\alpha+\alpha^\sigma=-1\) and
\(\alpha\alpha^\sigma=-1\). At 3, the two traces are \(-\sqrt5,\sqrt5\), so the corresponding polynomial is
\[
(X^2+3)^2-5X^2=X^4+X^2+9.
\tag{44}
\]
These have constant terms \(2^2\) and \(3^2\), as (26) requires. Over a completion of \(K\), one retains a quadratic factor rather than both conjugates.

## 8. Exact proof bindings and remaining required steps

The analytic newform assertions used here have written proofs. Lemmas 1.0a–1.0b supply the lowering traces and the full auxiliary Fourier-support argument, using Li's freely available original article, pp. 286–295, and the earlier newform lesson's actually proved one-prime Appendix A. Lemma 1.0c applies that lesson's same-character Theorem 4.4, §§4.2–4.4, and its level-induction proof of Theorem 4.5. The finite rational Fourier and Hecke structures used for coefficient conjugation are *Modular symbols and the algebraicity of Hecke eigenvalues*, Theorems 2.1 and 3.1–3.2, equations (3.5)–(3.8). Corollary 1.0d proves the bad Fourier coefficients directly. None of these arguments invokes an attached Galois representation to prove multiplicity one.

Lemma 2.0 writes the exponential-sequence and period proof of Abel–Jacobi uniformization. Its exact analytic prerequisites are the dimension lesson's Appendix A.1–A.7 and the group-cohomology lesson's Lemma 5.1, Proposition 5.2 and Theorem 5.3. The algebraic Picard construction and Abel projective bundles are *The Picard functor and the Picard scheme of a curve*, Theorems 6.2 and 7.2 and Proposition 7.1. The curve line-bundle comparison is the preceding lesson's Lemma 1.2. The quotient in (2C) is constructed from the actual earlier *Abelian varieties* proofs, Proposition 6.3 and Theorems 6.4 and 6.20; its complex uniformization and homomorphism compatibility are Theorems 6.23–6.24. The isogeny criterion and Tate-module passage are Theorem 6.25 and Corollary 6.10. Formula (3A) proves the integral homology–torsion comparison, including its transition maps. The determinant uses the preceding lesson's Lemma 1.3 and the curve-cohomology lesson's Theorem 10.1, Corollary 10.2, Theorem 11.1 and §12 for the cup realization and duality. The trace and projection formulas for finite maps are §§2 and 7 of that same curve-cohomology lesson. Lemma 4.1 then proves the coefficient-valued linear algebra. Its rational cup form is alternating by graded commutativity, also for \(\ell=2\).

The preceding lesson's §2 binds the algebraic correspondences and their transposes to their analytic Hecke action. Its torsion-specialization Lemma 1.3 applies when the required abelian scheme has been constructed. The general integral modular model and the complete geometric proof of its special-fibre congruence remain required geometric steps in that lesson. Its Lemma 1.4 now proves the degree-one \(\overline{\mathbf Q}\)-to-\(\mathbf C\) comparison, preserving cup and finite correspondences; its inseparable-factor argument also proves the stated all-characteristic version. The rank calculation here uses (3A) directly, and the cup pairing uses curve duality over \(\overline{\mathbf Q}\). Thus the arithmetic realization of the construction and its good-prime conclusion here depend on completion of the particular preceding model and congruence steps. After an unramified Tate module is obtained, good reduction of the quotient uses the actual arbitrary-dimensional Néron–Ogg–Shafarevich proof in *Néron models*, Lemmas 7.1–7.3 and Theorem 7.4.

Theorem 6.2 retains its full conductor and all-prime Euler-factor statements. Its missing mathematical step is the local comparison (29A), for every prime dividing \(N\), including wildly ramified parameters. Lemma 6.3 proves the possible rank-two parameters once their conductor and special sign are known; (29B) proves restriction of scalars, the exponent \(d\), and the product of bad Euler factors. These reductions do not prove (29A). The free original Carayol article states the full theorem in §§0.5–0.8; its actual local proof uses the geometry and vanishing cycles in §§4–11 and the exceptional residue-characteristic-two base change in §12. The present lesson has not reconstructed those arguments or located an earlier complete programme proof of them. This is an unresolved required proof, and this edition does not certify Theorem 6.2 as proved. The additional identification of the Artin conductor with the geometric conductor is the general abelian conductor step tracked in the earlier curve lesson. Ordinary semisimplification cannot replace the Weil–Deligne pair in any of these calculations.

At level 11 the preceding lesson's §6 tracks the exact modular model, with Weston's free conference notes, §4, as its primary source. The earlier Hecke lesson's §6 proves the eta form and one-dimensional cusp space. The isogeny (33)–(37), including its extension, pointed group law, pole degrees and kernel, is proved here; its pointed rigidity and law compatibility are *Abelian varieties*, Corollary 2.3 and Example 9.12, as checked in Lesson 01, Lemma 3.3. At level 23, (38A)–(38C) prove eta modularity on every group generator and at every cusp. The coefficient table, valence check, eigenspace and field argument prove (39)–(44); Alfes–Mertens is an independent free-source comparison of the expansion, not its proof.

These exact locators bind actually written programme arguments. Their complete transitive proof closure and freely accessible publication are separate edition-wide checks; neither is inferred from a lesson title or a bibliography. The unresolved modular-model and local-comparison obligations above prevent a claim that every result used by this lesson already has a complete proof.

## 9. Graded exercises with complete solutions

**Exercise 9.1 (easy).** Count points on (30) at \(p=2,3,5,7\) and compare with (31).

*Solution.* At 2, the two right sides are zero and \(Y^2+Y\) is zero for both \(Y\), giving \(1+2+2=5\). At 3, the right sides are \(1,0,0\); the values of \(Y^2+Y\) are \(0,2,0\), giving \(1+0+2+2=5\). At 5, the right sides are \(0,0,4,3,3\); \(Y^2+Y\) takes \(0,2,1,2,0\), giving \(1+2+2=5\). These produce \(-2,-1,1\).

At 7, reduce the polynomial to \(X^3-X^2+4X+1\). Substitution of \(X=0,\ldots,6\) gives \(1,5,6,3,2,2,2\). Since \(Y^2+Y\) takes \(0,2,6,5,6,2,0\), the solution counts are \(0,1,2,0,2,2,2\). There are \(1+9=10\) points, so \(a_7=8-10=-2\), agreeing with (31).

**Exercise 9.2 (medium).** Prove \(\dim A_f=[K: \mathbf Q]\), specifying why oldform multiplicities and the integral lattice cause no additional dimension.

*Solution.* The algebra of good Hecke operators is a product of number fields because its action is faithful and simultaneously diagonalizable. By Lemma 1.1 its \(f\)-factor is \(K\), with idempotent \(e\). Over \(\mathbf C\), exact-level multiplicity one gives one line \(\mathbf C f^\sigma\) for each of the \(d\) embeddings. Thus \(eS^\vee\) has dimension \(d\). The two inclusions \(eI_f=0\) and \(1-e\in I_f\otimes\mathbf Q\) imply \(I_fS^\vee=(1-e)S^\vee\). The image subvariety \(I_fJ\) has that tangent space, so the quotient has tangent space \(eS^\vee\), of dimension \(d\). Oldforms would give repeated eigenlines only if the same spectrum occurred at a lower exact level; multiplicity one excludes this for the chosen newform at level \(N\). The quotient's analytic lattice is the image of \(\Lambda\), not a claim that \(\Lambda/I_f\Lambda\) is torsion-free. Finite lattice indices do not change the tangent dimension.

**Exercise 9.3 (medium).** Show that elliptic curves isogenous over \(\mathbf Q\) have the same \(a_p\) at every common good prime. Apply the result to (30) and (32).

*Solution.* Let \(\phi:E\to E'\) be an isogeny of degree \(m\), with dual \(\widehat\phi\). Here is the required factorization: in characteristic zero its kernel is a finite group of order \(m\), so multiplication by \(m\) kills it. The finite-quotient and kernel-torsor proofs in *Abelian varieties*, Proposition 6.3 and Theorem 6.4, make \([m]:E\to E\) descend uniquely through \(\phi\) to \(\widehat\phi:E'\to E\). Thus \(\widehat\phi\phi=[m]\); surjectivity of \(\phi\) also gives \(\phi\widehat\phi=[m]\). This is the elliptic case of the actually proved Theorem 6.7 there. On rational Tate modules,
\[
V_\ell(\widehat\phi)V_\ell(\phi)=mI.
\]
Since \(m\) is invertible in \(\mathbf Q_\ell\), \(V_\ell(\phi)\) is an isomorphism, even if \(\ell\mid m\). It is Galois equivariant because \(\phi\) is defined over \(\mathbf Q\). For a common good prime \(p\), choose \(\ell\ne p\); the arithmetic Frobenius matrices are conjugate and have equal traces. The elliptic trace formula gives \(a_p(E)=a_p(E')\). Equations (33)–(37) exhibit such an isogeny of degree five for our two curves, so all their good-prime traces agree. The inverse on rational modules uses division by five; this argument does not identify their integral mod-5 representations.

**Exercise 9.4 (hard).** Prove freeness of rank two over \(K\otimes\mathbf Q_\ell\). Explain why total dimension alone is insufficient, and prove the determinant on each completion.

*Solution.* The rational homology \(H_1(A_f(\mathbf C),\mathbf Q)\) is a \(K\)-vector space of \(\mathbf Q\)-dimension \(2d\), hence has a \(K\)-basis of two elements. Homology comparison respects the field action and gives \(V_\ell A_f=H_1\otimes\mathbf Q_\ell\). Tensoring that basis gives \((K\otimes\mathbf Q_\ell)^2\); projecting to each \(\lambda\) gives \(K_\lambda^2\). For contrast, a module over \(\mathbf Q_\ell\times\mathbf Q_\ell\) with dimensions one and three on its two factors has total dimension four and is faithful, but is not free of rank two. The rational \(K\)-basis rules this out.

For the determinant, use the restriction of the Jacobian pairing to its self-adjoint \(e\)-factor. It is nondegenerate, has Galois multiplier \(\chi_\ell\), and satisfies \(b(ax,y)=b(x,ay)\). The perfect field-trace pairing defines \(B\) by (21). Testing against every \(a\) proves its \(K_\ell\)-bilinearity and Galois multiplier; the identity \(b(ax,x)=-b(ax,x)\) proves alternation. Nondegeneracy descends to each field factor. On a two-dimensional \(K_\lambda\)-space, a linear map scales an alternating form by its determinant. Comparing with the multiplier \(\chi_\ell(g)\) gives \(\det\rho_{f,\lambda}(g)=\chi_\ell(g)\) for every \(g\), completing both assertions.

## References and next reading

- W.-C. W. Li, [*Newforms and functional equations* (1975), original article](https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0212/LOG_0047.pdf), pp. 286–295: lowering operators, Fourier support, primitive multiplicity and bad coefficients.
- J. S. Milne, [*Abelian Varieties*, free author course notes, version 2.0 (2008)](https://www.jmilne.org/math/CourseNotes/AV.pdf), I.3, I.10, I.13–I.14 and IV.3, for comparison with the earlier programme proofs used above.
- H. Carayol, [*Sur les représentations \(\ell\)-adiques associées aux formes modulaires de Hilbert*, original article (1986)](https://www.numdam.org/article/ASENS_1986_4_19_3_409_0.pdf), §§0.5–0.8 and §§4–12. This is the free primary source for the still unresolved local comparison, not a substitute for its proof.
- T. Weston, [*The modular curves \(X_0(11)\) and \(X_1(11)\)*, free Arizona Winter School notes (2001)](https://swc-math.github.io/notes/files/01Weston1.pdf), §4.
- C. Alfes and M. H. Mertens, [*On Kleinian mock modular forms*, free author manuscript (2023)](https://arxiv.org/pdf/2306.14466v1), §4.3, for comparison with the independently constructed level-23 expansion.

Continue with *Deligne’s construction in weight at least two and the Ramanujan–Petersson bound*. In higher weight, the coefficient system on the modular curve changes; the quadratic determinant becomes \(p^{k-1}\) times the character, rather than \(p\).
