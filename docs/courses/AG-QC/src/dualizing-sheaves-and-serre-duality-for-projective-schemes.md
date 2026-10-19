# Dualizing sheaves and Serre duality for projective schemes

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

A projective scheme can be singular, nonreduced, or have components of different dimensions. Its top cohomology still has a representing sheaf. What can fail is the extension of that representation to lower cohomology using Ext into the same sheaf. The Cohen–Macaulay condition says that the ambient Ext calculation is concentrated in one degree; this is precisely what makes the all-degree formula possible.

We use [Serre duality on projective space](ext-sheaves-and-serre-duality-on-projective-space.md). The current *Commutative algebra for geometry* lessons supply the local inputs: Associated primes and primary decomposition, Sections 1–2 and Solution 8.5 proves associated-prime finiteness and prime avoidance; Regular sequences, depth and Cohen–Macaulay modules, Theorems 4.1, 5.1 and 6.1 supplies unmixedness, localization and the Cohen–Macaulay property of regular local rings; Projective dimension, Theorems 3.1 and 4.1 proves Auslander–Buchsbaum and the Koszul resolution; and Regular local rings, Theorem 2.2 and Proposition 3.3 gives finite free resolutions and regularity of the ambient stalks. The height and point-dimension formulas are Krull dimension and Noether normalization, Theorems 5.1 and 6.1. The exact Noetherian, finite-module, local and finite-type hypotheses for each use are recorded in the prerequisite guide. The global duality construction is proved below.

All schemes here are nonempty and projective over a field \(k\), unless stated otherwise. Dimension means Krull dimension. Write \(V^\vee=\operatorname{Hom}_k(V,k)\).

## 1. The representing property

Let \(X\) have dimension \(n\). A **dualizing sheaf with trace** is a coherent sheaf \(\omega_X^\circ\) and a functional
\[
t_X:H^n(X,\omega_X^\circ)\longrightarrow k
\]
such that, for every coherent \(F\), the map
\[
\operatorname{Hom}_X(F,\omega_X^\circ)
 \longrightarrow H^n(X,F)^\vee,
\qquad u\longmapsto t_X\circ H^n(u)
\tag{1}
\]
is an isomorphism. This represents a contravariant functor on coherent sheaves. It does not assert any higher Ext formula yet.

**Proposition 1.1 (uniqueness).** Two dualizing sheaves with traces have a unique isomorphism respecting their representing maps and traces.

