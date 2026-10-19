# Residual irreducibility and one specialization

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lifting theorem needs residual representations that are absolutely irreducible over a cyclotomic extension and decomposed generic. This lesson chooses one parameter \(t\in K\) for which all residual representations of the congruence chain have these properties, while \(t\) also satisfies the local conditions of Lesson 6. The geometric monodromy of the family of covers contains the two transvections of Lesson 4. On every nontrivial character space they act by opposite unipotent matrices, which forces absolute irreducibility, and a product of them is regular semisimple. Hilbert's irreducibility theorem, applied with prescribed local conditions, keeps these monodromy elements in the Galois image of one specialized curve. To make the Frobenius condition hold at every place above a split rational prime, the curve and its conjugate under \(\operatorname{Gal}(K/\mathbb Q)\) are specialized together, through the restriction of scalars of the parameter line from \(K\) to \(\mathbb Q\).

**Prerequisites.** [*Integral homology and Picard–Lefschetz transvections*](integral-homology-and-picard-lefschetz-transvections.md), Theorem 5.1; [*Rank-two systems and their congruences*](rank-two-systems-and-their-congruences.md); [*Prescribing the local reduction type*](prescribing-the-local-reduction-type.md), Proposition 5.1. From *The étale fundamental group*: [*Comparison with the topological fundamental group over the complex numbers*](course:AG-DFG/comparison-with-topology), the Riemann existence equivalence (4.1) and Proposition 4.1. From *Galois representations*: [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces), Theorem 3.0c (finite Chebotarev).

**Standing notation.** As in Lesson 5: \(p>100\), \(n=3p\), \(F=K(\mu_n)\), and \(U\subset\mathbb A^1_K\) is the parameter set. The pairs of covering degree \(m\) and residue characteristic \(\ell\) for which geometric monodromy is used are
\[
(m,\ell)=(3,p),\ (3,5),\ (p,3).\quad(0.1)
\]
In each case \(\ell\nmid m\), so after enlarging the finite coefficient field the residual cohomology \(H^1(C_m,\overline{\mathbb F}_\ell)\) is the direct sum of the eigenspaces of the generator \(u\) of the rotation group, one for each \(m\)-th root of unity \(\lambda\in\overline{\mathbb F}_\ell\).

## 1. Monodromy on the character spaces

For a smooth projective curve \(C\) over a field and \(\ell\) invertible, \(H^1(C,\mathbb F_\ell)=\operatorname{Hom}(J[\ell],\mathbb F_\ell)\), where \(J\) is the Jacobian. For the family \(\mathcal C_m\to U\) with its section \((O,1)\), the Jacobians form an abelian scheme over \(U\) [Milne, III, Theorem 8.1], whose \(\ell\)-torsion is a finite étale group scheme over \(U\), that is, a continuous action of \(\pi_1(U)\) on a finite group. Its fibre at \(t\in U(K)\) is \(J_t[\ell]\) with its action of \(G_K\), and its restriction to the geometric fundamental group \(\pi_1(U_{\overline{\mathbb Q}})\) is, after a complex embedding and the Riemann existence equivalence, the topological local system \(H_1(C_{m,t}(\mathbb C),\mathbb F_\ell)\) of Proposition 1.1 of Lesson 4. Its *geometric monodromy group* is the image of \(\pi_1(U_{\overline{\mathbb Q}})\); by Proposition 4.1 of [*Comparison with the topological fundamental group*](course:AG-DFG/comparison-with-topology), it is the image of the topological fundamental group of \(U(\mathbb C)\), which contains the reductions of the transvections of Theorem 5.1 of Lesson 4.

**Lemma 1.1.** For each pair \((m,\ell)\) in (0.1), the geometric monodromy group of \(H^1(C_m,\overline{\mathbb F}_\ell)\) over \(U\) has the following properties on every eigenspace with eigenvalue \(\lambda\ne1\):

1. it acts absolutely irreducibly;
2. it contains two elements acting by opposite nonidentity unipotent matrices;
3. one element of it acts regular semisimply on all these eigenspaces simultaneously.

