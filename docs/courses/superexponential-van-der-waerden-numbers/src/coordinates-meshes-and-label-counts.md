# Coordinates, meshes and label counts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson sets up the cyclic group on which the two-colouring of the main theorem of [Van der Waerden numbers](van-der-waerden-numbers.md) is built, and proves the counting estimates that make a random colouring work. Each element of the group is read through \(2D\) circle coordinates, and each coordinate circle is cut into small intervals; the tuple of intervals containing the coordinates of an element is its *label*. A colouring of labels induces a colouring of the group. Two counts drive the proof: the number of label words along all progressions is only \(e^{o(k^{1/2})}\) (Lemma 4.1), and the number of local patterns through a fixed label is at most \((CDh)^{6D}\), independently of how fine the intervals are (Lemma 4.3). The tools are those of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md).

Throughout, \(k\) is an integer larger than an absolute threshold, logarithms are natural, and all constants in \(O(\cdot)\) are absolute. Statements "for large \(k\)" hold above an absolute threshold, independent of the number of colours \(r\).

## 1. Parameters and a dilation

Set
\[
c=10^{-5},\quad\delta=\tfrac1{10},\quad\gamma=\tfrac1{100},\quad D=\lceil k^{1/10}\rceil,\quad M=\lceil k^{1/2}\rceil,\quad h_0=D^2,\quad p=k^{-1/20},\quad H=k^{-2},\quad\eta=\frac1{1000D},
\]
with \(k\) so large that \(h_0<2M<k\), and the integer *dilation*
\[
\lambda=\prod_{\ell\le h_0,\ \ell\ \text{prime}}\ell^{\lfloor\log(2M)/\log\ell\rfloor}.
\]

**Lemma 1.1** (Dilation of short periods). \(\log\lambda\le h_0\log(2M)\). If \(1\le h\le2M\), every prime power \(\ell^a\) dividing \(h\) with \(\ell\le h_0\) divides \(\lambda\). Consequently \(h\mid\lambda\) when \(h\le h_0\), and for every integer \(t\) the number \(s=h/\gcd(h,\lambda t)\) is either \(1\) or larger than \(h_0\).

*Proof.* Each of the at most \(h_0\) factors is at most \(2M\). If \(\ell^a\mid h\le2M\), then \(a\le\lfloor\log(2M)/\log\ell\rfloor\), so the whole \(\ell\)-part of \(h\) divides \(\lambda\) and hence \(\gcd(h,\lambda t)\). Every prime factor of \(s\) therefore exceeds \(h_0\). \(\square\)

## 2. The cyclic group and its coordinates

By Lemma 4.1 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md), choose a prime \(P\) with \(k<P\le2k^2\), and let \(q\) be the least power of \(P\) with \(q\ge k^{ck/D}\). Then
\[
k^{ck/D}\le q\le2k^2k^{ck/D},\qquad ck\log k\le D\log q\le ck\log k+D\log(2k^2). \tag{2.1}
\]
Since \(h_0<k<P\), \(\gcd(\lambda,q)=1\). Put
\[
H_x=H/\lambda,\qquad\alpha=q^{-(D+1)},\qquad N=q^D,\qquad G=\mathbb Z/N\mathbb Z .
\]
The following orders of magnitude are used repeatedly:
\[
D=O(k^{1/10}),\quad M=O(k^{1/2}),\quad\log\lambda=O(k^{1/5}\log k),\quad\log q=O(k^{9/10}\log k). \tag{2.2}
\]

A *progression* of \(G\) is a sequence \(n_j=n_0+jd\) (\(0\le j<k\)) with \(d\ne0\). Every nonzero element of \(G\) has order a power of \(P\), hence at least \(P>k\), so the \(k\) terms are distinct.

Let \(\mathbb T=\mathbb R/\mathbb Z\) be the circle of circumference \(1\). For \(1\le i\le D\), the homomorphisms
\[
x_i(n)=\frac n{q^i}\bmod1,\qquad y_i(n)=\lambda x_i(n)
\]
are well defined on \(G\) because \(q^i\mid N\). Write \(x(n)=(x_i(n))_i\), \(y(n)=(y_i(n))_i\), with representatives \(\hat x(n)\in[0,1)^D\) and \(\tilde y(n)\in[-1/2,1/2)^D\). The point \(1/2=-1/2\) of \(\mathbb T\) is the *cut* of the second system, and \(\rho(Y)=\operatorname{dist}_{\mathbb T}(Y,1/2)\) is the distance to it; \(0\le\rho\le1/2\), and \(\rho\) is \(1\)-Lipschitz.

