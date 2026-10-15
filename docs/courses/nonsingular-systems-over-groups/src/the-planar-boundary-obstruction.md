# The planar boundary obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A relation that kills an element of \(G\) is drawn, in [From a kernel relation to a solution](from-a-kernel-relation-to-a-solution.md), as a planar surface: disks whose boundaries read the relators or their inverses, joined by bands along occurrences of the same unknown with opposite signs. This lesson proves the key statement about such surfaces [OpenAI-NS, Proposition 4.1]: on a connected surface, if every boundary word but one is trivial in \(G\), so is the last one. The proof follows [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem), which treats one relator in one unknown with exponent sum \(\pm1\). A unitary operator \(S\Theta\) on \(\mathbb C^{\mathcal D}\otimes\ell^2(G)\), where \(\mathcal D\) is the set of slots, follows the boundary circles. Its spectral phase is bounded above by splitting \(S\Theta=(SJ)(J\Theta)\), where \(J\) mixes the positive and the negative disks of each relator type by a unitary matrix \(X_i\); the theorem of [Simultaneous fixed spaces](simultaneous-fixed-spaces.md) chooses the matrices \(X_i\) so that \(J\Theta\) has many fixed vectors. Computed one boundary circle at a time, the phase is the same number plus the phase of the exceptional boundary word, which must therefore vanish. Nonsingularity enters twice: it balances the numbers of positive and negative disks of each type, and it is the rank condition of the fixed-space theorem.

- Word disks for a system (Section 1).
- Counting disks and boundary circles (Section 2).
- The boundary operator (Section 3).
- Mixing the disks of each type: an upper bound (Section 4).
- Proof of the planar boundary obstruction (Section 5).

We use, from [The regular trace and spectral phase](course:the-kervaire-conjecture/the-regular-trace-and-spectral-phase), with the group \(G\) in place of \(A\): the algebra \(M_b(\mathcal M)\) of operators on \(\mathbb C^b\otimes\ell^2(G)\) commuting with the right translations, its trace \(\tau_b\), Lemma 2.1, and the spectral phase \(\ell\) with Lemmas 3.1 and 4.1. From [Disks, bands and boundary words](course:the-kervaire-conjecture/disks-bands-and-boundary-words) we use the statement (SURF) and Lemmas 3.1, 4.2 and 5.1; from [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem), the identity (0.1) and Lemma 3.1; and Theorem 1.1 of [Simultaneous fixed spaces](simultaneous-fixed-spaces.md).

## 1. Word disks for a system

Fix a group \(G\) and words \(w_1,\ldots,w_m\in G*F_n\) whose exponent-sum matrix \(A=(a_{ij})\) has rank \(m\) over \(\mathbb Q\). Every row of \(A\) is nonzero, so every \(w_i\) contains an unknown. Replacing \(w_i\) by a conjugate changes neither the normal closure of the system nor the exponent sums, so we may write (Exercise 6.1)
\[
\begin{gathered}
w_i=x_{\nu_{i,1}}^{s_{i,1}}g_{i,1}\,x_{\nu_{i,2}}^{s_{i,2}}g_{i,2}\cdots\\
\cdots x_{\nu_{i,N_i}}^{s_{i,N_i}}g_{i,N_i},\\
\nu_{i,t}\in\{1,\ldots,n\},\\
s_{i,t}\in\{1,-1\},\quad g_{i,t}\in G,
\end{gathered}\tag{1.1}
\]
with \(N_i\ge1\), read cyclically: the position \(t\) is taken modulo \(N_i\). Coefficients equal to \(1\) are allowed. Then \(a_{ij}=\sum_{t:\,\nu_{i,t}=j}s_{i,t}\).

