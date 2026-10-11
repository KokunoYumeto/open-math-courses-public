# First Čech cohomology of a compact metric space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(Z\) be a compact metric space covered by two open sets \(U\) and \(V\), and let \(u\) be a locally constant function on \(U\cap V\). Is \(u\) the difference of a locally constant function on \(V\) and one on \(U\)? On the circle, covered by two overlapping arcs, the answer can be no: the overlap has two pieces, and a function with different values on them is not such a difference. The first Čech cohomology group \(\check H^1(Z;k)\), with coefficients in an abelian group \(k\), collects the obstructions of this kind for all finite open covers.

This lesson defines the group by finite open covers and their nerves and proves the working form of its vanishing (Theorem 3.1): \(\check H^1(Z;k)=0\) exactly when, on every finite open cover, every system of locally constant transition functions is a system of differences of locally constant functions. From this follow the statement for two open sets (Corollary 4.1), the nonvanishing for the circle (Corollary 4.3), the passage to retracts (Corollary 4.4), and the extension of locally constant functions across a point (Corollary 4.5). The last section shows that in a space of covering dimension at most one every class on a closed subset comes from the whole space (Proposition 5.1), so vanishing passes to closed subsets (Corollary 5.2).

Only finite covers, constant coefficients and degree one occur. Čech cohomology of a cover with coefficients in a sheaf, in all degrees, is the subject of [Čech cohomology](course:AG-QC/cech-cohomology); the locally constant cocycles of Section 3 are overlap data of that kind for the sheaf of locally constant functions with values in \(k\).

