# The planar boundary theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 2.1 of [Disks, bands and boundary words](disks-bands-and-boundary-words.md): on a connected disk-and-band surface for a unimodular word, one boundary word cannot be the only nontrivial one [OpenAI-K, Section 4]. Travel along the boundary circles is encoded by an operator \(S\Theta\) on \(\mathbb C^D\otimes\ell^2(A)\), where \(D\) is the set of slots: \(\Theta\) crosses the bands and \(S\) follows the corners, multiplying by the inverse corner labels in the left regular representation. Its spectral phase \(\ell(S\Theta)\), from [The regular trace and spectral phase](the-regular-trace-and-spectral-phase.md), is computed in two ways. Splitting \(S\Theta=(SJ)(J\Theta)\) with an involution \(J\) that mixes the positive and the negative disks gives an upper bound, by subadditivity and the fixed-space lemma. Computing the phase one boundary circle at a time gives the same number plus the phase of the exceptional boundary word, which must therefore vanish.

- The boundary operator (Section 1).
- Mixing the disks: an upper bound (Section 2).
- The phase around one boundary circle (Section 3).
- Proof of the planar boundary theorem (Section 4).

We use, from [The regular trace and spectral phase](the-regular-trace-and-spectral-phase.md), the algebra \(M_b(\mathcal M)\), its trace \(\tau_b\), Lemmas 1.3 and 2.1, and the phase \(\ell\) with Lemmas 3.1 and 4.1; from [A unitary with a large fixed space](a-unitary-with-a-large-fixed-space.md), Lemma 5.1; from [Disks, bands and boundary words](disks-bands-and-boundary-words.md), the notation of Sections 1 and 3 and Lemmas 3.1, 4.1 and 5.1.

**Composition with maps of the circle.** For a unitary \(U\) and a continuous map \(\phi:\mathbb T\to\mathbb T\), \(\phi(U)\) is unitary and
\[
\begin{gathered}
f(\phi(U))=(f\circ\phi)(U)\\
(f\in B_b(\mathbb T)) .
\end{gathered}\tag{0.1}
\]
Indeed, \(g\mapsto(g\circ\phi)(U)\) is a unital \(*\)-homomorphism on the continuous functions on the spectrum of \(\phi(U)\), sending \(\iota\) to \(\phi(U)\), so it is the continuous calculus of \(\phi(U)\), and the measures of \(\phi(U)\) are the images of those of \(U\) under \(\phi\), exactly as in Lemma 2.1(3) and (5) of the trace lesson. We use \(\phi(z)=cz\) for a constant \(c\in\mathbb T\), and \(\phi(z)=z^m\).

## 1. The boundary operator

Let \(\Sigma\) be a connected disk-and-band surface for a word
\[
\begin{gathered}
w=t^{s_1}a_1\cdots t^{s_n}a_n,\\
\sum_is_i=\varepsilon\in\{1,-1\} ,
\end{gathered}
\]
with \(k\) positive and \(k\) negative disks (Lemma 4.1 of the disk lesson), slot set \(D\) of size \(2nk\), permutations \(\sigma,\theta\), corner labels \(c_d\), and \(q=nk-2k+2\) boundary circles, the cycles \(z\) of \(\sigma\theta\), with words \(r_z\). Let \((\gamma_d)\) be real numbers with \(\gamma_{\theta d}=-\gamma_d\), and put \(\eta_z=\sum_{d\in z}\gamma_d\).

Work in \(H=\mathbb C^D\otimes\ell^2(A)\), with matrix coordinates indexed by \(D\), so that \(M_{2nk}(\mathcal M)\) and \(\tau=\tau_{2nk}\) are defined. Define
\[
\begin{gathered}
S(e_d\otimes v)=e_{\sigma d}\otimes L(c_d^{-1})v,\\
\Theta(e_d\otimes v)=e^{2\pi i\gamma_d}\,e_{\theta d}\otimes v .
\end{gathered}\tag{1.1}
\]
Both are unitaries in \(M_{2nk}(\mathcal M)\): each permutes the coordinates with unitary weights, and the weights of \(S\) are left translations, which lie in \(\mathcal M\). \(\Theta\) is scalar, and \(\Theta^2=I\) because \(\gamma_{\theta d}+\gamma_d=0\). The product follows the boundary permutation:
\[
S\Theta(e_d\otimes v)=e_{\sigma\theta d}\otimes e^{2\pi i\gamma_d}L(c_{\theta d}^{-1})v .
\]
For a cycle \(z=(d_1,\ldots,d_m)\) of \(\sigma\theta\), with \(d_{j+1}=\sigma\theta d_j\), applying \(S\Theta\) \(m\) times to \(e_{d_1}\otimes v\) multiplies \(v\) by the *circuit weight*
\[
\begin{aligned}
&e^{2\pi i\gamma_{d_m}}L(c_{\theta d_m}^{-1})\cdots\\
&\qquad\cdots e^{2\pi i\gamma_{d_1}}L(c_{\theta d_1}^{-1})\\
&=e^{2\pi i\eta_z}L\bigl((c_{\theta d_1}\cdots c_{\theta d_m})^{-1}\bigr)\\
&=e^{2\pi i\eta_z}L(r_z^{-1}) ,
\end{aligned}\tag{1.2}
\]
by Lemma 3.1 of the disk lesson. The weights act on the left, so a full circuit multiplies the inverse corner labels in reverse order and produces the inverse boundary word.