Let \(S\) be an oriented sphere. A *word disk of type \(i\)* is a closed disk in \(S\), oriented by \(S\), whose boundary circle carries \(N_i\) pairwise disjoint closed intervals, the *slots*, indexed by \(t\in\{1,\ldots,N_i\}\), separated by \(N_i\) arcs, the *corners*, each carrying an element of \(G\). It is *positive* if, in the boundary orientation, the slots appear in the order \(1,2,\ldots,N_i\) and the corner from slot \(t\) to slot \(t+1\) carries \(g_{i,t}\); then the boundary reads \(w_i\). It is *negative* if the slots appear in the order \(N_i,\ldots,2,1\) and the corner from slot \(t\) to slot \(t-1\) carries \(g_{i,t-1}^{-1}\); then the boundary reads
\[
w_i^{-1}=g_{i,N_i}^{-1}x_{\nu_{i,N_i}}^{-s_{i,N_i}}\cdots g_{i,1}^{-1}x_{\nu_{i,1}}^{-s_{i,1}} .
\]
Slot \(t\) has *variable index* \(\nu_{i,t}\), and its *traversal sign* is \(s_{i,t}\) on a positive disk and \(-s_{i,t}\) on a negative disk. In summary, for slot \(t\) of a disk of type \(i\):
\[
\begin{array}{c|c|c|c}
\text{disk}&\sigma&\text{sign}&c\\\hline
+&t+1&s_{i,t}&g_{i,t}\\
-&t-1&-s_{i,t}&g_{i,t-1}^{-1}
\end{array}\tag{1.2}
\]

A *disk-and-band surface* for the system consists of finitely many pairwise disjoint word disks in \(S\), at least one, of any types and signs, together with pairwise disjoint arcs \(\alpha_1,\ldots,\alpha_E\) whose interiors lie outside the disks, such that every slot contains exactly one endpoint of one arc, in its interior, and the two slots at the ends of each arc have the same variable index and opposite traversal signs. By (SURF) we may take bands around the arcs, and we shrink the slots to the short arcs where the bands meet the disks; this changes no corner label. The surface \(\Sigma\) is the union of the disks and the bands. Its *boundary words* are read along each boundary circle of \(\Sigma\), in its boundary orientation from \(S\): the product of the corner labels met along the way, ignoring the band sides. Changing the starting point conjugates the word, which does not affect whether it is \(1\) in \(G\). For a single relator in a single unknown, these are the surfaces of [Disks, bands and boundary words](course:the-kervaire-conjecture/disks-bands-and-boundary-words), Section 1.

**Proposition 1.1** (planar boundary obstruction; [OpenAI-NS, Proposition 4.1]). Let \(\Sigma\) be a connected disk-and-band surface for a system (1.1) whose exponent-sum matrix has rank \(m\) over \(\mathbb Q\). If every boundary word of \(\Sigma\) except possibly one is trivial in \(G\), then the remaining boundary word is trivial as well.

For one relator in one unknown with exponent sum \(\pm1\), this is Theorem 2.1 of [Disks, bands and boundary words](course:the-kervaire-conjecture/disks-bands-and-boundary-words). The rank condition cannot be dropped (Exercise 6.3).

Let \(\mathcal D\) be the set of slots of \(\Sigma\). Let \(\sigma\) be the permutation of \(\mathcal D\) that sends a slot to the next slot on the same disk, in the boundary orientation, and \(\theta\) the involution, without fixed points, that exchanges the two slots at the ends of each band. For \(d\in\mathcal D\) let \(c_d\in G\) be the label of the corner from \(d\) to \(\sigma d\), given by (1.2).

**Lemma 1.2.**

1. The boundary circles of \(\Sigma\) correspond to the cycles of \(\sigma\theta\). For a cycle \(z=(d_1,\ldots,d_{|z|})\), with \(d_{j+1}=\sigma\theta d_j\), the boundary word of the corresponding circle is \(r_z=c_{\theta d_1}c_{\theta d_2}\cdots c_{\theta d_{|z|}}\).
2. If \(\Sigma\) is connected, every region of \(S\setminus\Sigma\) has exactly one boundary circle and is the closed disk bounded by that circle on the side away from \(\Sigma\).
3. If \(\Sigma\) is connected and \((\eta_z)\) are real numbers indexed by the cycles of \(\sigma\theta\) with \(\sum_z\eta_z=0\), there are real numbers \(\gamma_d\), \(d\in\mathcal D\), with \(\gamma_{\theta d}=-\gamma_d\) and \(\sum_{d\in z}\gamma_d=\eta_z\) for every cycle \(z\).