We assume the core course [Point-Set Topology (C90)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90) and, in Section 5, the definition of covering dimension from [Covering dimension and finite trivializing covers](course:index-theory-of-elliptic-operators/covering-dimension-and-finite-trivializing-covers#2-covering-dimension).

## 1. Covers, nerves and cochains

Throughout, \(Z\) is a compact metric space and \(k\) an abelian group, written additively. A map into \(k\) is *locally constant* if every point has a neighbourhood on which it is constant; equivalently it is continuous for the discrete topology on \(k\). A locally constant map on a connected set is constant, and a locally constant map on a compact set takes finitely many values.

A *finite open cover* of \(Z\) is a family \(\mathcal U=(U_i)_{i\in I}\) of open sets with union \(Z\), indexed by a finite set \(I\). Members may be empty or repeated. Its *nerve* records which members meet: a pair \((i,j)\) with \(U_i\cap U_j\ne\varnothing\) is an *edge*, a triple \((i,j,l)\) with \(U_i\cap U_j\cap U_l\ne\varnothing\) a *triangle*; repeated indices are allowed.

A *\(1\)-cochain* on \(\mathcal U\) assigns to every edge \((i,j)\) an element \(c_{ij}\in k\) with
\[
c_{ii}=0,\qquad c_{ji}=-c_{ij}.
\]
It is a *cocycle* if for every triangle \((i,j,l)\)
\[
c_{ij}+c_{jl}=c_{il}.
\]
For a function \(\varepsilon:I\to k\), the *coboundary* \(\delta\varepsilon\) is the cochain
\[
(\delta\varepsilon)_{ij}=\varepsilon_j-\varepsilon_i .
\]
Every coboundary is a cocycle. Cocycles form a group \(Z^1(\mathcal U;k)\), coboundaries a subgroup \(B^1(\mathcal U;k)\), and
\[
H^1(\mathcal U;k)=Z^1(\mathcal U;k)/B^1(\mathcal U;k).
\]

## 2. Refinement and the group

A finite open cover \(\mathcal V=(V_a)_{a\in J}\) *refines* \(\mathcal U\) if there is a map \(\rho:J\to I\), a *refinement map*, with \(V_a\subseteq U_{\rho(a)}\) for all \(a\). For a cochain \(c\) on \(\mathcal U\) the *pullback* \(\rho^\ast c\) is the cochain on \(\mathcal V\) with
\[
(\rho^\ast c)_{ab}=c_{\rho(a)\rho(b)} .
\]
This is defined, because \(V_a\cap V_b\ne\varnothing\) implies \(U_{\rho(a)}\cap U_{\rho(b)}\ne\varnothing\). Pullback sends cocycles to cocycles and \(\delta\varepsilon\) to \(\delta(\varepsilon\circ\rho)\), so it induces a homomorphism \(H^1(\mathcal U;k)\to H^1(\mathcal V;k)\).

**Lemma 2.1.** Let \(\rho,\rho'\) be two refinement maps from \(\mathcal V\) to \(\mathcal U\) and \(c\) a cocycle on \(\mathcal U\). Then \(\rho^\ast c-\rho'^\ast c\) is a coboundary. So the homomorphism \(H^1(\mathcal U;k)\to H^1(\mathcal V;k)\) does not depend on the refinement map.

**Proof.** For \(a\in J\) with \(V_a\ne\varnothing\) put \(\eta_a=c_{\rho(a)\rho'(a)}\); this is defined because \(V_a\subseteq U_{\rho(a)}\cap U_{\rho'(a)}\). For empty \(V_a\) put \(\eta_a=0\). Let \((a,b)\) be an edge of \(\mathcal V\) and \(z\in V_a\cap V_b\). The four sets with indices \(\rho(a),\rho'(a),\rho(b),\rho'(b)\) contain \(z\), so the cocycle identity applies to any three of them:
\[
\begin{aligned}
c_{\rho(a)\rho(b)}={}&c_{\rho(a)\rho'(a)}+c_{\rho'(a)\rho'(b)}\\
&+c_{\rho'(b)\rho(b)} .
\end{aligned}
\]
That is, \((\rho^\ast c)_{ab}-(\rho'^\ast c)_{ab}=\eta_a-\eta_b\), the value of the coboundary \(\delta(-\eta)\). \(\blacksquare\)

Any two finite open covers \((U_i)_{i\in I}\) and \((U'_j)_{j\in I'}\) have a common refinement, the cover \((U_i\cap U'_j)_{(i,j)\in I\times I'}\).

**Definition 2.2.** A *Čech \(1\)-class* on \(Z\) is represented by a pair \((\mathcal U,c)\) of a finite open cover and a cocycle on it. Two pairs \((\mathcal U,c)\) and \((\mathcal U',c')\) represent the same class if on some common refinement \(\mathcal V\), with refinement maps \(\rho,\rho'\), the cocycle \(\rho^\ast c-\rho'^\ast c'\) is a coboundary. Classes are added by pulling representatives back to a common refinement and adding there. The group of classes is \(\check H^1(Z;k)\), the *first Čech cohomology group of \(Z\) with coefficients in \(k\)*.

By Lemma 2.1 the condition does not depend on the refinement maps, and if it holds on \(\mathcal V\) it holds on every refinement of \(\mathcal V\); For transitivity, pull the two relations back to a common refinement of the two covers on which they hold and add them; the same argument shows that the sum of two classes does not depend on the representatives or on the common refinement. So "represent the same class" is an equivalence relation and addition is well defined. The class of \((\mathcal U,c)\) is zero exactly when \(c\) pulls back to a coboundary on some finite open refinement of \(\mathcal U\). Hence:

> \(\check H^1(Z;k)=0\) if and only if for every finite open cover \(\mathcal U\) and every cocycle \(c\) on it there are a finite open refinement \(\mathcal V\), with refinement map \(\rho\), and \(\varepsilon\) with \(\rho^\ast c=\delta\varepsilon\).

The definition uses only the open sets of \(Z\), so homeomorphic spaces have isomorphic groups.

## 3. Locally constant cocycles

Let \(\mathcal U=(U_i)_{i\in I}\) be a finite open cover of \(Z\). A *locally constant cocycle* on \(\mathcal U\) is a family of locally constant maps \(u_{ij}:U_i\cap U_j\to k\), one for each pair \((i,j)\), with
\[
\begin{gathered}
u_{ii}=0,\qquad u_{ji}=-u_{ij},\\
u_{ij}+u_{jl}=u_{il}\ \text{ on }U_i\cap U_j\cap U_l .
\end{gathered}
\]
It *splits* if there are locally constant maps \(f_i:U_i\to k\) with
\[
f_j-f_i=u_{ij}\quad\text{on }U_i\cap U_j\quad\text{for all }i,j.
\]
A cocycle \(c\) on the nerve gives the locally constant cocycle with the constant maps \(u_{ij}=c_{ij}\); we say that \(c\) splits if this one does.

**Theorem 3.1.** For a compact metric space \(Z\) and an abelian group \(k\) the following are equivalent.

1. \(\check H^1(Z;k)=0\).
2. Every locally constant cocycle on every finite open cover of \(Z\) splits.
3. Every cocycle on the nerve of every finite open cover of \(Z\) splits.

**Proof.** (2) implies (3) by the remark before the theorem.

*(3) implies (1).* Let \(c\) be a cocycle on \(\mathcal U=(U_i)\), split by locally constant maps \(h_i:U_i\to k\). Every \(z\in Z\) has an open neighbourhood \(N_z\) that lies in every \(U_i\) containing \(z\) and on which each of these finitely many \(h_i\) is constant. Finitely many of the sets \(N_z\) cover \(Z\); call them \(V_a=N_{z_a}\), \(a\in J\), and choose \(\rho(a)\) with \(z_a\in U_{\rho(a)}\). Then \(V_a\subseteq U_{\rho(a)}\), and \(h_{\rho(a)}\) is constant on \(V_a\), with value \(\varepsilon_a\), say. If \(y\in V_a\cap V_b\), then
\[
\begin{aligned}
\varepsilon_b-\varepsilon_a&=h_{\rho(b)}(y)-h_{\rho(a)}(y)\\
&=c_{\rho(a)\rho(b)} .
\end{aligned}
\]
So \(\rho^\ast c=\delta\varepsilon\).

*(1) implies (2).* Let \((u_{ij})\) be a locally constant cocycle on \(\mathcal U=(U_i)_{i\in I}\).

*Shrinking.* Let \(\lambda>0\) be a Lebesgue number of \(\mathcal U\): every subset of \(Z\) of diameter less than \(\lambda\) lies in some \(U_i\). Put \(U_i'=\{z:d(z,Z\setminus U_i)>\lambda/4\}\), with \(d(z,\varnothing)=\infty\). These sets are open; they cover \(Z\), because the closed ball of radius \(\lambda/3\) about \(z\) lies in some \(U_i\); and \(\overline{U_i'}\subseteq U_i\). Put \(C_{ij}=\overline{U_i'}\cap\overline{U_j'}\), a compact subset of \(U_i\cap U_j\).

*A fine cover.* On the compact set \(C_{ij}\) the map \(u_{ij}\) takes finitely many values, and the sets where it takes them are disjoint and compact. So there is \(\delta>0\) such that, for all \(i,j\), two points of \(C_{ij}\) at distance less than \(\delta\) have the same value of \(u_{ij}\). Take \(\delta\) also smaller than a Lebesgue number of \((U_i')\), and choose a finite open cover \((W_a)_{a\in J}\) of \(Z\) by sets of diameter less than \(\delta\), with \(\rho:J\to I\) such that \(W_a\subseteq U'_{\rho(a)}\). If \(W_a\cap W_b\ne\varnothing\), this intersection lies in \(C_{\rho(a)\rho(b)}\) and has diameter less than \(\delta\), so \(u_{\rho(a)\rho(b)}\) is constant on it. Let \(c_{ab}\) be its value.

*\(c\) is a cocycle on \((W_a)\).* The identities \(c_{aa}=0\) and \(c_{ba}=-c_{ab}\) come from those of \(u\). At a point of \(W_a\cap W_b\cap W_e\) the identity \(u_{\rho(a)\rho(b)}+u_{\rho(b)\rho(e)}=u_{\rho(a)\rho(e)}\) gives \(c_{ab}+c_{be}=c_{ae}\).

*Using (1).* There are a finite open cover \((Z_\alpha)_{\alpha\in A}\), a map \(r:A\to J\) with \(Z_\alpha\subseteq W_{r(\alpha)}\), and elements \(\kappa_\alpha\in k\) with
\[
\begin{gathered}
\kappa_\beta-\kappa_\alpha=c_{r(\alpha)r(\beta)}\\
\text{whenever }Z_\alpha\cap Z_\beta\ne\varnothing .
\end{gathered}
\]
Write \(\sigma(\alpha)=\rho(r(\alpha))\in I\); then \(Z_\alpha\subseteq U_{\sigma(\alpha)}\), and for \(z\in Z_\alpha\cap Z_\beta\) the displayed identity reads \(\kappa_\beta-\kappa_\alpha=u_{\sigma(\alpha)\sigma(\beta)}(z)\).

*The splitting.* For \(i\in I\) and \(z\in U_i\cap Z_\alpha\) put
\[
f_i(z)=\kappa_\alpha+u_{\sigma(\alpha)i}(z).
\]
This does not depend on \(\alpha\): if also \(z\in Z_\beta\), then
\[
\begin{aligned}
&\kappa_\beta+u_{\sigma(\beta)i}(z)-\kappa_\alpha-u_{\sigma(\alpha)i}(z)\\
&\quad=u_{\sigma(\alpha)\sigma(\beta)}(z)+u_{\sigma(\beta)i}(z)\\
&\qquad-u_{\sigma(\alpha)i}(z)=0
\end{aligned}
\]
by the cocycle identity at \(z\). So \(f_i:U_i\to k\) is well defined, and it is locally constant, because on the open set \(U_i\cap Z_\alpha\) it is a constant plus a locally constant map. For \(z\in U_i\cap U_j\cap Z_\alpha\),
\[
\begin{aligned}
f_j(z)-f_i(z)&=u_{\sigma(\alpha)j}(z)-u_{\sigma(\alpha)i}(z)\\
&=u_{ij}(z).
\end{aligned}
\]
So \((u_{ij})\) splits. \(\blacksquare\)

## 4. Consequences

**Corollary 4.1** (two open sets). Let \(\check H^1(Z;k)=0\) and \(Z=U\cup V\) with \(U,V\) open. For every locally constant \(u:U\cap V\to k\) there are locally constant maps \(f_U:U\to k\) and \(f_V:V\to k\) with
\[
u=f_V-f_U\quad\text{on }U\cap V .
\]

**Proof.** On the cover \((U_1,U_2)=(U,V)\) put \(u_{12}=u\), \(u_{21}=-u\), \(u_{11}=0\), \(u_{22}=0\). Every triple of indices has a repeated index, and for such triples the cocycle identity follows from the first two conditions. Theorem 3.1 gives the splitting. \(\blacksquare\)

**Corollary 4.2.** Let \(k\ne0\). If \(Z=U\cup V\) with \(U\) and \(V\) connected and open and \(U\cap V\) not connected, then \(\check H^1(Z;k)\ne0\).

**Proof.** Write \(U\cap V=S\cup T\) with \(S,T\) disjoint, nonempty and open, and let \(u\) be \(g\ne0\) on \(S\) and \(0\) on \(T\). If \(\check H^1(Z;k)\) were zero, Corollary 4.1 would give \(u=f_V-f_U\) with \(f_U\), \(f_V\) locally constant on connected sets, hence constant; but \(u\) is not constant. \(\blacksquare\)

**Corollary 4.3** (the circle). For \(k\ne0\) and every simple closed curve \(C\), \(\check H^1(C;k)\ne0\).

**Proof.** It suffices to treat \(S^1\). Let \(U=S^1\setminus\{1\}\) and \(V=S^1\setminus\{-1\}\). Both are homeomorphic to open intervals, hence connected, and \(U\cap V\) is the union of the open upper and the open lower half circle, which is not connected. Apply Corollary 4.2. \(\blacksquare\)

**Corollary 4.4** (retracts). Let \(A\subseteq Z\) be closed and \(r:Z\to A\) a retraction, that is, a continuous map with \(r(a)=a\) for \(a\in A\). If \(\check H^1(Z;k)=0\), then \(\check H^1(A;k)=0\).

**Proof.** Let \((V_i)\) be a finite cover of \(A\) by relatively open sets and \((u_{ij})\) a locally constant cocycle on it. The sets \(r^{-1}(V_i)\) form a finite open cover of \(Z\), and the maps \(u_{ij}\circ r\) a locally constant cocycle on it. By Theorem 3.1 it is split by locally constant maps \(f_i\) on \(r^{-1}(V_i)\). Since \(V_i\subseteq r^{-1}(V_i)\) and \(r\) is the identity on \(A\), the restrictions \(f_i|_{V_i}\) split \((u_{ij})\). By Theorem 3.1 for \(A\), \(\check H^1(A;k)=0\). \(\blacksquare\)

**Corollary 4.5** (extension across a point). Let \(\check H^1(Z;k)=0\), and let \(x\in Z\) be a point such that \(Z\setminus\{x\}\) is connected. Let \(V\) be an open neighbourhood of \(x\) and \(u:V\setminus\{x\}\to k\) locally constant. Then \(u\) extends to a locally constant map on \(V\). If \(x\) is not an isolated point of \(Z\), the extension is unique.

**Proof.** Let \(U=Z\setminus\{x\}\), an open set with \(U\cup V=Z\) and \(U\cap V=V\setminus\{x\}\). By Corollary 4.1, \(u=f_V-f_U\) on \(V\setminus\{x\}\). Since \(U\) is connected, \(f_U\) is a constant \(c\), and \(f_V-c\) is a locally constant map on \(V\) that extends \(u\). If \(x\) is not isolated, \(V\setminus\{x\}\) is dense in \(V\), and two continuous maps into the discrete space \(k\) that agree on a dense set agree. \(\blacksquare\)

## 5. Dimension at most one: closed subsets

Recall that \(\dim Z\le1\) means that every finite open cover of \(Z\) has an open refinement in which every point lies in at most two members. For compact \(Z\) finitely many members of the refinement cover \(Z\), so the refinement can be taken finite; we index it by its members, so that the indices of a triangle take at most two distinct values.

Let \(A\subseteq Z\) be closed. A finite open cover \(\mathcal O=(O_s)_{s\in S}\) of \(Z\) restricts to the cover \(\mathcal O|_A=(O_s\cap A)_{s\in S}\) of \(A\), and a cocycle \(\hat c\) on \(\mathcal O\) restricts to the cocycle \(\hat c|_A\) on \(\mathcal O|_A\) that has the same values on those edges and triangles whose intersections meet \(A\). Restriction commutes with pullback along refinements and sends coboundaries to coboundaries, so it defines a homomorphism \(\check H^1(Z;k)\to\check H^1(A;k)\).

**Proposition 5.1.** Let \(Z\) be a compact metric space with \(\dim Z\le1\) and \(A\subseteq Z\) closed. Let \(c\) be a cocycle on a finite cover \(\mathcal V=(V_i)_{i\in I}\) of \(A\) by relatively open sets. There are a finite open cover \(\mathcal O=(O_s)_{s\in S}\) of \(Z\), a refinement map \(\rho\) from \(\mathcal O|_A\) to \(\mathcal V\), and a cocycle \(\hat c\) on \(\mathcal O\) with
\[
\hat c|_A=\rho^\ast c .
\]
Consequently the restriction \(\check H^1(Z;k)\to\check H^1(A;k)\) is onto.

**Proof.** Choose open sets \(W_i\subseteq Z\) with \(W_i\cap A=V_i\). The sets \(W_i\) and \(Z\setminus A\) form a finite open cover of \(Z\). Let \(\mathcal O=(O_s)_{s\in S}\) be a finite open refinement of it in which every point lies in at most two members. A member \(O_s\) that meets \(A\) does not lie in \(Z\setminus A\), so it lies in some \(W_i\); choose such an \(i\) as \(\rho(s)\). For the other \(s\) choose \(\rho(s)\) arbitrarily. Then \(O_s\cap A\subseteq V_{\rho(s)}\) for all \(s\).

For an edge \((s,t)\) of \(\mathcal O\) put
\[
\hat c_{st}=\begin{cases}c_{\rho(s)\rho(t)}&\text{if }O_s\cap O_t\text{ meets }A,\\0&\text{otherwise.}\end{cases}
\]
In the first case \(V_{\rho(s)}\cap V_{\rho(t)}\ne\varnothing\), so the value is defined. Then \(\hat c_{ss}=0\) and \(\hat c_{ts}=-\hat c_{st}\). The cocycle identity has to be checked on triangles only, and in a triangle two of the three indices are equal; for such triples the identity follows from \(\hat c_{ss}=0\) and \(\hat c_{ts}=-\hat c_{st}\). So \(\hat c\) is a cocycle, and on the edges of \(\mathcal O|_A\) it equals \(\rho^\ast c\) by definition.

The class of \((\mathcal O,\hat c)\) restricts to the class of \((\mathcal O|_A,\rho^\ast c)\), which is the class of \((\mathcal V,c)\). \(\blacksquare\)

**Corollary 5.2.** Let \(\dim Z\le1\) and \(A\subseteq Z\) closed. If \(\check H^1(Z;k)=0\), then \(\check H^1(A;k)=0\).

**Proof.** Let \(c\) be a cocycle on a finite relatively open cover \(\mathcal V\) of \(A\), and take \(\mathcal O\), \(\rho\), \(\hat c\) as in Proposition 5.1. Since \(\check H^1(Z;k)=0\), there are a finite open refinement \(\mathcal Q\) of \(\mathcal O\), with refinement map \(\tau\), and \(\varepsilon\) with \(\tau^\ast\hat c=\delta\varepsilon\). Restricting to \(A\): the cover \(\mathcal Q|_A\) refines \(\mathcal V\) through \(\rho\circ\tau\), and on its edges
\[
\begin{aligned}
(\rho\circ\tau)^\ast c&=\tau^\ast(\hat c|_A)\\
&=(\tau^\ast\hat c)|_A=\delta\varepsilon .
\end{aligned}
\]
So the class of \((\mathcal V,c)\) is zero. \(\blacksquare\)

The interval \([0,1]\), and so every arc, has \(\dim\le1\) and vanishing first Čech cohomology (Exercise 6.4); the circle has \(\dim\le1\) and nonvanishing first Čech cohomology for \(k\ne0\) (Corollary 4.3). The dimensions are by Theorems 3.2 and 4.2 of the lesson on covering dimension: a compact subset of the line has \(\dim\le1\), and the circle is a union of two closed arcs.

## 6. Exercises

**6.1.** Let \(Z\) be the disjoint union of two nonempty compact metric spaces \(Z_1,Z_2\). Show that \(\check H^1(Z;k)=0\) if and only if \(\check H^1(Z_1;k)=0\) and \(\check H^1(Z_2;k)=0\).

**6.2.** Show that a compact metric space \(Z\) in which every point has arbitrarily small neighbourhoods that are both open and closed has \(\check H^1(Z;k)=0\).

**6.3.** Let \(u\) be the function on \(U\cap V\) used for the circle in Corollary 4.3, with \(k=\mathbb F_2\) and \(g=1\). Describe the locally constant maps \(f_U,f_V\) with \(u=f_V-f_U\) that exist on the cover of \(S^1\setminus\{i\}\) by \(U\setminus\{i\}\) and \(V\setminus\{i\}\). Why is this no contradiction?

**6.4.** Show that \(\check H^1([0,1];k)=0\), using Theorem 3.1(3) and a Lebesgue number.

**6.5.** Let \(Z\) be compact metric with \(\check H^1(Z;\mathbb F_2)=0\), and let \(x\) be a point such that \(Z\setminus\{x\}\) is connected and \(x\) is not isolated. Show that there is no open neighbourhood \(V\) of \(x\) such that \(V\setminus\{x\}\) is the union of two disjoint nonempty open sets both having \(x\) in their closure.

## 7. Solutions

**6.1.** \(Z_1\) is a retract of \(Z\): map \(Z_2\) to one point of \(Z_1\). So Corollary 4.4 gives one direction. Conversely, let \((u_{ij})\) be a locally constant cocycle on a finite open cover \((U_i)\) of \(Z\). Its restrictions to the covers \((U_i\cap Z_1)\) and \((U_i\cap Z_2)\) split, by maps \(f_i^1\) and \(f_i^2\). Since \(Z_1,Z_2\) are open in \(Z\), the map \(f_i\) on \(U_i\) that equals \(f_i^1\) on \(U_i\cap Z_1\) and \(f_i^2\) on \(U_i\cap Z_2\) is locally constant, and these maps split \((u_{ij})\).

**6.2.** Let \(c\) be a cocycle on \((U_i)_{i\in I}\). Every point has an open and closed neighbourhood inside some \(U_i\); finitely many of them, \(N_1,\dots,N_m\), cover \(Z\). The sets \(P_1=N_1\), \(P_e=N_e\setminus(N_1\cup\dots\cup N_{e-1})\) are open, pairwise disjoint, cover \(Z\), and \(P_e\subseteq U_{\rho(e)}\) for a suitable \(\rho\). On this refinement the only edges are \((e,e)\) for nonempty \(P_e\), where \(\rho^\ast c\) is zero. So \(\rho^\ast c=\delta0\).

**6.3.** Here \(u=1\) on the open upper half circle and \(u=0\) on the open lower half circle. Removing \(i\) cuts \(U\) into two open arcs: the first quadrant arc \(U_a\) between \(1\) and \(i\), and the arc \(U_b\) from \(i\) through \(-1\) and \(-i\) to \(1\). It cuts \(V\) into the second quadrant arc \(V_a\) between \(i\) and \(-1\), and the arc \(V_b\) from \(-1\) through \(-i\) and \(1\) to \(i\). Let \(f_U=1\) on \(U_a\) and \(0\) on \(U_b\), and \(f_V=1\) on \(V_a\) and \(0\) on \(V_b\). The intersection of the two sets has three pieces. On the first quadrant arc, which lies in \(U_a\cap V_b\), \(f_V-f_U=0-1=1\) in \(\mathbb F_2\). On the second quadrant arc, in \(U_b\cap V_a\), \(f_V-f_U=1-0=1\). On the lower half circle, in \(U_b\cap V_b\), \(f_V-f_U=0\). So \(f_V-f_U=u\). This is no contradiction: the proof of Corollary 4.2 uses that \(U\) and \(V\) are connected, and \(U\setminus\{i\}\), \(V\setminus\{i\}\) are not.

**6.4.** Let \(c\) be a cocycle on a finite open cover \((U_i)\) of \([0,1]\), and \(\lambda\) a Lebesgue number. Choose \(0=x_0<x_1<\dots<x_m=1\) with \(x_e-x_{e-1}<\lambda/2\), and indices \(i_e\) with \([x_{e-1},x_e]\subseteq U_{i_e}\). Define \(h_i\) on \(U_i\) as follows: for \(z\in U_i\cap[x_{e-1},x_e]\),
\[
\begin{aligned}
h_i(z)={}&c_{i_1i_2}+c_{i_2i_3}+\dots\\
&+c_{i_{e-1}i_e}+c_{i_ei} .
\end{aligned}
\]
The sums are defined: \(x_e\in U_{i_e}\cap U_{i_{e+1}}\), and \(z\in U_{i_e}\cap U_i\). At a division point \(z=x_e\) the two rules agree, because \(c_{i_ei}=c_{i_ei_{e+1}}+c_{i_{e+1}i}\) there. So \(h_i\) is well defined and constant on each piece \(U_i\cap[x_{e-1},x_e]\); since these finitely many pieces are closed in \(U_i\) and the rules agree on overlaps, \(h_i\) is locally constant. For \(z\in U_i\cap U_j\cap[x_{e-1},x_e]\), \(h_j(z)-h_i(z)=c_{i_ej}-c_{i_ei}=c_{ij}\). So \(c\) splits, and Theorem 3.1 gives the claim.

**6.5.** If \(V\setminus\{x\}=S\cup T\) were such a decomposition, the map \(u\) equal to \(1\) on \(S\) and \(0\) on \(T\) would be locally constant on \(V\setminus\{x\}\). By Corollary 4.5 it would extend to a locally constant map on \(V\), which is constant near \(x\); but \(u\) takes both values in every neighbourhood of \(x\).

## References

- OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026: the extension across a point (Corollary 4.5) is used in its Section 8, the statement on closed subsets (Proposition 5.1) in its Section 10. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