**Proof.** Suppose \((\omega,t)\) and \((\omega',t')\) both represent the functor. Apply the representation by \(\omega'\) to the element \(t\in H^n(X,\omega)^\vee\). It gives a unique map \(u:\omega\to\omega'\) with \(t'\circ H^n(u)=t\). Interchange the pairs to obtain \(v\). The composite \(vu\) represents the same element as the identity of \(\omega\), and hence is that identity. Likewise \(uv\) is the identity. Uniqueness follows from the same representing property. \(\square\)

Keeping the trace matters. Without the specified representation, multiplying an isomorphism by a scalar can change its normalization. The construction will inherit the ordered Čech trace on the ambient projective space.

## 2. The two local Ext facts

Let \(i:X\hookrightarrow P=\mathbf P^N_k\), and put \(c=N-n\). We need a lower bound on ambient Ext degrees and a sharper concentration statement for Cohen–Macaulay schemes.

**Lemma 2.1.** The coherent sheaves \(\mathcal E xt_P^j(i_*\mathcal O_X,\omega_P)\) vanish for \(j<c\). If \(X\) is Cohen–Macaulay and equidimensional of dimension \(n\), they vanish for every \(j\ne c\).

**Proof.** At \(x\in X\), let \(R=\mathcal O_{P,x}\) and \(B=\mathcal O_{X,x}=R/I\). The ring \(R\) is regular local, and the stalk of \(\omega_P\) is free of rank one. Every prime containing \(I\) has height at least \(c\): components of \(X\) have dimension at most \(n\), hence codimension at least \(N-n\) in \(P\), and localization at \(x\) keeps the chains below their primes. This also follows from the finite-type dimension formula.

The ideal \(I\) contains an \(R\)-regular sequence of length \(c\). To construct it, suppose \(r<c\) regular elements have been chosen. Their quotient ring is Cohen–Macaulay. Its associated primes are minimal and, viewed in \(R\), have height \(r\), by unmixedness and the dimension formula. The ideal \(I\), of height at least \(c\), is contained in none of them. Choose its next element outside their finite union by prime avoidance. It is a nonzerodivisor on the current quotient. This works over finite residue fields as well.

If \(a\) is a nonzerodivisor on \(R\) and annihilates a module \(M\), its two-term free resolution gives
\[
\operatorname{Ext}^j_R(M,R)
 \cong\operatorname{Ext}^{j-1}_{R/aR}(M,R/aR).
\tag{2}
\]
Indeed, applying \(\operatorname{Hom}_R(R/aR,-)\) to an injective resolution of \(R\) gives a complex of injective \(R/aR\)-modules with only one cohomology module, \(R/aR\) in degree one. Underived adjunction identifies Hom from \(M\) into this complex with the complex computing the left side. Its shift gives (2). Iterate along the regular sequence, whose elements annihilate \(B\), to conclude vanishing below \(c\).

Now impose the stronger hypotheses. If the closure of \(x\) has dimension \(s\), the dimension formula gives \(\dim R=N-s\) and \(\dim B=n-s\). Equidimensionality gives the latter equality, and Cohen–Macaulayness gives \(\operatorname{depth}B=\dim B\). Regularity of \(R\) makes the projective dimension finite, so Auslander–Buchsbaum gives
\[
\operatorname{pd}_R B=\dim R-\operatorname{depth}B=N-n=c.
\]
Its finite free resolution has length \(c\), killing Ext above \(c\). The stalk formula for coherent sheaf Ext proves the claimed sheaf vanishings. \(\square\)

Lower vanishing needed only the dimension bound. Upper vanishing needed depth and equidimensionality. Components of different dimensions do not have the same constant codimension in this calculation.

## 3. Transferring Hom across a closed immersion

For an \(\mathcal O_P\)-module \(G\), its sections annihilated by the ideal of \(X\) form an \(\mathcal O_X\)-module, denoted \(i^bG\). Thus
\[
i_*i^bG=\mathcal H om_P(i_*\mathcal O_X,G).
\]
The elementary adjunction is
\[
\operatorname{Hom}_X(F,i^bG)
 =\operatorname{Hom}_P(i_*F,G).
\tag{3}
\]
A map from a sheaf annihilated by the ideal must have image annihilated by that ideal, which proves (3). Closed pushforward is exact by its stalk description. Hence its right adjoint \(i^b\) takes injectives to injectives.

Choose an injective resolution \(\omega_P\to I^\bullet\) and put \(J^\bullet=i^bI^\bullet\). It is a bounded-below complex of injectives on \(X\), with
\[
i_*\mathcal H^q(J^\bullet)
 =\mathcal E xt^q_P(i_*\mathcal O_X,\omega_P).
\tag{4}
\]
Termwise adjunction identifies \(\operatorname{Hom}_X(F,J^\bullet)\) with \(\operatorname{Hom}_P(i_*F,I^\bullet)\). Its cohomology-sheaf filtration gives
\[
\operatorname{Ext}^p_X(F,\mathcal H^qJ)
 \ \Longrightarrow\ \operatorname{Ext}^{p+q}_P(i_*F,\omega_P),
\qquad p,q\geq0.
\tag{5}
\]
This change-of-rings spectral sequence is obtained by applying derived Hom to the truncation filtration of \(J\). An injective double resolution of its cohomology sheaves realizes the filtration. Each total degree has only finitely many possible terms, so it converges. The abutment is the termwise Hom complex already computed, because \(J\) is bounded below and injective in each degree. Thus (5) requires no finite globally locally free resolution on \(X\).

Lemma 2.1 eliminates rows below \(q=c\). The only term of total degree \(c\) therefore gives the canonical edge isomorphism
\[
\operatorname{Hom}_X(F,\mathcal H^cJ)
 \cong\operatorname{Ext}^c_P(i_*F,\omega_P).
\tag{6}
\]
No differential enters or leaves it: such a differential would have a negative first degree or enter a row below \(c\). In the Cohen–Macaulay equidimensional case there is only the row \(q=c\), giving for every \(i\geq0\)
\[
\operatorname{Ext}^i_X(F,\mathcal H^cJ)
 \cong\operatorname{Ext}^{c+i}_P(i_*F,\omega_P).
\tag{7}
\]
Equivalently, \(J\simeq(\mathcal H^cJ)[-c]\). The minus sign places this sheaf in degree \(c\).

## 4. Existence and Serre duality

**Theorem 4.1 (existence).** Every projective \(k\)-scheme \(X\) of dimension \(n\) has a dualizing sheaf with trace. For an embedding in \(\mathbf P^N_k\), it is
\[
\omega_X^\circ=\mathcal E xt^{N-n}_P(\mathcal O_X,\omega_P),
\tag{8}
\]
regarded as a sheaf on \(X\). The representing pair is independent of the embedding up to the unique isomorphism of Proposition 1.1.

**Proof.** Take \(\omega_X^\circ=\mathcal H^cJ\), coherent by the preceding local calculation. Combining (6) with ambient Serre duality gives
\[
\operatorname{Hom}_X(F,\omega_X^\circ)
 \cong\operatorname{Ext}^c_P(i_*F,\omega_P)
 \cong H^{N-c}(P,i_*F)^\vee
 =H^n(X,F)^\vee.
\]
The last equality uses exact closed pushforward and its preservation of cohomology. These maps are natural. Define \(t_X\) as the functional corresponding to the identity of \(\omega_X^\circ\). Naturality applied to \(F\to\omega_X^\circ\) says that the representing map is exactly (1). This proves existence with trace; Proposition 1.1 proves embedding independence. \(\square\)

The representation also holds for arbitrary quasi-coherent \(F\). Such a sheaf on a Noetherian scheme is a filtered union of coherent subsheaves. Cohomology commutes with filtered colimits here, as the finite affine Čech complex shows. Hom from a colimit is the inverse limit of Hom, and the linear dual of a colimit is the inverse limit of duals. Taking these limits extends (1).

**Theorem 4.2 (Serre duality).** If \(X\) is projective, Cohen–Macaulay and equidimensional of dimension \(n\), then for every coherent \(F\) and every integer \(i\),
\[
\operatorname{Ext}^i_X(F,\omega_X^\circ)
 \cong H^{n-i}(X,F)^\vee.
\tag{9}
\]
The maps are natural, compatible with connecting maps, and extend (1).

**Proof.** For \(i\geq0\), combine (7) with ambient duality in degree \(c+i\). Its cohomology degree is \(N-c-i=n-i\), as required. Injective adjunction and the truncation isomorphism respect connecting maps. For \(i<0\), Ext and cohomology above \(n\) both vanish. \(\square\)

For a vector bundle \(E\), global Ext is cohomology of \(E^\vee\otimes\omega_X^\circ\), so (9) gives a perfect cohomology pairing. This works even when the dualizing sheaf is not invertible. Invertibility is an additional condition: Cohen–Macaulay schemes need not be complete intersections.

## 5. Adjunction for complete intersections

Suppose \(X\subset\mathbf P^N_k\) is a complete intersection defined by a homogeneous regular sequence \(f_1,\ldots,f_r\) of degrees \(d_1,\ldots,d_r\). Assume it is nonempty, so \(r\leq N\). Its dimension is \(n=N-r\), and it is Cohen–Macaulay and equidimensional.

**Theorem 5.1 (adjunction).** There is an isomorphism
\[
\omega_X^\circ\cong
 \mathcal O_X(d_1+\cdots+d_r-N-1).
\tag{10}
\]

**Proof.** Set \(E=\bigoplus_{j=1}^r\mathcal O_P(-d_j)\). The Koszul complex \(K^{-a}=\bigwedge^aE\), with differential contraction by the equations, resolves \(\mathcal O_X\). Its exactness follows locally by induction on the regular sequence: the one-element complex resolves its quotient, and adjoining the next nonzerodivisor makes a mapping cone whose cohomology sequence leaves only the new quotient in degree zero.

Hom into \(\omega_P\) has top term \((\det E)^\vee\otimes\omega_P\). The preceding differential has image the equation ideal times this line; thus its cokernel is
\[
\mathcal E xt^r_P(\mathcal O_X,\omega_P)
 =((\det E)^\vee\otimes\omega_P)|_X.
\]
Other cohomology terms vanish by Lemma 2.1. Since \(\det E=\mathcal O_P(-\sum d_j)\), (8) gives (10). \(\square\)

For a plane curve of degree \(d\geq1\), the result gives \(\omega_C=\mathcal O_C(d-3)\), without assuming smoothness or reducedness. Its hypersurface sequence gives
\[
h^0(C,\mathcal O_C)=1,
\qquad p_a(C)=h^1(C,\mathcal O_C)=\frac{(d-1)(d-2)}2.
\]
By duality, \(h^1(\mathcal O_C)=h^0(\omega_C)\). This is arithmetic genus; interpreting it as the genus of a smooth curve requires that extra assumption.

An intersection of two quadrics in \(\mathbf P^3\) has trivial dualizing sheaf. Its Koszul sequence gives \(H^0(\mathcal O_X)=k\): the first cohomology of its ideal is zero because intermediate cohomology of twists on \(\mathbf P^3\) vanishes. Duality gives \(h^1(\mathcal O_X)=1\). A smooth such curve is a genus-one curve; specifying a rational point makes it an elliptic curve.

For a reducible example, take the conic \(C=V(XY)\subset\mathbf P^2\). It consists of two lines meeting at the rational point \(p=[0:0:1]\). Its canonical sheaf is \(\mathcal O_C(-1)\), by (10). The exact sequence
\[
0\to\mathcal O_C\to\mathcal O_{L_1}\oplus\mathcal O_{L_2}
 \xrightarrow{(a,b)\mapsto a(p)-b(p)}k(p)\to0
\]
is checked at the crossing from \(k[x,y]/(xy)\) and elsewhere from one branch. On global sections the difference map \(k^2\to k\) is surjective. Thus \(H^0(\mathcal O_C)=k\) and \(H^1(\mathcal O_C)=0\), confirming the genus formula. The canonical sheaf has no sections, also as duality predicts. Its restriction to either line is \(\mathcal O_{\mathbf P^1}(-1)\), whereas that line's own canonical sheaf is \(\mathcal O_{\mathbf P^1}(-2)\). The difference is the crossing point: the restricted sheaf is \(\omega_{L_i}(p)\). Normalization therefore changes the canonical sheaf even for this simple reduced Cohen–Macaulay curve; one must account for the gluing at its singular point.

## 6. A non-Cohen–Macaulay counterexample

Before examining failure, consider the zero-dimensional case, where duality always holds. A projective zero-dimensional scheme is finite over \(k\), by properness and finite fibers, so it is \(\operatorname{Spec}B\) for a finite-dimensional \(k\)-algebra \(B\). Its dualizing sheaf corresponds to
\[
D_B=\operatorname{Hom}_k(B,k),
\qquad (b\phi)(a)=\phi(ba).
\]
The trace is evaluation at one: \(t_B(\phi)=\phi(1)\). For any finite \(B\)-module \(M\), the representing isomorphism is
\[
\operatorname{Hom}_B(M,D_B)\cong\operatorname{Hom}_k(M,k).
\]
One direction takes \(h\) to \(m\mapsto h(m)(1)\); its inverse takes \(\lambda\) to the map \(m\mapsto[b\mapsto\lambda(bm)]\). These formulas are inverse and verify \(B\)-linearity explicitly. The functor on the right is exact, so \(D_B\) is injective as a \(B\)-module. Higher Ext therefore vanishes, agreeing with the absence of positive cohomology on a finite affine scheme. This verifies all-degree duality directly, including nonreduced Artinian rings.

For \(B=k[\epsilon]/\epsilon^2\), let \(\lambda\) extract the coefficient of \(\epsilon\). The map \(B\to D_B\), \(b\mapsto b\lambda\), is an isomorphism: its multiplication pairing on the basis \(1,\epsilon\) has matrix
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Under this identification the trace of a section \(b\) is its \(\epsilon\)-coefficient. Even though the scheme has only one underlying point, its duality sees both dimensions of its algebra.

On the other hand, set \(B=k[x,y]/(x,y)^2\). This Artinian ring is Cohen–Macaulay, as every zero-dimensional local ring is, but its dualizing module is not free of rank one. The socle of \(B\), namely the elements killed by \((x,y)\), has dimension two. The socle of \(D_B\) consists of functionals vanishing on \((x,y)\), and has dimension one. Thus \(D_B\not\cong B\); an invertible module over this local ring would be free of rank one, so the dualizing sheaf is not invertible. This is a concrete instance of the distinction after Theorem 4.2.

For a finite field extension \(K/k\), the module \(D_K\) is nevertheless a one-dimensional \(K\)-vector space. Any nonzero functional \(\lambda:K\to k\) identifies it with \(K\), since a nonzero \(K\)-linear map between these one-dimensional spaces is an isomorphism. This must not be confused with always using the field trace. For a purely inseparable extension of degree \(p\), the field trace is zero. A coefficient functional in a basis \(1,u,\ldots,u^{p-1}\), extracting the last coefficient, instead gives a valid nonzero duality functional. Choosing an identification of the dualizing line changes its trace expression; the representing pair itself remains the canonical object.

We now turn to a one-dimensional scheme with an embedded point. Its local ring is not Cohen–Macaulay, and the preceding all-degree conclusion fails.

In \(P=\mathbf P^2_k\) with coordinates \(X,Y,Z\), let \(T\) be defined by \((X^2,XY)\). Its support is the line \(L=V(X)\), with an embedded point \(p=[0:0:1]\). At \(p\), the nonzero class of \(X/Z\) is killed by both local coordinates. The one-dimensional local ring has depth zero, so \(T\) is not Cohen–Macaulay.

There is an exact sequence
\[
0\to k(p)\to\mathcal O_T\to\mathcal O_L\to0.
\]
Its kernel is the ideal generated by the class of \(X\), a one-dimensional skyscraper at \(p\). Choosing its basis gives the displayed identification. The global unit lifts the unit on \(L\), so \(h^0(\mathcal O_T)=2\) and \(h^1(\mathcal O_T)=0\).

The resolution
\[
0\to\mathcal O_P(-3)\xrightarrow{(-Y,X)}
 \mathcal O_P(-2)^2\xrightarrow{(X^2,XY)}
 \mathcal O_P\to\mathcal O_T\to0
\]
is exact: the relations between \(X^2\) and \(XY\) are multiples of \((-Y,X)\), since \(X,Y\) are relatively prime. Hom into \(\omega_P=\mathcal O_P(-3)\) gives
\[
\mathcal O_P(-3)\xrightarrow{(X^2,XY)}
 \mathcal O_P(-1)^2\xrightarrow{(-Y,X)}\mathcal O_P.
\]
The middle kernel consists of \((Xb,Yb)\), with \(b\) a section of \(\mathcal O_P(-2)\); the first image corresponds to multiples of \(X\). Hence
\[
\mathcal E xt^1_P(\mathcal O_T,\omega_P)=\mathcal O_L(-2),
\qquad\mathcal E xt^2_P(\mathcal O_T,\omega_P)=k(p).
\]
Its dualizing sheaf is \(\omega_T^\circ=\mathcal O_L(-2)\). Top-degree representation works, but an all-degree formula with \(F=\mathcal O_T\) would require
\[
\operatorname{Ext}^1_T(\mathcal O_T,\omega_T^\circ)
 =H^1(L,\mathcal O_L(-2))=k
 \quad\cong\quad H^0(T,\mathcal O_T)^\vee=k^2,
\]
which is impossible. The extra ambient Ext sheaf in degree two is precisely the information discarded by taking only one sheaf.

## 7. Exercises with solutions

**Exercise 7.1 (easy: plane curves).** Compute the dualizing sheaf and arithmetic genus of a plane curve of degree \(d\geq1\).

**Solution.** Its equation is a regular sequence, so (10) gives \(\mathcal O_C(d-3)\). In \(0\to\mathcal O_P(-d)\to\mathcal O_P\to\mathcal O_C\to0\), intermediate projective-plane cohomology vanishes. Hence \(H^0(\mathcal O_C)=k\), and \(H^1(\mathcal O_C)=H^2(\mathcal O_P(-d))\) has dimension \(\binom{d-1}{2}\) for \(d\geq3\), zero for \(d=1,2\). These values equal the arithmetic-genus polynomial in all cases.

**Exercise 7.2 (easy: a Cohen–Macaulay curve).** Prove \(h^1(\mathcal O_C)=h^0(\omega_C^\circ)\) for a projective Cohen–Macaulay equidimensional curve.

**Solution.** Set \(F=\mathcal O_C\), \(n=1\), \(i=0\) in (9). Hom from the structure sheaf is global sections, so \(H^0(\omega_C^\circ)=H^1(\mathcal O_C)^\vee\). Finiteness gives equality of dimensions. Neither smoothness, algebraic closure of \(k\), nor equality of the constants with \(k\) is required.

**Exercise 7.3 (medium: the determinant).** Recover the complete-intersection twist from its Koszul resolution.

**Solution.** The last Koszul term is \(\mathcal O(-\sum d_j)\). Its Hom into \(\mathcal O(-N-1)\) is \(\mathcal O(\sum d_j-N-1)\). The preceding image is its equation ideal, so its cokernel is the restriction to \(X\). Since \(r=N-n\), this is the Ext sheaf defining the dualizing sheaf. Regularity is essential for the Koszul complex to resolve the structure sheaf.

**Exercise 7.4 (medium: Ext concentration).** Explain both vanishing ranges for Cohen–Macaulay equidimensional \(X\).

**Solution.** Codimension supplies a regular sequence of length \(c\) in the local annihilator ideal; iteration of (2) kills Ext below \(c\). At a point with closure dimension \(s\), the ambient regular dimension is \(N-s\) and the quotient depth is \(n-s\). Auslander–Buchsbaum gives projective dimension \(c\), killing Ext above it. Localization of coherent sheaf Ext transfers these module vanishings to the sheaves.

**Exercise 7.5 (hard: the embedded point).** Verify the failure of all-degree duality for the scheme \(T\) in Section 6.

**Solution.** The length-one kernel and lifted unit give \(H^0(\mathcal O_T)=k^2\). The dualized resolution gives \(\omega_T^\circ=\mathcal O_L(-2)\). Since \(\mathcal O_T\) is free of rank one as a module over itself, its first global Ext into this sheaf is \(H^1(\mathcal O_L(-2))=k\). Thus the two sides of degree-one duality have different dimensions. The degree-two ambient Ext verifies failure of concentration directly.

**Exercise 7.6 (hard: different component dimensions).** Find the top-degree dualizing sheaf for \(X=\mathbf P^1_k\amalg\operatorname{Spec}k\), where \(n=1\).

**Solution.** It is \(\mathcal O(-2)\) on the line and zero on the isolated point. The point contributes no first cohomology for any coherent sheaf, so the representing Hom functor must vanish on all sheaves supported there. This proves (1) componentwise. Although \(X\) is Cohen–Macaulay, its components have different dimensions. First Ext into this sheaf cannot represent the nonzero zeroth cohomology of the structure sheaf of the isolated point. Equidimensionality is a separate hypothesis for the single-shift formula.

## 8. Dualizing complexes

The ambient construction naturally retains a complex
\[
C_X=R i^b(\omega_P)[N].
\]
Its degree \(-n\) cohomology is \(\omega_X^\circ\). In the Cohen–Macaulay equidimensional case, Lemma 2.1 gives \(C_X\simeq\omega_X^\circ[n]\). For the embedded-point example it has both \(\mathcal H^{-1}=\mathcal O_L(-2)\) and \(\mathcal H^0=k(p)\). The complex retains the information needed for lower-degree duality.

**Proposition 8.1 (the normalized complex, independently of an embedding).** For every bounded complex \(F\) with coherent cohomology on \(X\), evaluation and the ambient trace induce a natural isomorphism
\[
R\operatorname{Hom}_X(F,C_X)
\cong R\operatorname{Hom}_k(R\Gamma(X,F),k).
\tag{11}
\]
The complex \(C_X\) and its trace are independent of the projective embedding, up to the unique compatible isomorphism.

**Proof.** Injective adjunction in Section 3 gives
\[
R\operatorname{Hom}_X(F,Ri^b\omega_P[N])
=R\operatorname{Hom}_P(i_*F,\omega_P[N]).
\]
The counit \(i_*Ri^b\omega_P\to\omega_P\), followed by the ordered projective-space trace, defines \(R\Gamma(X,C_X)\to k\). Evaluation followed by this trace gives the morphism in (11). For a coherent sheaf \(F\), its map in degree \(m\) is exactly the projective-space Serre isomorphism
\(\operatorname{Ext}^{N+m}_P(i_*F,\omega_P)=H^{-m}(X,F)^\vee\),
including its connecting-map normalization. Hence it is a quasi-isomorphism. A bounded coherent complex has a finite cohomology-sheaf truncation filtration. Apply the two exact functors in (11) to its triangles; induction along that filtration and the long cohomology sequences prove the same assertion for every such complex.

The local finite free resolutions over the regular ambient stalks put \(C_X\) in the bounded coherent derived category. Formula (11) in degree zero represents on that category the functor \(F\mapsto H^0(R\Gamma F)^\vee\). If another embedding gives \(C'_X\), the two representing isomorphisms give maps \(C_X\to C'_X\) and back by evaluating at these objects. Naturality makes their composites identities and makes the maps respect the trace. This is the Yoneda argument of Proposition 1.1, now applied to the bounded derived category. It proves the asserted independence without the later right-adjoint theorem.

The same object is a dualizing complex in the local sense. On an affine ambient regular ring \(R\) and quotient \(B\), it is \(R\operatorname{Hom}_R(B,R)\), up to the displayed normalization and a locally trivial ambient line. Derived Hom adjunction identifies duality of a finite \(B\)-complex with its \(R\)-dual. The complex is perfect over \(R\), by the finite regular-local resolution theorem already cited, and the evaluation into its double \(R\)-dual is an isomorphism term by term on finite free resolutions. Applying the adjunction twice gives its \(B\)-biduality as well. The finite injective-dimension bound follows from the regular-local resolution bound: derived Hom into this complex is the \(R\)-Hom complex and vanishes above that bound for module inputs. These statements localize and prove the local dualizing property. \(\square\)

**Proposition 8.2 (the smooth canonical bundle).** If \(X/k\) is smooth of pure dimension \(n\), then
\[
C_X\simeq\bigwedge^n\Omega_{X/k}[n],
\qquad \omega_X^\circ\simeq\bigwedge^n\Omega_{X/k}.
\tag{12}
\]

**Proof.** At a point of the closed embedding \(X\hookrightarrow P\), the earlier *Smooth algebras over a field and the Jacobian criterion*, Lemma 1.1 and its standard smooth presentation, makes its ideal locally generated by \(c=N-n\) equations with independent differentials. The earlier *Regular local rings* proves that such independent classes extend to regular parameters, hence these equations are a regular sequence. The split conormal sequence is proved in *Kähler differentials*, Proposition 3.4 and Theorem 5.1:
\[
0\to I/I^2\to\Omega_{P/k}|_X\to\Omega_{X/k}\to0.
\]
Its terms are locally free. Koszul Hom into \(\omega_P\), by the calculation of Section 5, gives
\(\mathcal Ext^c_P(\mathcal O_X,\omega_P)=
\omega_P|_X\otimes\det(I/I^2)^\vee\).
Changing the regular generators changes the last Koszul term by their determinant, which is precisely the transition of \(\det(I/I^2)\); thus these local identifications glue. Taking the determinant of the conormal sequence identifies the last displayed line with \(\det\Omega_{X/k}\), since the Euler-sequence computation in the preceding duality lesson identifies \(\omega_P=\det\Omega_{P/k}\). The concentration of Lemma 2.1 now gives the shift \(C_X=\omega_X^\circ[n]\), proving (12). \(\square\)

The next lesson identifies the same normalized complex with the right adjoint of derived pushforward applied to \(k\). Its existence, embedding independence, bounded coherent duality and smooth specialization have already been proved here; the free Stacks sources below offer parallel treatments.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: dualizing modules [Tag 0AWH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-section-dualizing-module), their properties [Tag 0AWK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-dualizing-module), and Cohen–Macaulay concentration [Tag 0AWT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-dualizing-module-CM-scheme).
- Closed-immersion adjunction [Tag 0A9X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-twisted-inverse-image-closed); normalized proper duality [Tag 0FVV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-duality-proper-over-field); its Cohen–Macaulay form [Tag 0FVZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-duality-proper-over-field-CM); smooth proper calculation [Tag 0BRT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-smooth-proper). These open reference proofs retain their GFDL licence.
- Local homological algebra: Auslander–Buchsbaum [Tag 090V](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-Auslander-Buchsbaum), and finite regular-local resolutions [Tag 00O7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-regular-finite-gl-dim). The global arguments and computations here are independently written.

Kiran S. Kedlaya, MIT OpenCourseWare 18.726 (Spring 2009), [*Dualizing sheaves and Riemann–Roch*](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/be1fa559e68ba14f8cefb4484bc54de1_MIT18_726s09_lec24_dualizing.pdf), updated 6 May 2009, and [*Cohen–Macaulay schemes and Serre duality*](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/0ea66a0bdcf4f8127c826882531f1642_MIT18_726s09_lec25_serre_dual.pdf), provide parallel scholarly reading.
