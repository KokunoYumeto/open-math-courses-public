# Vertices of large depth

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Component labels and annular depth](component-labels-and-annular-depth.md) attaches to a closed set \(A\) and a group element \(g\) the depth \(D(A,g)\), the largest number of nested annuli between \(A\) and \(g\). This lesson studies the vertices of the graph \(K\) that have depth at least \(m\), and the components into which they fall. Its results are the following.

- If the depths \(D(A,g_n)\) tend to infinity, then, along a subsequence, the translates \(g_n^{-1}A\) shrink to one point \(q\) of the continuum \(L\) (Lemma 2.1). The depth measured from such a translate is the sum of two depths, with an error that is bounded (Lemma 3.1).
- The vertices of depth at least \(m\) form a set \(I_m\). Away from \(A\), the vertices outside \(I_m\) do not accumulate on \(L\), so there is a component label \(Q_m\) on \(L\setminus A\) (Section 4).
- Let \(g_n\) have depth at least \(m_n\), with \(m_n\to\infty\). Then any two points \(z,z'\) of \(L\) other than \(q\) have translates \(g_nz\), \(g_nz'\) with the same label \(Q_{m_n+1}\), for all large \(n\) (Theorem 6.1).

These statements are the preparation for the proof that \(L\) is locally connected. The lesson follows the first half of Section 9 of [OpenAI-S].

## 1. The setting

We use the data \(Y=H\cup L\), \(K\), \(I\) and the properties (S1) to (S7) of the lesson on component labels and annular depth, the set \(\mathcal A\) of annuli of Theorem 3.2 there, and the depth \(D\) of Section 4 there. The identity \(1\) of \(H\) is a point of \(Y\). A sequence \((h_n)\) in \(H\) *tends to infinity* if every element of \(H\) occurs in it only finitely often; by (S4), \(\rho(h_nw,h_n)\to0\) for such a sequence and every \(w\in I\).

Throughout the lesson, \(A\) is a closed subset of \(Y\) with
\[
1\in A,\qquad L\not\subseteq A .
\]
The following facts and notations are used.

- (D1) \(D(gF,gv)=D(F,v)\) for \(g\in H\). If \(F\) contains a point of \(H\) and \(v\in H\), then \(D(F,v)\) is finite. In particular \(D(A,g)\) is finite for every \(g\in H\). (Theorem 4.1(1) and (2) of that lesson.)
- (D2) If \(F\) is closed, \(x\in L\setminus F\) and \(N\ge1\), then \(D(F,v)\ge N\) for all \(v\) in some neighbourhood of \(x\) in \(Y\). (Theorem 4.1(3).)
- (D3) In a chain \(\sigma_1<\dots<\sigma_n\) of annuli the negative sides increase, the positive sides decrease, and the annuli are pairwise different (Lemma 3.1 of that lesson):
\[
\begin{gathered}
\sigma_1^-\subseteq\dots\subseteq\sigma_n^-,\\
\sigma_1^+\supseteq\dots\supseteq\sigma_n^+ .
\end{gathered}
\]
- Let \(d_0\) be the distance from \(1\) to \(L\). It is positive, because \(L\) is closed and \(1\notin L\). Every side of an annulus meets \(L\). So a side that contains \(1\) has diameter at least \(d_0\).
- For \(a,b>0\) let \(N(a,b)\) be the number of annuli \(\sigma\in\mathcal A\) with \(\operatorname{diam}\sigma^-\ge a\) and \(\operatorname{diam}\sigma^+\ge b\). It is finite, by Theorem 3.2(1) of that lesson with \(\delta\) the smaller of \(a\) and \(b\).
- A sequence \((F_n)\) of subsets of \(Y\) *shrinks to* the point \(q\in Y\) if for every \(r>0\) the set \(F_n\) lies in the ball \(B(q,r)\) for all but finitely many \(n\). Every subsequence then shrinks to \(q\) as well.

**Lemma 1.1.** Let \(p\in I\), and let \((a_n)\) be a sequence in \(H\) such that the vertices \(a_np\) are pairwise distinct and converge to a point \(x\) of \(Y\). Then \(x\in L\) and \(a_n\to x\).

**Proof.** A limit of pairwise distinct points is not an isolated point, so \(x\in L\) by (S1). The elements \(a_n\) are pairwise distinct, so \((a_n)\) tends to infinity, and \(\rho(a_np,a_n)\to0\) by (S4). \(\blacksquare\)