## 2. Mixing the disks: an upper bound

Number the disks of each kind \(1,\ldots,k\). For a slot index \(i\in\{1,\ldots,n\}\) and \(u\in\mathbb C^k\), let \(e_{+,i}(u)\in\mathbb C^D\) be the vector with coordinate \(u_p\) at slot \(i\) of the \(p\)-th positive disk, \(p=1,\ldots,k\), and \(0\) elsewhere; define \(e_{-,i}(u)\) with the negative disks. Given \(X\in\mathrm U(k)\), define the scalar unitary \(J\) by
\[
\begin{gathered}
J\,e_{+,i}(u)=e_{-,i}(Xu),\\
J\,e_{-,i}(u)=e_{+,i}(X^{-1}u) .
\end{gathered}\tag{2.1}
\]
Then \(J^2=I\), so \(J=J^*=J^{-1}\).

**Lemma 2.1.** \(JSJ=S^{-1}\). Consequently \(SJ\) is a self-adjoint unitary, \(\tau(SJ)=0\), and
\[
\ell(SJ)=\frac{nk}2 .\tag{2.2}
\]

*Proof.* By (3.1) of the disk lesson, the same coefficient acts on the slots \(i\) of all disks of one kind:
\[
\begin{gathered}
S(e_{+,i}(u)\otimes v)=e_{+,i+1}(u)\otimes L(a_i^{-1})v,\\
S(e_{-,i}(u)\otimes v)=e_{-,i-1}(u)\otimes L(a_{i-1})v .
\end{gathered}
\]
Hence \(S^{-1}(e_{+,i}(u)\otimes v)=e_{+,i-1}(u)\otimes L(a_{i-1})v\) and \(S^{-1}(e_{-,i}(u)\otimes v)=e_{-,i+1}(u)\otimes L(a_i^{-1})v\). Since \(J\) acts only on \(\mathbb C^D\),
\[
\begin{aligned}
&JSJ(e_{+,i}(u)\otimes v)\\
&\quad=JS(e_{-,i}(Xu)\otimes v)\\
&\quad=J(e_{-,i-1}(Xu)\otimes L(a_{i-1})v)\\
&\quad=e_{+,i-1}(u)\otimes L(a_{i-1})v ,
\end{aligned}
\]
and similarly \(JSJ(e_{-,i}(u)\otimes v)=e_{-,i+1}(u)\otimes L(a_i^{-1})v\). So \(JSJ=S^{-1}\), \((SJ)^2=S(JSJ)=I\), and the unitary \(SJ\) equals its inverse, which is its adjoint. \(S\) preserves the two kinds of disks and \(J\) exchanges them, so all diagonal entries of \(SJ\) vanish and \(\tau(SJ)=0\). The spectrum of \(SJ\) lies in \(\{1,-1\}\), where \(h(1)=0\) and \(h(-1)=\frac12\); so \(h(SJ)=\frac12\cdot\frac{I-SJ}2\), and \(\ell(SJ)=\frac14\tau(I-SJ)=\frac{2nk}4\). \(\square\)

Let \(V_+\) and \(V_-\) be the coordinate subspaces of \(\mathbb C^D\) spanned by the slots of traversal sign \(+1\) and \(-1\). Each has dimension \(nk\), because the bands pair the signs. Both \(\Theta\) and \(J\) exchange \(V_+\) and \(V_-\): \(\Theta\) because bands join opposite traversal signs, and \(J\) because slot \(i\) has traversal sign \(s_i\) on positive disks and \(-s_i\) on negative disks. Order \(V_+\) in \(n\) blocks of size \(k\): block \(i\) consists of the slots \(i\) of the positive disks if \(s_i=1\) and of the negative disks if \(s_i=-1\), ordered by disk number; order \(V_-\) in the same way with the opposite kinds. In these bases \(\Theta|_{V_+}:V_+\to V_-\) is a unitary matrix \(P\in\mathrm U(nk)\) that does not depend on \(X\), and by (2.1), \(J|_{V_-}:V_-\to V_+\) is \(\operatorname{diag}(X^{-s_1},\ldots,X^{-s_n})\). Hence
\[
\begin{aligned}
&(J\Theta)|_{V_+}=\\
&\operatorname{diag}(X^{-s_1},\ldots,X^{-s_n})\,P .
\end{aligned}\tag{2.3}
\]

