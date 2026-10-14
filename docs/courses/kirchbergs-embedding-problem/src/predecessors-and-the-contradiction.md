# Predecessors and the contradiction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that the full C\*-algebra of the group \(G\) has no unital embedding into the norm ultrapower \(B^\omega\) of a nuclear C\*-algebra \(B\). Suppose there is one. Lifting the images of the group elements to sequences of unitaries of \(B\) gives, for every index \(n\), a tuple of unitaries of \(B\) and with it a finite set \(D_n\) of irreducible representations of the subgroup \(\Gamma\): those that the tuple matches approximately. The set is finite because \(B\) is nuclear. For most \(n\) it contains the representation \(\pi_*\). The element \(t\) of \(G\), which conjugates \(\Gamma\) onto a subgroup of index \(8\), forces every member \(\pi\) of \(D_n\) to have a *predecessor* \(\pi'\) in \(D_n\): a member with \(\pi\prec\pi'\circ\theta\). In a finite set, chains of predecessors must repeat, and this makes \(\pi_*\) equivalent to \(\pi_*\circ\theta^p\) for some \(p\ge1\), which is false.

- The lifts and the sets \(D_n\) (Section 1).
- A gap for representations of varying dimension (Lemma 2.1).
- Induced representations (Lemma 3.1) and a form of Frobenius reciprocity (Lemma 3.2).
- The representation \(\pi_*\) is matched (Lemma 4.1).
- Every member of \(D_n\) has a predecessor (Proposition 5.1).
- Finite chains (Lemma 6.1) and the proof of the theorem (Section 7).
- Kirchberg's problem and consequences quoted from the literature (Section 8).

The lesson follows [OpenAI-K, Sections 5 and 6]. It uses all of [Norm ultrapowers and a group with property (T)](norm-ultrapowers-and-a-group-with-property-t.md) and, from [A spectral test and nuclear finiteness](a-spectral-test-and-nuclear-finiteness.md), the Laplacian, Lemmas 1.2, 2.1, 2.2, 3.1 and 3.2, and Proposition 8.1.

## 1. The setting

Assume the hypothesis (T). The group \(G\), its subgroup \(\Gamma\), the element \(t\), the endomorphism \(\theta\) with \(t\gamma t^{-1}=\theta(\gamma)\), the subgroup \(\Lambda=\theta(\Gamma)\) with the coset representatives \(r_1=e,r_2,\dots,r_8\), the representation \(\pi_*\), the generating set \(S\) and the numbers \(\kappa\), \(R=4|S|\), \(b=\kappa^2/(4|S|)\) and \(a<b\) are as in the first two lessons.

Fix a nuclear unital C\*-algebra \(B\) and a free ultrafilter \(\omega\) on \(\mathbb N\), and suppose that
\[
\Phi\colon C^*(G)\to B^\omega
\]
is a unital embedding. Sections 1 to 6 derive consequences of this assumption; Section 7 obtains a contradiction.

*Lifts.* For \(g\in G\) the element \(\Phi(u_g)\) is a unitary of \(B^\omega\). By the lemma on unitary lifts choose unitaries \(x_n(g)\in B\), \(n\in\mathbb N\), with
\[
\Phi(u_g)=[(x_n(g))_n] ,
\]
and \(x_n(e)=1\). Since \(\Phi(u_g)\Phi(u_h)=\Phi(u_{gh})\), the norm formula for ultraproducts gives, for every fixed pair \(g,h\in G\),
\[
\lim_\omega\|x_n(g)\,x_n(h)-x_n(gh)\|=0 .
\]
We refer to this as the *lift relation*. For a single \(n\) the map \(g\mapsto x_n(g)\) need not be a homomorphism. Every use of the lift relation below concerns finitely many fixed group elements.

*The sets \(D_n\).* Let \(\mathbf x_n=(x_n(s))_{s\in S}\), a tuple of unitaries of \(B\), and
\[
D_n=\{\,[\pi]:\ d(\mathbf x_n,\pi)<a\,\} ,
\]
where \(\pi\) runs through the irreducible unitary representations of \(\Gamma\) of finite dimension and \([\pi]\) is the equivalence class. By the proposition on nuclear finiteness, every \(D_n\) is finite.

