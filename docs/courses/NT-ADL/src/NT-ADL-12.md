# The spherical Hecke algebra of GL₂ and Hecke operators on lattices

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A double coset records a finite family of lattices. Convolution records successive choices from two such families. This interpretation will determine every coefficient below, including the central scalar term that disappears when one passes from lattices to homothety classes.

We use the Cartan decomposition, triangular lattice bases and finite-adèlic lattice dictionary proved in *Lattices over a local field: the tree of GL_2 and its decompositions*. Fix a nonarchimedean local field \(F\), its valuation ring \(\mathcal O\), a uniformizer \(\pi\), and residue cardinality \(q\). Put \(G=\mathrm{GL}_2(F)\), \(K=\mathrm{GL}_2(\mathcal O)\), and \(L_0=\mathcal O^2\). Normalize Haar measure on \(G\) by \(\operatorname{vol}(K)=1\), and additive measure on \(F\) by \(\operatorname{vol}(\mathcal O)=1\). Thus \(|\pi|=q^{-1}\).

## Convolution as a finite count

First let \(G\) be any unimodular locally profinite group with a compact open subgroup \(K\) of volume one. Define \(\mathcal H(G,K)\) to be the space of compactly supported, locally constant, complex functions invariant under multiplication by \(K\) on either side. Its convolution is

\[
 (f*h)(g)=\int_G f(x)h(x^{-1}g)\,dx
          =\sum_{xK\in G/K}f(x)h(x^{-1}g).
 \tag{1}
\]

The summand is independent of the representative of \(xK\). Only finitely many terms occur: the compact support of \(f\) has finite image in the discrete space \(G/K\). Likewise every compact double coset has finitely many right cosets.

**Proposition 12.1.** Convolution makes \(\mathcal H(G,K)\) an associative unital algebra. Its unit is \(1_K\), and the indicators \(1_{KgK}\), one for each double coset, form a vector-space basis.

**Proof.** The support of a product is contained in the compact set \(\operatorname{supp}(f)\operatorname{supp}(h)\). A substitution \(x=ky\) proves left \(K\)-invariance; right invariance follows directly from that of \(h\). These invariances also imply local constancy. For associativity, both iterated integrals are absolutely integrable: the variables range over two compact supports and all functions are bounded. Substituting \(x=yz\) in the integral defining \((f*h)*j\) gives
\(\int\int f(y)h(z)j(z^{-1}y^{-1}g)\,dz\,dy\), which is \(f*(h*j)\). Left Haar invariance justifies this substitution. Integrating over \(K\) proves the two unit identities. Finally, the double-coset quotient is discrete; a compact support meets finitely many of its points. The corresponding indicators have disjoint supports and span every such function. □

For our matrix group, unimodularity can be checked directly. On the open set of invertible matrices, \(|\det g|^{-2}\,d^4g\) is invariant under both left and right multiplication: either multiplication by \(a\) has additive Jacobian \(|\det a|^2\), which cancels the determinant factor. A positive constant normalizes \(K\). Transposition preserves this measure, since it permutes entries and preserves determinants. Inversion also preserves Haar measure in a unimodular group.

**Theorem 12.2.** The algebra \(\mathcal H(G,K)\) for \(\mathrm{GL}_2(F)\) is commutative.

**Proof.** Set \(f^\tau(g)=f(g^t)\). Transposition reverses products and preserves measure. In the expression for \((f*h)(g^t)\), make the substitution \(x=z^t\), then \(z=y^{-1}g\). Transposition, inversion and right translation preserve measure, and the result is
\[
 (f*h)^\tau(g)=\int_G h^\tau(y)f^\tau(y^{-1}g)\,dy
             =(h^\tau*f^\tau)(g).
 \tag{2}
\]
By Cartan decomposition, every double coset has a representative \(\operatorname{diag}(\pi^a,\pi^b)\), with \(a\ge b\). Its transpose is itself, and \(K^t=K\). Thus transposition fixes each double coset, so \(f^\tau=f\) for every spherical function. Equation (2) gives \(f*h=h*f\). □

## Lattice operators and the polynomial algebra

Write
\[
 C_{a,b}=1_{K\operatorname{diag}(\pi^a,\pi^b)K},\qquad
 T=C_{1,0},\qquad R=C_{1,1}=1_{\pi K},\qquad
 H_n=\sum_{\substack{a\ge b\ge0\\a+b=n}}C_{a,b}.
 \tag{3}
\]
Here \(H_0=1_K\) and \(H_1=T\). The notation \(T(\pi^n)\) will mean \(H_n\); it includes every integral elementary-divisor type of determinant valuation \(n\).