## 3. Two meshes

*The uniform mesh* \(U\) consists of the intervals \([aH_x,(a+1)H_x)\), \(0\le a<k^2\lambda\), an exact partition of \([0,1)\).

*The adaptive mesh* \(V\) becomes finer near the cut. Put
\[
R=\log\Bigl(1+\frac1{2\alpha}\Bigr),\qquad m=\lceil k^2R\rceil,\qquad a_\ell=\alpha\bigl(e^{\ell R/m}-1\bigr)\quad(0\le\ell\le m),
\]
so \(a_0=0\) and \(a_m=1/2\). The \(2m\) intervals
\[
[-\tfrac12+a_\ell,-\tfrac12+a_{\ell+1}),\qquad[\tfrac12-a_{\ell+1},\tfrac12-a_\ell)\qquad(0\le\ell<m)
\]
partition \([-1/2,1/2)\); we use the same names for their images in \(\mathbb T\). For \(X,Y\in\mathbb T\), \(U(X)\) and \(V(Y)\) denote the intervals containing them. The *label* of \((X,Y)\in\mathbb T^D\times\mathbb T^D\) and of \(n\in G\) are
\[
L(X,Y)=\bigl((U(X_i))_{i=1}^D,(V(Y_i))_{i=1}^D\bigr),\qquad L(n)=L(x(n),y(n)),
\]
elements of the finite set \(\mathcal L=U^D\times V^D\). A label specifies the intervals themselves, including their positions.

**Lemma 3.1** (Widths). For every \(I\in V\) and every \(Y\) in the closure of \(I\),
\[
\tfrac14H\bigl(\rho(Y)+\alpha\bigr)\le|I|\le2H\bigl(\rho(Y)+\alpha\bigr)\le2H .
\]
Moreover \(|V|=2m=O(k^3\log k)\).

*Proof.* For large \(k\), \(\alpha\le1/4\) and \(R\ge1\). With \(\theta=R/m\), \(k^2R\le m\le2k^2R\) gives \(H/2\le\theta\le H\). On the closure of either interval with index \(\ell\), \(\rho(Y)+\alpha\) ranges between \(b=\alpha e^{\ell\theta}\) and \(be^\theta\), while \(|I|=b(e^\theta-1)\). Hence \(1-e^{-\theta}\le|I|/(\rho(Y)+\alpha)\le e^\theta-1\), and for \(0\le\theta\le1\) these bounds lie between \(\theta/2\) and \(2\theta\). Also \(\rho+\alpha\le3/4\). Finally \(R\le(D+1)\log q=O(k\log k)\) by (2.1), so \(2m=O(k^3\log k)\). \(\square\)

**Lemma 3.2** (Neighbourhoods). For \(I\in V\) with \(w=|I|\), let \(\mathcal N(I)\) be the set of points of \(\mathbb T\) within distance \(w\) of the closure of \(I\). Every \(J\in V\) whose closure meets \(\mathcal N(I)\) has \(|J|\ge w/16\), and \(\mathcal N(I)\) contains at most \(49\) endpoints of the mesh.

*Proof.* Fix \(Y_0\) in the closure of \(I\) and put \(r_0=\rho(Y_0)+\alpha\). Points of \(\mathcal N(I)\) are within \(2w\le4Hr_0\) of \(Y_0\), so by Lemma 3.1 and the Lipschitz property, \(\rho(Y)+\alpha\ge(1-4H)r_0\ge r_0/2\) there. At a point of the closure of \(J\) in \(\mathcal N(I)\), Lemma 3.1 gives \(|J|\ge\frac18Hr_0\ge w/16\). The arc \(\mathcal N(I)\) has length \(3w\); consecutive mesh endpoints in it enclose a mesh interval of length at least \(w/16\), so \(b\) endpoints satisfy \((b-1)w/16\le3w\), and \(b\le49\). \(\square\)

Near the cut the mesh is extremely fine. For counting along rotating coordinates we ignore it within distance \(\eta\) of the cut, through the *truncated output*
\[
V_\eta(Y)=V(Y)\ \text{if }\rho(Y)\ge\eta,\qquad V_\eta(Y)=*\ \text{if }\rho(Y)<\eta,
\]
where \(*\) is a new symbol.

**Lemma 3.3** (Truncated complexity). On every arc of length at most \(4H\), \(V_\eta\) is constant between at most \(16004D\) breakpoints, and its values at the breakpoints are determined.

