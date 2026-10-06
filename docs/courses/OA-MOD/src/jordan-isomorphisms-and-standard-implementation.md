# Implementing Jordan symmetries on standard forms

**Independently written mathematical draft.**

A Jordan star isomorphism preserves squares and adjoints, but it can reverse the order of multiplication on part of an algebra. Its standard-form implementation must therefore preserve the positive cone and its vector functionals. Conjugation of the entire left algebra is generally the wrong requirement.

The source target is Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise IX.1(7). We prove the assertion for arbitrary von Neumann algebras. The central splitting is proved below from Jordan identities and closed invariant subspaces; no classification by type, global faithful state, or external splitting theorem is assumed. The subsequent construction uses the written standard-form corners and equivalence Every projection has a faithful cone corner and Patching the unique comparisons, commutant form The commutant sees the same positive cone, and cone implementation uniqueness The valid quadratic identity and the source correction. The elementary operator inputs are The bounded prerequisite boundary and Finite-vector approximation and the bicommutant and normality criterion The positive-map equivalence.

Throughout, \(M\) and \(N\) are von Neumann algebras, and \(\theta:M\to N\) is a complex-linear bijection preserving adjoints and squares. This is the Jordan star convention. The adjoint requirement is essential, as the last section explains. Inner products are linear in the first variable.

## Order, normality and two polynomial identities

Write \(a\circ b=ab+ba\), without a factor of two. Polarization of squares gives

\[
 \theta(a\circ b)=\theta(a)\circ\theta(b).
\]

Conversely, square preservation follows by putting \(b=a\). The inverse map has the same properties: lift any elements of \(N\) and apply injectivity to the identities in \(M\).

The map is unital. Put \(q=\theta(1)\). Since \(1\circ a=2a\), surjectivity gives \(q\circ y=2y\) for every \(y\in N\). Taking \(y=1\) gives \(q=1\). Every positive element is the square of a self-adjoint element by BK-01. Therefore \(\theta\) and its inverse are positive. They are inverse order isomorphisms.

For self-adjoint \(a\), apply the order bounds \(-\|a\|1\le a\le\|a\|1\). They show \(\|\theta(a)\|\le\|a\|\), and applying the inverse gives equality. The decomposition \(x=\operatorname{Re}x+i\operatorname{Im}x\) consequently gives \(\|\theta(x)\|\le2\|x\|\), which suffices for boundedness. A bounded increasing positive net is characterized by its least upper bound in the order. An order bijection preserves that characterization, in both directions; its image net is bounded by the image of the original bound. NP-04 proves normality of \(\theta\) and \(\theta^{-1}\).

Two identities will control multiplication. Direct expansion gives

\[
 \begin{gathered}
 2aba=a\circ(a\circ b)-a^2\circ b,\\
 [[a,b],c]
 =a\circ(b\circ c)-b\circ(a\circ c).
 \end{gathered}
\]

Thus \(\theta\) preserves the triple product \(aba\), and

\[
 \begin{gathered}
 \theta([[a,b],c])\\
 =[[\theta(a),\theta(b)],\theta(c)].
 \end{gathered}
 \tag{JI.1}
\]

These statements hold for arbitrary elements, not only self-adjoint ones. They use Jordan products only; they do not assert that \(\theta\) preserves a single commutator.

## Separate the two defects for one pair

Fix self-adjoint \(a,b\in M\), and abbreviate

\[
 \begin{gathered}
 A=\theta(a),\quad B=\theta(b),\\
 d=[a,b],\quad h=\theta(d),\quad k=[A,B].
 \end{gathered}
\]

Both \(h\) and \(k\) are skew-adjoint. The elementary identity

\[
 [a,b]^2=(a\circ b)^2-2ab^2a-2ba^2b
\]

contains only squares and triple products on its right. Apply JI-01 to it. This proves \(h^2=k^2\). Putting \(c=d\) in (JI.1) gives \([k,h]=0\). Hence

\[
 h^2=k^2,\qquad hk=kh.
 \tag{JI.2}
\]

For \(y=\theta(c)\), apply (JI.1) twice to \([d,[d,c]]\). One obtains \([k,[k,y]]\). Alternatively expand that same expression in the domain as \(d^2c-2dcd+cd^2\), and use preservation of the Jordan product and the triple product. Its image is \(h^2y-2hyh+yh^2\). Equation (JI.2) cancels the square terms. Surjectivity of \(\theta\) is used here to obtain