Let \(V\) be the free complex vector space on actual lattices. It has a right Hecke action
\[
 [gL_0]\cdot f=\sum_{xK}f(x)[gxL_0].
 \tag{4}
\]
Changing \(g\) to \(gk\) permutes the sum by left \(K\)-invariance. Successive application of two operators gives (1), so this is a right module. It is faithful: applying \(f\) to \([L_0]\) recovers its value on each right coset, since \(G/K\) is exactly the set of lattices.

Under this action, \(T\) selects every index-\(q\) sublattice once, \(R\) sends \(L\) to \(\pi L\), and \(H_n\) selects every index-\(q^n\) sublattice once. These statements follow from elementary divisors and the double-coset basis. The [edge-stabilizer calculation in the preceding lesson](NT-ADL-11.md) also identifies these \(q+1\) choices with \(K/I\). The matrices \(\operatorname{diag}(1,\pi)\) and \(\operatorname{diag}(\pi,1)\) lie in the same \(K\)-double coset, since a permutation matrix interchanges their diagonal entries. Convolution by \(R\) is central translation, \((R*f)(g)=f(\pi^{-1}g)\). Its inverse is \(1_{\pi^{-1}K}\).

**Theorem 12.3.** The elements \(T,R\) are algebraically independent, and
\[
 \mathcal H(G,K)=\mathbb C[T,R,R^{-1}],\qquad
 TH_n=H_{n+1}+qRH_{n-1}\quad(n\ge1),\qquad
 \sum_{n\ge0}H_nX^n=(1-TX+qRX^2)^{-1}.
 \tag{5}
\]
The series identity is formal.

**Proof.** Count chains \(M\subset N\subset L\) with \([L:N]=q\) and \([N:M]=q^n\). All possible final \(M\) have index \(q^{n+1}\). The choices of \(N\) are the inverse images of lines in \(L/\pi L\) containing the image of \(M\). If \(M\not\subset\pi L\), that image is one-dimensional: determinant divisibility excludes dimension two. There is exactly one choice. If \(M\subset\pi L\), there are \(q+1\) choices. The latter lattices are precisely \(M=\pi M'\) with \([L:M']=q^{n-1}\). Thus \(H_{n+1}\) supplies one copy of every final lattice and \(qRH_{n-1}\) supplies the remaining copies. Faithfulness proves the recurrence. Multiplying the series by \(1-TX+qRX^2\), the constant coefficient is one, the linear coefficient is zero, and every higher coefficient vanishes by that recurrence.

Put \(C_n=C_{n,0}\). Elementary divisors give
\[
 H_n=C_n+RC_{n-2}+R^2C_{n-4}+\cdots,\qquad
 C_n=H_n-RH_{n-2}\quad(n\ge2).
 \tag{6}
\]
The recurrence expresses \(H_n\), then \(C_n\), as a polynomial in \(T,R\). Also \(C_{a,b}=R^bC_{a-b}\), for arbitrary integers \(a\ge b\). This proves generation.

To prove independence, the recurrence shows that \(H_n\) has leading term \(T^n\); conversely \(T^n\) equals \(C_n\) plus terms supported on double cosets of distance at most \(n-2\). Here distance means the difference of elementary-divisor exponents, as in the preceding lesson. This last assertion follows inductively from the recurrence and (6). In a nonzero finite linear combination of monomials \(T^nR^b\), choose the largest occurring \(n\). Their distance-\(n\) terms are the distinct basis elements \(C_{n+b,b}\), each with coefficient one. Terms with smaller \(n\) cannot cancel them. Hence no nonzero Laurent polynomial vanishes. In particular there is no polynomial relation between \(T\) and \(R\). □

All of this works over \(\mathbb Z\): the structure constants count finite sets. If the support is restricted to integral matrices, its algebra is \(\mathbb Z[T,R]\), or \(\mathbb C[T,R]\) with complex coefficients. It omits \(R^{-1}\). Indeed all its elementary divisors satisfy \(a\ge b\ge0\), and (6) proves generation without negative powers. The full local algebra is its localization at \(R\): multiplying a compact support by a sufficiently large scalar \(\pi^j\) makes every matrix entry integral.