**Lemma 2.2** (the upper bound). There is \(X\in\mathrm U(k)\) for which \(\dim\ker(J\Theta-I)\ge2k\). For such \(X\),
\[
\begin{gathered}
\ell(J\Theta)\le nk-k,\\
\ell(S\Theta)\le\frac32nk-k .
\end{gathered}\tag{2.4}
\]

*Proof.* The signs \(-s_1,\ldots,-s_n\) add up to \(-\varepsilon=\pm1\), so Lemma 5.1 of the fixed-space lesson gives \(X\) for which (2.3) fixes a subspace of \(V_+\) of dimension at least \(k\). Since \(J^2=\Theta^2=I\), \(J(J\Theta)J=\Theta J=(J\Theta)^{-1}\); so if \(x\in V_+\) is fixed by \(J\Theta\), then \(Jx\in V_-\) is fixed by \((J\Theta)^{-1}\), hence by \(J\Theta\). This gives \(k\) more fixed directions, in \(V_-\).

The scalar unitary \(J\Theta\) is conjugate to its inverse, so its eigenvalues \(\lambda_1,\ldots,\lambda_{2nk}\), with multiplicity, are invariant under \(\lambda\mapsto\lambda^{-1}\). For \(\lambda=e^{2\pi ix}\) with \(0<x<1\), \(\lambda^{-1}=e^{2\pi i(1-x)}\), so \(h(\lambda)+h(\lambda^{-1})=1\) for \(\lambda\ne1\), while \(h(1)=0\). By Lemma 3.1(4) there,
\[
\begin{aligned}
\ell(J\Theta)&=\sum_jh(\lambda_j)\\
&=\frac12\sum_j\bigl(h(\lambda_j)+h(\lambda_j^{-1})\bigr)\\
&=\frac{2nk-\dim\ker(J\Theta-I)}2\\
&\le nk-k .
\end{aligned}
\]
Finally \(S\Theta=(SJ)(J\Theta)\), and Lemma 4.1 of the trace lesson with (2.2) gives \(\ell(S\Theta)\le\frac{nk}2+nk-k\). \(\square\)

The bound holds for every choice of the numbers \(\gamma_d\); the matrix \(X\), and with it \(J\), may depend on them.

## 3. The phase around one boundary circle

The space \(H\) is the orthogonal direct sum of the subspaces \(\mathbb C^z\otimes\ell^2(A)\) over the cycles \(z\) of \(\sigma\theta\), each invariant under \(S\Theta\) and its inverse. Let \(T_z\) be the restriction of \(S\Theta\) to the cycle \(z\); then \(h(S\Theta)\) is the direct sum of the \(h(T_z)\), and \(\ell(S\Theta)=\sum_z\ell(T_z)\), where \(\ell(T_z)\) uses the trace \(\tau_{|z|}\).

**Lemma 3.1** (phase of a cycle). For every cycle \(z\),
\[
\begin{aligned}
&\ell(T_z)=\frac{|z|-1}2\\
&\quad+\tau\bigl(h(e^{2\pi i\eta_z}L(r_z^{-1}))\bigr).
\end{aligned}\tag{3.1}
\]

*Proof.* Write \(m=|z|\), number the cycle \(d_0,\ldots,d_{m-1}\) with \(d_{j+1}=\sigma\theta d_j\) (indices modulo \(m\)), so that \(T(e_{d_j}\otimes v)=e_{d_{j+1}}\otimes W_jv\) with unitaries \(W_j\in\mathcal M\). Let \(\zeta=e^{2\pi i/m}\) and let \(\Delta\) be the scalar unitary \(e_{d_j}\mapsto\zeta^je_{d_j}\). Then \(\Delta^{-1}T\Delta=\zeta^{-1}T\), so every \(\zeta^jT\) is conjugate to \(T\) by a power of \(\Delta\), and \(\tau_m(h(\zeta^jT))=\ell(T)\) by Lemma 3.1(3) of the trace lesson.