The same holds for the family built from the conjugate curve \(E^c\) under \(\operatorname{Gal}(K/\mathbb Q)\).

**Proof.** Work with homology; duality preserves all three properties. By Exercise 6.3 of Lesson 4, on the eigenspace with eigenvalue \(\lambda\) the transvections act in a suitable basis by
\[
\begin{gathered}
T_a=\begin{pmatrix}1&\sigma c_\lambda\\0&1\end{pmatrix},\qquad
T_b=\begin{pmatrix}1&0\\\tau c_\lambda&1\end{pmatrix},\\
c_\lambda=2-\lambda-\lambda^{-1}=-\frac{(\lambda-1)^2}{\lambda},
\end{gathered}
\]
with signs \(\sigma,\tau\in\{1,-1\}\). For \(\lambda\ne1\), \(c_\lambda\ne0\). The only invariant line of \(T_a\) is spanned by the first basis vector, and that of \(T_b\) by the second, also over \(\overline{\mathbb F}_\ell\). So the two have no common invariant line, which proves (1) and (2).

For (3), the matrix \(T_aT_b^k\) has determinant one and trace
\[
2+\sigma\tau k\,c_\lambda^2 .
\tag{1.1}
\]
In odd characteristic a matrix of determinant one is regular semisimple exactly when its trace is not \(\pm2\), because its eigenvalues are distinct exactly when the discriminant \(\operatorname{tr}^2-4\) does not vanish.

If \(m=3\), the nontrivial \(\lambda\) are the primitive cube roots of unity, with \(\lambda+\lambda^{-1}=-1\), so \(c_\lambda=3\) for both. Take \(k=2\): the trace (1.1) is \(20\) or \(-16\). Modulo \(5\) these are \(0\) and \(4\), neither of which is \(2\) or \(-2\). Modulo \(p>100\) they are also different from \(\pm2\), because \(p\) divides none of \(18,22,14\).

If \(m=p\) and \(\ell=3\), take \(k=1\). The trace is \(2\) only if \(c_\lambda=0\), which is excluded, and \(-2\) only if \(c_\lambda^2=\pm4\). Multiplying \(c_\lambda^2=\pm4\) by \(\lambda^2\) gives \((\lambda-1)^4\mp4\lambda^2=0\), a nonzero polynomial equation of degree four over \(\mathbb F_3\). Then \(\lambda\) lies in an extension of \(\mathbb F_3\) of degree \(d\le4\), and its multiplicative order divides \(3^d-1\le80\). But \(\lambda\) is a nontrivial \(p\)-th root of unity, of order \(p>100\). So the single element \(T_aT_b\) is regular semisimple on every nontrivial eigenspace.

The transvections lie in the monodromy of the constant family over \(E^\circ\), which is contained in the geometric monodromy over \(U\) (Theorem 5.1 of Lesson 4). The argument used only the topology of a complex elliptic curve, so it applies verbatim to the family of \(E^c\). \(\square\)

## 2. The trivial character

The trivial character space is \(H^1\) of the twist \(B_t\), whose residual image comes from the choice of \(p\).

**Lemma 2.1.** For every \(t\in U(K)\), the representation \(\overline V_{1,p}\) is absolutely irreducible on \(G_{F(\zeta_p)}=G_F\) and decomposed generic over \(F\).

**Proof.** Let \(\Gamma\) be the image of \(G_K\) on \(E[p]\); it contains \(\mathrm{SL}_2(\mathbb F_p)\). The extension \(F/K\) is abelian, so the image of \(G_F\) contains the commutator subgroup \([\Gamma,\Gamma]\), which contains \([\mathrm{SL}_2(\mathbb F_p),\mathrm{SL}_2(\mathbb F_p)]=\mathrm{SL}_2(\mathbb F_p)\), since \(\mathrm{SL}_2(\mathbb F_p)\) is perfect for \(p\ge5\). The determinant is the mod-\(p\) cyclotomic character, trivial on \(G_F\) because \(\mu_p\subset F\). Hence \(G_F\) acts on \(E[p]\) through all of \(\mathrm{SL}_2(\mathbb F_p)\). The same holds for the conjugate curve \(E^c\), because \(F/\mathbb Q\) is Galois.