\[
 \begin{gathered}
 hyh=kyk\\
 (y\in N).
 \end{gathered}
 \tag{JI.3}
\]

Define the multiplicative and reversed defects by

\[
 \begin{gathered}
 D(a,b)=\theta(ab)-AB=\tfrac12(h-k),\\
 E(a,b)=\theta(ab)-BA=\tfrac12(h+k).
 \end{gathered}
\]

For this fixed pair write them as \(D,E\). They are skew-adjoint. Equation (JI.2) gives \(DE=ED=0\), while (JI.3) gives

\[
 DyE+EyD=0\qquad(y\in N).
\]

Multiply the latter identity on the left by \(D\). Since \(DE=0\), this gives \(D^2yE=0\). A skew-adjoint bounded operator satisfies \(\ker D^2=\ker D\): if \(D^2v=0\), then

\[
 \|Dv\|^2=\langle D^*Dv,v\rangle
          =-\langle D^2v,v\rangle=0.
\]

Apply this to each vector \(yE\xi\). We have proved the stronger separation

\[
 \begin{gathered}
 D(a,b)\,N\,E(a,b)\\
 =\{0\}\\
 (a=a^*,\ b=b^*).
 \end{gathered}
 \tag{JI.4}
\]

The insertion of every \(y\in N\) is crucial. The bare equation \(DE=0\) would not alone justify the global central decomposition.

## Central supports and two polarization steps

Represent \(N\) concretely on its Hilbert space \(H\). For \(t\in N\), let \(z(t)\) be the orthogonal projection onto

\[
 \overline{\operatorname{span}\{xty:
       x\in N,\ y\in H\}}.
\]

This notation uses \(y\) as a Hilbert vector. The subspace is invariant under \(N\) and its adjoints. It is also invariant under \(N'\) and its adjoints, because those operators commute with \(x\) and \(t\). The orthogonal projection therefore belongs to \(N'\cap N''=Z(N)\), by BK-02. It fixes the range of \(t\). Any central projection fixing that range fixes the whole displayed subspace. Thus \(z(t)\) is the least central projection satisfying \(z(t)t=t\); for \(t=0\), it is zero.

If \(uNv=\{0\}\), then \(u\) kills the entire subspace defining \(z(v)\), so \(uz(v)=0\). Since \(z(v)\) is central, \(u=(1-z(v))u\), whence minimality gives

\[
 z(u)z(v)=0.
\]

Conversely, that central orthogonality implies \(uNv=\{0\}\). No normality assumption on \(u\) or \(v\) is needed for this central-support argument.

We now extend (JI.4) to different pairs. Keep \(b=b^*\) fixed. Apply (JI.4) to \(a+c,b\), where \(a,c\) are self-adjoint, and subtract its two diagonal versions. Bilinearity gives

\[
 \begin{gathered}
 D(a,b)yE(c,b)\\
 +D(c,b)yE(a,b)=0.
 \end{gathered}
\]

Multiply by the central projection \(z(D(a,b))\). The first term is unchanged. The second vanishes, because (JI.4) implies \(z(D(a,b))E(a,b)=0\). Hence \(D(a,b)NE(c,b)=\{0\}\) for all self-adjoint \(a,c,b\).

Next replace the common second argument by \(b+d\) and subtract the two diagonal versions of this new conclusion. This gives

\[
 \begin{gathered}
 D(a,b)yE(c,d)\\
 +D(a,d)yE(c,b)=0.
 \end{gathered}
\]

Again multiply by \(z(D(a,b))\). The first term is unchanged, and the second vanishes by the already proved fixed-second-argument conclusion. Therefore

\[
 \begin{gathered}
 D(a,b)\,N\,E(c,d)\\
 =\{0\}.
 \end{gathered}
 \tag{JI.5}
\]

whenever \(a,b,c,d\) are self-adjoint. In particular every central support of a multiplicative defect is orthogonal to every central support of a reversed defect. Both polarization steps used sums of self-adjoint elements, so the hypotheses of JI-02 were retained throughout.

## Split the whole map along a central projection