On tree vertices, which are homothety classes, \(R\) acts as the identity and \(T\) as the sum over the \(q+1\) neighbours. Dually, on functions \(\varphi\) on vertices, \((T\varphi)(v)=\sum_{w\sim v}\varphi(w)\). The operators \(H_n\) are not simply sphere operators: scalar multiples of smaller-distance lattices also occur. In particular
\[
 T^2=H_2+qR=C_2+(q+1)R.
 \tag{7}
\]
For \(F=\mathbb Q_2\), the three neighbours come from the lines generated by \(e_1,e_2,e_1+e_2\) modulo two. On vertices the return coefficient in \(T^2\) is three; on actual lattices the return is to \(2L\).

## The normalized Satake transform

Use the upper triangular Borel \(B\), its unipotent subgroup \(N=\{n(u):u\in F\}\), and
\[
 n(u)=\begin{pmatrix}1&u\\0&1\end{pmatrix},\qquad
 t_{a,b}=\operatorname{diag}(\pi^a,\pi^b),\qquad
 \delta(t_{a,b})=|\pi^a/\pi^b|=q^{b-a}.
 \tag{8}
\]
The modulus \(\delta\) is the scaling of additive measure under conjugation on \(N\). Define
\[
 Sf=\sum_{a,b\in\mathbb Z}
 q^{(b-a)/2}\left(\int_F f(t_{a,b}n(u))\,du\right)x^ay^b.
 \tag{9}
\]
This formula fixes the convention: upper unipotents, \(tn\) in that order, and \(\delta^{1/2}\).

The Laurent variables have a concrete convolution meaning. Diagonal matrices modulo diagonal units form the group \(\mathbb Z^2\). Its finite-support functions have a basis \(\delta_{(a,b)}\), with \(\delta_{(a,b)}*\delta_{(c,d)}=\delta_{(a+c,b+d)}\). Sending that basis element to \(x^ay^b\) identifies the group algebra \(\mathbb C[\mathbb Z^2]\) with \(\mathbb C[x^{\pm1},y^{\pm1}]\). The interchange of the two diagonal coordinates acts by swapping \(x,y\). Thus the target below consists of symmetric Laurent polynomials, and evaluations use two nonzero parameters. This gives the torus algebra in the Satake comparison directly from its basis and product.

The expression is a finite Laurent polynomial. A compact matrix support and its inverse have uniform lower bounds on entry valuations, bounding both \(a\) and \(b\) above and below. For fixed \(a,b\), the upper-right entry bounds \(u\) in a compact additive ball. Right \(K\)-invariance makes the integrand constant on cosets of \(\mathcal O\), so its integral is a finite sum. Changing uniformizer by a unit changes neither the integral nor the monomial: a diagonal unit and a unit change of additive variable remove that change.

**Theorem 12.4 (Satake for \(\mathrm{GL}_2\)).** The map \(S\) is an algebra isomorphism
\[
 \mathcal H(G,K)\longrightarrow
 \mathbb C[x^{\pm1},y^{\pm1}]^{S_2},\qquad
 S(T)=q^{1/2}(x+y),\qquad S(R)=xy.
 \tag{10}
\]
Its unital complex algebra characters are parametrized by unordered pairs \(\{\alpha,\beta\}\) of nonzero complex numbers.

**Proof.** We first prove multiplicativity directly. A triangular basis for a lattice has first-axis intersection \(\pi^a\mathcal Oe_1\), second-coordinate projection \(\pi^b\mathcal O\), and second generator \(\pi^aue_1+\pi^be_2\), where \(u\) is unique modulo \(\mathcal O\). Consequently \(t_{a,b}n(u)K\), for \(u\in F/\mathcal O\), parametrizes \(G/K\) without repetition.

Fix \(\alpha,\beta\ne0\), and define the unramified character \(\chi\) of \(B\) by \(\chi(t_{a,b}n(u))=\alpha^a\beta^b\), trivial on diagonal units. Consider smooth functions \(\Phi\) on \(G\) satisfying \(\Phi(bg)=\delta(b)^{1/2}\chi(b)\Phi(g)\), acted on by \((\rho(g)\Phi)(h)=\Phi(hg)\). Here smooth means invariant on the right under some compact open subgroup. Iwasawa decomposition \(G=BK\) implies that the \(K\)-fixed space is a line: its distinguished element \(\Phi_0\) takes value one on \(K\) and value \(\delta(b)^{1/2}\chi(b)\) on \(bK\). This is well defined because both factors are one on \(B\cap K\).

A bi-\(K\) function acts on this line by \(\rho(f)=\int f(g)\rho(g)\,dg\). On \(\Phi_0\) this is a finite sum over right \(K\)-cosets. Its scalar, obtained by evaluation at one, is exactly \(Sf(\alpha,\beta)\), by the parametrization above. The representation identity and compact-support Fubini give \(\rho(f*h)=\rho(f)\rho(h)\). Hence \(S(f*h)(\alpha,\beta)=Sf(\alpha,\beta)Sh(\alpha,\beta)\) for every nonzero pair. A Laurent polynomial vanishing on all such pairs is zero: clear negative exponents and apply the one-variable polynomial root bound successively. Thus \(S\) is multiplicative.

For \(T\), only \((a,b)=(1,0),(0,1)\) contribute. In the first case integrality requires \(u\in\pi^{-1}\mathcal O\), of volume \(q\), and the modulus factor is \(q^{-1/2}\). In the second case \(u\in\mathcal O\), and the factor is \(q^{1/2}\). Both contributions are \(q^{1/2}\). For \(R\), only \((1,1)\) occurs; being in \(\pi K\) requires \(u\in\mathcal O\), and the modulus is one. This proves (10) and gives \(S(R^{-1})=(xy)^{-1}\).

Every symmetric Laurent polynomial is a polynomial in \(x+y,xy,(xy)^{-1}\). Multiply by a large power of \(xy\) to reduce to symmetric ordinary polynomials. For a homogeneous such polynomial, its largest pair of exponents \((a,b),(b,a)\), with \(a>b\), is removed by a multiple of \((xy)^b(x+y)^{a-b}\); a diagonal term is removed by \((xy)^a\). Repeating decreases the largest exponent and terminates. Apply this to every homogeneous component.

Moreover \(x+y\) and \(xy\) are algebraically independent: for every \(c\in\mathbb C\) and \(d\ne0\), the two roots of \(z^2-cz+d\) give nonzero \(x,y\) with that sum and product. A polynomial relation would vanish for all \(c,d\ne0\) and hence identically. The polynomial presentation in Theorem 12.3 now proves both injectivity and surjectivity of \(S\).

A character assigns a value \(t\) to \(T\) and a nonzero value \(r\) to the invertible element \(R\). The roots of \(z^2-(t/q^{1/2})z+r\) are the required unordered nonzero parameters. Conversely evaluating symmetric Laurent polynomials at such a pair gives a character. □

The trivial representation supplies a normalization check. In the preceding induced model, a constant function corresponds to \(\delta^{1/2}\chi=1\), namely \(\alpha=q^{1/2},\beta=q^{-1/2}\). Formula (10) then gives \(T=q+1\) and \(R=1\), exactly the lattice count. These Satake parameters classify algebra characters here; a classification of irreducible spherical representations requires further representation theory.

## Local multiplication and the global algebra

Write \(h_n(x,y)=\sum_{j=0}^n x^{n-j}y^j\). Applying \(S\) to the series in (5) gives
\[
 SH_n=q^{n/2}h_n(x,y),\qquad
 \sum_{n\ge0}SH_nX^n=
 \frac1{(1-q^{1/2}xX)(1-q^{1/2}yX)}.
 \tag{11}
\]
For every \(m,n\ge0\), the elementary polynomial identity
\[
 h_mh_n=\sum_{j=0}^{\min(m,n)}(xy)^j h_{m+n-2j}
 \tag{12}
\]
holds. Indeed the coefficient of \(x^{m+n-k}y^k\) on the left counts pairs \(r+s=k\) with \(0\le r\le m\), \(0\le s\le n\). For \(0\le k\le m+n\) this count is \(1+\min(m,n,k,m+n-k)\). On the right, exactly the integers \(0\le j\le\min(m,n,k,m+n-k)\) contribute one each. Thus all coefficients agree. Injectivity of \(S\) proves
\[
 H_mH_n=\sum_{j=0}^{\min(m,n)}q^jR^jH_{m+n-2j}.
 \tag{13}
\]

Now put \(G_f=\mathrm{GL}_2(\mathbb A_f)\) and \(K_f=\mathrm{GL}_2(\widehat{\mathbb Z})\), of volume one. The restricted product uses the local \(K_p\). Every \(K_f\)-double coset is the product of local double cosets, with only finitely many nontrivial components. The local elementary-divisor exponents determine it uniquely. Its indicator is therefore an elementary tensor, with factor \(1_{K_p}\) almost everywhere. Finite sums of these tensors are all compactly supported bi-\(K_f\) functions, since the double-coset quotient is discrete. Factoring the finite convolution sums, or the corresponding product integrals, proves
\[
 \mathcal H(G_f,K_f)\simeq\bigotimes_p'\mathcal H_p.
 \tag{14}
\]
The reference vectors for this algebraic restricted tensor product are its local units; no topological completion is involved.