Let \(J\subseteq\mathrm{SL}_2(\mathbb F_p)\times\mathrm{SL}_2(\mathbb F_p)\) be the image of \(G_F\) acting on \(E[p]\times E^c[p]\); both projections are onto. A matrix \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\mathrm{SL}_2(\mathbb F_p)\) of trace \(2\) has \(d=2-a\) and \(bc=-(a-1)^2\). For \(a=1\) this gives \(bc=0\), with \(2p-1\) solutions; for each of the other \(p-1\) values of \(a\) it gives \(p-1\) solutions. So there are \((2p-1)+(p-1)^2=p^2\) matrices of trace \(2\), and by \(M\mapsto-M\) also \(p^2\) of trace \(-2\). Since \(|\mathrm{SL}_2(\mathbb F_p)|=p(p^2-1)\) and each projection of \(J\) has fibres of equal size, the proportion of elements of \(J\) whose first or second coordinate has trace \(\pm2\) is at most
\[
2\cdot\frac{2p^2}{p(p^2-1)}=\frac{4p}{p^2-1}<1 .
\]
So some \(g\in G_F\) acts regular semisimply on both \(E[p]\) and \(E^c[p]\).

Let \(N/\mathbb Q\) be a finite Galois extension containing \(F\) and the fields of definition of \(E[p]\) and \(E^c[p]\). By the Chebotarev density theorem there are infinitely many primes \(q\), unramified in \(N\), whose Frobenius class in \(\operatorname{Gal}(N/\mathbb Q)\) is that of \(g\); discard \(q=p\) and the primes of bad reduction of \(E\), \(E^c\) and of the twist \(B_t\). Since \(g\) fixes \(F\), so do all its conjugates, and \(q\) splits completely in \(F\). For a place \(v\mid q\) of \(F\), the Frobenius at \(v\) is \(\gamma g\gamma^{-1}\) for some \(\gamma\in\operatorname{Gal}(N/\mathbb Q)\). If \(\gamma\) fixes \(K\), then \(\gamma\) maps \(E[p]\) to itself and \(\gamma g\gamma^{-1}\) acts on \(E[p]\) by a conjugate of the action of \(g\). If \(\gamma\) does not fix \(K\), then \(\gamma\) maps \(E^c[p]\) bijectively to \(E[p]\), and \(\gamma g\gamma^{-1}\) acts on \(E[p]\) by a conjugate of the action of \(g\) on \(E^c[p]\). In both cases the action is regular semisimple. Since \(\mu_p\subset F\) and \(q\) splits in \(F\), \(q\equiv1\pmod p\), so by Lemma 1.3 of Lesson 1 the eigenvalue condition for decomposed genericity is the distinctness just obtained.

The curve \(B_t\) is the quadratic twist of \(E\) by \(h(t)\): its residual representation is that of \(E\) multiplied by a quadratic character, which multiplies both eigenvalues of each element by the same sign. This preserves absolute irreducibility and distinctness of eigenvalues. Dualizing gives \(H^1\), and Proposition 5.2(2) of Lesson 5 identifies \(\overline V_{1,p}\) with \(\overline{H^1(B_t)}\). \(\square\)

## 3. Hilbert irreducibility with local conditions