*Proof.* These are Lemmas 3.1, 4.2 and 5.1 of [Disks, bands and boundary words](course:the-kervaire-conjecture/disks-bands-and-boundary-words). Their proofs use the disks, slots, corners and bands, the permutations \(\sigma\) and \(\theta\), the labels \(c_d\) and the statement (SURF), but not the word written on the disks, its number of letters or its exponents, and they apply without change to the surfaces of this lesson. \(\square\)

## 2. Counting disks and boundary circles

**Lemma 2.1.** Let \(\Sigma\) be a disk-and-band surface for a system (1.1) whose exponent-sum matrix has rank \(m\), with \(p_i^+\) positive and \(p_i^-\) negative disks of type \(i\).

1. \(p_i^+=p_i^-\) for every \(i\).
2. Let \(I\) be the set of types that occur, and \(k_i=p_i^+=p_i^-\ge1\) for \(i\in I\). Put
\[
\begin{gathered}
K=\sum_{i\in I}k_i,\\
b=\sum_{i\in I}N_ik_i .
\end{gathered}\tag{2.1}
\]
Then \(\Sigma\) has \(2K\) disks, \(2b\) slots and \(b\) bands.
3. If \(\Sigma\) is connected and has \(q\) boundary circles, then
\[
q=2-2K+b .\tag{2.2}
\]

*Proof.* (1) Fix an unknown \(x_j\) and add up the traversal signs of all slots with variable index \(j\). The bands pair these slots with each other, each pair having opposite traversal signs, so the sum is \(0\). A positive disk of type \(i\) contributes \(\sum_{t:\,\nu_{i,t}=j}s_{i,t}=a_{ij}\), and a negative disk contributes \(-a_{ij}\). Hence
\[
\sum_{i=1}^m(p_i^+-p_i^-)\,a_{ij}=0\qquad(1\le j\le n),
\]
a linear relation among the rows of \(A\). The rows are linearly independent, so \(p_i^+=p_i^-\) for all \(i\).

(2) A disk of type \(i\) has \(N_i\) slots, every slot carries exactly one band end, and every band has two ends.

(3) By Lemma 1.2(2) and (SURF) 1 and 3, the regions of \(S\setminus\Sigma\) are \(q\) closed disks, one for each boundary circle, each of Euler characteristic \(1\). By (SURF) 2, with \(2K\) disks and \(b\) bands, these Euler characteristics add up to \(2-2K+b\). \(\square\)

Since \(\mathcal D\) is not empty, \(\sigma\theta\) has at least one cycle, so \(q\ge1\).

## 3. The boundary operator

In the rest of the lesson \(\Sigma\) is connected, with the notation of Lemma 2.1. Let \((\gamma_d)_{d\in\mathcal D}\) be real numbers with \(\gamma_{\theta d}=-\gamma_d\), and put \(\eta_z=\sum_{d\in z}\gamma_d\) for each cycle \(z\) of \(\sigma\theta\).

Work in \(H=\mathbb C^{\mathcal D}\otimes\ell^2(G)\), with matrix coordinates indexed by \(\mathcal D\), so that \(M_{2b}(\mathcal M)\) and its trace \(\tau_{2b}\) are defined; \(\tau\) denotes \(\tau_1\), the trace on \(\mathcal M\) itself. Define
\[
\begin{gathered}
S(e_d\otimes v)=e_{\sigma d}\otimes L(c_d^{-1})v,\\
\Theta(e_d\otimes v)=e^{2\pi i\gamma_d}\,e_{\theta d}\otimes v .
\end{gathered}
\]
Both are unitaries in \(M_{2b}(\mathcal M)\): each permutes the coordinates with unitary weights, and the weights of \(S\) are left translations, which lie in \(\mathcal M\). \(\Theta\) is scalar, and \(\Theta^2=I\) because \(\gamma_{\theta d}+\gamma_d=0\). The product follows the boundary permutation:
\[
S\Theta(e_d\otimes v)=e_{\sigma\theta d}\otimes e^{2\pi i\gamma_d}L(c_{\theta d}^{-1})v .
\]
For a cycle \(z=(d_1,\ldots,d_a)\) of \(\sigma\theta\), applying \(S\Theta\) \(a\) times to \(e_{d_1}\otimes v\) multiplies \(v\) by
\[
\begin{aligned}
&e^{2\pi i\gamma_{d_a}}L(c_{\theta d_a}^{-1})\cdots\\
&\qquad\cdots e^{2\pi i\gamma_{d_1}}L(c_{\theta d_1}^{-1})\\
&\quad=e^{2\pi i\eta_z}L(c_{\theta d_1}\cdots c_{\theta d_a})^{-1}\\
&\quad=e^{2\pi i\eta_z}L(r_z^{-1}),
\end{aligned}\tag{3.1}
\]
by Lemma 1.2(1). The space \(H\) is the orthogonal direct sum of the subspaces \(\mathbb C^z\otimes\ell^2(G)\) over the cycles \(z\), each invariant under \(S\Theta\) and its inverse. Let \(T_z\) be the restriction of \(S\Theta\) to the cycle \(z\); then \(h(S\Theta)\) is the direct sum of the \(h(T_z)\), and
\[
\ell(S\Theta)=\sum_z\ell(T_z),\tag{3.2}
\]
where \(\ell(T_z)\) uses the trace \(\tau_{|z|}\), as in Section 3 of [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem).