For \(\lambda=e^{2\pi ix}\), the numbers \(h(\zeta^j\lambda)\), \(j=0,\ldots,m-1\), are the fractional parts of \(x+j/m\), and
\[
\begin{aligned}
&\sum_{j=0}^{m-1}h(\zeta^j\lambda)\\
&\quad=\frac{m-1}2+h(\lambda^m) .
\end{aligned}\tag{3.2}
\]
To see this, let \(y\in[0,1/m)\) and \(l\in\{0,\ldots,m-1\}\) with \(x-\lfloor x\rfloor=y+l/m\); the fractional parts of \(x+j/m\) are \(y+p/m\) for \(p=0,\ldots,m-1\) in some order, with sum \(my+\frac{m-1}2\), and \(h(\lambda^m)=my\). Apply the calculus of \(T\) to (3.2), using (0.1) with \(\phi(z)=\zeta^jz\) and \(\phi(z)=z^m\):
\[
\sum_{j=0}^{m-1}h(\zeta^jT)=\frac{m-1}2I+h(T^m).
\]
The operator \(T^m\) is diagonal, with entries the circuit weights starting at \(d_0,\ldots,d_{m-1}\). The weight starting at \(d_{j+1}\) is \(W_j\) times the weight starting at \(d_j\) times \(W_j^{-1}\), so all are conjugate in \(\mathcal M\) to the weight (1.2), and \(\tau_m(h(T^m))=m\,\tau(h(e^{2\pi i\eta_z}L(r_z^{-1})))\). Taking \(\tau_m\) of both sides gives \(m\,\ell(T)=\frac{m(m-1)}2+m\,\tau(h(e^{2\pi i\eta_z}L(r_z^{-1})))\). \(\square\)

## 4. Proof of the planar boundary theorem

*Proof of Theorem 2.1 of the disk lesson.* Let \(z_0\) be the boundary circle whose word may be nontrivial; all other words \(r_z\) are \(1\). For \(0<\delta<1/q\) put
\[
\begin{gathered}
\eta_z=-\delta\quad(z\ne z_0),\\
\eta_{z_0}=(q-1)\delta .
\end{gathered}
\]
These numbers add up to \(0\), so Lemma 5.1 of the disk lesson gives \(\gamma_d\) with \(\gamma_{\theta d}=-\gamma_d\) and \(\sum_{d\in z}\gamma_d=\eta_z\). With the corresponding \(\Theta\), Lemma 2.2 gives
\[
\ell(S\Theta)\le\frac32nk-k .
\]
On the other hand, Lemma 3.1 computes \(\ell(S\Theta)=\sum_z\ell(T_z)\). Since \(\sum_z|z|=2nk\) and there are \(q\) cycles,
\[
\begin{aligned}
\ell(S\Theta)&=\frac{2nk-q}2+\sum_{z\ne z_0}h(e^{-2\pi i\delta})\\
&\quad+\tau\bigl(h(e^{2\pi i(q-1)\delta}L(r_{z_0}^{-1}))\bigr)\\
&=\frac{2nk-q}2+(q-1)(1-\delta)\\
&\quad+\tau\bigl(f_\delta(L(r_{z_0}^{-1}))\bigr) ,
\end{aligned}
\]
where \(f_\delta(\lambda)=h(e^{2\pi i(q-1)\delta}\lambda)\), by (0.1). As \(\delta\downarrow0\), \(f_\delta\to h\) pointwise on \(\mathbb T\): the angle of \(\lambda\) is shifted forward by \((q-1)\delta\ge0\), and \(h\) is continuous from that side everywhere, including at \(1\). The functions are bounded by \(1\), so Lemma 2.1(2) of the trace lesson gives \(\tau(f_\delta(L(r_{z_0}^{-1})))\to\tau(h(L(r_{z_0}^{-1})))\). Using \(q=nk-2k+2\) (Lemma 4.1 of the disk lesson),
\[
\begin{aligned}
&\lim_{\delta\downarrow0}\ell(S\Theta)\\
&\quad=\frac{2nk-q}2+q-1+\tau\bigl(h(L(r_{z_0}^{-1}))\bigr)\\
&\quad=\frac32nk-k+\tau\bigl(h(L(r_{z_0}^{-1}))\bigr) .
\end{aligned}
\]
The upper bound holds for every \(\delta\), so \(\tau(h(L(r_{z_0}^{-1})))\le0\). Since \(h\ge0\) and \(\tau\) is faithful, \(h(L(r_{z_0}^{-1}))=0\), and \(L(r_{z_0}^{-1})=e^{2\pi ih(L(r_{z_0}^{-1}))}=I\) by Lemma 3.1(1) of the trace lesson. As \(L(a)\delta_1=\delta_a\), this means \(r_{z_0}=1\). \(\square\)