Let \(z\) be the supremum of the central projections \(z(D(a,b))\), with \(a,b\) self-adjoint, and set \(q=1-z\). This supremum exists concretely: take the projection onto the closed span of their ranges. That subspace reduces \(N\) and \(N'\), so its projection is central; its range characterization proves it is the least upper bound. There is no countability restriction on the family.

By construction \(qD(a,b)=0\). Equation (JI.5) shows that every projection in the defining family annihilates \(E(c,d)\). Its range is therefore orthogonal to their closed span, and \(zE(c,d)=0\). Complex bilinearity extends both conclusions from self-adjoint pairs to all pairs. We have proved

\[
 \begin{gathered}
 q\theta(ab)\\
 =q\theta(a)\theta(b),\\
 (1-q)\theta(ab)\\
 =(1-q)\theta(b)\theta(a).
 \end{gathered}
 \tag{JI.6}
\]

Put \(p=\theta^{-1}(q)\). It is a projection, because the inverse preserves adjoints and squares. For every \(x\in M\), preservation of triple products gives

\[
 \begin{gathered}
 \theta(pxp+(1-p)x(1-p))\\
 =q\theta(x)q+(1-q)\theta(x)(1-q)\\
 =\theta(x).
 \end{gathered}
\]

The last equality uses centrality of \(q\). Injectivity makes every \(x\) block diagonal with respect to \(p\). Multiplying on either side by \(p\) proves \(px=xp\). Thus \(p\) is central, and

\[
 \begin{gathered}
 \theta(px)=q\theta(x),\\
 \theta((1-p)x)=(1-q)\theta(x).
 \end{gathered}
\]

Surjectivity now identifies the restrictions as a normal star isomorphism \(Mp\to Nq\) and a normal star anti-isomorphism \(M(1-p)\to N(1-q)\). Their inverses are normal by JI-01, or by the same order argument on the corners. The terms may be zero; a zero summand will simply have a zero Hilbert space. We have supplied the complete central splitting needed below.

## Implement the multiplicative and reversed parts

First let \(\alpha:M_1\to M_2\) be a star isomorphism between algebras in arbitrary standard forms \((M_i,H_i,J_i,P_i)\). SE-10 provides the unique complex-linear unitary \(V\) with

\[
 \begin{gathered}
 VxV^*=\alpha(x),\\
 VJ_1=J_2V,\quad VP_1=P_2.
 \end{gathered}
\]

For every \(v\in P_1\), algebra intertwining immediately gives \(\omega_{Vv}\circ\alpha=\omega_v\), where \(\omega_v(x)=\langle xv,v\rangle\).

Now let \(\beta:M_1\to M_2\) be a star anti-isomorphism. Define

\[
 \begin{gathered}
 \pi(x)=J_2\beta(x)^*J_2,\\
 \pi(x)\in M_2'.
 \end{gathered}
 \tag{JI.7}
\]

The adjoint and conjugation each conjugate scalars, so \(\pi\) is complex-linear. Reversal of multiplication by \(\beta\), followed by the adjoint, gives

\[
 \begin{gathered}
 \pi(xy)=J_2\beta(x)^*\beta(y)^*J_2\\
 =\pi(x)\pi(y).
 \end{gathered}
\]

It preserves adjoints and is bijective onto \(M_2'\), since \(J_2M_2J_2=M_2'\). It and its inverse preserve positive order, so they are normal by JI-01's net argument. VP-01 proves that \((M_2',H_2,J_2,P_2)\) is itself a standard form. Apply SE-10 to \(\pi\). The resulting unitary \(V\) maps \(P_1\) onto \(P_2\), intertwines the conjugations, and satisfies \(VxV^*=\pi(x)\).

For \(w\in P_2\), use \(J_2w=w\) and antiunitarity to obtain

\[
 \begin{gathered}
 \langle J_2\beta(x)^*J_2w,w\rangle\\
 =\langle w,\beta(x)^*w\rangle
 =\langle\beta(x)w,w\rangle.
 \end{gathered}
\]

Consequently this unitary also satisfies \(\omega_{Vv}\circ\beta=\omega_v\) for every \(v\in P_1\). Its algebra intertwining is with the commutant action (JI.7). The required cone-vector identity concerns the original left action, and the displayed calculation is the reason both descriptions agree there.

## Assemble the cone unitary and prove canonicity

Apply JI-04 to the given \(\theta:M_1\to M_2\), obtaining central projections \(p,q\). For a central projection in a standard form, the central axiom gives \(J_1pJ_1=p\), so its standard corner projection \(pJ_1pJ_1\) is just \(p\). SE-03 therefore gives the standard form of \(M_1p\) on \(pH_1\), with cone \(pP_1\); the complementary corner has cone \((1-p)P_1\). Moreover

\[
 \begin{gathered}
 H_1=pH_1\oplus(1-p)H_1,\\
 P_1=pP_1\oplus(1-p)P_1.
 \end{gathered}
\]