**Lemma 3.1** (phase of a cycle; [OpenAI-NS, Lemma 3.2]). For every cycle \(z\),
\[
\begin{gathered}
\ell(T_z)=\frac{|z|-1}2\\
+\tau\bigl(h(e^{2\pi i\eta_z}L(r_z^{-1}))\bigr).
\end{gathered}\tag{3.3}
\]

*Proof.* This is Lemma 3.1 of [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem). Its proof uses only that \(T_z\) shifts the coordinates of the cycle \(z\) cyclically with unitary weights in \(\mathcal M\), and that the product of the weights around the cycle is (3.1); both hold here. \(\square\)

## 4. Mixing the disks of each type: an upper bound

Number the positive disks of type \(i\) by \(1,\ldots,k_i\), and likewise the negative ones. For \(i\in I\), a position \(t\in\{1,\ldots,N_i\}\) and \(u\in\mathbb C^{k_i}\), let \(e^i_{+,t}(u)\in\mathbb C^{\mathcal D}\) be the vector with coordinate \(u_p\) at slot \(t\) of the \(p\)-th positive disk of type \(i\), \(p=1,\ldots,k_i\), and \(0\) elsewhere; define \(e^i_{-,t}(u)\) with the negative disks. Given \(X_i\in\mathrm U(k_i)\) for \(i\in I\), define the scalar unitary \(J\) by
\[
\begin{gathered}
J\,e^i_{+,t}(u)=e^i_{-,t}(X_iu),\\
J\,e^i_{-,t}(u)=e^i_{+,t}(X_i^{-1}u) .
\end{gathered}\tag{4.1}
\]
The same \(X_i\) acts at every position \(t\) of type \(i\) (Exercise 6.5). Then \(J^2=I\), so \(J=J^*=J^{-1}\).

**Lemma 4.1.** \(JSJ=S^{-1}\). Consequently \(SJ\) is a self-adjoint unitary, \(\tau_{2b}(SJ)=0\), and
\[
\ell(SJ)=\frac b2 .\tag{4.2}
\]