## 2. A gap for varying dimensions

**Lemma 2.1.** Let \(\pi_1,\pi_2,\dots\) be unitary representations of \(\Gamma\) of finite dimensions \(d_n\ge1\), not necessarily bounded. Then
\[
\lim_\omega d(\mathbf x_n,\pi_n)\in\{0\}\cup[\kappa,R] .
\]
In particular, if \(d(\mathbf x_n,\pi_n)<a\) for all \(n\) in a large set, the limit is \(0\).

**Proof.** Let \(C_n=M_{d_n}(B)\) and let \(C_\omega\) be the ultraproduct of the \(C_n\). For \(g\in\Gamma\) put \(U_n(g)=x_n(g)\otimes\bar\pi_n(g)\), a unitary of \(C_n\). Since \(\bar\pi_n\) is a homomorphism, with \(y_n=x_n(g)x_n(h)-x_n(gh)\),
\[
U_n(g)U_n(h)-U_n(gh)=y_n\otimes\bar\pi_n(gh) ,
\]
and the norm of this element is \(\|y_n\|\). By the lift relation, \(g\mapsto[(U_n(g))_n]\) is a homomorphism from \(\Gamma\) into the unitary group of \(C_\omega\). By the lemma on the spectral gap, the Laplacian of this homomorphism has its spectrum in \(\{0\}\cup[\kappa,R]\). This Laplacian is the class of the sequence
\[
\begin{gathered}
P_n=L\bigl((x_n(s)\otimes\bar\pi_n(s))_{s\in S}\bigr),\\
0\le P_n\le R ,
\end{gathered}
\]
and \(\min\operatorname{spec}P_n=d(\mathbf x_n,\pi_n)\). By the lemma on spectral minima in ultraproducts, the smallest point of the spectrum of the class is \(\lim_\omega d(\mathbf x_n,\pi_n)\). In the last statement the limit is at most \(a<\kappa\). \(\blacksquare\)

The lemma is where the approximate relations are turned into exact ones: the ultraproduct of the matrix algebras over \(B\) carries a true representation of \(\Gamma\), whatever the dimensions \(d_n\) are.

## 3. Induced representations

Let \(H\) be a subgroup of a group \(G_0\), and let \((q_i)_{i\in I}\) be representatives of the left cosets, so that every element of \(G_0\) is \(q_ih\) for exactly one \(i\in I\) and one \(h\in H\). Let the index \(1\in I\) have \(q_1=e\). For \(g\in G_0\) and \(i\in I\) define \(j(g,i)\in I\) and \(h(g,i)\in H\) by
\[
g\,q_i=q_{j(g,i)}\,h(g,i) .
\]
Let \(\alpha\) be a unitary representation of \(H\) on \(V=\mathbb C^d\). Let \(\ell^2(I;V)\) be the Hilbert space of the families \(w=(w_i)_{i\in I}\) in \(V\) with \(\sum_i\|w_i\|^2<\infty\). The *induced representation* \(\varrho=\operatorname{Ind}_H^{G_0}\alpha\) is defined on it by
\[
\bigl(\varrho(g)w\bigr)_{j(g,i)}=\alpha\bigl(h(g,i)\bigr)\,w_i\qquad(i\in I) .
\]

**Lemma 3.1.** 1. \(\varrho\) is a unitary representation of \(G_0\).

2. For \(h\in H\): \((\varrho(h)w)_1=\alpha(h)w_1\). So the families with \(w_i=0\) for \(i\ne1\) form a subspace that is invariant under \(H\), on which \(H\) acts by \(\alpha\). In particular \(\alpha\prec\varrho|_H\) if \(\alpha\) is irreducible.

3. For every \(i\): \((\varrho(q_i^{-1})w)_1=w_i\).

4. If \(I\) is finite, the conjugate \(\bar\varrho\) is given by the same rule with \(\bar\alpha\) in place of \(\alpha\).