*Proof.* The part of the arc where \(\rho\ge\eta\) has at most two components. In it, consecutive mesh endpoints are at least \(H\eta/4\) apart, by Lemma 3.1 at an endpoint; so it contains at most \(4H/(H\eta/4)+2=16/\eta+2\) endpoints. Adding the at most two points with \(\rho=\eta\) gives at most \(16/\eta+4=16000D+4\) breakpoints; on \(\{\rho<\eta\}\) the output is constant. The half-open conventions fix the values at the breakpoints. \(\square\)

## 4. Counting label words and local patterns

**Lemma 4.1** (Global label words). The number \(T_{\mathrm{glob}}\) of words \((L(n_j))_{0\le j<k}\) over all progressions of \(G\) satisfies
\[
\log T_{\mathrm{glob}}=O\bigl(D(\log k+\log\lambda)\bigr)=O(k^{3/10}\log k)=o(M).
\]

*Proof.* Fix one coordinate circle with a partition having \(F\) endpoints (the cut included), represented by numbers \(\tau\in[0,1)\), and let \(a,b\in[0,1)\) be a start and a step. For \(0\le j<k\), \(a+jb\in[0,k)\), and the interval containing \(a+jb\bmod1\) is determined by the signs of \(a+jb-(\tau+z)\) for all endpoints \(\tau\) and integers \(-1\le z\le k\). These are at most \(3k^2F\) affine functions of \((a,b)\), so by Corollary 1.2 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md) at most \(9(3k^2F+1)^2\) scalar words occur. Letting the starts and steps of the \(2D\) coordinates vary independently only enlarges the count. With \(F=|U|+|V|=k^2\lambda+O(k^3\log k)\), \(\log F=O(\log k+\log\lambda)\), and \(T_{\mathrm{glob}}\le[9(3k^2F+1)^2]^{2D}\). The orders of magnitude follow from (2.2) and \(M\ge k^{1/2}\). \(\square\)

For the local patterns fix an integer \(h\) with \(h_0<h\le2M\) and a vector \(t\in\{0,\dots,h-1\}^D\). In coordinate \(i\) put \(s_i=h/\gcd(h,\lambda t_i)\). The second-system coordinate \(i\) is *stationary* if \(s_i=1\) and *rotating* otherwise; by Lemma 1.1 a rotating coordinate has \(s_i>h_0\).

**Definition 4.2** (Eligible patterns). For \(x,y\in\mathbb T^D\) and \(u,v\in\mathbb R^D\), form
\[
X_z=x+\frac zh(t+u),\qquad Y_z=y+\frac zh(\lambda t+v)\qquad(0\le z<h)\quad\text{in }\mathbb T^D .
\]
A position \(z\) is *regular* if \(\rho(Y_{z,i})\ge\eta\) in every rotating coordinate. Record \(L(X_z,Y_z)\) at regular positions and \(*\) at the others. The resulting word in \((\mathcal L\cup\{*\})^h\) is an *eligible pattern for \(h,t\)* if it has a realization with:

1. at least \(h/2\) regular positions, whose labels are pairwise distinct;
2. \(|u_i|\le H_x\) for all \(i\), and \(|v_i|\le H\) in every rotating coordinate;
3. \(|v_i|\le|V(Y_{z,i})|\) at every regular position \(z\), in every stationary coordinate \(i\).

Different realizations of one word give the same pattern. The relative bound in condition 3 is what makes the next count independent of the width of the intervals.

**Lemma 4.3** (Local patterns through a label). There is an absolute constant \(C\) such that for every \(h_0<h\le2M\) and every \(\beta\in\mathcal L\), the number of pairs \((t,\text{pattern})\), with \(t\in\{0,\dots,h-1\}^D\) and an eligible pattern for \(h,t\) containing \(\beta\), is at most \((CDh)^{6D}\).

*Proof.* Fix \(t\) and a position \(z_0\) at which the pattern equals \(\beta\); it is regular. In each scalar coordinate, write the value at \(z_0\) as a real number \(a\) in the interval prescribed by \(\beta\), and let \(b\) be the drift, \(u_i\) or \(v_i\). At a position \(z\) an unreduced value is
\[
a+\tau_z+\frac{z-z_0}hb,\qquad\tau_z=\frac{(z-z_0)t_i}h\ \text{or}\ \frac{(z-z_0)\lambda t_i}h,
\]
with \(\tau_z\) fixed once \(t,z_0,z,i\) are. We keep only the constraints on \(a,b\) at the anchor, which can only enlarge the count.

*First system.* \(a\) lies in an interval of length \(H_x\) and \(|b|\le H_x\); since \(|z-z_0|/h<1\), the values at \(z\) lie in a fixed real interval of length at most \(3H_x\), which meets at most four lifts of endpoints of \(U\).

