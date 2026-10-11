# Surjective isometries and normality

A surjective complex-linear isometry remembers more than the norm: it carries the identity to a unitary, and removing that unitary leaves a Jordan *-isomorphism. For von Neumann algebras this also proves normality. Neither the original isometry nor the Jordan map is assumed multiplicative.

We follow the programme's proof of the isometry classification in *Tensor products of Banach and Hilbert spaces, Jordan homomorphisms and isometries of C*-algebras*, Section 11, making its bounded-functional factorization explicit. The classical result is [Kadison, *Isometries of Operator Algebras*, Theorem 7, printed 330, proof 331–333](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-kadison/1950s/1951_IsometriesOfOperatorAlgebras.pdf). The argument below supplies the proof rather than using that citation as an input.

The preceding readings provide states and their positivity test, ST03, cyclic representations, BG02–03, the universal bidual and normal extensions, UB04–05, bounded-operator polar decomposition, BK07, and spectral step approximation in a von Neumann algebra, SK08. Continuous functional calculus and positive order are proved in AC1–4. Inner products are linear first.

The remaining direct proof steps are BG03, UB05, AB01 and SK04.

## Functionals that attain their norm at a contraction

First, let \(F\) be a bounded complex-linear functional on a unital C*-algebra and suppose
\[
 F(h)=\|F\|,\qquad 0\le h\le1.
 \tag{KI.1}
\]
Then \(F\) is positive. Write \(c=\|F\|\). Functional calculus gives \(\|h+z(1-h)\|\le1\) whenever \(|z|\le1\), since every spectral value is a convex combination of \(1\) and \(z\). Thus \(|c+zF(1-h)|\le c\), and a choice of phase forces \(F(1-h)=0\). Consequently \(F(1)=c\). There is nothing to prove if \(c=0\). For \(x=x^*\), the unitary \(e^{itx}\) satisfies
\[
 F(e^{itx})=c+itF(x)+O(t^2).
\]
The remainder estimate follows by applying the bounded functional to the norm-convergent exponential series. The inequality \(\operatorname{Re}F(e^{itx})\le c\), for positive and negative \(t\), forces \(\operatorname{Im}F(x)=0\). For \(0\le x\le1\), the norm bound on \(1-x\) now gives \(F(x)=c-F(1-x)\ge0\). Scaling proves positivity.

We also need a support calculation that assumes no normality. Suppose \(F(a)=\|F\|\), \(\|a\|\le1\), and \(a=ap\) for a projection \(p\). For every \(x\) and complex \(z\), the cross terms vanish, so
\[
 \|a+zx(1-p)\|^2
 =\|aa^*+|z|^2x(1-p)x^*\|
 \le1+|z|^2\|x\|^2.
 \tag{KI.2}
\]
Choose the phase of \(z\) so that \(zF(x(1-p))\) is nonnegative real. With \(r=|z|>0\),
\[
 \|F\|+r|F(x(1-p))|
 \le\|F\|\sqrt{1+r^2\|x\|^2}.
\]
Subtract \(\|F\|\), divide by \(r\), and let \(r\downarrow0\). It follows that
\[
 F(x)=F(xp)\qquad\text{for every }x.
 \tag{KI.3}
\]

Now let \(B\) be any C*-algebra, and suppose \(f\in B^*\) and \(a\in B\) satisfy
\[
 \|f\|=\|a\|=f(a)=1.
 \tag{KI.4}
\]
UB04–05 extend \(f\) isometrically to the normal functional \(F(X)=X(f)\) on the von Neumann algebra \(N=B^{**}\). We identify \(B\) with its isometric image in \(N\). No normality of \(f\) on an originally given von Neumann algebra \(B\) is asserted here.