**Proof.** *Part 1.* For fixed \(g\) the map \(i\mapsto j(g,i)\) is a bijection of \(I\): from \(g^{-1}q_{j(g,i)}=q_i\,h(g,i)^{-1}\) its inverse is \(j(g^{-1},\cdot)\). So \(\varrho(g)\) permutes the coordinates and applies unitaries; it is unitary. For \(g_1,g_2\) and \(i\), write \(i'=j(g_2,i)\). Then
\[
\begin{aligned}
g_1g_2\,q_i&=g_1\,q_{i'}\,h(g_2,i)\\
&=q_{j(g_1,i')}\,h(g_1,i')\,h(g_2,i) .
\end{aligned}
\]
So \(j(g_1g_2,i)=j(g_1,i')\) and \(h(g_1g_2,i)=h(g_1,i')\,h(g_2,i)\), which gives \(\varrho(g_1g_2)=\varrho(g_1)\varrho(g_2)\).

*Part 2.* \(h\,q_1=q_1\,h\), so \(j(h,1)=1\) and \(h(h,1)=h\). *Part 3.* \(q_i^{-1}q_i=q_1\,e\), so \(j(q_i^{-1},i)=1\) and \(h(q_i^{-1},i)=e\). *Part 4.* In the standard basis of \(V^I\) the matrix of \(\varrho(g)\) consists of the blocks \(\alpha(h(g,i))\) at the places \((j(g,i),i)\). \(\blacksquare\)

**Lemma 3.2** (Frobenius reciprocity, one direction). Let \(H\) have finite index in \(G_0\), let \(\alpha\) be an irreducible unitary representation of \(H\) of finite dimension, \(\varrho=\operatorname{Ind}_H^{G_0}\alpha\), and let \(\pi'\) be an irreducible representation of \(G_0\) with \(\pi'\prec\varrho\). Then \(\alpha\prec\pi'|_H\).

**Proof.** Let \(W\) be an invariant subspace of \(\varrho\) on which \(\varrho\) is equivalent to \(\pi'\), and let \(P_1\) be the map \(w\mapsto w_1\) from \(W\) to \(V\). By part 2 of Lemma 3.1, \(P_1\varrho(h)=\alpha(h)P_1\) on \(W\) for \(h\in H\). The map \(P_1\) is not zero: a vector \(w\ne0\) of \(W\) has a coordinate \(w_i\ne0\), and by part 3 the vector \(\varrho(q_i^{-1})w\in W\) has the first coordinate \(w_i\). Taking adjoints, \(P_1^*\) is a nonzero intertwiner from \(\alpha\) to the restriction of \(\varrho|_H\) to \(W\). By Schur's lemma \(\alpha\) occurs in this restriction, which is equivalent to \(\pi'|_H\). \(\blacksquare\)

We apply this to \(\Lambda=\theta(\Gamma)\) in \(\Gamma\). If \(\pi\) is an irreducible representation of \(\Gamma\), then \(\alpha=\pi\circ\theta^{-1}\) is an irreducible representation of \(\Lambda\). If \(\pi'\) is an irreducible representation of \(\Gamma\) with \(\pi'\prec\operatorname{Ind}_\Lambda^\Gamma\alpha\), the lemma gives an isometry \(T\) with \(\pi'(\lambda)T=T\alpha(\lambda)\) for \(\lambda\in\Lambda\); putting \(\lambda=\theta(g)\) gives \(\pi'(\theta(g))T=T\pi(g)\) for \(g\in\Gamma\). So
\[
\pi'\prec\operatorname{Ind}_\Lambda^\Gamma(\pi\circ\theta^{-1})\quad\Longrightarrow\quad\pi\prec\pi'\circ\theta .
\]

**Definition.** For irreducible representations \(\pi,\pi'\) of \(\Gamma\), \(\pi'\) is a *predecessor* of \(\pi\) if \(\pi\prec\pi'\circ\theta\).

## 4. The first representation is matched

**Lemma 4.1.** \(\lim_\omega d(\mathbf x_n,\pi_*)=0\). Consequently the set of the \(n\) with \([\pi_*]\in D_n\) is large.

**Proof.** Let \(d\) be the dimension of \(\pi_*\) and \(\varrho=\operatorname{Ind}_\Gamma^G\pi_*\), a unitary representation of \(G\) on a Hilbert space \(H\). By Lemma 3.1, \(\pi_*\prec\varrho|_\Gamma\). By the lemma on representations in the lesson on the spectral test, the number \(d\) for the tuple \((\varrho(s))_{s\in S}\) and \(\pi_*\) is \(0\).

By the universal property, \(\varrho\) extends to a unital \(*\)-homomorphism from \(C^*(G)\) to \(\mathcal B(H)\) with \(u_g\mapsto\varrho(g)\). Let \(\mathbf u=(u_s)_{s\in S}\) in \(C^*(G)\), and \(L_{\mathbf u}=L((u_s\otimes\bar\pi_*(s))_s)\) in \(M_d(C^*(G))\). If \(L_{\mathbf u}\ge m\cdot1\) with \(m>0\), its image \(L((\varrho(s)\otimes\bar\pi_*(s))_s)\) would be \(\ge m\) too, by (C1) and (C6). So \(d(\mathbf u,\pi_*)=0\).

The embedding \(\Phi\) is unital and injective, so \(d(\Phi(\mathbf u),\pi_*)=0\), where \(\Phi(\mathbf u)=([(x_n(s))_n])_{s\in S}\) in \(B^\omega\). By the lemma on matrices over ultraproducts, the Laplacian for \(\Phi(\mathbf u)\) and \(\pi_*\) is the class of the sequence \(P_n=L((x_n(s)\otimes\bar\pi_*(s))_s)\) in \(M_d(B)\). By the lemma on spectral minima, \(0=\lim_\omega\min\operatorname{spec}P_n=\lim_\omega d(\mathbf x_n,\pi_*)\). The last statement follows since \(a>0\). \(\blacksquare\)

This is the only place where the injectivity of \(\Phi\) is used.

## 5. Predecessors

**Proposition 5.1.** The set of the \(n\) for which every class in \(D_n\) has a predecessor in \(D_n\) is large.

In symbols: the set of the \(n\) such that for all \([\pi]\in D_n\) there is \([\pi']\in D_n\) with \(\pi\prec\pi'\circ\theta\) belongs to \(\omega\). The order of the quantifiers matters: one large set of indices serves for all members of \(D_n\), although the sets \(D_n\) vary with \(n\) and the dimensions of their members are not bounded.

**Proof.** Suppose the set is not large. Then its complement \(F\) is large. For \(n\in F\) choose an irreducible \(\pi_n\) with \([\pi_n]\in D_n\) that has no predecessor in \(D_n\). For \(n\notin F\) let \(\pi_n\) be the trivial representation of dimension \(1\). Let \(d_n\) be the dimension of \(\pi_n\).

*Step 1: almost invariant vectors.* Since \(d(\mathbf x_n,\pi_n)<a\) on \(F\), Lemma 2.1 gives \(\lim_\omega d(\mathbf x_n,\pi_n)=0\). Let \(B\) act faithfully with its unit on a Hilbert space \(\mathcal H\), and let \(U_n(g)=x_n(g)\otimes\bar\pi_n(g)\) on \(\mathcal H^{d_n}\) for \(g\in\Gamma\). Choose unit vectors \(\xi_n\in\mathcal H^{d_n}\) with
\[
\sum_{s\in S}\|U_n(s)\xi_n-\xi_n\|^2<d(\mathbf x_n,\pi_n)+\frac1n .
\]
Since \(\omega\) is free, \(\lim_\omega\|U_n(s)\xi_n-\xi_n\|=0\) for every \(s\in S\). We claim that for every \(g\in\Gamma\)
\[
\lim_\omega\|U_n(g)\xi_n-\xi_n\|=0 .
\]
Let \(\Gamma_0\) be the set of the \(g\in\Gamma\) for which this holds. As in the proof of Lemma 2.1, \(\|U_n(g)U_n(g')-U_n(gg')\|\to0\) along \(\omega\) for fixed \(g,g'\), and \(U_n(e)=1\). For \(g,g'\in\Gamma_0\),
\[
\begin{aligned}
&\|U_n(gg')\xi_n-\xi_n\|\\
&\quad\le\|U_n(gg')-U_n(g)U_n(g')\|\\
&\qquad+\|U_n(g')\xi_n-\xi_n\|\\
&\qquad+\|U_n(g)\xi_n-\xi_n\| ,
\end{aligned}
\]
so \(gg'\in\Gamma_0\). For \(g\in\Gamma_0\),
\[
\begin{aligned}
&\|U_n(g^{-1})\xi_n-\xi_n\|\\
&\quad\le\|\xi_n-U_n(g)\xi_n\|\\
&\qquad+\|U_n(g^{-1})U_n(g)-1\| ,
\end{aligned}
\]
so \(g^{-1}\in\Gamma_0\). So \(\Gamma_0\) is a subgroup that contains the generating set \(S\), and \(\Gamma_0=\Gamma\).

*Step 2: transport to \(\Lambda\).* Let \(\alpha_n=\pi_n\circ\theta^{-1}\), a representation of \(\Lambda\) on \(\mathbb C^{d_n}\), and let
\[
\eta_n=(x_n(t)\otimes1)\,\xi_n ,
\]
a unit vector of \(\mathcal H^{d_n}\). We claim that for every \(h\in\Lambda\)
\[
\lim_\omega\|(x_n(h)\otimes\bar\alpha_n(h))\,\eta_n-\eta_n\|=0 .
\]
Let \(g=\theta^{-1}(h)\in\Gamma\). Then \(h=tgt^{-1}\), so \(ht=tg\) in \(G\), and \(\bar\alpha_n(h)=\bar\pi_n(g)\). So
\[
\begin{aligned}
&(x_n(h)\otimes\bar\alpha_n(h))\,\eta_n\\
&\qquad=(x_n(h)x_n(t)\otimes\bar\pi_n(g))\,\xi_n,\\
&(x_n(t)\otimes1)\,U_n(g)\,\xi_n\\
&\qquad=(x_n(t)x_n(g)\otimes\bar\pi_n(g))\,\xi_n .
\end{aligned}
\]
The difference of the two vectors has a norm of at most \(\|x_n(h)x_n(t)-x_n(t)x_n(g)\|\), which tends to \(0\) along \(\omega\) by the lift relation, because both products are close to \(x_n(ht)=x_n(tg)\). And the second vector differs from \(\eta_n\) by \((x_n(t)\otimes1)(U_n(g)\xi_n-\xi_n)\), whose norm tends to \(0\) by Step 1.

*Step 3: induction to \(\Gamma\).* Let \(\varrho_n=\operatorname{Ind}_\Lambda^\Gamma\alpha_n\), with the coset representatives \(r_1=e,\dots,r_8\); it has the dimension \(8d_n\), and we write the vectors of \(\mathcal H^{8d_n}\) as families \((\zeta_i)_{i\le8}\) with \(\zeta_i\in\mathcal H^{d_n}\). For \(g\in\Gamma\) the operator \(x_n(g)\otimes\bar\varrho_n(g)\) maps the family \(\zeta\) to the family whose entry at \(j(g,i)\) is \((x_n(g)\otimes\bar\alpha_n(h(g,i)))\,\zeta_i\), by part 4 of Lemma 3.1. Define the unit vector \(\zeta_n\) by
\[
(\zeta_n)_i=8^{-1/2}\,(x_n(r_i)\otimes1)\,\eta_n
\]
for \(1\le i\le8\).
Fix \(s\in S\) and \(i\), and write \(j=j(s,i)\) and \(h=h(s,i)\), so that \(sr_i=r_jh\). Put \(c_n=x_n(s)x_n(r_i)-x_n(r_j)x_n(h)\) and \(\epsilon_n=(x_n(h)\otimes\bar\alpha_n(h))\eta_n-\eta_n\). The entry at \(j\) of \((x_n(s)\otimes\bar\varrho_n(s))\zeta_n-\zeta_n\) is \(8^{-1/2}\) times the difference of \((x_n(s)x_n(r_i)\otimes\bar\alpha_n(h))\,\eta_n\) and \((x_n(r_j)\otimes1)\,\eta_n\), and this difference is
\[
(c_n\otimes\bar\alpha_n(h))\,\eta_n+(x_n(r_j)\otimes1)\,\epsilon_n .
\]
The first term has a norm of at most \(\|c_n\|\), which tends to \(0\) along \(\omega\) by the lift relation and \(sr_i=r_jh\). The second has the norm \(\|\epsilon_n\|\), which tends to \(0\) by Step 2. There are \(8|S|\) pairs \((s,i)\), all fixed. So
\[
\lim_\omega\sum_{s\in S}\|(x_n(s)\otimes\bar\varrho_n(s))\zeta_n-\zeta_n\|^2=0 ,
\]
and therefore \(\lim_\omega d(\mathbf x_n,\varrho_n)=0\). None of the estimates depends on \(d_n\).

*Step 4: a predecessor.* Let \(F'\) be the large set of the \(n\) with \(d(\mathbf x_n,\varrho_n)<a\). The representation \(\varrho_n\) is equivalent to a direct sum of irreducible representations. By parts 2 and 3 of the lemma on the properties of \(d\), for \(n\in F'\) one of them, \(\pi'_n\), has \(d(\mathbf x_n,\pi'_n)<a\); so \([\pi'_n]\in D_n\). Since \(\pi'_n\prec\varrho_n=\operatorname{Ind}_\Lambda^\Gamma(\pi_n\circ\theta^{-1})\), the consequence of Lemma 3.2 gives \(\pi_n\prec\pi'_n\circ\theta\). So for \(n\in F\cap F'\), which is not empty, \(\pi_n\) has a predecessor in \(D_n\), against its choice. \(\blacksquare\)

The roles of the pieces: the element \(t\) carries a vector that is almost invariant for \(\Gamma\) in the representation \(\pi_n\) to a vector that is almost invariant for the smaller group \(\Lambda\) (Step 2). The induction with eight cosets spreads it to a vector that is almost invariant for \(\Gamma\) in the larger representation \(\varrho_n\) (Step 3). The gap of Lemma 2.1 and the finiteness of the index turn this into a member of \(D_n\) (Step 4).

## 6. Finite chains

**Lemma 6.1.** Let \(\theta\) be a homomorphism from a group \(\Gamma\) to itself, and \(D\) a finite set of equivalence classes of irreducible unitary representations of \(\Gamma\) of finite dimension such that every \([\pi]\in D\) has a predecessor \([\pi']\in D\): \(\pi\prec\pi'\circ\theta\). Then for every \([\pi]\in D\) there is \(p\ge1\) with \(\pi\simeq\pi\circ\theta^p\).

**Proof.** We use three simple facts for representations of finite dimension: if \(\alpha\prec\beta\), then \(\alpha\circ\theta\prec\beta\circ\theta\); the relation \(\prec\) is transitive; and if \(\alpha\prec\beta\) and the dimensions are equal, then \(\alpha\simeq\beta\).

Choose \(\tau_0=\pi\) and then \(\tau_1,\tau_2,\dots\) with classes in \(D\) and \(\tau_i\prec\tau_{i+1}\circ\theta\). Since \(D\) is finite, there are \(l\ge0\) and \(p\ge1\) with \(\tau_l\simeq\tau_{l+p}\). Composing the relations along the chain,
\[
\tau_l\prec\tau_{l+p}\circ\theta^p\simeq\tau_l\circ\theta^p .
\]
The dimensions are equal, so \(\tau_l\simeq\tau_l\circ\theta^p\), and by iteration \(\tau_l\simeq\tau_l\circ\theta^{kp}\) for all \(k\ge0\).

For every \(i\ge0\) the representation \(\tau_l\circ\theta^i\) is irreducible. Indeed, choose \(k\) with \(kp\ge i\). A subspace that is invariant under \(\tau_l(\theta^i(\Gamma))\) is invariant under \(\tau_l(\theta^{kp}(\Gamma))\), because \(\theta^{kp}(\Gamma)\subseteq\theta^i(\Gamma)\); and \(\tau_l\circ\theta^{kp}\simeq\tau_l\) is irreducible.

The beginning of the chain gives \(\pi\prec\tau_l\circ\theta^l\). The right side is irreducible, so \(\pi\simeq\tau_l\circ\theta^l\). Hence
\[
\begin{aligned}
\pi\circ\theta^p&\simeq\tau_l\circ\theta^{l+p}=(\tau_l\circ\theta^p)\circ\theta^l\\
&\simeq\tau_l\circ\theta^l\simeq\pi .
\end{aligned}
\]
\(\blacksquare\)

Finiteness is essential (Exercise 9.2).

## 7. Proof of the theorem

**Theorem 7.1** ([OpenAI-K, Section 1]). Assume (T). For every nuclear unital C\*-algebra \(B\) and every free ultrafilter \(\omega\) on \(\mathbb N\) there is no unital embedding of \(C^*(G)\) into \(B^\omega\).

**Proof.** Suppose \(\Phi\) is one, and use the notation of Section 1. By Lemma 4.1 and Proposition 5.1 there is an index \(n\) such that \([\pi_*]\in D_n\) and every class in \(D_n\) has a predecessor in \(D_n\): two large sets have a common element. The set \(D_n\) is finite because \(B\) is nuclear. By Lemma 6.1 there is \(p\ge1\) with \(\pi_*\simeq\pi_*\circ\theta^p\). This contradicts the lemma on \(\pi_*\) in the first lesson: \(\pi_*\) is not trivial on the translations, and \(\pi_*\circ\theta^p\) is. \(\blacksquare\)

The proof used the following properties of \(G\) and nothing else: \(G\) contains a finitely generated subgroup \(\Gamma\) with property (T) and an element \(t\) such that \(\gamma\mapsto t\gamma t^{-1}\) maps \(\Gamma\) onto a subgroup of finite index of \(\Gamma\); and \(\Gamma\) has an irreducible unitary representation \(\pi_*\) of finite dimension that is not equivalent to \(\pi_*\circ\theta^p\) for any \(p\ge1\).

Where the assumptions on the target enter: that \(B\) is nuclear is used only for the finiteness of \(D_n\). The ultrapower is used through the lift relation and the norm formula. That \(\Phi\) is injective is used only in Lemma 4.1.

## 8. Kirchberg's problem and quoted consequences

With the hypothesis (O) of the first lesson, that \(\mathcal O_2\) is nuclear, Theorem 7.1 for \(B=\mathcal O_2\) gives: the separable unital C\*-algebra \(C^*(G)\) has no unital embedding into \(\mathcal O_2^\omega\). This is the negative answer to Kirchberg's embedding problem (Corollary 4.2 of the first lesson).

[OpenAI-K, Section 6] derives three further statements from this answer by theorems of Goldbring and Sinclair [GS, Proposition 3.2, Theorems 3.3 and 3.7]. They are reported here without proof; the theorems of [GS] are not part of the programme, and their statements were not checked for this course.

- Neither \(\mathcal O_2\) nor any exact or nuclear unital C\*-algebra is existentially closed among unital C\*-algebras, in the sense of the model theory of C\*-algebras.
- For every free ultrafilter \(\omega\) there are a separable unital C\*-algebra \(D\) and an automorphism of \(D\) such that \(D\) embeds unitally into \(\mathcal O_2^\omega\) and the crossed product of \(D\) by the automorphism does not.
- There is a satisfiable finite condition in the language of unital C\*-algebras that has no good nuclear witnesses.

## 9. Exercises

**9.1.** Let \(H=\{e\}\) and let \(\alpha\) be the trivial representation of dimension \(1\). Show that \(\operatorname{Ind}_H^{G_0}\alpha\), with \(I=G_0\) and \(q_g=g\), is the representation of \(G_0\) on \(\ell^2(G_0)\) by left translation.

**9.2.** Let \(\Gamma=\mathbb Z\) and \(\theta(k)=2k\). The irreducible unitary representations of finite dimension are the characters \(\chi_z(k)=z^k\), \(|z|=1\). Find an infinite set \(D\) of characters in which every member has a predecessor in \(D\), and a member \(\chi\) with \(\chi\not\simeq\chi\circ\theta^p\) for all \(p\ge1\).

**9.3.** For \(\Lambda\) in \(\Gamma\) with the representatives \(r_a=(a,I)\), \(a\in\{0,1\}^3\), compute \(j(g,a)\) and \(h(g,a)\) for \(g=(v,M)\).

**9.4.** Let \(\mathbf 1_\Lambda\) be the trivial representation of \(\Lambda\) of dimension \(1\). Show that \(\operatorname{Ind}_\Lambda^\Gamma\mathbf 1_\Lambda\) is the representation of \(\Gamma\) on the functions on \((\mathbb Z/2)^3\) of Exercise 7.5 of the first lesson, and conclude that the representation \(\pi_7\) there is a predecessor of the trivial representation of \(\Gamma\). Verify this directly.

**9.5.** Show that Theorem 7.1 also excludes embeddings that are not unital, in the following sense: there is no injective \(*\)-homomorphism \(\Phi\) from \(C^*(G)\) into \(B^\omega\) such that the projection \(\Phi(1)\) is the class of a sequence of projections \(e_n\in B\) for which the algebras \(e_nBe_n\) are nuclear.

## 10. Solutions

**9.1.** \(g\,q_{g'}=q_{gg'}\,e\), so \(j(g,g')=gg'\) and \(h(g,g')=e\). The rule reads \((\varrho(g)w)_{gg'}=w_{g'}\), which is left translation.

**9.2.** \(\chi_z\circ\theta=\chi_{z^2}\), and for characters \(\prec\) is equality. So \(\chi_{z'}\) is a predecessor of \(\chi_z\) exactly if \(z'^2=z\). Let \(z_i=e^{i\pi/2^i}\), \(i\ge0\); then \(z_{i+1}^2=z_i\) and \(z_0=-1\). In \(D=\{\chi_{z_i}:i\ge0\}\) every member has a predecessor, and \(\chi_{-1}\circ\theta^p=\chi_1\ne\chi_{-1}\) for all \(p\ge1\).

**9.3.** \(g\,r_a=(v+Ma,M)\). Let \(a'\in\{0,1\}^3\) be the residue of \(v+Ma\) modulo \(2\). Then \(g\,r_a=r_{a'}\,(v+Ma-a',M)\), so \(j(g,a)=a'\) and \(h(g,a)=(v+Ma-a',M)\in\Lambda\).

**9.4.** By Exercise 9.3 the induced representation permutes the eight coordinates by \(a\mapsto\bar M a+\bar v\), the action of Exercise 7.5 of the first lesson; a family \((w_a)\) is a function on \((\mathbb Z/2)^3\), and \(\varrho(g)\) is the translation of functions by \(g\). The functions of sum zero form an invariant subspace on which \(\varrho\) is \(\pi_7\). So \(\pi_7\prec\operatorname{Ind}_\Lambda^\Gamma\mathbf 1_\Lambda=\operatorname{Ind}_\Lambda^\Gamma(\mathbf 1_\Gamma\circ\theta^{-1})\), and the consequence of Lemma 3.2 gives \(\mathbf 1_\Gamma\prec\pi_7\circ\theta\). Directly: \(\pi_7(\theta(v,M))=\pi_7(2v,M)\) acts by the linear map \(\bar M\). The function that is \(7\) at \(0\) and \(-1\) at the seven other points has the sum zero and is invariant under all linear maps.

**9.5.** Let \(e=\Phi(1)=[(e_n)]\). Since \(\Phi\) is injective, \(e\ne0\), so the set of the \(n\) with \(e_n\ne0\) is large; for the other \(n\) replace \(e_nBe_n\) by \(\mathbb C\), which does not change the ultraproduct. The corner \(e\,B^\omega e\) is the ultraproduct of the unital C\*-algebras \(e_nBe_n\), by the norm formula, and \(\Phi\) is a unital embedding of \(C^*(G)\) into it. The proof of Theorem 7.1 works for an ultraproduct of nuclear unital C\*-algebras \(B_n\) in place of an ultrapower: the proposition on nuclear finiteness is applied to each \(B_n\) separately, and all other steps concern ultraproducts of varying algebras already.

## References

- [OpenAI-K] OpenAI, *An explicit obstruction to nuclear norm-ultrapower embeddings*, OpenAI Math Release preprint, 23 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/An-explicit-obstruction-to-nuclear-norm-ultrapower-embeddings-September-23-2026
- [GS] I. Goldbring and T. Sinclair, *On Kirchberg's embedding problem*, arXiv:1404.1861, version 6, Section 3. https://arxiv.org/abs/1404.1861