*Proof.* By (1.2), one coefficient acts on the slots \(t\) of all disks of one type and one sign:
\[
\begin{gathered}
S(e^i_{+,t}(u)\otimes v)=e^i_{+,t+1}(u)\otimes L(g_{i,t}^{-1})v,\\
S(e^i_{-,t}(u)\otimes v)=e^i_{-,t-1}(u)\otimes L(g_{i,t-1})v .
\end{gathered}
\]
Hence
\[
\begin{aligned}
&S^{-1}(e^i_{+,t}(u)\otimes v)\\
&\quad=e^i_{+,t-1}(u)\otimes L(g_{i,t-1})v,\\
&S^{-1}(e^i_{-,t}(u)\otimes v)\\
&\quad=e^i_{-,t+1}(u)\otimes L(g_{i,t}^{-1})v .
\end{aligned}
\]
Since \(J\) acts only on \(\mathbb C^{\mathcal D}\),
\[
\begin{aligned}
&JSJ(e^i_{+,t}(u)\otimes v)\\
&\quad=JS(e^i_{-,t}(X_iu)\otimes v)\\
&\quad=J(e^i_{-,t-1}(X_iu)\otimes L(g_{i,t-1})v)\\
&\quad=e^i_{+,t-1}(u)\otimes L(g_{i,t-1})v ,
\end{aligned}
\]
and in the same way \(JSJ(e^i_{-,t}(u)\otimes v)=e^i_{-,t+1}(u)\otimes L(g_{i,t}^{-1})v\). These vectors span \(H\), so \(JSJ=S^{-1}\), \((SJ)^2=S(JSJ)=I\), and the unitary \(SJ\) equals its inverse, which is its adjoint. \(S\) preserves the sign of each disk and \(J\) exchanges the signs, so all diagonal entries of \(SJ\) vanish and \(\tau_{2b}(SJ)=0\). The spectrum of \(SJ\) lies in \(\{1,-1\}\), where \(h(1)=0\) and \(h(-1)=\frac12\), so \(h(SJ)=\frac14(I-SJ)\) by Lemma 2.1 of the trace lesson, and \(\ell(SJ)=\frac14\tau_{2b}(I-SJ)=\frac{2b}4\). \(\square\)

**Regrouping by unknowns.** For \(j\in\{1,\ldots,n\}\) let \(V_{j,+}\) and \(V_{j,-}\) be the coordinate subspaces of \(\mathbb C^{\mathcal D}\) spanned by the slots with variable index \(j\) and traversal sign \(1\), respectively \(-1\). Bands join slots with the same variable index and opposite traversal signs, so \(\Theta\) exchanges \(V_{j,+}\) and \(V_{j,-}\). So does \(J\): it maps the slot \(t\) of a positive disk of type \(i\), of traversal sign \(s_{i,t}\), into the span of the slots \(t\) of the negative disks of type \(i\), of traversal sign \(-s_{i,t}\) and the same variable index \(\nu_{i,t}\), and conversely.

Order \(V_{j,+}\) in blocks indexed by the pairs \((i,t)\) with \(i\in I\) and \(\nu_{i,t}=j\), in a fixed order: block \((i,t)\) consists of the slots \(t\) of the positive disks of type \(i\) if \(s_{i,t}=1\), and of the negative disks of type \(i\) if \(s_{i,t}=-1\), ordered by disk number. Order \(V_{j,-}\) in the same blocks with the opposite signs of disks. Both spaces have dimension
\[
\begin{gathered}
d_j=\sum_{\substack{(i,t):\ i\in I,\\ \nu_{i,t}=j}}k_i,\\
\sum_{j=1}^nd_j=b .
\end{gathered}\tag{4.3}
\]
In these bases, \(\Theta|_{V_{j,+}}:V_{j,+}\to V_{j,-}\) is a unitary matrix \(P_j\in\mathrm U(d_j)\) that does not depend on the matrices \(X_i\). By (4.1), \(J|_{V_{j,-}}:V_{j,-}\to V_{j,+}\) is block diagonal with the block \(X_i^{-s_{i,t}}\) at \((i,t)\): if \(s_{i,t}=1\), the block of \(V_{j,-}\) lies on the negative disks and \(J\) acts there by \(X_i^{-1}\); if \(s_{i,t}=-1\), it lies on the positive disks and \(J\) acts by \(X_i\). Hence
\[
\begin{aligned}
&(J\Theta)|_{V_{j,+}}\\
&\quad=\operatorname{diag}_{(i,t)}\bigl(X_i^{-s_{i,t}}\bigr)\,P_j ,
\end{aligned}\tag{4.4}
\]
the blocks running over the pairs \((i,t)\) with \(i\in I\) and \(\nu_{i,t}=j\), in the chosen order.

**Lemma 4.2** (the upper bound). There are \(X_i\in\mathrm U(k_i)\), \(i\in I\), for which \(\dim\ker(J\Theta-I)\ge2K\). For such \(X_i\),
\[
\begin{gathered}
\ell(J\Theta)\le b-K,\\
\ell(S\Theta)\le\frac32b-K .
\end{gathered}\tag{4.5}
\]