For the cone equality, both central projections preserve the cone by SE-03, and the cone is closed under addition. The same statements hold for \(q\) in the second form. Both conjugations preserve these summands.

JI-05 implements the multiplicative corner by \(V_+:pH_1\to qH_2\) and the antimultiplicative corner by \(V_-:(1-p)H_1\to(1-q)H_2\). On a zero corner take the unique map between zero Hilbert spaces. The direct sum

\[
 U_\theta=V_+\oplus V_-
\]

is a complex-linear surjective unitary. The corner cone equalities give \(U_\theta P_1=P_2\), and the corner conjugation identities give \(U_\theta J_1=J_2U_\theta\).

Every algebra element is block diagonal for these central decompositions. Write \(v=pv+(1-p)v\in P_1\), use the functional identity of each corner, and add. Orthogonality eliminates cross terms and proves

\[
 \begin{gathered}
 \omega_{U_\theta v}\circ\theta=\omega_v\\
 (v\in P_1).
 \end{gathered}
 \tag{JI.8}
\]

Putting \(v=U_\theta^{-1}\xi_2\) gives precisely the source's identity for every \(\xi_2\in P_2\) and every \(x\in M_1\).

Uniqueness follows from JR-03. Explicitly, two such cone unitaries send each \(v\in P_1\) to positive vectors representing the same normal functional on \(M_2\); SE-11 makes those vectors equal. The complex span of the cone is dense, so the unitaries agree. In particular the answer is independent of choices in any central splitting, including choices on an abelian summand where the two product orders coincide.

The identity map has the identity unitary. If \(\rho:M_2\to M_3\) is another Jordan star isomorphism, the composition of its cone unitary with \(U_\theta\) maps cones onto cones and satisfies (JI.8) for \(\rho\theta\). Uniqueness proves

\[
 U_{\rho\theta}=U_\rho U_\theta,
 \qquad U_{\theta^{-1}}=U_\theta^*.
\]

Finally JR-01/03 applied to \(U_\theta\) recovers the same Jordan map, since its cone-vector functionals are (JI.8) and such functionals separate algebra elements. Thus, with \(j_i(x)=(x+J_ix^*J_i)/2\),

\[
 U_\theta j_1(x)U_\theta^*
       =j_2(\theta(x)).
 \tag{JI.9}
\]

This operator identity holds on the entire Hilbert space. The unsymmetrized identity (JI.8) is asserted on the positive cone, as required. The construction makes no sigma-finiteness or separability assumption.

## Two matrix checks distinguish the hypotheses

Consider \(M=M_2(\mathbb C)\oplus M_2(\mathbb C)\) in its direct-sum Hilbert–Schmidt standard form, and define

\[
 \theta(x,y)=(x,y^{\mathsf T}).
\]

The multiplicative central projection is \(p=q=(1,0)\). The cone consists of pairs of positive matrices, the conjugation takes adjoints in both entries, and the canonical unitary is

\[
 U_\theta(s,t)=(s,t^{\mathsf T}).
\]

Transposition preserves the sum of squared matrix-entry moduli, is complex-linear, and commutes with the adjoint operation. It maps positive matrices onto positive matrices. Thus the displayed map is indeed a cone unitary intertwining the conjugations. For positive matrices \(s,t\), both sides of (JI.8) equal

\[
 \operatorname{Tr}(xs^2)+\operatorname{Tr}(yt^2),
\]

by finite trace cyclicity and invariance of trace under transposition. Taking the second algebra entry \(y=E_{11}\) and the second Hilbert vector \(t=E_{12}\) gives quadratic values one and zero before and after transport, exactly as in JR-03. Thus even this direct sum of two matrix algebras precludes an unsymmetrized all-Hilbert-vector extension.

The star hypothesis cannot be dropped. Let \(D=\operatorname{diag}(2,1)\), and let \(T(x)=DxD^{-1}\) on \(M_2(\mathbb C)\). This is a complex-linear associative isomorphism, hence preserves squares and Jordan products. But the positive matrix

\[
 a=\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]

is sent to

\[
 T(a)=\begin{pmatrix}1&2\\ {1/2}&1\end{pmatrix},
\]

which is not self-adjoint and therefore not positive. If a cone unitary satisfied (JI.8) for \(T\), its surjectivity on the cone would make every cone-vector functional nonnegative on \(T(a)\). SE-11 represents every ordinary vector functional by a cone vector; BK-01's positivity criterion would then imply \(T(a)\ge0\), a contradiction. This explains why the source's Jordan terminology must be read with its operator-algebra star convention.