**Theorem 3.1 (named result N5: Hilbert's irreducibility theorem, counting form).** Let \(f(x,T_1,\ldots,T_d)\in\mathbb Q(T_1,\ldots,T_d)[x]\) be monic and irreducible, \(L\) its splitting field and \(G=\operatorname{Gal}(L/\mathbb Q(T))\). Outside a proper Zariski-closed set of \(t\in\mathbb Q^d\), the specialized polynomial \(f(x,t)\) is defined and separable, and its splitting field has a Galois group \(G_t\) that embeds in \(G\), well defined up to conjugacy. Then
\[
\begin{aligned}
&\#\{t\in\mathbb Z^d:\ \max_i|t_i|\le B,\ G_t\ne G\}\\
&\qquad\ll_f B^{\,d-1/2}\log B .
\end{aligned}
\]

This is the theorem of Cohen and Serre as stated in [Zyw, Theorem 1.2]; no assumption that \(L\) contains no constants beyond \(\mathbb Q\) is made. The course uses it without proof.

For a connected finite étale Galois cover \(Y\to W\) of an open subset \(W\subseteq\mathbb A^d_{\mathbb Q}\) with group \(H\), corresponding to a surjection \(\pi_1(W)\to H\), a point \(x\in W(\mathbb Q)\) gives a homomorphism \(s_x\colon G_{\mathbb Q}\to H\), defined up to conjugacy; its image is the decomposition group of a point of the fibre \(Y_x\), and \(s_x\) is surjective exactly when \(Y_x\) is connected. Taking a primitive element of the function field of \(Y\) over \(\mathbb Q(T)\) puts this in the form of Theorem 3.1, with \(G_t\) the image of \(s_t\) for \(t\) outside a proper closed set [Zyw, Section 2.1].

**Lemma 3.2.** Let \(W\subseteq\mathbb A^d_{\mathbb Q}\) be a nonempty open subset, \(Y\to W\) a connected finite étale Galois cover with group \(H\), and \(D/\mathbb Q\) a finite Galois extension such that the composite \(\pi_1(W)\to H\to\operatorname{Gal}(D/\mathbb Q)\) is the map induced by the constant field. For finitely many primes \(r\), prescribe nonempty open subsets \(\Omega_r\subseteq W(\mathbb Q_r)\). Then there is \(x\in W(\mathbb Q)\) lying in every \(\Omega_r\) for which \(s_x\colon G_{\mathbb Q}\to H\) is surjective, and for it
\[
\begin{aligned}
&s_x(G_D)\\
&\quad=\ker\bigl(H\to\operatorname{Gal}(D/\mathbb Q)\bigr).\quad(3.1)
\end{aligned}
\]

**Proof.** The set \(\mathbb Q^d\) is dense in \(\prod_r\mathbb Q_r^d\), and the complement of \(W\) is a proper Zariski-closed subset, so there is \(a\in W(\mathbb Q)\) with \(a\in\Omega_r\) for every \(r\). Choose \(k\) so large that \(a+r^k\mathbb Z_r^d\subseteq\Omega_r\) for every \(r\), and put \(M_0=\prod_rr^k\). The affine automorphism \(\alpha(y)=a+M_0y\) of \(\mathbb A^d_{\mathbb Q}\) maps \(\mathbb Z^d\) into \(a+r^k\mathbb Z_r^d\) for every \(r\). Pull the cover back along \(\alpha\): it is still connected and Galois with group \(H\) over \(\alpha^{-1}(W)\). By Theorem 3.1, at most \(O(B^{d-1/2}\log B)\) points \(y\in\mathbb Z^d\) with \(\max|y_i|\le B\) have non-surjective specialization, and at most \(O(B^{d-1})\) lie in the proper closed complement of \(\alpha^{-1}(W)\) or in the exceptional closed set of Theorem 3.1. There are \((2B+1)^d\) points in total, so for large \(B\) some \(y\) avoids all of these. Then \(x=\alpha(y)\) lies in \(W(\mathbb Q)\) and in every \(\Omega_r\), and \(s_x\) is surjective.

The composite of \(s_x\) with \(H\to\operatorname{Gal}(D/\mathbb Q)\) is the restriction map \(G_{\mathbb Q}\to\operatorname{Gal}(D/\mathbb Q)\), whose kernel is \(G_D\). So \(s_x(G_D)\) is contained in the kernel \(H^0\) of \(H\to\operatorname{Gal}(D/\mathbb Q)\). Conversely, every \(h\in H^0\) has a preimage \(\gamma\in G_{\mathbb Q}\) under the surjection \(s_x\), and \(\gamma\) restricts to the identity on \(D\), so \(\gamma\in G_D\). \(\square\)

Geometric connectedness of \(Y\) is not required: \(H\) may be larger than the image of \(\pi_1(W_{\overline{\mathbb Q}})\), the difference being measured by the constant field \(D\).

## 4. One specialization for all the residual conditions

**Proposition 4.1.** Let \(S_K\) be a finite set of finite places of \(K\) containing those above \(3p\), and for each \(v_0\in S_K\) let \(\Omega_{v_0}\subseteq U(K_{v_0})\) be a nonempty open subset. There is \(t\in U(K)\) lying in every \(\Omega_{v_0}\) such that, over \(F=K(\mu_{3p})\):

1. for each pair \((m,\ell)\) in (0.1) and each character \(\theta\) of order \(m\), the representation \(\overline V_{\theta,\ell}\) is absolutely irreducible on \(G_{F(\zeta_\ell)}\) and decomposed generic;
2. \(\overline V_{1,p}\) has the same two properties;
3. the elliptic curve \(A_t=\operatorname{Jac}(C_{3,t}/\langle w\rangle)\) has no complex multiplication.

Taking for the \(\Omega_{v_0}\), \(v_0\mid3p\), the open sets of Proposition 5.1 of Lesson 6, the same \(t\) satisfies all the local conclusions of Corollary 6.1 of Lesson 6.

**Proof.** *The parameter space.* Let \(W=\operatorname{Res}_{K/\mathbb Q}U\), the Weil restriction. Choosing a basis of \(K\) over \(\mathbb Q\) identifies \(\operatorname{Res}_{K/\mathbb Q}\mathbb A^1_K\) with \(\mathbb A^2_{\mathbb Q}\), and \(W\) is an open subset with \(W(\mathbb Q)=U(K)\). For a rational prime \(r\), \(W(\mathbb Q_r)=\prod_{v_0\mid r}U(K_{v_0})\), so the sets \(\Omega_{v_0}\) define nonempty open subsets of \(W(\mathbb Q_r)\) for the finitely many \(r\) below \(S_K\), with no condition at the factors outside \(S_K\). Let \(c\) be the nontrivial automorphism of \(K\), \(U^c\) the conjugate open set and \(\mathcal C^c_m\to U^c\) the conjugate families. Over any field \(D\supseteq K\),
\[
W_D\cong U_D\times U^c_D .
\tag{4.1}
\]

*The finite cover.* Let \(D/\mathbb Q\) be a finite Galois extension containing \(F\) and \(\zeta_\ell\) for \(\ell\in\{3,5,p\}\). Over \(W_D\), pull back the finite local systems \(H^1(\mathcal C_m,\mathbb F_\ell)\) from the first factor of (4.1) and \(H^1(\mathcal C^c_m,\mathbb F_\ell)\) from the second, for the three pairs (0.1). Their joint monodromy is a continuous action of \(\pi_1(W_D)\) on a finite set, whose kernel is an open subgroup. Its normal core in \(\pi_1(W)\) is an open normal subgroup contained in \(\pi_1(W_D)\); let \(H\) be the quotient of \(\pi_1(W)\) by it. Then \(H\) records all these actions and maps onto \(\operatorname{Gal}(D/\mathbb Q)\), compatibly with the constant field. Let \(Y\to W\) be the corresponding connected Galois cover.

*Geometric elements.* Over \(\mathbb C\), a loop in one factor of (4.1) acts trivially on the local systems pulled back from the other factor. Hence the elements of Lemma 1.1 can be realized independently in the two factors. For each pair \((m,\ell)\) let \(h_{m,\ell}\in H\) be the image of a product of a loop in the first factor and a loop in the second, each giving the element of Lemma 1.1(3): it acts regular semisimply on every nontrivial eigenspace of both families. The opposite unipotents of Lemma 1.1(2) are also in the image of geometric monodromy. Being geometric, all these elements map to the identity of \(\operatorname{Gal}(D/\mathbb Q)\).

*Specialization.* Apply Lemma 3.2 to \(Y\to W\) with the prescribed local conditions. It gives \(x\in W(\mathbb Q)\), that is \(t\in U(K)\), in every \(\Omega_{v_0}\), with \(s_x\colon G_{\mathbb Q}\to H\) surjective and \(s_x(G_D)=\ker(H\to\operatorname{Gal}(D/\mathbb Q))\). Over \(D\) the point \(x\) has coordinates \((t,t^c)\) in (4.1). The fibres of the local systems at \(x\), with the action of \(G_D\) through \(s_x\), are the residual cohomology of \(C_m(t)\) and \(C^c_m(t^c)\).

*Absolute irreducibility.* By (3.1), the geometric elements above are images of elements of \(G_D\). So the opposite unipotents act on each specialized nontrivial eigenspace through \(G_D\), which proves absolute irreducibility on \(G_D\), and hence on the larger group \(G_{F(\zeta_\ell)}\supseteq G_D\). Since \(\ell\nmid m\), taking rotation eigenspaces commutes with reduction modulo \(\ell\) after adjoining the character values (Exercise 7.2 of Lesson 5), so these eigenspaces are the reductions of the systems \(V_{\theta,\ell}\) defined on \(C_m\); by Proposition 5.2(1) and Corollary 6.2 of Lesson 5 they give \(\overline V_{\theta,\ell}\), also when \(V_\theta\) is defined using \(C_n\).

*Decomposed genericity.* Fix \((m,\ell)\) and choose \(g\in G_D\) with \(s_x(g)=h_{m,\ell}\). The kernel of \(s_x\) cuts out a finite Galois extension \(N/\mathbb Q\) containing \(D\). By the Chebotarev density theorem there are infinitely many primes \(q\), unramified in \(N\), with Frobenius class that of \(g\); discard \(q=\ell\) and the finitely many primes at which the curves or the residual representations ramify. Since \(g\) fixes \(D\), so do its conjugates, so \(q\) splits completely in \(D\supseteq F(\zeta_\ell)\); in particular \(q\equiv1\pmod\ell\), and every place \(v\mid q\) of \(F\) has residue degree one. The Frobenius at \(v\) is \(\gamma g\gamma^{-1}\) for some \(\gamma\in G_{\mathbb Q}\). Such a \(\gamma\) preserves or exchanges the two specialized families according to its restriction to \(K\), and permutes the rotation characters through its action on roots of unity. So the action of \(\gamma g\gamma^{-1}\) on a nontrivial eigenspace of \(C_m(t)\) is conjugate to the action of \(g\) on some nontrivial eigenspace of \(C_m(t)\) or of \(C^c_m(t^c)\), which is regular semisimple. Its two eigenvalues are therefore distinct, and Lemma 1.3 of Lesson 1 gives decomposed genericity. A different \(q\) may be used for each pair. Assertion (2) is Lemma 2.1.

*No complex multiplication.* For \((m,\ell)=(3,p)\) the residual image of \(V_{\eta,p}\) contains two opposite nonidentity unipotents. By Proposition 5.2(3) of Lesson 5 this residual representation is that of \(H^1(A_t)\); both are irreducible, so they agree without semisimplification. If \(A_t\) had complex multiplication, its endomorphisms would be defined over an extension of \(F\) of degree at most two, over which the \(p\)-adic Galois image lies in the commutative centralizer of the endomorphism algebra; its reduction is then abelian, and the residual image of \(G_F\) has an abelian normal subgroup of index at most two. Both unipotents have odd order \(p\), so both lie in that subgroup. But
\[
\begin{aligned}
\begin{pmatrix}1&a\\0&1\end{pmatrix}\begin{pmatrix}1&0\\b&1\end{pmatrix}
&=\begin{pmatrix}1+ab&a\\b&1\end{pmatrix}\\
&\ne\begin{pmatrix}1&a\\b&1+ab\end{pmatrix}\\
&=\begin{pmatrix}1&0\\b&1\end{pmatrix}\begin{pmatrix}1&a\\0&1\end{pmatrix}
\end{aligned}
\]
for \(ab\ne0\). This contradiction proves (3).

Finally, the specialization was made inside the prescribed local open sets, so with the sets of Proposition 5.1 of Lesson 6 the local conclusions of its Corollary 6.1 hold for the same \(t\). \(\square\)

The parameter \(t\) of Proposition 4.1, with the local open sets of Lesson 6, is fixed for the rest of the course.

## 5. Exercises

**5.1.** Check the claim that \(\mathrm{SL}_2(\mathbb F_p)\) is perfect for \(p\ge5\) by showing that it is generated by the elementary matrices \(\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}1&0\\x&1\end{smallmatrix}\right)\), and that each of these is a commutator.

**5.2.** For \(m=3\) and \(\ell=7\), compute the traces of \(T_aT_b^2\) modulo \(7\) and decide whether the element of Lemma 1.1(3) still works. (The prime \(7\) is not used in the course.)

**5.3.** Show that a subgroup of \(\mathrm{GL}_2(\overline{\mathbb F}_\ell)\) containing two unipotent elements with distinct fixed lines acts absolutely irreducibly on \(\overline{\mathbb F}_\ell^2\), and that it is not abelian.

**5.4.** Explain why the specialization in Section 4 has to be made for the curve and its conjugate together: give the reason why controlling the Frobenius at one place \(v\mid q\) of \(F\) does not control it at the other places above \(q\), unless the conjugate family is included.

## 6. Solutions

**5.1.** Row reduction shows that every matrix of determinant one is a product of elementary matrices, so they generate. For \(a\in\mathbb F_p^\times\),
\[
\begin{aligned}
&\operatorname{diag}(a,a^{-1})\begin{pmatrix}1&x\\0&1\end{pmatrix}\\
&\qquad\cdot\operatorname{diag}(a,a^{-1})^{-1}\begin{pmatrix}1&x\\0&1\end{pmatrix}^{-1}\\
&\quad=\begin{pmatrix}1&(a^2-1)x\\0&1\end{pmatrix}.
\end{aligned}
\]
For \(p\ge5\) there is \(a\) with \(a^2\ne1\), and \((a^2-1)x\) runs over \(\mathbb F_p\) as \(x\) does, so every upper elementary matrix is a commutator; the lower ones likewise. Hence \(\mathrm{SL}_2(\mathbb F_p)\) equals its commutator subgroup. (For \(p=3\) every \(a\in\mathbb F_3^\times\) has \(a^2=1\), and indeed \(\mathrm{SL}_2(\mathbb F_3)\) is not perfect.)

**5.2.** With \(c_\lambda=3\) and \(k=2\), the traces are \(2\pm18\), that is \(20\) and \(-16\). Modulo \(7\) these are \(6\) and \(5\), that is \(-1\) and \(-2\). The second equals \(-2\), so for one choice of signs \(\sigma\tau\) the element \(T_aT_b^2\) is not regular semisimple modulo \(7\). One would take another \(k\): with \(k=1\) the traces are \(2\pm9\), that is \(11\equiv4\) and \(-7\equiv0\), neither \(\pm2\) modulo \(7\).

**5.3.** A common invariant line would be a fixed line of each unipotent, since a unipotent \(2\times2\) matrix different from the identity has exactly one invariant line, its fixed line. The two fixed lines are distinct, so there is no invariant line, over any extension. If the group were abelian, the second unipotent would preserve the fixed line of the first (it commutes with it, so it maps its fixed space to itself), a contradiction.

**5.4.** The places of \(F\) above a split prime \(q\) are permuted transitively by \(\operatorname{Gal}(F/\mathbb Q)\). Half of these elements act on \(K\) by \(c\). For such \(\gamma\), the Frobenius at the place \(\gamma v\) acts on the cohomology of \(C_m(t)\) like the Frobenius at \(v\) acts on the cohomology of the conjugate curve \(C^c_m(t^c)\). So regular semisimplicity at every place above \(q\) requires the chosen Frobenius element to act regular semisimply on the cohomology of both curves, which is what the joint cover over \(W=\operatorname{Res}_{K/\mathbb Q}U\) arranges.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 8 (one specialization with all residual properties). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [Zyw] D. Zywina, *Hilbert's irreducibility theorem and the larger sieve*, Theorem 1.2 (the theorem of Cohen and Serre) and Section 2.1. https://arxiv.org/abs/1011.6465
- [Milne] J. S. Milne, *Abelian Varieties* (version 2.00, 2008), Chapter III, Theorem 8.1. https://www.jmilne.org/math/CourseNotes/AV.pdf