*Stationary second-system coordinates.* Let \(I\) be the interval of \(\beta\); condition 3 at \(z_0\) gives \(|b|\le|I|\), and \(\tau_z=(z-z_0)\lambda t_i/h\) is an integer. So the values at \(z\) lie, modulo \(1\), in \(\mathcal N(I)\), which contains at most \(49\) mesh endpoints (Lemma 3.2), and their real range has length at most \(3|I|<1\), so each endpoint has at most one relevant lift.

*Rotating second-system coordinates.* The interval of \(\beta\) has length at most \(2H\) and \(|b|\le H\), so the values at \(z\) lie in a range of length at most \(4H\), on which at most \(16004D\) breakpoints determine \(V_\eta\) (Lemma 3.3), again with one lift each.

In every case the breakpoint lifts are fixed before \(a,b\) vary, and comparing \(a+\tau_z+(z-z_0)b/h\) with them gives at most \(16004Dh\) affine functions of \((a,b)\) over all \(z<h\). Their signs determine the scalar outputs at all positions, including the values at breakpoints. By Corollary 1.2 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md), at most \(9(16004Dh+1)^2\le C_0(Dh)^2\) scalar output sequences occur, for an absolute \(C_0\). The outputs of all \(2D\) coordinates, with truncation in the rotating ones, determine the pattern: a position is \(*\) exactly when some rotating output is \(*\), and otherwise the outputs form its label. With \(h^D\) choices of \(t\) and \(h\) of \(z_0\), the number of pairs is at most
\[
h^{D+1}\bigl[C_0(Dh)^2\bigr]^{2D}=C_0^{2D}D^{4D}h^{5D+1}\le(CDh)^{6D}.\qquad\square
\]

## 5. Exercises

**5.1.** Compute \(\lambda\) when \(h_0=4\) and \(2M=10\), and verify the conclusion of Lemma 1.1 for all \(h\le10\) and \(t\in\{0,1\}\).

**5.2.** Show that the intervals of \(V\) adjacent to the cut have length \(\alpha(e^{R/m}-1)\), and that this is between \(\alpha H/2\) and \(2\alpha H\).

**5.3.** In the proof of Lemma 4.1, explain why the integers \(z\) with \(-1\le z\le k\) suffice to determine the interval containing \(a+jb\bmod1\).

**5.4.** Why does condition 3 of Definition 4.2 bound \(|v_i|\) by the width of the local interval rather than by \(H\)? Describe what would go wrong in the count of Lemma 4.3 for a stationary coordinate with a very narrow anchor interval if only \(|v_i|\le H\) were known.

## 6. Solutions

**5.1.** The primes at most \(4\) are \(2,3\), with \(\lfloor\log10/\log2\rfloor=3\) and \(\lfloor\log10/\log3\rfloor=2\), so \(\lambda=2^3\cdot3^2=72\). Every \(h\le10\) has its \(2\)- and \(3\)-parts dividing \(72\): \(h\in\{1,\dots,10\}\) gives \(s=h/\gcd(h,72t)\in\{1,5,7\}\), the values \(5,7\) occurring for \(h\in\{5,10\}\) and \(h=7\) with \(t=1\); both exceed \(h_0=4\).

**5.2.** For \(\ell=0\), the interval \([-1/2,-1/2+a_1)\) has length \(a_1=\alpha(e^\theta-1)\) with \(\theta=R/m\in[H/2,H]\), and \(\theta\le e^\theta-1\le2\theta\) for \(\theta\le1\).

**5.3.** Let \(z=\lfloor a+jb\rfloor\in\{0,\dots,k-1\}\). The interval containing \(a+jb\bmod1\) is determined by the position of \(a+jb\) relative to the lifts \(\tau+z'\) of the endpoints with \(z'\in\{z-1,z,z+1\}\), which cover \([z,z+1)\) together with the neighbouring lifts of an interval that wraps around \(0\); all these have \(-1\le z'\le k\). The comparisons with the lifts of the endpoint \(0\), which belongs to both meshes, also determine \(z\).

**5.4.** A stationary coordinate does not rotate, so its values stay within \(|v_i|\) of the anchor. With only \(|v_i|\le H\), the values could cross up to about \(H/|I|\) mesh intervals around a narrow anchor interval \(I\) near the cut, and the number of breakpoints, hence the count, would depend on the width of \(I\), which can be as small as about \(\alpha H\). The relative bound keeps the values in \(\mathcal N(I)\), with at most \(49\) breakpoints.

## References

- [OpenAI-vdW] OpenAI, *Quantitative superexponential bounds for van der Waerden numbers*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf
