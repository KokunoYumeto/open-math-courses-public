# The bounded trace ideal and cyclic transport

All Hilbert spaces below are complex, complete and possibly nonseparable or zero-dimensional. Inner products are linear in the first variable. Operators are bounded and everywhere defined unless a different qualification is given. A sum of nonnegative numbers over an arbitrary set means the supremum of its finite subsums. Absolutely summable complex families are summed by finite-subset limits. Zorn's maximality principle is the set-theoretic assumption used to choose orthonormal bases.

The proofs give the trace ideal between two Hilbert spaces, its complete norm, the basis-independent trace and rectangular cyclicity. They use no unbounded spectral theorem, Fredholm criterion or differential-operator calculus. The original programme expression is dedicated under CC0 1.0 Universal, to the extent rights are held.

<a id="AN03-TRC-001"></a>

## AN03-TRC-001 — Hilbert and positive-root foundations

### Orthogonal projection, bases and adjoints

Let \(M\) be a closed subspace of a Hilbert space \(H\), and let \(d=\inf_{y\in M}\|x-y\|\). Choose \(y_n\in M\) with \(\|x-y_n\|^2\to d^2\). The parallelogram identity gives
\[
\|y_n-y_k\|^2
=2\|x-y_n\|^2+2\|x-y_k\|^2
 -4\left\|x-\frac{y_n+y_k}{2}\right\|^2\longrightarrow0.
\]
Completeness and closedness give a limit \(y\in M\) attaining the infimum. Minimizing \(\|x-y-tz\|^2\) for real \(t\), and then replacing \(z\) by \(iz\), proves \(x-y\perp M\). The decomposition \(H=M\oplus M^\perp\) is unique. Its projection \(P_M\) is linear and has norm at most one, by the Pythagorean identity.

Every orthonormal system extends to a maximal one by Zorn: the union of a chain is still orthonormal. If the closed span of a maximal system were proper, its orthogonal complement would contain a unit vector that could be added. Thus the system is an orthonormal basis. For a finite subset \(F\) of a basis \((e_i)\), orthogonal projection gives
\[
P_Fx=\sum_{i\in F}\langle x,e_i\rangle e_i,
\qquad \sum_{i\in F}|\langle x,e_i\rangle|^2\leq\|x\|^2.
\]
The finite-subset net \(P_Fx\) converges to \(x\), since finite linear combinations are dense and \(\|P_F\|\leq1\). Taking squared norms gives Parseval. In particular, each square-summable scalar family has at most countable support: for each positive integer \(n\), only finitely many terms can exceed \(1/n\).

A bounded complex-linear functional \(\ell\) has the form \(\ell(x)=\langle x,v\rangle\) for a unique \(v\). For \(\ell\ne0\), project onto \(\ker\ell\). Its orthogonal complement is one-dimensional: subtracting a suitable multiple of any vector with nonzero functional value places an arbitrary vector in the kernel. For a unit vector \(u\) in that complement, take \(v=\overline{\ell(u)}u\). This proves the formula; uniqueness and \(\|v\|=\|\ell\|\) follow by testing unit vectors. The zero functional is represented by zero. Applying this to \(x\mapsto\langle Tx,y\rangle\) constructs the bounded adjoint, with
\[
\langle Tx,y\rangle=\langle x,T^*y\rangle,
\qquad \|T^*\|=\|T\|,
\qquad (\operatorname{ran}T)^\perp=\ker T^*.
\]
Linearity of \(T^*\) follows from the conjugate-linearity in the second variable. Its norm equality follows by taking the two unit-ball suprema in the adjoint identity.

### The bounded positive square root

For a positive bounded operator \(A\), positivity means selfadjointness and \(\langle Ax,x\rangle\geq0\). Positivity of \(\langle A(x+ty),x+ty\rangle\), minimized over complex \(t\), gives
\[
|\langle Ax,y\rangle|^2
\leq\langle Ax,x\rangle\langle Ay,y\rangle.
\tag{R1}
\]
This also follows when a diagonal term is zero by letting the modulus of \(t\) tend to zero with its argument chosen against the cross term. If \(c=\sup_{\|x\|=1}\langle Ax,x\rangle\), taking the supremum over unit \(y\) in (R1) gives \(\|Ax\|^2\leq c\langle Ax,x\rangle\). Consequently \(\|A\|=c\). Thus \(0\leq A\leq MI\) implies \(\|A\|\leq M\), without a spectral theorem.

Suppose \(A\ne0\), put \(M=\|A\|\), and set \(E=I-A/M\). Then \(E\) is a positive contraction. Define
\[
a_0=1,\qquad
a_n=\frac{\binom{2n}{n}}{4^n},\qquad
b_n=a_{n-1}-a_n=\frac{a_{n-1}}{2n}>0\quad(n\geq1).
\]
The ratio \(a_n/a_{n-1}=1-1/(2n)\) shows \(a_n\to0\): use \(1-t\leq e^{-t}\) and the divergence of the harmonic series, whose dyadic blocks are bounded below by \(1/2\). Therefore \(\sum_{n\geq1}b_n=1\). The series
\[
S=I-\sum_{n\geq1}b_nE^n
\tag{R2}
\]
converges absolutely in operator norm. Every partial sum is positive, because each \(E^n\) is a positive contraction and
\(I-\sum_{n=1}^N b_nE^n\geq(1-\sum_{n=1}^N b_n)I\).
Even powers are positive by \(E^{2k}=(E^k)^*E^k\), and odd powers by \(E^{2k+1}=(E^k)^*EE^k\). Positivity passes to a norm limit.

Here is the scalar coefficient identity needed to square (R2). For \(|r|<1\), let \(G(r)=\sum_{n\geq0}a_nr^n\). Its coefficient recurrence gives
\((1-r)G'(r)=G(r)/2\). Direct differentiation therefore gives
\(((1-r)G(r)^2)'=0\), so \((1-r)G(r)^2=1\). The equality
\(1-\sum_{n\geq1}b_nr^n=(1-r)G(r)\) follows by subtracting coefficients. Squaring gives \((1-\sum b_nr^n)^2=1-r\). These operations are justified by uniform convergence of power series and their derivatives on each smaller closed disk; the coefficient bounds \(a_n\leq1\) make the differentiated series there summable. Equality of coefficients now gives the operator identity for \(rE\), \(0<r<1\), by norm-convergent multiplication. As \(r\uparrow1\), the summability of \(b_n\) gives norm convergence of the same series, hence \(S^2=I-E\).

Thus \(C=\sqrt M\,S\) is a positive root of \(A\). For \(A=0\), use \(C=0\). The construction commutes with every bounded operator commuting with \(A\). If \(D\) is any other positive root, it commutes with \(A=D^2\), hence with \(C\). Therefore \((C+D)(C-D)=0\). A vector in \(\ker(C+D)\) is in both \(\ker C\) and \(\ker D\), by positivity and (R1). For \(y=(C-D)x\), it follows that \((C-D)y=0\), and then
\(\|y\|^2=\langle (C-D)x,y\rangle=\langle x,(C-D)y\rangle=0\).
So \(C=D\). Finally
\[
\|Cx\|^2=\langle Ax,x\rangle,
\qquad \ker C=\ker A,
\qquad \|C\|^2=\|A\|.
\tag{R3}
\]
For the kernel assertion, (R1) shows that a zero quadratic value of \(A\) implies \(Ax=0\). The norm assertion follows by taking the unit-ball supremum in the first identity.

### Operator limits, compactness and bounded inverses

An operator-norm Cauchy sequence of bounded maps \(H\to K\) has a bounded operator limit: define its value on each vector by completeness of \(K\), pass linearity and a common norm bound to the limit, and then take the unit-ball supremum in the Cauchy estimate. Thus these operator spaces are Banach. Finite-rank maps are compact because a bounded set in a finite-dimensional space is totally bounded. An operator-norm limit of compact maps has totally bounded unit-ball image: a sufficiently close approximant and its finite \(\varepsilon\)-net give a finite \(2\varepsilon\)-net for the limit. The closure of that image is complete and totally bounded, hence compact. To see the last assertion directly, finite covers by balls of radii tending to zero give a Cauchy subsequence of every sequence. If an open cover of this closure had no finite subcover, then for every positive integer \(n\) some radius-\(1/n\) ball about a point would fail to lie in any member; otherwise total boundedness would give a finite subcover. A convergent subsequence of those points lies eventually in a single open member together with its radius-\(1/n\) ball, a contradiction.

For use in bounded similarity, we also prove the bounded inverse theorem. In a complete metric space, a countable intersection of dense open sets is dense: inside any given nonempty open set, choose successively closed balls of positive radii at most \(2^{-n}\), with each ball inside the preceding open ball and the \(n\)-th dense open set. Their centres form a Cauchy sequence, and its limit belongs to every closed ball. This proves the assertion, including isolated points. Consequently a nonempty complete space covered by countably many closed sets has one of them with nonempty interior.

Let \(V:H\to K\) be a bounded bijection, with both spaces nonzero. Surjectivity gives
\(K=\bigcup_{n\geq1}\overline{V(nB_H)}\), where \(B_H\) is the open unit ball. Baire gives \(B_K(y_0,r)\subset\overline{V(nB_H)}\) for some \(r>0\). Subtract approximants for \(y_0+y\) and \(y_0\), and rescale, to obtain
\[
B_K(0,\delta)\subset\overline{V(B_H)},
\qquad \delta=r/(2n)>0.
\]
If \(\|y\|<\delta/2\), choose \(x_1\) with \(\|x_1\|<1/2\) and residual norm below \(\delta/4\). At the next step use the scaled inclusion to choose \(\|x_j\|<2^{-j}\) so that the residual after \(j\) steps is below \(\delta2^{-j-1}\). Completeness gives \(x=\sum_jx_j\), \(\|x\|\leq1\), and continuity gives \(Vx=y\). Apply this to \(\delta y/(4\|y\|)\) and rescale. Uniqueness of preimages proves \(\|V^{-1}y\|\leq4\|y\|/\delta\). The zero spaces have the unique zero inverse. Thus every bounded Hilbert-space bijection has a bounded inverse.

### Hilbert-Schmidt maps

Let \((e_i)_{i\in I}\) be an orthonormal basis of \(H\). For \(A:H\to K\), set

\[
\|A\|_2^2=\sum_{i\in I}\|Ae_i\|^2.                            \tag{T1}
\]

The operator is **Hilbert-Schmidt** when this is finite; the class is denoted \(\mathcal S_2(H,K)\).

**Theorem.** Formula (T1) is independent of the basis. The adjoint has the same Hilbert-Schmidt norm. The class is complete in that norm, contains every finite-rank operator densely, and

\[
\|A\|\leq\|A\|_2,\qquad
\|BAC\|_2\leq\|B\|\|A\|_2\|C\|                               \tag{T2}
\]

for bounded maps of the indicated source and target spaces. Every Hilbert-Schmidt map is compact.

**Proof.** Choose an orthonormal basis \((f_j)_{j\in J}\) of \(K\). Parseval, followed by the definition of a nonnegative double sum, gives

\[
\sum_i\|Ae_i\|^2
=\sum_{i,j}|\langle Ae_i,f_j\rangle|^2
=\sum_j\|A^*f_j\|^2.                                        \tag{T3}
\]

Both orders of summation equal the supremum over finite subsets of \(I\times J\). For any finite subset of the product, its two coordinate projections are finite, so finite rectangles give the same supremum. Fixing either basis in (T3) proves independence of the other, and proves adjoint equality.

For a finite orthogonal expansion \(x=\sum_i c_ie_i\), Cauchy-Schwarz gives \(\|Ax\|\leq(\sum_i|c_i|^2)^{1/2}(\sum_i\|Ae_i\|^2)^{1/2}\); passing to the dense span proves the first estimate in (T2). The left ideal estimate follows directly from \(\|BAe_i\|\leq\|B\|\|Ae_i\|\). Taking adjoints gives the right ideal estimate, and combining them proves (T2).

If \(A\) has finite rank, then \((\ker A)^\perp=\operatorname{ran}A^*\) is finite-dimensional. Here equality follows because the finite-dimensional range of \(A^*\) is closed and its orthogonal complement is \(\ker A\); finite rank of \(A^*\) follows by writing \(A\) in coordinates in its finite-dimensional range. A basis adapted to \(\ker A\) makes (T1) a finite sum. Conversely, if (T1) is finite, let \(P_F\) project onto the span of a finite subset \(F\subset I\). Then

\[
\|A-AP_F\|_2^2=\sum_{i\notin F}\|Ae_i\|^2\longrightarrow0.    \tag{T4}
\]

Thus finite-rank maps are dense. One can choose a sequence of finite sets giving errors below \(1/n\); no countability of \(I\) is being assumed. The operator norm estimate makes the same approximation converge in operator norm, so \(A\) is compact by the operator-norm closure argument above.

For completeness, a Hilbert-Schmidt Cauchy sequence \(A_n\) is operator norm Cauchy and has a bounded operator limit \(A\). The existence of the operator norm limit follows by taking limits \(A_nx\) in the Banach target and passing linearity and the uniform norm bound to those limits. For each finite \(F\),

\[
\sum_{i\in F}\|(A-A_n)e_i\|^2
=\lim_{m\to\infty}\sum_{i\in F}\|(A_m-A_n)e_i\|^2
\leq\liminf_{m\to\infty}\|A_m-A_n\|_2^2.
\]

Taking the supremum in \(F\) proves both \(A\in\mathcal S_2\) and \(\|A-A_n\|_2\to0\). The mixed sum \(\sum_i\langle Ae_i,Be_i\rangle\) converges absolutely by Cauchy-Schwarz; polarization of the basis-independent squared norm makes it a basis-independent inner product. Together with completeness, this makes \(\mathcal S_2(H,K)\) a Hilbert space. \(\square\)

Nonseparability causes no missing sums here. For a Hilbert-Schmidt \(A\), only countably many basis vectors have nonzero image, and the range is contained in the closed span of their images. It is the operator's effective support that becomes separable.

<a id="AN03-TRC-002"></a>

## AN03-TRC-002 — The trace ideal from paired orthonormal systems

For \(T:H\to K\), define

\[
q(T)=\sup\left\{
\sum_{i\in F}|\langle Te_i,f_i\rangle|:
(e_i)_{i\in F},(f_i)_{i\in F}\text{ finite orthonormal systems}
\right\}.                                                    \tag{T5}
\]

The same finite set labels the two systems; they need not be complete bases. The value may be infinite.

**Theorem: factorization.** The following conditions are equivalent:

1. \(q(T)<\infty\).
2. For every pair of orthonormal systems with a common, possibly infinite index set, \(\sum_i|\langle Te_i,f_i\rangle|<\infty\).
3. For some Hilbert space \(G\), there are \(A\in\mathcal S_2(H,G)\) and \(B\in\mathcal S_2(K,G)\) such that \(T=B^*A\).

When these hold,

\[
q(T)=\inf_{T=B^*A}\|A\|_2\|B\|_2
=\sum_i\langle |T|e_i,e_i\rangle,\qquad |T|=(T^*T)^{1/2},     \tag{T6}
\]

where the last sum is over any orthonormal basis of \(H\). In particular, the infimum is attained by a factorization constructed below.

**Proof.** If \(T=B^*A\), then for any paired systems,

\[
\sum_i|\langle Te_i,f_i\rangle|
\leq\left(\sum_i\|Ae_i\|^2\right)^{1/2}
     \left(\sum_i\|Bf_i\|^2\right)^{1/2}
\leq\|A\|_2\|B\|_2.                                        \tag{T7}
\]

Extend each orthonormal system to a basis to justify the last inequality. Finite sums and then suprema justify Cauchy-Schwarz for arbitrary indices. Thus 3 implies 1, and 1 implies 2.

Suppose 2. Put \(C=|T|\) and \(N=\ker T=\ker C\). Indeed \(\|Cx\|^2=\langle T^*Tx,x\rangle=\|Tx\|^2\). The map \(Cx\mapsto Tx\) is a well-defined isometry on \(\operatorname{ran}C\), whose closure is \(N^\perp\). Extend it continuously to \(N^\perp\), and by zero on \(N\), obtaining a partial isometry \(U:H\to K\) with \(T=UC\). This is a direct construction of the bounded polar factor, using the bounded positive square root proved in AN03-TRC-001.

Choose an orthonormal basis \((e_i)\) of \(N^\perp\). Then \((Ue_i)\) is orthonormal in \(K\), so condition 2 gives

\[
s=\sum_i\langle Ce_i,e_i\rangle
=\sum_i|\langle Te_i,Ue_i\rangle|<\infty.                    \tag{T8}
\]

Let \(D=C^{1/2}\). Its kernel is \(N\): \(\|Dx\|^2=\langle Cx,x\rangle\), and \(C=D^2\). Therefore \(\operatorname{ran}D\subset N^\perp\). A basis of \(N\) contributes zeros, so (T8) and (T1) give \(\|D\|_2^2=s\). Since \(U\) is isometric on \(\operatorname{ran}D\), \(\|UD\|_2=\|D\|_2\). Take

\[
G=H,\qquad A=D,\qquad B=DU^*.
\]

Then \(B^*A=UD^2=T\), and \(\|A\|_2\|B\|_2=s\) by adjoint equality. On the other hand, the finite parts of the paired systems in (T8) show \(q(T)\geq s\). Inequality (T7) proves the reverse inequality and the infimum formula. The final sum in (T6) is independent of basis because it equals \(\|C^{1/2}\|_2^2\). This also covers \(T=0\), with zero factors. \(\square\)

The distinction between the existence of a Hilbert-Schmidt factorization and a statement about arbitrary specified factors is essential. A trace-class product does not force its two given factors to be Hilbert-Schmidt; the zero operator composed with the identity on an infinite-dimensional space is an immediate counterexample.

Define \(\mathcal S_1(H,K)\) to be this class, and \(\|T\|_1=q(T)\).

**Theorem: norm and ideal properties.** This is a Banach space. Finite-rank maps are dense, and for bounded \(L:K\to K'\), \(R:H'\to H\),

\[
\|T\|\leq\|T\|_1,\qquad
\|LTR\|_1\leq\|L\|\|T\|_1\|R\|.                             \tag{T9}
\]

Every trace-class map is compact, and \(\|T^*\|_1=\|T\|_1\).

**Proof.** Homogeneity and the triangle inequality follow from the supremum of finite absolute sums in (T5). For unit \(x\) with \(Tx\ne0\), pair \(x\) with \(Tx/\|Tx\|\); this proves \(\|T\|\leq q(T)\), including definiteness. From \(T=B^*A\) obtain \(LTR=(BL^*)^*(AR)\), and apply (T2), then the infimum in (T6). Exchanging the two orthonormal systems proves the adjoint equality.

For density, choose Hilbert-Schmidt finite-rank approximations \(A_n\to A\), \(B_n\to B\). Then \(B_n^*A_n\) has finite rank and

\[
\|B^*A-B_n^*A_n\|_1
\leq\|B-B_n\|_2\|A\|_2+\|B_n\|_2\|A-A_n\|_2\longrightarrow0. \tag{T10}
\]

In particular, trace-class maps are compact, by (T9) and operator norm closure of the compact maps.

If \(T_n\) is trace norm Cauchy, it converges in operator norm to some \(T\). For every finite paired system, continuity of its finitely many terms gives

\[
\sum_i|\langle (T-T_n)e_i,f_i\rangle|
\leq\liminf_{m\to\infty}\|T_m-T_n\|_1.
\]

Taking the supremum proves that \(T-T_n\) is trace class with trace norm tending to zero. Thus \(T\) is trace class and the space is complete. \(\square\)

For later use, the rank-one operator \(u\otimes v^*:x\mapsto\langle x,v\rangle u\) satisfies

\[
\|u\otimes v^*\|_1=\|u\|\|v\|.                               \tag{T11}
\]

The lower bound comes from pairing the normalized \(v,u\) when neither is zero. For the upper bound use \(G=\mathbb C\), \(Ax=\langle x,v\rangle\), \(By=\langle y,u\rangle\) in (T7); Parseval gives their Hilbert-Schmidt norms \(\|v\|,\|u\|\).

<a id="AN03-TRC-003"></a>

## AN03-TRC-003 — Traces, invariant subspaces, and cyclic transport

For \(T\in\mathcal S_1(H,H)\), define

\[
\operatorname{Tr}_H T=\sum_i\langle Te_i,e_i\rangle.           \tag{T12}
\]

The sum is absolutely convergent by (T5). It is independent of the orthonormal basis.

**Proof of independence and continuity.** Factor \(T=B^*A\). The sum is \(\sum_i\langle Ae_i,Be_i\rangle\). It can be recovered from the four basis-independent Hilbert-Schmidt norms of \(A+B,A-B,A+iB,A-iB\) by complex polarization. More explicitly, with the chosen convention it equals

\[
\frac14\left(\|A+B\|_2^2-\|A-B\|_2^2
+i\|A+iB\|_2^2-i\|A-iB\|_2^2\right).
\]

Expansion of each squared norm verifies the formula, with all mixed sums absolutely convergent by Cauchy-Schwarz. This proves independence. Linearity follows termwise using any one basis, and \(|\operatorname{Tr}T|\leq\|T\|_1\) follows from (T5). On a nonzero Hilbert space this functional has norm one, since a rank-one orthogonal projection has trace and trace norm one. On the zero space the functional has norm zero. \(\square\)

The rank-one formula is

\[
\operatorname{Tr}(u\otimes v^*)=\langle u,v\rangle,            \tag{T13}
\]

by Parseval. This also recovers the ordinary matrix trace in finite dimension.

**Invariant-subspace additivity.** If \(M\subset H\) is closed and \(TM\subset M\), then \(T|_M\) and the induced map \(\overline T\) on the Hilbert quotient \(H/M\) are trace class, and

\[
\operatorname{Tr}_H T
=\operatorname{Tr}_M(T|_M)+\operatorname{Tr}_{H/M}\overline T. \tag{T14}
\]

Indeed identify \(H/M\) isometrically with \(M^\perp\). The induced map is the compression \(P_{M^\perp}T|_{M^\perp}\); the restriction is \(P_MT|_M\). These are trace class by the ideal estimate. Joining bases of \(M\) and \(M^\perp\) proves (T14). The off-diagonal block can be nonzero and contributes no diagonal terms. The same reasoning gives \(\operatorname{Tr}_M(P_MT|_M)=\operatorname{Tr}_H(P_MTP_M)\) even if \(M\) is not invariant.

**Cyclicity and bounded similarity.** If \(T:H\to K\) is trace class and \(S:K\to H\) bounded, then

\[
\operatorname{Tr}_K(TS)=\operatorname{Tr}_H(ST).              \tag{T15}
\]

For rank one, (T13) and the adjoint identity give \(\langle u,S^*v\rangle=\langle Su,v\rangle\). Every finite-rank operator is a finite sum of rank-one maps: choose an orthonormal basis \(u_1,\ldots,u_r\) of its range and write \(Tx=\sum_j\langle x,T^*u_j\rangle u_j\). Thus (T15) holds in finite rank. Approximate in trace norm and use (T9) and trace continuity to obtain the general statement. For \(T\in\mathcal S_1(H,H)\), if \(V:H\to K\) is a bounded bijection, its inverse is bounded by the bounded inverse proof in AN03-TRC-001, and (T15) gives

\[
\operatorname{Tr}_K(VTV^{-1})=\operatorname{Tr}_H T.          \tag{T16}
\]

The boundedness of \(V\) and \(V^{-1}\) supplies the ideal estimates used in this proof; \(V\) may be any bounded Hilbert-space bijection.

## Related freely proved programme foundations

The Hilbert projection, basis and adjoint argument is also proved in [Compact-group foundations, CPT-F-006](../../../representations-of-compact-groups/compact-foundations.html#cpt-f-006). The complete Baire and bounded inverse arguments are also given in [Banach foundations, Sections 6 and 8](../../reader/dependency-banach-foundations.html#section-8). These links identify independently written programme proofs; every result used in the bounded trace proofs above has been proved locally.