For a rational rank-two integer lattice \(L\subset\mathbb Q^2\), define right operators
\([L]\cdot T(n)=\sum_{L'\subset L,\,[L:L']=n}[L']\)
and \([L]\cdot R(d)=[dL]\), for positive integers \(n,d\). The finite-adèlic dictionary from the preceding lesson sends completion of \(L\) to the corresponding compact module. Elementary divisors show that
\[
 T(n)=\prod_p H_{p,v_p(n)},\qquad
 R(d)=\prod_p R_p^{v_p(d)}.
 \tag{15}
\]
The local data are finite, and their rational intersection reconstructs the unique integer sublattice. In particular there is no extra multiplicity in this factorization.

Here is the precise classical comparison. Let \(\Gamma=\mathrm{SL}_2(\mathbb Z)\), \(G^+=\mathrm{GL}_2^+(\mathbb Q)\), and \(\Delta=M_2(\mathbb Z)\cap G^+\). Let \(\mathcal H_{\mathbb Z}(\Delta,\Gamma)\) be the integral double-coset ring, with finite sums and the counting convolution (1). The subgroup \(\Gamma\) is commensurated by every rational invertible matrix: if both \(dA\) and \(dA^{-1}\) are integral, conjugation of \(I+d^2B\) by \(A\) or \(A^{-1}\) is integral. Thus a principal congruence subgroup of finite index lies in each required intersection. This proves finiteness of the coset sums. Support in \(\Delta\) is preserved by multiplication.

**Theorem 12.5.** On lattices in \(\mathbb Q^2\),
\[
 T(m)T(n)=\sum_{d\mid(m,n)}d\,R(d)T(mn/d^2).
 \tag{16}
\]
Moreover the classical integral ring, with matching integral coefficients, is
\[
 \mathcal H_{\mathbb Z}(\Delta,\Gamma)
   \simeq\bigotimes_p'\mathbb Z[T_p,R_p].
 \tag{17}
\]
After extending coefficients to \(\mathbb C\) and inverting every \(R_p\), it becomes the full algebra in (14). Without that localization, its complexification is the subalgebra supported on integral finite-adèlic matrices.

We prove the elementary approximation assertion needed for the comparison first.

**Lemma 12.6.** For every positive integer \(N\), the map \(\mathrm{SL}_2(\mathbb Z)\to\mathrm{SL}_2(\mathbb Z/N\mathbb Z)\) is surjective. Consequently \(\Gamma\) is dense in \(\mathrm{SL}_2(\widehat{\mathbb Z})\).

**Proof.** The case \(N=1\) is immediate. Work in \(A=\mathbb Z/N\mathbb Z\), and let the first column of a determinant-one matrix be \((a,c)^t\). For every prime dividing \(N\), the two entries cannot both vanish modulo that prime. Choose a residue \(t\) making \(a+tc\ne0\) modulo each such prime: if \(c\ne0\), avoid its unique forbidden value; if \(c=0\), every value works. The Chinese remainder theorem gives a common \(t\). Thus \(u=a+tc\) is a unit in \(A\).

Left multiplication by the elementary matrices \(E_{12}(t)\) and \(E_{21}(-cu^{-1})\) makes the first column \((u,0)^t\). The remaining diagonal entry is \(u^{-1}\), by the determinant, and another upper elementary operation clears the upper-right entry. Finally
\[
 w(u)=E_{12}(u)E_{21}(-u^{-1})E_{12}(u)
      =\begin{pmatrix}0&u\\-u^{-1}&0\end{pmatrix},\qquad
 \operatorname{diag}(u,u^{-1})=w(u)w(-1).
 \tag{18}
\]
Every matrix used, and its inverse, is therefore a product of elementary matrices. Each elementary parameter lifts to an integer, giving a lift in \(\mathrm{SL}_2(\mathbb Z)\). The congruence kernels form a neighbourhood basis in the profinite group, so surjectivity for every \(N\) proves density. □

**Proof of Theorem 12.5.** Equations (13) and (15) prove (16): the choices \(j_p\) become the divisor \(d=\prod p^{j_p}\), their coefficients multiply to \(d\), and their central factors to \(R(d)\). This argument keeps the actual scalar lattice \(dL\).

For (17), first establish the integer Smith form in rank two. Integral invertible row and column operations move a nonzero entry to the upper-left corner and apply Euclidean division to its row and column. Whenever a division produces a nonzero remainder, move it to the pivot position; its positive absolute value is smaller. Once the first row and column clear, the matrix is diagonal \(\operatorname{diag}(b,a)\). If \(b\nmid a\), adding the second row to the first and dividing the new off-diagonal entry by \(b\) produces a smaller nonzero remainder, so pivot descent resumes. Positive descent terminates at \(b\mid a\). Signs and a simultaneous interchange of rows and columns give \(D=\operatorname{diag}(a,b)\), with \(a,b>0\) and \(b\mid a\). The smaller entry \(b\) is the greatest common divisor of all entries, and \(ab\) is the positive determinant, proving uniqueness.

Initially the reducing matrices may be in \(\mathrm{GL}_2(\mathbb Z)\). Their determinants have the same sign because both \(A\) and \(D\) have positive determinant. If both signs are negative, put \(J=\operatorname{diag}(-1,1)\) and replace a factorization \(UAV=D\) by \((JU)A(VJ)=D\). Since \(JDJ=D\), both new reducing matrices have determinant one. Thus the classical \(\Gamma\)-double cosets are precisely the classes of these \(D\).

The local elementary divisors of \(D\) are \((v_p(a),v_p(b))\). Conversely any finitely supported list with \(a_p\ge b_p\ge0\) reconstructs unique positive integers \(a=\prod p^{a_p}\), \(b=\prod p^{b_p}\), with \(b\mid a\). This gives the double-coset bijection. To identify multiplication, we must also identify every right coset inside each double coset.

The classical right cosets in \(\Gamma D\Gamma\) are exactly the distinct lattices \(\gamma D\mathbb Z^2\). If two such matrices give the same lattice, their basis change is integral with determinant one, so they differ on the right by \(\Gamma\). The adelic right cosets in \(K_fDK_f\) give the compact modules \(kD\widehat{\mathbb Z}^2\). Their stabilizer within \(K_f\) is \(J_D=K_f\cap DK_fD^{-1}\), a compact open subgroup. Its determinant maps onto \(\widehat{\mathbb Z}^{\times}\): every diagonal unit matrix lies in \(J_D\). For any \(k\in K_f\), choose \(h\in J_D\) with \(\det h=(\det k)^{-1}\). Then \(kh\in\mathrm{SL}_2(\widehat{\mathbb Z})\) gives the same module as \(k\). Lemma 12.6 supplies \(\gamma\in\Gamma\) in the open coset \(kh(J_D\cap\mathrm{SL}_2(\widehat{\mathbb Z}))\); it gives exactly that module. The rational-intersection dictionary makes this a bijection of actual lattices. Notice that only special-linear density was used.

These right-coset bijections preserve chains of sublattices. The faithful action on their free vector space therefore identifies all convolution coefficients, not just the basis labels. Each local integral ring is \(\mathbb Z[T_p,R_p]\), by the integer form of Theorem 12.3, proving (17).

Finally \(R(p)\) has no inverse in the classical integral ring. Grade a double coset by its positive integer determinant. Multiplying by \(R(p)\) multiplies that grade by \(p^2\). No finite linear combination of the resulting grades can equal the grade-one identity. In the rational ring \(\mathcal H_{\mathbb Z}(G^+,\Gamma)\), however, its inverse is the single scalar coset \(p^{-1}\Gamma\). Every finite rational support can be made integral by an integer scalar \(d\) clearing its entry denominators. The same is true of a compact adelic support, either by its finite double-coset expansion or the restricted-product compactness criterion. Hence
\[
 \mathcal H(G_f,K_f)
 \simeq\left(\mathbb C\otimes_{\mathbb Z}
       \mathcal H_{\mathbb Z}(\Delta,\Gamma)\right)
       [R(p)^{-1}:p\text{ prime}].
 \tag{19}
\]
Injectivity follows from the faithful embedding of the integral algebra and the invertibility of its scalar translations; clearing denominators proves surjectivity. The same proof identifies the rational classical integral-coefficient ring with the corresponding localization of (17). □

For example \(T(2)T(3)=T(6)\), while \(T(6)^2=T(36)+2R(2)T(9)+3R(3)T(4)+6R(6)\). The central term \(R(d)\) is indispensable. Passing to tree vertices makes a local \(R\) equal one, but applying a weight-dependent homogeneity rule to functions on complex lattices is a different operation.

## Why the ax + b Hecke algebra can fail to commute

The preceding arguments use matrix elementary divisors. They do not imply commutativity for every Hecke pair. For a direct contrast, let
\[
 P=\left\{\begin{pmatrix}1&b\\0&a\end{pmatrix}:
                  b\in\mathbb Q,\ a\in\mathbb Q_{>0}\right\},\qquad
 P_0=\left\{\begin{pmatrix}1&n\\0&1\end{pmatrix}:n\in\mathbb Z\right\}.
 \tag{20}
\]
Conjugation by an element with lower-right entry \(a\) sends integer translations to \(a^{-1}\mathbb Z\), commensurable with \(\mathbb Z\). Thus the right-coset convolution (1) again has finite sums for double-coset indicators. Equivalently, setting \(y=x^{-1}g\) writes it as a sum over left cosets, \(\sum_{P_0y}f(gy^{-1})h(y)\).

Put \(s=\operatorname{diag}(1,2)\), and let \(A,B\) be the indicators of \(P_0sP_0,P_0s^{-1}P_0\). Since \(sP_0s^{-1}\) is the half-integer translation subgroup, the first double coset is \(sP_0\), with one right coset. The second has two right cosets, because \(s^{-1}P_0s\) is the even-integer translation subgroup. At the identity, every coset of the first support contributes one to \(A*B\), while every coset of the second contributes one to \(B*A\). Therefore
\[
 (A*B)(1)=1,\qquad (B*A)(1)=2.
 \tag{21}
\]
This proves noncommutativity already in the algebraic Hecke algebra. The dynamical completion, equilibrium states and symmetry breaking of the Bost–Connes system require additional analysis.

## Exercises

1. **Easy.** For a rank-two \(\mathbb Z_p\)-lattice \(L\), count length-two chains of index-\(p\) inclusions and prove \(T(p)^2=T(p^2)+pR(p)\). Explain the coefficient of \(pL\).
2. **Medium.** Prove the commutativity assertion using transposition, keeping the measure changes explicit.
3. **Medium.** Compute \(S(T),S(R)\) from the defining integral and use them to verify the generating series. Check the trivial representation.
4. **Hard.** Prove (16), including its scalar factors and all multiplicities.

**Solution 1.** A final index-\(p^2\) lattice \(M\) has quotient type \(\mathbb Z/p^2\) or \((\mathbb Z/p)^2\). In the cyclic case its unique subgroup of order \(p\) gives exactly one intermediate lattice. In the second case, elementary divisors force \(M=pL\); the intermediate lattices correspond to the \(p+1\) lines of \(L/pL\). Thus the sum over all final lattices has coefficient one everywhere except coefficient \(p+1\) at \(pL\). The operator \(T(p^2)\) includes \(pL\) once, and \(pR(p)\) contributes its other \(p\) copies. This proves the identity, including the scalar term.

**Solution 2.** Matrix-entry Haar measure times \(|\det|^{-2}\) is invariant under both translations and transposition. Unimodularity makes inversion measure preserving. For \(\tau(g)=g^t\),
\((f*h)(g^t)=\int f(z^t)h((gz^{-1})^t)\,dz\). Substitute \(z=y^{-1}g\), using inversion and right translation, to get \(\int h(y^t)f((y^{-1}g)^t)\,dy\). This is \(h^\tau*f^\tau\). Cartan decomposition writes every double coset as \(K\operatorname{diag}(\pi^a,\pi^b)K\); transposition fixes this set because it fixes the diagonal representative and maps \(K\) to itself. Hence \(f^\tau=f,h^\tau=h\), proving commutativity.

**Solution 3.** For \(t_{1,0}n(u)\), integral entries and determinant valuation one give exactly \(u\in\pi^{-1}\mathcal O\). Its volume \(q\) times \(\delta^{1/2}=q^{-1/2}\) is \(q^{1/2}\). For \(t_{0,1}n(u)\), the allowed set is \(\mathcal O\), of volume one, and the factor is \(q^{1/2}\). No other diagonal exponents have nonzero contribution. Thus \(S(T)=q^{1/2}(x+y)\). The scalar coset requires \(a=b=1\) and \(u\in\mathcal O\), giving \(S(R)=xy\). The quadratic series denominator becomes \(1-q^{1/2}(x+y)X+qxyX^2=(1-q^{1/2}xX)(1-q^{1/2}yX)\). Expanding both geometric series gives \(SH_n=q^{n/2}\sum_{j=0}^n x^{n-j}y^j\), which verifies every coefficient. At \(x=q^{1/2},y=q^{-1/2}\), the values are \(q+1\) and one, the trivial-representation values.

**Solution 4.** First work at one prime, with \(m=p^u,n=p^v\). The coefficient of \(x^{u+v-k}y^k\) in \(h_uh_v\) counts all \(r\) in the interval \(\max(0,k-v)\le r\le\min(u,k)\). For \(0\le k\le u+v\), its size is \(1+\min(u,v,k,u+v-k)\). The sum \(\sum_{j=0}^{\min(u,v)}(xy)^jh_{u+v-2j}\) has precisely that coefficient, since its contributing indices satisfy \(j\le k\) and \(j\le u+v-k\). This proves (12). Multiplying by \(p^{(u+v)/2}\) and using (11) converts its \(j\)-term into \(S(p^jR_p^jH_{u+v-2j})\). Injectivity gives the local product with coefficient \(p^j\). Factor arbitrary \(m,n\) over all primes by (15). Each tuple \((j_p)\), with \(0\le j_p\le\min(v_p(m),v_p(n))\), is exactly one divisor \(d\mid(m,n)\). The coefficients, scalar operations and remaining indices become respectively \(d,R(d),mn/d^2\). Distributing the finite product gives every term of (16) once.

## Prerequisites and further directions

The local Cartan and Iwasawa decompositions, identification of \(G/K\) with lattices, tree distance and finite-adèlic rational-intersection dictionary are the exact results of *Lattices over a local field: the tree of GL_2 and its decompositions*, Theorem 11.2, Proposition 11.4, Proposition 11.1 and equation (9). The restricted-product topology and compactness criterion are from *Restricted products and profinite completions*. These are the course-specific prerequisites used without proof here. We also use basic Haar integration and compact-support Fubini, the Chinese remainder theorem from *Restricted products and profinite completions*, and elementary polynomial root facts.

We have classified spherical algebra characters, without asserting that all irreducible spherical representations have been constructed or classified. We do not derive the weight factors of modular-form Hecke operators, the Kirillov model, the representation-theoretic tensor product theorem, or the Bost–Connes equilibrium-state classification. The lattice operators here use counting measure and retain \(R(d)\); further specializations must state their own conventions.

## References and convention comparisons

- Jacquet and Langlands, [*Automorphic Forms on GL(2)*, IAS retyped edition](https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2_rpl.pdf), §9, especially the restricted tensor algebra and its idempotents PDF pages 159–162. Equation (14) proves the compact-open spherical algebra factorization independently; no representation tensor-product theorem is imported.
- Getz and Hahn, [*An Introduction to Automorphic Representations*, April 22, 2022 draft](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §§5.1–5.2 and 5.5, Example 5.2, §§7.2 and 7.5, Definition 7.27: spherical convolution, elementary divisors and the Satake transform. Our upper-triangular \(tn\) integral uses the modulus in (8); the direct calculation and trivial-representation test fix its normalization. The Laurent group algebra is constructed explicitly above, and Theorem 12.4 supplies the complete \(\mathrm{GL}_2\) proof.
- Connes and Marcolli, [*Noncommutative Geometry, Quantum Fields and Motives*, author version](https://alainconnes.org/wp-content/uploads/bookwebfinal-2.pdf), Chapter 3, §5.2, (3.183)–(3.200), PDF pages 444–448: the two-dimensional rational-lattice groupoid and its convolution. Its extra finite torsion datum and archimedean variable are part of that larger groupoid; our integral semigroup, scalar localization and coefficient extension in (17)–(19) concern the spherical lattice algebra.
- Bost and Connes, [*Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, author scan](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf), §1 PDF pages 3–4: the classical lattice algebra and almost-normal-pair convolution. Equation (21) exhibits the ax + b contrast by a complete finite coset count. The present operators act on actual lattices, retain \(R(d)\), and carry no modular weight factor.
- Deligne, [*Formes modulaires et représentations de GL(2)*, IAS edition](https://publications.ias.edu/sites/default/files/Number21.pdf), §§0.1 and 2.3, printed pages 59–61 and 83–84, PDF pages 5–7 and 29–30: the full-adèlic lattice dictionary and normalized local Hecke operator. The operator in §2.3 is \(p^{-1}\) times the double-coset indicator operator; our \(T\) is the unscaled indicator.