## 2. Translates that shrink to a point

**Lemma 2.1.** Let \((g_n)\) be a sequence in \(H\) with \(D(A,g_n)\to\infty\). Then \((g_n)\) has a subsequence for which the sets \(g_n^{-1}A\) shrink to a point \(q\) of \(L\).

**Proof.** Let \(F_n=g_n^{-1}A\). By (D1),
\[
D(F_n,1)=D(A,g_n).
\]
*The diameters tend to zero.* Let \(\varepsilon>0\) and let \(\sigma_1<\dots<\sigma_\ell\) be a chain from \(F_n\) to \(\{1\}\). By (D3), every positive side \(\sigma_i^+\) contains \(1\), so its diameter is at least \(d_0\); every negative side \(\sigma_i^-\) contains \(F_n\); and the \(\ell\) annuli are pairwise different. If \(\ell>N(\varepsilon,d_0)\), then not all of them have a negative side of diameter at least \(\varepsilon\), so \(\operatorname{diam}F_n<\varepsilon\). Since \(D(F_n,1)\to\infty\), such chains exist for all large \(n\). Hence \(\operatorname{diam}F_n\to0\).

*The limit point.* For every \(g\in H\) the number \(D(A,g)\) is finite, so \(g\) occurs only finitely often among the \(g_n\). Pass to a subsequence in which the elements \(g_n^{-1}\) are pairwise distinct and converge to a point \(q\) of the compact space \(Y\). Then \(q\in L\), because a limit of pairwise distinct points is not isolated. Since \(1\in A\), the point \(g_n^{-1}\) lies in \(F_n\). For \(r>0\) and all large \(n\) we have \(\rho(g_n^{-1},q)<r/2\) and \(\operatorname{diam}F_n<r/2\), so \(F_n\subseteq B(q,r)\). \(\blacksquare\)

## 3. A comparison of depths

In the situation of Lemma 2.1, a chain from \(F_n\) to a group element \(b\) far from \(q\) can be built from two chains: one from \(F_n\) to \(1\), and one from \(1\) to \(b\). Only a bounded number of annuli is lost.

**Lemma 3.1.** Let \((g_n)\) be a sequence in \(H\) with \(D(A,g_n)\to\infty\) such that the sets \(F_n=g_n^{-1}A\) shrink to a point \(q\in Y\). For \(r>0\) let
\[
C_r=N(r/2,d_0)+N(d_0,r)+2 .
\]
Then there is \(n_r\) such that for all \(n\ge n_r\) and all \(b\in H\) with \(\rho(b,q)\ge3r\),
\[
D(F_n,b)\ge D(F_n,1)+D(1,b)-C_r .
\]

**Proof.** Let \(N_-=N(r/2,d_0)\) and \(N_+=N(d_0,r)\). Choose \(n_r\) such that for \(n\ge n_r\)
\[
\begin{gathered}
F_n\subseteq B(q,r/2),\\
D(F_n,1)\ge N_-+2 .
\end{gathered}
\]
Fix \(n\ge n_r\) and \(b\in H\) with \(\rho(b,q)\ge3r\). The set \(F_n\) contains the group element \(g_n^{-1}\), so \(\ell=D(F_n,1)\) and \(t=D(1,b)\) are finite, by (D1). Let
\[
\begin{gathered}
U=B(q,r),\\
V=\{y\in Y\mid\rho(y,q)>2r\}.
\end{gathered}
\]
These are disjoint open sets, and \(b\in V\).

*The first chain.* Let \(\sigma_1<\dots<\sigma_\ell\) be a chain from \(F_n\) to \(\{1\}\). Suppose \(\sigma_j^-\not\subseteq U\). The side \(\sigma_j^-\) contains a point of \(F_n\), at distance less than \(r/2\) from \(q\), and a point at distance at least \(r\) from \(q\); so its diameter is at least \(r/2\). The side \(\sigma_j^+\) contains \(1\), so its diameter is at least \(d_0\). Since the annuli of the chain are pairwise different, there are at most \(N_-\) such indices \(j\). The negative sides increase along the chain, so these are the last \(k\) indices, for some \(k\le N_-\). Let
\[
p=\ell-k-1\ge1 .
\]
Then \(\sigma_{p+1}^-\subseteq U\), and \(\sigma_p^+\cup\sigma_{p+1}^-=Y\) gives \(Y\setminus U\subseteq\sigma_p^+\). So \(\sigma_1<\dots<\sigma_p\) is a chain from \(F_n\) to \(Y\setminus U\), of length at least \(\ell-N_--1\).