*Proof.* The matrices (4.4) have the form of Theorem 1.1 of [Simultaneous fixed spaces](simultaneous-fixed-spaces.md), with the variables \(X_i\), \(i\in I\), of sizes \(k_i\), and for each \(j\) the list \(\mathcal B_j\) of the pairs \((i,-s_{i,t})\) over the \((i,t)\) with \(i\in I\) and \(\nu_{i,t}=j\). Its signed block counts are
\[
b_{ij}=\sum_{t:\ \nu_{i,t}=j}(-s_{i,t})=-a_{ij},
\]
so the matrix of signed counts consists of the rows of \(-A\) indexed by \(I\), which are linearly independent. That theorem gives \(X_i\) with
\[
\begin{aligned}
&\sum_j\dim\ker\bigl((J\Theta)|_{V_{j,+}}-I\bigr)\\
&\quad\ge\sum_{i\in I}k_i=K .
\end{aligned}
\] Since \(J\Theta\) maps each \(V_{j,+}\) into itself, this gives a space of fixed vectors of dimension at least \(K\) in \(V_+=\bigoplus_jV_{j,+}\). Since \(J^2=\Theta^2=I\), \(J(J\Theta)J=\Theta J=(J\Theta)^{-1}\); so if \(x\in V_+\) is fixed by \(J\Theta\), then \(Jx\in V_-=\bigoplus_jV_{j,-}\) is fixed by \((J\Theta)^{-1}\), hence by \(J\Theta\). This gives \(K\) more fixed directions, in \(V_-\).

The scalar unitary \(J\Theta\) is conjugate to its inverse, so its eigenvalues \(\lambda_1,\ldots,\lambda_{2b}\), listed with multiplicity, are invariant under \(\lambda\mapsto\lambda^{-1}\). Since \(h(\lambda)+h(\lambda^{-1})=1\) for \(\lambda\ne1\) and \(h(1)=0\), Lemma 3.1(4) of the trace lesson gives
\[
\begin{aligned}
&\ell(J\Theta)=\sum_jh(\lambda_j)\\
&\quad=\frac12\sum_j\bigl(h(\lambda_j)+h(\lambda_j^{-1})\bigr)\\
&\quad=\frac{2b-\dim\ker(J\Theta-I)}2\le b-K .
\end{aligned}
\]
Finally \(S\Theta=(SJ)(J\Theta)\), and Lemma 4.1 of the trace lesson with (4.2) gives \(\ell(S\Theta)\le\frac b2+b-K\). \(\square\)

The bound holds for every choice of the numbers \(\gamma_d\); the matrices \(X_i\), and with them \(J\), may depend on that choice.

## 5. Proof of the planar boundary obstruction

*Proof of Proposition 1.1.* Let \(z_0\) be the boundary circle whose word may be nontrivial; all other words \(r_z\) are \(1\). For \(0<\delta<1/q\) put
\[
\eta_z=-\delta\quad(z\ne z_0),\qquad\eta_{z_0}=(q-1)\delta .
\]
These numbers add up to \(0\), so Lemma 1.2(3) gives numbers \(\gamma_d\) with \(\gamma_{\theta d}=-\gamma_d\) and \(\sum_{d\in z}\gamma_d=\eta_z\). With the corresponding \(\Theta\), Lemma 4.2 gives
\[
\ell(S\Theta)\le\frac32b-K .
\]
On the other hand, (3.2) and Lemma 3.1 compute \(\ell(S\Theta)\). For \(z\ne z_0\), \(r_z=1\), and \(h(e^{-2\pi i\delta}I)\) has trace \(1-\delta\). Since \(\sum_z|z|=2b\) and there are \(q\) cycles,
\[
\begin{aligned}
\ell(S\Theta)&=\frac{2b-q}2+(q-1)(1-\delta)\\
&\quad+\tau\bigl(f_\delta(L(r_{z_0}^{-1}))\bigr),
\end{aligned}
\]
where \(f_\delta(\lambda)=h(e^{2\pi i(q-1)\delta}\lambda)\), by (0.1) of [The planar boundary theorem](course:the-kervaire-conjecture/the-planar-boundary-theorem). As \(\delta\downarrow0\), \(f_\delta\to h\) pointwise on \(\mathbb T\): the angle of \(\lambda\) is shifted forward by \((q-1)\delta\ge0\), and \(h\) is continuous from that side everywhere, including at \(1\). The functions are bounded by \(1\), so Lemma 2.1(2) of the trace lesson gives \(\tau(f_\delta(L(r_{z_0}^{-1})))\to\tau(h(L(r_{z_0}^{-1})))\). Using \(q=2-2K+b\) from (2.2),
\[
\begin{aligned}
&\lim_{\delta\downarrow0}\ell(S\Theta)\\
&\quad=\frac{2b-q}2+q-1+\tau\bigl(h(L(r_{z_0}^{-1}))\bigr)\\
&\quad=\frac32b-K+\tau\bigl(h(L(r_{z_0}^{-1}))\bigr).
\end{aligned}
\]
The upper bound holds for every \(\delta\), so \(\tau(h(L(r_{z_0}^{-1})))\le0\). Since \(h\ge0\) and \(\tau\) is faithful, \(h(L(r_{z_0}^{-1}))=0\), and \(L(r_{z_0}^{-1})=e^{2\pi ih(L(r_{z_0}^{-1}))}=I\) by Lemma 3.1(1) of the trace lesson. As \(L(a)\delta_1=\delta_a\), this means \(r_{z_0}=1\). \(\square\)