Take the bounded-operator polar decomposition in \(N\),
\[
 a^*=v|a^*|,\qquad a=|a^*|v^*,\qquad p=vv^*.
\]
BK07 constructs the partial isometry, and its commutation with \(N'\) puts it in \(N\). We have \(a=ap\). Put \(\omega(x)=F(xv^*)\). Its norm is at most one, whereas \(\omega(|a^*|)=F(a)=1\); hence its norm is one, and (KI.1) makes it positive. Equation (KI.3) gives
\[
 F(x)=F(xp)=\omega(xv)\qquad(x\in N).
 \tag{KI.5}
\]
Let \((\pi,K,\xi)\) be its cyclic representation from BG02–03. Since \(N\) is unital, nondegeneracy gives \(\pi(1)=I\), and \(\|\xi\|^2=\omega(1)=1\). With \(\eta=\pi(v)\xi\), we obtain
\[
 \|\eta\|\le1,\qquad
 f(x)=\langle\pi(x)\eta,\xi\rangle\quad(x\in B).
 \tag{KI.6}
\]
Finally \(f(a)=1\) and \(\|\pi(a)\|\le1\) imply \(\|\eta\|=1\) and \(\pi(a)\eta=\xi\), by expanding \(\|\pi(a)\eta-\xi\|^2\). Positivity of \(I-\pi(a^*a)\) then gives
\[
 \pi(a^*a)\eta=\eta,\qquad
 f(x)=\langle\pi(a^*x)\eta,\eta\rangle.
 \tag{KI.7}
\]
Indeed its positive square root annihilates \(\eta\), because its quadratic value there is \(\|\eta\|^2-\|\pi(a)\eta\|^2=0\). This proves exactly the functional representation needed below; no uniqueness theorem for polar decompositions of functionals is used.

## A unital onto isometry preserves Jordan products

Let \(J:A\to B\) be a surjective complex-linear isometry of unital C*-algebras with \(J(1)=1\). For every state \(\rho\) of \(B\), the functional \(\rho J\) has norm at most one and takes the value one at the identity. Its norm is therefore one, and (KI.1) makes it positive. The state test in ST03 proves that \(J\) is positive. The same argument applies to \(J^{-1}\). Both maps preserve adjoints: a self-adjoint element is a difference of two positive ones, and every element is \(h+ik\) with \(h,k\) self-adjoint.

First suppose \(A=M\) and \(B=N\) are von Neumann algebras. The maps are inverse order isomorphisms between the intervals \([0,1]\). We verify that the extreme points of such an interval are precisely the projections. If \(0\le x\le1\) is not a projection, the nonzero element \(y=x-x^2\) satisfies
\[
 x-y=x^2\in[0,1],\qquad x+y=1-(1-x)^2\in[0,1],
\]
so \(x\) is not extreme. Conversely, let a projection \(e\) be the midpoint of \(b,c\in[0,1]\). Compressing by \(1-e\) gives a sum of two positive operators equal to zero. Thus \((1-e)b(1-e)=0\), so \(b^{1/2}(1-e)=0\) and \(b=eb=be\). Compressing \((1-b)+(1-c)\) by \(e\) similarly gives \((1-b)e=0\), so \(b=e\); then \(c=e\).

An affine bijection preserves extreme points and its inverse does too. Hence \(J\) maps projections onto projections. If \(e\) and \(q\) are orthogonal projections, \(J(e)+J(q)=J(e+q)\) is a projection. Writing \(r=J(e)\), \(s=J(q)\), we have \(rs+sr=0\). Compression by \(r\) gives \(rsr=0\), and \((sr)^*sr=rsr\) gives \(sr=rs=0\). Therefore for every finite real spectral sum,
\[
 J\left(\left(\sum_j t_je_j\right)^2\right)
 =\sum_j t_j^2J(e_j)
 =\left(\sum_j t_jJ(e_j)\right)^2.
 \tag{KI.8}
\]
SK08 approximates every bounded self-adjoint element in norm by such sums. Norm continuity of \(J\) and of squaring yields \(J(h^2)=J(h)^2\) for every self-adjoint \(h\).

For general unital \(A,B\), use UB05 to regard their Banach biduals as von Neumann algebras. The second adjoint \(J^{**}:A^{**}\to B^{**}\) is an onto isometry: the second adjoint of \(J^{-1}\) is its inverse, and both have norm at most one, as follows by testing the defining dual norms. It is unital. Indeed, \(j_A(1)\) acts as the identity on \(j_A(A)\); separate ultraweak continuity of multiplication and density from UB05 extend this to all \(A^{**}\). Thus \(j_A(1)=1_{A^{**}}\), and likewise for \(B\), while \(J^{**}j_A=j_BJ\).

The von Neumann algebra argument applies to \(J^{**}\). Restriction to \(A\) therefore gives
\[
 J(h^2)=J(h)^2\quad(h=h^*),\qquad
 J(x\circ y)=J(x)\circ J(y),\qquad
 x\circ y=\tfrac12(xy+yx).
 \tag{KI.9}
\]
For the second identity, first expand \((h+k)^2\) for self-adjoint \(h,k\), then use complex bilinearity. Together with preservation of adjoints and bijectivity, this is precisely a Jordan *-isomorphism. It does not assert multiplicativity.

## Removing the unitary from an arbitrary onto isometry

Let \(A\) be a nonzero unital C*-algebra, \(B\) any C*-algebra, and \(T:A\to B\) a surjective complex-linear isometry. Set \(u=T(1)\), so \(\|u\|=1\), and consider
\[
 \mathcal D_u=\{f\in B^*:\|f\|=1,\ f(u)=1\}.
 \tag{KI.10}
\]
This family separates the points of \(B\). For every state \(\rho\) of \(A\), the functional \(f=\rho T^{-1}\) lies in \(\mathcal D_u\), since \(T^{-1}\) carries the unit ball onto the unit ball. If all these functionals vanish at \(y\), all states vanish at \(T^{-1}y=h+ik\). Their real and imaginary parts show that all states vanish at \(h\) and \(k\); the norm-detection statement in ST03 gives \(h=k=0\).

Apply KI01 to each \(f\in\mathcal D_u\) and the contraction \(a=u\). Its representation may depend on \(f\), but (KI.7) always gives
\[
 \begin{aligned}
 f(y-yu^*u)
 &=\langle\pi(u^*y)\eta,\eta\rangle
   -\langle\pi(u^*y)\pi(u^*u)\eta,\eta\rangle\\
 &=0\qquad(y\in B).
 \end{aligned}
 \tag{KI.11}
\]
Separation gives \(y=yu^*u\) for every \(y\in B\). Applying this to \(y^*\) and taking adjoints also gives \(y=u^*uy\). Thus \(u^*u\), which belongs to \(B\), is a two-sided identity for \(B\). In particular \(u^*uu^*=u^*\). Now (KI.7) gives \(f(y-uu^*y)=0\) for every \(f\in\mathcal D_u\), because \(u^*(y-uu^*y)=0\). Separation again gives \(y=uu^*y\). Taking \(y=1_B\) proves \(uu^*=1_B\). Consequently \(u\) is unitary.

Left multiplication by \(u^*\) is an onto isometry, since
\(\|u^*y\|^2=\|y^*uu^*y\|=\|y^*y\|=\|y\|^2\).
The map \(J(x)=u^*T(x)\) is therefore a unital onto isometry. KI02 proves
\[
 T(x)=uJ(x),\qquad
 u=T(1)\text{ unitary},\qquad
 J\text{ a unital Jordan *-isomorphism}.
 \tag{KI.12}
\]
If \(A=0\), surjectivity forces \(B=0\), and the conclusion holds with their zero identity and zero map. No separability, faithful state, trace, or multiplicativity hypothesis has entered the proof.

## Normality for von Neumann algebras

Let \(T:M\to N\) be a surjective complex-linear isometry of von Neumann algebras. KI03 writes it as \(uJ\). The maps \(J,J^{-1}\) are positive by KI02. For a bounded increasing positive net \(x_i\uparrow x\), \(J(x)\) is an upper bound of \(J(x_i)\). If \(y\) is any self-adjoint upper bound of that net, \(J^{-1}(y)\) is an upper bound of all \(x_i\), so \(J^{-1}(y)\ge x\) and \(y\ge J(x)\). Thus
\[
 J(x_i)\uparrow J(x).
 \tag{KI.13}
\]
The bounded positive map criterion NP04 makes \(J\) normal. The vector-series description in CP06 proves the required continuity directly. For a fixed \(u\in N\) and a normal functional
\[
 \rho(y)=\sum_n\langle y\xi_n,\eta_n\rangle,
 \qquad \sum_n\|\xi_n\|^2<\infty,\quad\sum_n\|\eta_n\|^2<\infty,
\]
we have
\[
 \rho(uy)=\sum_n\langle y\xi_n,u^*\eta_n\rangle,
 \qquad\sum_n\|u^*\eta_n\|^2\leq\|u\|^2\sum_n\|\eta_n\|^2<\infty.
\]
Thus every normal functional pulls back to a normal functional under left multiplication by \(u\). By the defining weak-star topology, this multiplication is ultraweakly continuous. Consequently \(T=uJ\) is normal. Applying the same argument to \(T^{-1}\) makes it normal too.

In particular, every map in the pointwise ultraweakly continuous group of isometries considered in AG01 is an ultraweak homeomorphism. This justifies applying the real-time maps to its weak-star continuous strips without restricting the group to automorphisms.