*The case \(t\le N_++1\).* The first chain goes from \(F_n\) to \(\{b\}\), because \(b\notin U\). So
\[
D(F_n,b)\ge\ell-N_--1\ge\ell+t-C_r .
\]

*The case \(t\ge N_++2\).* Let \(\tau_1<\dots<\tau_t\) be a chain from \(\{1\}\) to \(\{b\}\). Suppose \(\tau_j^+\not\subseteq V\). The side \(\tau_j^+\) contains \(b\) and a point at distance at most \(2r\) from \(q\), so its diameter is at least \(r\). The side \(\tau_j^-\) contains \(1\), so its diameter is at least \(d_0\). Hence there are at most \(N_+\) such indices \(j\). The positive sides decrease along the chain, so these are the first \(k'\) indices, for some \(k'\le N_+\). Let
\[
p'=k'+2\le t .
\]
Then \(\tau_{p'-1}^+\subseteq V\), and \(\tau_{p'-1}^+\cup\tau_{p'}^-=Y\) gives \(Y\setminus V\subseteq\tau_{p'}^-\). The chain \(\tau_{p'}<\dots<\tau_t\) has length at least \(t-N_+-1\).

Since \(U\) and \(V\) are disjoint,
\[
\sigma_p^+\cup\tau_{p'}^-\supseteq(Y\setminus U)\cup(Y\setminus V)=Y ,
\]
that is, \(\sigma_p<\tau_{p'}\). So
\[
\sigma_1<\dots<\sigma_p<\tau_{p'}<\dots<\tau_t
\]
is a chain from \(F_n\) to \(\{b\}\). Its length is at least
\[
\begin{aligned}
&(\ell-N_--1)+(t-N_+-1)\\
&\qquad=\ell+t-C_r .
\end{aligned}
\]
\(\blacksquare\)

**Corollary 3.2.** Let \((g_n)\), \(F_n\) and \(q\) be as in Lemma 3.1, and let \((b_n)\) be a sequence in \(H\) that converges to a point \(z\in L\) with \(z\ne q\). Then \(D(1,b_n)\to\infty\), and there is a number \(C\) such that for all but finitely many \(n\)
\[
D(F_n,b_n)\ge D(F_n,1)+D(1,b_n)-C .
\]

**Proof.** Choose \(r>0\) with \(4r<\rho(q,z)\). Then \(\rho(b_n,q)\ge3r\) for all large \(n\), and Lemma 3.1 gives the inequality with \(C=C_r\). By (D2) with \(F=\{1\}\) and \(x=z\), for every \(N\) the elements \(b_n\) with large \(n\) satisfy \(D(1,b_n)\ge N\). \(\blacksquare\)

## 4. Vertices of depth at least m

A vertex of \(K\) is in general the image of a base vertex under many group elements, and each of these has its own depth. The following definition asks for a bound on all of them.

By (S3) the set \(I\) consists of finitely many orbits of \(H\). Choose one point \(p_1,\dots,p_k\) in each orbit; if \(I=H\), there is one orbit, and we choose \(p_1=1\). For a vertex \(u\) in the orbit of \(p_i\) let
\[
R(u)=\{g\in H\mid gp_i=u\},
\]
the set of *representatives* of \(u\). For \(g\in H\) we have \(R(gu)=gR(u)\).

For an integer \(m\ge0\) let \(I_m\) be the set of all vertices \(u\in I\setminus A\) such that \(D(A,g)\ge m\) for every \(g\in R(u)\). So
\[
I\setminus A=I_0\supseteq I_1\supseteq I_2\supseteq\cdots .
\]
We use the notation of Section 2 of the lesson on component labels and annular depth: \(D'\) is the set of limits of sequences of pairwise distinct points of \(D\), and \(\Omega_T=L\setminus(I\setminus T)'\).

**Lemma 4.1.**

1. For every \(m\ge0\), no point of \(L\setminus A\) is the limit of a sequence of pairwise distinct vertices in \(I\setminus I_m\). So \(L\setminus A\subseteq\Omega_{I_m}\).
2. For every finite set \(E\subseteq I\) there is \(m\) with \(E\cap I_m=\varnothing\).

**Proof.** (1) Suppose pairwise distinct vertices \(u_n\in I\setminus I_m\) converge to \(x\in L\setminus A\). Since \(A\) is closed, \(u_n\notin A\) for large \(n\); for these \(n\) there is \(a_n\in R(u_n)\) with \(D(A,a_n)<m\), by the definition of \(I_m\). Pass to a subsequence in which all \(u_n\) lie in the orbit of one \(p_i\), so that \(u_n=a_np_i\). By Lemma 1.1, \(a_n\to x\). By (D2), \(D(A,a_n)\ge m\) for large \(n\). This is a contradiction.

(2) For every \(u\in E\setminus A\) choose one \(a_u\in R(u)\). If \(m\) is larger than the finitely many numbers \(D(A,a_u)\), no point of \(E\setminus A\) lies in \(I_m\); and no point of \(A\) lies in \(I_m\). \(\blacksquare\)

By Lemma 4.1(1) and Theorem 2.1 of the lesson on component labels and annular depth, applied to the set \(T=I_m\) of allowed vertices, there is for every \(m\ge0\) a map
\[
Q_m\colon L\setminus A\to\{\text{components of }K[I_m]\}
\]
with the following properties.

- (Q1) Every \(x\in L\setminus A\) is the limit of a sequence of pairwise distinct vertices in \(I_m\), and all vertices of \(I_m\) in some neighbourhood of \(x\) in \(Y\) belong to the component \(Q_m(x)\).
- (Q2) \(Q_m\) is locally constant on the open subset \(L\setminus A\) of \(L\).

By (Q1), \(Q_m(x)\) is the only component of \(K[I_m]\) that contains a sequence of pairwise distinct vertices converging to \(x\).

## 5. Deleted vertices after a translation

For Sections 5 and 6 we fix integers \(m_n\ge0\) with \(m_n\to\infty\) and elements \(g_n\in H\) with
\[
D(A,g_n)\ge m_n ,
\]
such that the sets \(F_n=g_n^{-1}A\) shrink to a point \(q\in L\). By Lemma 2.1, every pair of sequences \((m_n)\), \((g_n)\) with \(m_n\to\infty\) and \(D(A,g_n)\ge m_n\) has a subsequence of this kind.

The translate \(g_n^{-1}(I\setminus I_{m_n+1})\) is the set of vertices \(w\) whose image \(g_nw\) is deleted at depth \(m_n+1\). The next lemma says that away from \(q\) only finitely many vertices are of this kind, and that the finite set does not depend on \(n\).

**Lemma 5.1.** For every compact set \(E\subseteq Y\setminus\{q\}\) there are a finite set \(S_E\subseteq I\) and an index \(n_E\) such that for all \(n\ge n_E\): every vertex \(w\in I\cap E\) with \(g_nw\notin I_{m_n+1}\) belongs to \(S_E\).

**Proof.** Suppose there are no such \(S_E\) and \(n_E\). Then there are indices \(n_1<n_2<\cdots\) and pairwise distinct vertices \(w_1,w_2,\dots\) in \(I\cap E\) with
\[
g_{n_j}w_j\notin I_{m_{n_j}+1} .
\]
Indeed, when \(n_1,\dots,n_{j-1}\) and \(w_1,\dots,w_{j-1}\) are chosen, the finite set \(\{w_1,\dots,w_{j-1}\}\) and the index \(n_{j-1}+1\) do not have the property of the lemma, which gives \(n_j\) and \(w_j\). Replace \((m_n)\) and \((g_n)\) by the subsequences with the indices \(n_j\); the assumptions of this section still hold. So there are pairwise distinct vertices \(w_n\in I\cap E\) with \(g_nw_n\notin I_{m_n+1}\) for all \(n\).

Pass to a subsequence such that \(w_n\) converges to a point \(z\) of the compact set \(E\) and all \(w_n\) lie in the orbit of one \(p_i\). Then \(z\in L\), because the \(w_n\) are pairwise distinct, and \(z\ne q\).

Since \(E\) is compact and \(q\notin E\), some ball \(B(q,r)\) does not meet \(E\), and \(F_n\subseteq B(q,r)\) for large \(n\). For these \(n\), \(w_n\notin F_n\), that is, \(g_nw_n\notin A\). So \(g_nw_n\) is a vertex outside \(A\) and outside \(I_{m_n+1}\), and by the definition of \(I_{m_n+1}\) there is \(c_n\in R(g_nw_n)\) with \(D(A,c_n)\le m_n\). Let \(b_n=g_n^{-1}c_n\). Then
\[
\begin{gathered}
b_np_i=w_n,\\
D(F_n,b_n)=D(A,c_n)\le m_n ,
\end{gathered}
\]
by (D1). By Lemma 1.1, \(b_n\to z\). By Corollary 3.2, \(D(1,b_n)\to\infty\) and
\[
\begin{aligned}
D(F_n,b_n)&\ge D(F_n,1)+D(1,b_n)-C\\
&\ge m_n+D(1,b_n)-C ,
\end{aligned}
\]
because \(D(F_n,1)=D(A,g_n)\ge m_n\). For large \(n\) the right side is larger than \(m_n\). This is a contradiction. \(\blacksquare\)

## 6. Labels after a translation

**Theorem 6.1.** Let \((m_n)\), \((g_n)\) and \(q\) be as in Section 5.

1. For every \(z\in L\setminus\{q\}\) there are a neighbourhood \(V_z\) of \(z\) in \(L\) and an index \(n_z\) such that for all \(n\ge n_z\) and all \(w\in V_z\): \(g_nw\notin A\) and
\[
Q_{m_n+1}(g_nw)=Q_{m_n+1}(g_nz).
\]
2. For any two points \(z,z'\in L\setminus\{q\}\) there is an index \(n_0\) such that for all \(n\ge n_0\): \(g_nz\notin A\), \(g_nz'\notin A\) and
\[
Q_{m_n+1}(g_nz)=Q_{m_n+1}(g_nz').
\]

**Proof.** (1) Choose an open neighbourhood \(O\) of \(z\) in \(Y\) and \(r>0\) such that \(\overline O\) does not meet \(B(q,r)\). Lemma 5.1 for the compact set \(\overline O\) gives a finite set \(S\subseteq I\) and an index \(n_1\). Let
\[
T=(I\cap O)\setminus S .
\]
For \(n\ge n_1\) and \(t\in T\) the vertex \(g_nt\) lies in \(I_{m_n+1}\), by Lemma 5.1. So
\[
g_nT\subseteq I_{m_n+1}\qquad(n\ge n_1).
\]
The set \(I\setminus T\) is the union of the finite set \(S\) and a subset of the closed set \(Y\setminus O\). So no point of \(O\) is a limit of pairwise distinct points of \(I\setminus T\), and \(O\cap L\subseteq\Omega_T\). By Theorem 2.1 of the lesson on component labels and annular depth there are a component \(G\) of \(K[T]\) and a neighbourhood \(V_z\subseteq O\cap L\) of \(z\) in \(L\) such that \(Q_T(w)=G\) for all \(w\in V_z\).

Choose \(n_z\ge n_1\) such that \(F_n\subseteq B(q,r)\) for \(n\ge n_z\). Fix \(n\ge n_z\) and \(w\in V_z\). Then \(w\notin F_n\), so \(g_nw\notin A\).

The map \(g_n\) sends edges of \(K\) to edges and \(T\) into \(I_{m_n+1}\). So it sends paths of \(K[T]\) to paths of \(K[I_{m_n+1}]\), and \(g_nG\) lies in one component \(G_n\) of \(K[I_{m_n+1}]\). By Theorem 2.1(1) and (2) of that lesson, \(w\) is the limit of a sequence \((t_j)\) of pairwise distinct vertices in \(G\). The vertices \(g_nt_j\) are pairwise distinct, lie in \(G_n\), and converge to \(g_nw\), because \(g_n\) is a homeomorphism of \(Y\). By the remark after (Q2),
\[
Q_{m_n+1}(g_nw)=G_n .
\]
The component \(G_n\) does not depend on \(w\in V_z\), and \(z\in V_z\). This proves (1).

(2) For \(z,z'\in L\setminus\{q\}\) write \(z\sim z'\) if the conclusion of (2) holds for them. By (1) with \(w=z\), \(z\sim z\). The relation is symmetric, and it is transitive: if the labels of \(g_nz\) and \(g_nz'\) agree for \(n\ge n_0\) and those of \(g_nz'\) and \(g_nz''\) agree for \(n\ge n_0'\), then those of \(g_nz\) and \(g_nz''\) agree for \(n\) at least the larger of \(n_0\) and \(n_0'\). By (1), \(w\sim z\) for every \(w\in V_z\). So the classes of \(\sim\) are open subsets of \(L\setminus\{q\}\). This set is connected, because \(q\) is not a cut point of \(L\), by (S1). A connected space is not the union of two or more disjoint nonempty open sets, so there is one class. \(\blacksquare\)

The threshold \(n_0\) in (2) depends on the two points. The set of labels changes with \(n\), since \(Q_{m_n+1}\) takes values in the components of a graph that depends on \(n\); the relation \(\sim\) compares labels for one \(n\) at a time.

## 7. Exercises

**7.1.** In Lemma 2.1, show that \(g_n^{-1}\to q\) along the subsequence. Let \(A_1\) be another closed subset of \(Y\) with \(1\in A_1\), \(L\not\subseteq A_1\) and \(D(A_1,g_n)\to\infty\). Show that the sets \(g_n^{-1}A_1\) shrink to the same point \(q\) along that subsequence.

**7.2.** Show that \(N(a,b)=N(b,a)\), and that \(N(a_1,b_1)\le N(a,b)\) if \(a_1\ge a\) and \(b_1\ge b\).

**7.3.** Let \(I=H\) and \(A=\{1\}\). Show that \(I_m\) is the set of all \(g\in H\) with \(D(1,g)\ge m\), that \(H\setminus I_m\) is finite for every \(m\), and that \(Q_m\) is constant on \(L\).

**7.4.** Show that every \(I_m\) is infinite and that the intersection of all \(I_m\) is empty.

**7.5.** Let \(I\subseteq L\) and \(u\in I\). Show that \(R(u)=gR(p_i)\) for every \(g\in R(u)\), where \(p_i\) is the chosen point in the orbit of \(u\), that \(R(p_i)\) is the stabilizer of \(p_i\) in \(H\), and that \(R(u)\) is infinite.

## 8. Solutions

**7.1.** Since \(1\in A\), the point \(g_n^{-1}\) lies in \(g_n^{-1}A\), and these sets shrink to \(q\); so \(g_n^{-1}\to q\). The first part of the proof of Lemma 2.1 uses only that the set is closed, contains \(1\) and has depths tending to infinity; applied to \(A_1\) it shows that the diameter of \(g_n^{-1}A_1\) tends to \(0\). These sets contain \(g_n^{-1}\), which converges to \(q\) along the subsequence. So they shrink to \(q\).

**7.2.** The reversal \((\sigma^-,\sigma^+)\mapsto(\sigma^+,\sigma^-)\) maps \(\mathcal A\) onto itself and is its own inverse. It maps the annuli counted by \(N(a,b)\) onto those counted by \(N(b,a)\). If \(a_1\ge a\) and \(b_1\ge b\), every annulus counted by \(N(a_1,b_1)\) is counted by \(N(a,b)\).

**7.3.** Here \(p_1=1\) and \(R(g)=\{g\}\), so \(I_m\) consists of the \(g\in H\setminus\{1\}\) with \(D(1,g)\ge m\). For \(m\ge1\) the condition \(D(1,g)\ge m\) excludes \(g=1\) (Exercise 5.3 of the lesson on component labels and annular depth); for \(m=0\) the set is \(H\setminus\{1\}\), and the description holds for \(m\ge1\). By Exercise 5.4 of that lesson, \(D(1,g)\ge m\) for all but finitely many \(g\). So \(H\setminus I_m\) is finite. The map \(Q_m\) is defined on \(L\setminus A=L\) and locally constant; a locally constant map on a connected space is constant.

**7.4.** By (Q1), a point of \(L\setminus A\) is the limit of a sequence of pairwise distinct vertices in \(I_m\); so \(I_m\) is infinite. If \(u\) were in every \(I_m\), Lemma 4.1(2) for \(E=\{u\}\) would be contradicted.

**7.5.** By definition \(R(p_i)=\{h\mid hp_i=p_i\}\) is the stabilizer. If \(g\in R(u)\), then \(g'p_i=u\) holds exactly if \(g^{-1}g'\) fixes \(p_i\); so \(R(u)=gR(p_i)\). By (S6) the stabilizer of \(p_i\) contains an element of infinite order, so it is infinite. This is why the definition of \(I_m\) bounds the depth of every representative: a vertex in \(L\) has infinitely many of them.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 9. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