Only the upper bound is used, for each \(\delta\) separately; the matrices \(X_i\) are chosen anew for every \(\delta\), and no limit of them is taken. Planarity enters through the count (2.2), connectedness through (2.2) and Lemma 1.2(3), and nonsingularity through Lemma 2.1(1) and the rank condition of the fixed-space theorem.

## 6. Exercises

**6.1** (easy). Show that every element of \(G*F_n\) that contains an unknown is conjugate to a product of the form (1.1). Write \(w=a\,x_1x_2\,b\,x_1^{-1}\), with \(a,b\in G\), in this form and compute its exponent sums.

**6.2** (easy). Let \(m=n=1\) and \(w_1=x_1g\) with \(g\in G\). Let \(\Sigma\) consist of one positive and one negative disk joined by one band. Compute \(\sigma\), \(\theta\), the cycles of \(\sigma\theta\) and the boundary word, and check (2.2) and Proposition 1.1.

**6.3** (medium). Let \(c\in G\), \(c\ne1\), and consider the singular system \(w_1=x_1\), \(w_2=x_1c^{-1}\). Build a connected disk-and-band surface with one positive disk of type \(1\), one negative disk of type \(2\) and one band, and show that its only boundary word is \(c\). Which step of the proof of Proposition 1.1 fails?

**6.4** (medium). For the system \(x_1ax_2b=1\), \(x_1^2cx_2^{-1}d=1\) of Example 2.4 of [Systems of equations over groups](systems-of-equations-over-groups.md), write both words in the form (1.1). Suppose that a connected surface \(\Sigma\) has one disk of each type and each sign. Compute \(K\), \(b\), \(q\), \(d_1\), \(d_2\), the lists \(\mathcal B_1\), \(\mathcal B_2\) of (4.4) and the matrix of signed counts.

**6.5** (medium). Suppose that \(J\) were defined by (4.1) with a unitary \(X_{i,t}\) depending on the position \(t\). Compute \(JSJ(e^i_{+,t}(u)\otimes v)\) and show that \(JSJ=S^{-1}\) forces \(X_{i,t}=X_{i,t-1}\) for all \(t\).

## 7. Solutions

**6.1.** Write the element as a product of letters \(x_j^{\pm1}\) and elements of \(G\), multiply adjacent elements of \(G\), and insert the coefficient \(1\) between two adjacent letters \(x_j^{\pm1}\). If the product begins with an element \(g\in G\), conjugation by \(g\) moves it to the end: \(g^{-1}(gu)g=ug\). For the example, \(a^{-1}wa=x_1\cdot1\cdot x_2\cdot b\cdot x_1^{-1}\cdot a\), so \(N=3\), \((\nu_{1,t},s_{1,t})=(1,1),(2,1),(1,-1)\) and \((g_{1,1},g_{1,2},g_{1,3})=(1,b,a)\). The exponent sums are \(0\) for \(x_1\) and \(1\) for \(x_2\).