Only the uniform upper bound was used; the matrices \(X\) and \(J\) are chosen anew for every \(\delta\), and no limit of them is taken. The phases \(\eta_z\) approach the cut from below on the trivial circles, where \(h(e^{-2\pi i\delta})=1-\delta\) is close to \(1\), and from above on the exceptional circle, where the phase keeps its value \(h\ge0\). Planarity enters only through the count \(q=nk-2k+2\) (Exercise 5.2). For several relators in several unknowns, the same argument with one mixing matrix for each relator is [The planar boundary obstruction](course:nonsingular-systems-over-groups/the-planar-boundary-obstruction).

## 5. Exercises

**5.1** (easy). Let \(n=1\), \(w=ta\), and let \(\Sigma\) be the surface of Exercise 6.2 of the disk lesson. Write \(S\), \(\Theta\) and \(J\) as \(2\times2\) matrices over \(\mathcal M\), and check \(\ell(SJ)=\frac12\) and \(\ell(S\Theta)\le\frac12\) directly.

**5.2** (medium). Suppose that a connected oriented surface of genus \(g\) were built from \(k\) positive and \(k\) negative word disks and \(nk\) bands, so that its number of boundary circles is \(q=nk-2k+2-2g\). Show that the argument of Section 4 then gives only \(\tau(h(L(r_{z_0}^{-1})))\le g\).

**5.3** (easy). Check (3.2) for \(m=2\).

**5.4** (medium). Show that the upper bound \(\ell(J\Theta)\le nk-k\) is the only place where the fixed-space lemma is used, and that without it one would only get \(\ell(J\Theta)\le nk\), which gives no conclusion.

## 6. Solutions

**5.1.** Here \(k=1\) and \(D=\{d_+,d_-\}\), with \(\sigma\) the identity, corners \(c_{d_+}=a\) and \(c_{d_-}=a^{-1}\), and \(\gamma_{d_\pm}=\pm\gamma\) with \(\gamma\) arbitrary (\(q=1\), so \(\eta=0\) forces nothing). In the basis \((d_+,d_-)\), \(S=\operatorname{diag}(L(a^{-1}),L(a))\), \(\Theta=\begin{pmatrix}0&e^{-2\pi i\gamma}\\e^{2\pi i\gamma}&0\end{pmatrix}\), and with \(X=x\in\mathrm U(1)\), \(J=\begin{pmatrix}0&\bar x\\x&0\end{pmatrix}\). Then \(SJ=\begin{pmatrix}0&\bar xL(a^{-1})\\xL(a)&0\end{pmatrix}\) squares to \(I\) and has trace \(0\), so \(\ell(SJ)=\frac12\cdot\frac{2}{2}=\frac12\). By Lemma 3.1 with one cycle of length \(2\) and \(r=1\), \(\ell(S\Theta)=\frac12+h(e^{0})=\frac12\).

**5.2.** The upper bound of Lemma 2.2 does not use planarity. The lower computation gives
\[
\begin{aligned}
&\frac{2nk-q}2+q-1+\tau(\cdot)\\
&\quad=nk+\frac q2-1+\tau(\cdot)\\
&\quad=\frac32nk-k-g+\tau(\cdot).
\end{aligned}
\]
Comparing, \(\tau(h(L(r_{z_0}^{-1})))\le g\), which says nothing once \(g\ge1\), since \(0\le\tau(h(\cdot))\le1\).

**5.3.** For \(\lambda=e^{2\pi ix}\), \(x\in[0,1)\): if \(x<\frac12\), the left side is \(x+(x+\frac12)=2x+\frac12\) and \(h(\lambda^2)=2x\); if \(x\ge\frac12\), it is \(x+(x-\frac12)=2x-\frac12\) and \(h(\lambda^2)=2x-1\). In both cases the difference is \(\frac12=\frac{m-1}2\).

**5.4.** \(J\) and \(\Theta\) are scalar, and \(\ell(J\Theta)=\frac{2nk-\dim\ker(J\Theta-I)}2\) by the computation in Lemma 2.2, which is at most \(nk\) with no information on the kernel. The lower computation gives \(\frac32nk-k+\tau(\cdot)\); against \(\frac{nk}2+nk\) this yields only \(\tau(h(L(r_{z_0}^{-1})))\le k\), which is empty because \(\tau(h(\cdot))\le1\le k\).

## References

- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