**6.2.** \(\mathcal D=\{d_+,d_-\}\). Each disk has one slot, so \(\sigma\) fixes both; \(\theta\) exchanges them, and \(\sigma\theta=\theta\) has the single cycle \((d_+,d_-)\). So \(q=1\), and with \(K=1\), \(b=1\), (2.2) gives \(2-2+1=1\). By (1.2), \(c_{d_+}=g_{1,1}=g\) and \(c_{d_-}=g_{1,0}^{-1}=g^{-1}\), so \(r=c_{\theta d_+}c_{\theta d_-}=c_{d_-}c_{d_+}=g^{-1}g=1\). With one boundary circle, the hypothesis of Proposition 1.1 holds trivially, and its conclusion \(r=1\) is confirmed.

**6.3.** In the form (1.1), \(w_1=x_1\cdot1\) and \(w_2=x_1\cdot c^{-1}\). The slot \(d_1\) of the positive disk of type \(1\) has traversal sign \(1\) and next corner \(g_{1,1}=1\); the slot \(d_2\) of the negative disk of type \(2\) has traversal sign \(-1\) and next corner \(g_{2,1}^{-1}=c\). Both have variable index \(1\), so one band may join them. As in Exercise 6.2, \(\sigma\theta=\theta\) has one cycle, and the boundary word is \(c_{d_2}c_{d_1}=c\cdot1=c\ne1\). The exponent-sum matrix \(\begin{pmatrix}1\\1\end{pmatrix}\) has rank \(1<2\). The proof fails at Lemma 2.1(1): \(p_1^+=1\ne0=p_1^-\), so the disks of each type cannot be paired by matrices \(X_i\).

**6.4.** \(w_1=x_1\cdot a\cdot x_2\cdot b\), with \(N_1=2\), and \(w_2=x_1\cdot1\cdot x_1\cdot c\cdot x_2^{-1}\cdot d\), with \(N_2=3\). With \(k_1=k_2=1\): \(K=2\), \(b=2+3=5\), \(q=2-4+5=3\). The unknown \(x_1\) occurs at \((1,1)\), \((2,1)\), \((2,2)\), so \(d_1=3\); \(x_2\) occurs at \((1,2)\) and \((2,3)\), so \(d_2=2\), and \(d_1+d_2=b\). Then \(\mathcal B_1=((1,-1),(2,-1),(2,-1))\) and \(\mathcal B_2=((1,-1),(2,1))\), and the matrix of signed counts is \(\begin{pmatrix}-1&-1\\-2&1\end{pmatrix}=-A\), of determinant \(-3\).

**6.5.** With the matrices \(X_{i,t}\) in (4.1),
\[
\begin{aligned}
&JSJ(e^i_{+,t}(u)\otimes v)\\
&\quad=JS(e^i_{-,t}(X_{i,t}u)\otimes v)\\
&\quad=J(e^i_{-,t-1}(X_{i,t}u)\otimes L(g_{i,t-1})v)\\
&\quad=e^i_{+,t-1}(X_{i,t-1}^{-1}X_{i,t}u)\\
&\qquad\otimes L(g_{i,t-1})v,
\end{aligned}
\]
while
\[
\begin{aligned}
&S^{-1}(e^i_{+,t}(u)\otimes v)\\
&\quad=e^i_{+,t-1}(u)\otimes L(g_{i,t-1})v .
\end{aligned}
\] Equality for all \(u\) and \(v\) means \(X_{i,t-1}^{-1}X_{i,t}=I\). So one matrix \(X_i\) serves all positions of type \(i\), and in (4.4) only the signed number of its occurrences next to each unknown matters.

## References

- [OpenAI-NS] OpenAI, *Nonsingular systems of equations over arbitrary groups*, OpenAI Math Release preprint, 5 October 2026, Sections 3 and 4, Lemma 3.2 and Proposition 4.1. https://github.com/openai/math/tree/main/preprints/Nonsingular-systems-of-equations-over-arbitrary-groups-October-5-2026
- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
