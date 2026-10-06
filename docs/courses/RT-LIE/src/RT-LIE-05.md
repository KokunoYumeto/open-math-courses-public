# Representations of \(\mathfrak{sl}_2\)

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The three operators of \(\mathfrak{sl}_2\) move along one sequence of weights. In finite dimension that sequence has two endpoints, and the commutator relation determines both its length and every coefficient. The same formulas, continued without a lower endpoint, produce Verma modules. This lesson develops both constructions and uses the finite ones to compute tensor products.

All vector spaces and Lie algebras here are over \(\mathbb C\). We use [Complete reducibility: Casimir elements and Weyl's theorem](RT-LIE-04.md), especially Weyl's theorem and preservation of Jordan decomposition, and the enveloping-algebra universal property from [Lie algebras: definitions, examples and first constructions](RT-LIE-01.md). We distinguish a highest weight from a dimension: \(V(n)\) has highest weight \(n\) and dimension \(n+1\).

## 1. The commutator determines the sequence

Fix
\[
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
Their relations are
\[
[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h.
\tag{1.1}
\]
The Killing-form calculation in the preceding lessons proves that this algebra is semisimple. Its adjoint action makes \(h\) semisimple, with eigenvalues \(2,0,-2\); the adjoint actions of \(e\) and \(f\) are nilpotent, each with cube zero. Preservation of Jordan decomposition therefore says that, on every finite-dimensional module, \(h\) is diagonalizable and \(e,f\) are nilpotent.

For a module with diagonalizable \(h\), define its **weight space**
\[
V[\lambda]=\{v:hv=\lambda v\}.
\]
Equation (1.1) gives
\[
eV[\lambda]\subseteq V[\lambda+2],\qquad
fV[\lambda]\subseteq V[\lambda-2]:
\tag{1.2}
\]
indeed \(h(ev)=ehv+2ev=(\lambda+2)ev\), and \(h(fv)=fhv-2fv=(\lambda-2)fv\).

A **highest-weight vector** is a nonzero vector \(v\) such that \(ev=0\) and \(hv=\lambda v\). Every nonzero finite-dimensional module contains one. Take a nonzero \(h\)-eigenvector and apply \(e\) until the last nonzero iterate; nilpotence guarantees such an iterate, and (1.2) keeps it an eigenvector.

The following identity applies to any highest-weight vector, in finite or infinite dimension:
\[
h f^i v=(\lambda-2i)f^i v,\qquad
e f^i v=i(\lambda-i+1)f^{i-1}v \quad(i\ge1).
\tag{1.3}
\]
The first assertion follows by repeating (1.2). For the second, the case \(i=1\) is \(efv=f ev+hv=\lambda v\). If it holds for \(i\), then
\[
\begin{aligned}
ef^{i+1}v
&=(fe+h)f^iv\\
&=\bigl(i(\lambda-i+1)+\lambda-2i\bigr)f^iv\\
&=(i+1)(\lambda-i)f^iv.
\end{aligned}
\]
This proves it by induction.

If \(v\) belongs to a finite-dimensional module, let \(n\) be the last index for which \(f^nv\ne0\). It exists because \(f\) is nilpotent. The earlier iterates are nonzero, and their distinct \(h\)-weights make them independent. Applying (1.3) to the zero vector \(f^{n+1}v\) yields
\[
0=(n+1)(\lambda-n)f^nv.
\]
Thus
\[
\lambda=n\in\mathbb Z_{\ge0}.
\tag{1.4}
\]
This calculation is the reason that highest weights in finite dimension are nonnegative integers.

## 2. All finite-dimensional simple modules

**Theorem 2.1.** For every \(n\ge0\) there is, up to isomorphism, exactly one irreducible \(\mathfrak{sl}_2\)-module \(V(n)\) of dimension \(n+1\). It has a basis \(v_0,\ldots,v_n\) with
\[
\begin{aligned}
hv_i&=(n-2i)v_i,\\
fv_i&=v_{i+1}\quad(i<n),\qquad fv_n=0,\\
ev_i&=i(n-i+1)v_{i-1}\quad(i>0),\qquad ev_0=0.
\end{aligned}
\tag{2.1}
\]
Every finite-dimensional irreducible module is one of these. Its weights are \(n,n-2,\ldots,-n\), each with multiplicity one.

**Proof.** First construct \(V(n)\). On the homogeneous polynomials of degree \(n\) in variables \(u,t\), put
\[
e=u\partial_t,\qquad f=t\partial_u,\qquad
h=u\partial_u-t\partial_t.
\tag{2.2}
\]
The product rule gives their brackets. For example, on any polynomial \(P\),
\[
(ef-fe)P=u\partial_uP-t\partial_tP=hP;
\]
the mixed second derivatives cancel. Computing similarly gives \([h,e]P=2eP\) and \([h,f]P=-2fP\). Degree is preserved, so this is a representation on the indicated space.

Its basis
\[
v_i=f^i u^n=\frac{n!}{(n-i)!}u^{n-i}t^i,\qquad 0\le i\le n,
\tag{2.3}
\]
satisfies (2.1). The coefficients in (2.3) are nonzero, including the coefficient for \(i=0\). The monomials are a basis, so these vectors are independent and span.

To prove irreducibility, let \(W\) be a nonzero submodule. A nonzero vector of \(W\) has a nonzero component along some \(v_i\). Polynomial interpolation in \(h\) isolates that component: the polynomial which is \(1\) on \(n-2i\) and \(0\) on the other finitely many weights sends it to a nonzero multiple of \(v_i\). Hence \(v_i\in W\). All coefficients encountered in \(e^i v_i\) are nonzero, so \(v_0\in W\). Its successive \(f\)-iterates give every \(v_j\), and \(W=V(n)\).

Now take any finite-dimensional irreducible module and a highest-weight vector \(v\). Section 1 gives its weight \(n\ge0\). The span of \(v,fv,\ldots,f^nv\) is a nonzero submodule by (1.3); irreducibility makes it the entire module. Its basis has precisely (2.1), so sending \(v_i\) to \(f^iv\) gives an isomorphism with the constructed \(V(n)\). Finally, different \(n\)'s have different dimensions. This proves existence, uniqueness and exhaustiveness. \(\square\)

In particular \(V(0)\) is the trivial line and \(V(1)\) is the standard module. The module \(V(2)\) is the adjoint module. An explicit intertwiner is
\[
v_0\longmapsto e,\qquad v_1\longmapsto-h,\qquad
v_2\longmapsto-2f.
\tag{2.4}
\]
Bracketing these images with \(e,h,f\) gives exactly (2.1).

### 2.2. The polynomial action of \(SL_2\)

**Proposition 2.2.** For every commutative ring \(R\), the free module of homogeneous polynomials \(R[u,t]_n\cong\operatorname{Sym}^n(R^2)\) has the polynomial \(SL_2(R)\)-action
\[
\rho_n\!\begin{pmatrix}a&b\\c&d\end{pmatrix}P(u,t)
=P(au+ct,bu+dt).
\tag{2.5}
\]
These actions commute with homomorphisms of ground rings. Their differentials are exactly (2.2). Over \(\mathbb Q\), and after any characteristic-zero field extension, this differential representation is \(V(n)\).

**Proof.** Regard \((u,t)\) as a row of formal variables. Formula (2.5) substitutes \((u,t)g\) for \((u,t)\). Applying the substitutions for \(h\) and then \(g\) yields \(P((u,t)gh)\), so \(\rho_n(g)\rho_n(h)=\rho_n(gh)\). The identity matrix acts identically and \(g^{-1}\) gives the inverse. Linear substitution preserves homogeneous degree. Expanding monomials shows that all matrix coefficients are polynomials with integer coefficients in \(a,b,c,d\), so the formula defines an action of the group scheme \(SL_2\), and extension of coefficients preserves it.

To differentiate, work with \(\varepsilon^2=0\). The upper unipotent matrix with entry \(\varepsilon\) sends \((u,t)\) to \((u,t+\varepsilon u)\), giving \(u\partial_t\). The lower unipotent sends it to \((u+\varepsilon t,t)\), giving \(t\partial_u\). The diagonal matrix with entries \(1+\varepsilon,1-\varepsilon\) gives \(u\partial_u-t\partial_t\). Thus the three infinitesimal generators agree with (2.2). Over a characteristic-zero field the basis change (2.3) has nonzero factorial coefficients, and the same weight-projection and raising/lowering proof of Theorem 2.1 proves irreducibility. \(\square\)

The group action exists over rings and in positive characteristic, while the irreducibility statement has its characteristic-zero hypothesis. For example, in characteristic \(p\), the two-dimensional span of \(u^p,t^p\) is preserved inside \(R[u,t]_p\), because \((au+ct)^p=a^pu^p+c^pt^p\); over a field this is a proper submodule. The polynomial construction therefore supplies an integral action without extending the characteristic-zero classification to characteristic \(p\).

The basis in (2.1) uses \(f^iv_0\), without dividing by \(i!\). If the diagonal generator is instead \(h/2\), its eigenvalues are half the weights used here and the spin parameter is \(j=n/2\). Replacing the basis by \(f^iv_0/i!\) changes the displayed raising and lowering coefficients by the corresponding factorial ratios. These changes of normalization do not change the module.

## 3. A weight count determines the decomposition

**Corollary 3.1.** Every finite-dimensional module is a finite direct sum of the \(V(n)\). If
\[
d_r=\dim V[r],\qquad r\in\mathbb Z,
\]
then the multiplicity \(a_n\) of \(V(n)\), for \(n\ge0\), is
\[
a_n=d_n-d_{n+2}.
\tag{3.1}
\]
In particular its weights and their multiplicities determine its isomorphism class.

**Proof.** Weyl's theorem and Theorem 2.1 give the direct sum. A copy of \(V(q)\) contributes one to \(d_n\) exactly when \(q\ge n\) and \(q-n\) is even. Therefore
\[
d_n=a_n+a_{n+2}+a_{n+4}+\cdots,
\]
a finite sum. Subtract the corresponding formula for \(d_{n+2}\) to obtain (3.1). The multiplicities are unique, and direct sums with those multiplicities are isomorphic. \(\square\)

All weights are integers and \(d_r=d_{-r}\). For instance, if a module has multiplicities
\[
d_4=d_{-4}=1,\quad d_2=d_{-2}=3,\quad d_0=4
\]
and no other weights, then it is \(V(4)\oplus2V(2)\oplus V(0)\), of dimension \(5+6+1=12\).

For each \(r\ge0\), the correctly directed weight-reversal maps are
\[
f^r:V[r]\longrightarrow V[-r],\qquad
e^r:V[-r]\longrightarrow V[r],
\tag{3.2}
\]
and both are isomorphisms. On each simple summand having these weights, the relevant indices in (2.1) are \((n-r)/2\) and \((n+r)/2\). The first map traverses \(r\) nonzero lowering steps; the second traverses \(r\) raising steps with nonzero coefficients. Summands having neither weight contribute zero spaces. Direct sums prove (3.2), including \(r=0\). Raising by \(e\) cannot map a positive weight to its negative; the two operator names in the displayed maps of [Kirillov, Theorem 4.60(2)] are interchanged.

For bookkeeping write
\[
\operatorname{ch}V=\sum_{r\in\mathbb Z}d_r z^r.
\]
This is a finite Laurent polynomial, called the **formal character**. Characters add on direct sums and multiply on tensor products: the tensor action of \(h\) adds the two weights, and tensor products of weight-space bases give a basis of each resulting weight space. Equation (3.1) proves that equal characters imply isomorphic finite-dimensional modules.

## 4. Tensor products and the form used for the Casimir

Let \(B(x,y)=\operatorname{tr}_{\mathbb C^2}(xy)\) on the algebra. The preceding lesson proved centrality of
\[
C_B=ef+fe+\frac12h^2,\qquad C_\kappa=\frac14C_B,
\tag{4.1}
\]
where \(\kappa=4B\) is the Killing form.

**Proposition 4.1.** On \(V(n)\) these elements act, respectively, by
\[
\frac{n(n+2)}2,\qquad \frac{n(n+2)}8.
\tag{4.2}
\]

**Proof.** Since \(ev_0=0\), \(fev_0=0\) and \(efv_0=hv_0=nv_0\). Thus \(C_Bv_0=(n+n^2/2)v_0\). Centrality makes \(C_B\) commute with \(f\), so it has this scalar on all \(f^iv_0\). Scaling gives the Killing value. \(\square\)

The form \(B\) in (4.1) is the trace form of the standard two-dimensional module, even when the element acts on another module. It is not the trace form of \(V(n)\). In fact, for \(n>0\) the latter is
\[
B_n=\frac{n(n+1)(n+2)}6 B.
\tag{4.3}
\]
Here is a direct check. In (2.1),
\[
\operatorname{tr}(h^2)=\sum_{i=0}^n(n-2i)^2
=\frac{n(n+1)(n+2)}3.
\]
The sum follows by expansion using
\(\sum i=n(n+1)/2\) and \(\sum i^2=n(n+1)(2n+1)/6\), both verified by induction. The products \(e^2,f^2,eh,he,fh,hf\) have zero diagonal. Trace cyclicity and (1.1) give
\(\operatorname{tr}(h^2)=\operatorname{tr}(h[e,f])=\operatorname{tr}([h,e]f)=2\operatorname{tr}(ef)\).
These nine pairings prove (4.3). Consequently the Casimir for \(B_n\) has scalar \(3/(n+1)\), as the faithful trace-form theorem predicts. For \(n=0\), \(B_n=0\) and cannot define a dual-basis Casimir.

**Theorem 4.2 (Clebsch–Gordan).** For \(m,n\ge0\),
\[
V(m)\otimes V(n)\simeq
\bigoplus_{k=0}^{\min(m,n)}V(m+n-2k).
\tag{4.4}
\]

**Proof from weights.** Interchanging tensor factors is an intertwiner, so suppose \(m\le n\). The multiplicity of weight \(m+n-2r\) in the tensor product is the number of pairs
\[
0\le a\le m,\quad0\le b\le n,\quad a+b=r.
\]
For \(0\le r\le m+n\), it is
\[
\min(m,r)-\max(0,r-n)+1
=\min(m,r,m+n-r)+1.
\tag{4.5}
\]
The equality follows in the three ranges \(r\le m\), \(m\le r\le n\), and \(r\ge n\). Outside this interval the multiplicity is zero.

In the right side of (4.4), that weight occurs in \(V(m+n-2k)\) exactly when \(k\le r\le m+n-k\), with \(0\le k\le m\). Its multiplicity is therefore also (4.5). All other weights have zero multiplicity on both sides. The character and multiplicity result of Section 3 proves the claimed isomorphism. \(\square\)

One can also locate every summand explicitly. In the bases (2.1), write the tensor factors' vectors as \(v_i,w_j\). For \(0\le k\le\min(m,n)\), set
\[
q_k=\sum_{i=0}^k c_i v_i\otimes w_{k-i},\qquad c_0=1,
\]
where
\[
c_{i+1}=-c_i\,
\frac{(k-i)(n-k+i+1)}{(i+1)(m-i)}
\quad(0\le i<k).
\tag{4.6}
\]
All denominators are nonzero. The coefficient of \(v_i\otimes w_{k-1-i}\) in \(eq_k\) is
\[
c_{i+1}(i+1)(m-i)+c_i(k-i)(n-k+i+1)=0.
\]
Thus \(q_k\) is a nonzero highest-weight vector of weight \(m+n-2k\). Section 1 and Theorem 2.1 show that its iterates generate the corresponding simple module. Their Casimir scalars (4.2) are distinct, since these highest weights are distinct nonnegative integers. Polynomial projection in \(C_B\) makes their sum direct. Its dimension, when \(m\le n\), is
\[
\sum_{k=0}^m(m+n-2k+1)=(m+1)(n+1),
\]
so these explicitly constructed submodules exhaust the tensor product.

For example,
\[
V(1)\otimes V(1)=V(2)\oplus V(0),\qquad
V(1)^{\otimes3}=V(3)\oplus2V(1).
\tag{4.7}
\]
In the first tensor square, \(v_0\otimes v_1-v_1\otimes v_0\) generates the trivial summand. Its \(e,f,h\) images all vanish. The highest-weight-two vector \(v_0\otimes v_0\) generates the other summand. Applying (4.4) to these two summands and the third factor gives the second decomposition. The weight-three, one, minus-one, minus-three dimensions are \(1,3,3,1\), confirming multiplicities \(1\) and \(2\) by (3.1).

## 5. Continue the sequence: Verma modules

Let \(\mathfrak b=\mathbb Ch\oplus\mathbb Ce\), the upper triangular subalgebra. For \(\lambda\in\mathbb C\), let \(\mathbb C_\lambda\) be its one-dimensional module with \(h\) acting by \(\lambda\) and \(e\) by zero. Its action respects \([h,e]=2e\).

Define the **Verma module**
\[
M(\lambda)=U(\mathfrak{sl}_2)\otimes_{U(\mathfrak b)}\mathbb C_\lambda.
\tag{5.1}
\]
Equivalently it is the left module
\[
U(\mathfrak{sl}_2)\big/\bigl(U(\mathfrak{sl}_2)e+
U(\mathfrak{sl}_2)(h-\lambda)\bigr).
\tag{5.2}
\]
To check the equivalence, the coset \(v\) of \(1\) in (5.2) satisfies \(ev=0\), \(hv=\lambda v\). Every element \(a\in U(\mathfrak b)\) acts on \(v\) by its scalar action on \(\mathbb C_\lambda\), as follows by induction on products of \(e,h\). Therefore \(u\otimes c\mapsto cuv\) is well-defined. Conversely \(u\mapsto u\otimes1\) kills the displayed left ideal and induces a map from (5.2). The two maps are inverse on generators.

More generally, if a module \(N\) contains a highest-weight vector \(w\) of weight \(\lambda\), there is a unique module map
\[
M(\lambda)\longrightarrow N,\qquad u\otimes1\longmapsto uw.
\tag{5.3}
\]
The formula is well-defined by the same tensor relation, and uniqueness follows because \(v=1\otimes1\) generates. This is the highest-weight universal property.

**Lemma 5.1.** The vectors \(v_i=f^iv\), \(i\ge0\), are a basis of \(M(\lambda)\), and
\[
fv_i=v_{i+1},\qquad hv_i=(\lambda-2i)v_i,\qquad
ev_i=i(\lambda-i+1)v_{i-1},
\tag{5.4}
\]
with \(ev_0=0\).

**Proof.** For spanning, order the letters as \(f<h<e\). The relations replace every adjacent out-of-order pair by its ordered pair and a word of smaller length:
\[
ef=fe+h,\qquad eh=he-2e,\qquad hf=fh-2f.
\]
Induction first on length and then on the number of inversions shows that \(U(\mathfrak{sl}_2)\) is spanned by \(f^a h^b e^c\). In (5.2), acting on \(v\) eliminates \(c>0\); for \(c=0\) the value is \(\lambda^b f^av\). Thus the stated vectors span. No independence of all ordered enveloping monomials was assumed.

For independence, construct a vector space with independent basis \(t_0,t_1,\ldots\), and give it the formulas (5.4). The weight shifts give \([h,e]=2e\) and \([h,f]=-2f\). On \(t_i\),
\[
(ef-fe)t_i=
\bigl((i+1)(\lambda-i)-i(\lambda-i+1)\bigr)t_i
=(\lambda-2i)t_i.
\]
This includes \(i=0\), with the absent negative-index term zero. Hence it is a Lie representation. Its vector \(t_0\) has the required highest weight, so (5.3) maps \(f^iv\) to \(t_i\). Independence of these images proves independence in \(M(\lambda)\). Finally (1.3) gives its action formulas. \(\square\)

This proves the particular basis needed here directly. For comparison, the PBW theorem for this ordered basis states that the monomials \(f^a h^b e^c\), with \(a,b,c\ge0\), form a basis of \(U(\mathfrak{sl}_2)\). That stronger assertion is stated here without proof and is not used above. Its general form will be proved in *The universal enveloping algebra and the Poincaré–Birkhoff–Witt theorem*.

**Theorem 5.2.** The module \(M(\lambda)\) is irreducible exactly when \(\lambda\notin\mathbb Z_{\ge0}\). If \(\lambda=n\ge0\), it has exactly one proper nonzero submodule:
\[
\langle v_{n+1},v_{n+2},\ldots\rangle\simeq M(-n-2).
\tag{5.5}
\]
Its quotient is \(V(n)\).

**Proof.** Every vector is a finite linear combination of the \(v_i\), whose weights \(\lambda-2i\) are distinct. Given a submodule \(W\), interpolation in \(h\) isolates each nonzero weight component of any vector of \(W\). Thus \(W\) is spanned by the \(v_i\) which it contains.

If \(W\ne0\), choose the least \(j\) with \(v_j\in W\). Applying \(f\) gives all vectors with index at least \(j\), and minimality excludes lower ones. Hence
\[
W=\langle v_j,v_{j+1},\ldots\rangle.
\]
If \(j=0\), this is the whole module. If \(j>0\), invariance under \(e\) requires
\[
j(\lambda-j+1)=0,
\]
since \(v_{j-1}\notin W\). It follows that \(\lambda=j-1=n\ge0\), and \(j=n+1\). Conversely, for this parameter the indicated tail is invariant: \(e v_{n+1}=0\), and all later actions stay in the tail. This proves both irreducibility outside those parameters and uniqueness of the proper nonzero submodule at them.

Its vector \(v_{n+1}\) has highest weight \(-n-2\). Sending the \(i\)-th basis vector of \(M(-n-2)\) to \(v_{n+1+i}\) matches \(f\) and \(h\). Its \(e\)-coefficient is
\[
(n+1+i)(-i)=i(-n-2-i+1),
\]
so the map also intertwines \(e\). It is a basis bijection and proves (5.5). The quotient has basis \(v_0,\ldots,v_n\) with (2.1), hence is \(V(n)\). \(\square\)

For \(n\ge0\), the resulting exact sequence
\[
0\longrightarrow M(-n-2)\longrightarrow M(n)
\longrightarrow V(n)\longrightarrow0
\tag{5.6}
\]
does not split. The operator \(f\) is injective on \(M(n)\), as it shifts its basis. On a nonzero finite-dimensional module it is nilpotent and therefore has a nonzero kernel. An invariant complement in (5.6) would be a copy of \(V(n)\) inside \(M(n)\), contradicting those two properties.

In particular, \(M(0)\) has \(hv_i=-2iv_i\) and \(ev_i=i(1-i)v_{i-1}\); its unique proper nonzero submodule is \(M(-2)\), starting at \(v_1\), and its quotient is the trivial line. This is the infinite-dimensional nonsplitting example constructed in the preceding lesson.

Centrality and the cyclic highest-weight vector also give
\[
C_B|_{M(\lambda)}=\frac{\lambda(\lambda+2)}2\,1.
\tag{5.7}
\]
The reflected parameter \(-\lambda-2\) has the same scalar. Conversely equality of these quadratic scalars means that two parameters are equal or are related by that reflection, by factoring their difference. This equality does not assert that the Verma modules are isomorphic.

## 6. Exercises with complete solutions

**Exercise 6.1 (easy).** Write the matrices of \(e,h,f\) on \(V(2)\) in the basis (2.1), and identify this module with the adjoint representation.

**Solution.** Columns are images of basis vectors, so
\[
e=\begin{pmatrix}0&2&0\\0&0&2\\0&0&0\end{pmatrix},\quad
h=\begin{pmatrix}2&0&0\\0&0&0\\0&0&-2\end{pmatrix},\quad
f=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix}.
\]
The independent vectors \(e,-h,-2f\) of the algebra have these same action columns under brackets. For example \([e,-h]=2e\), \([e,-2f]=-2h\), \([f,e]=-h\), and \([f,-h]=-2f\); the \(h\)-weights are \(2,0,-2\). Sending the ordered module basis to these three vectors is the required intertwining isomorphism.

**Exercise 6.2 (medium).** Prove Clebsch–Gordan from weight multiplicities, including the endpoints and the case of a trivial factor.

**Solution.** Assume \(m\le n\) by the tensor flip. Weight \(m+n-2r\) has multiplicity equal to the number of integers \(a\) between \(\max(0,r-n)\) and \(\min(m,r)\). For \(0\le r\le m\) this number is \(r+1\); for \(m\le r\le n\) it is \(m+1\); for \(n\le r\le m+n\) it is \(m+n-r+1\). No pair exists outside \(0\le r\le m+n\).

In \(\bigoplus_{k=0}^m V(m+n-2k)\), the same weight appears once for each \(k\) satisfying \(0\le k\le\min(m,r,m+n-r)\). This gives exactly those three numbers and zero outside the interval. All weights have the same parity as \(m+n\), so none were omitted. Equality of characters and (3.1) prove the isomorphism. If \(m=0\), the sum has only \(V(n)\), consistent with tensoring by the trivial line. The endpoint weights correspond to \(r=0,m+n\), each of multiplicity one.

**Exercise 6.3 (medium).** Compute the Casimir eigenvalues on \(V(n)\) for the trace form of \(\mathbb C^2\) and for the Killing form. Convert them to the spin normalization.

**Solution.** For \(B(x,y)=\operatorname{tr}_{\mathbb C^2}(xy)\), the basis \(e,h,f\) has dual \(f,h/2,e\). Thus \(C_B=ef+fe+h^2/2\). On the highest vector, \(ef\) acts by \(n\), \(fe\) by zero and \(h^2/2\) by \(n^2/2\). Commutation with \(f\) gives scalar \(n(n+2)/2\) on the whole module. Since \(\kappa=4B\), \(C_\kappa=C_B/4\) has scalar \(n(n+2)/8\). Put \(J_3=h/2\), \(J_+=e\), \(J_-=f\). The usual spin element
\[
J^2=\tfrac12(J_+J_-+J_-J_+)+J_3^2
=\tfrac12 C_B=2C_\kappa
\]
has scalar \(n(n+2)/4=j(j+1)\) with \(j=n/2\). For \(n=1\) the first two values are \(3/2,3/8\); for \(n=2\) they are \(4,1\), verifying the standard and adjoint normalizations.

**Exercise 6.4 (hard).** Prove the Verma-module irreducibility and unique-submodule assertion, and determine the quotient when it is reducible.

**Solution.** The normal-ordering and explicit-model argument of Lemma 5.1 gives a basis \(v_i=f^iv_0\), with \(hv_i=(\lambda-2i)v_i\) and \(ev_i=i(\lambda-i+1)v_{i-1}\). For any nonzero submodule, each vector has finite support, and polynomial interpolation in \(h\) puts every one of its weight components in that submodule. Choose its least occupied index \(j\). Since \(f\) moves from \(v_i\) to \(v_{i+1}\), the submodule is exactly the tail beginning at \(v_j\). If \(j=0\), it is all of \(M(\lambda)\). If \(j>0\), its \(e\)-stability forces \(j(\lambda-j+1)=0\), so \(\lambda=j-1=n\ge0\).

Conversely the tail beginning at \(v_{n+1}\) is invariant, since its first vector is killed by \(e\). It is the only possible proper nonzero submodule by the preceding argument. The map from \(M(-n-2)\) taking its \(i\)-th basis vector to \(v_{n+1+i}\) is a basis bijection; its \(h\)-weight is \(-n-2-2i\) and its \(e\)-coefficient is \(-i(n+1+i)\), precisely those of \(M(-n-2)\). Hence it is an intertwiner. The quotient has the finite basis through \(v_n\) and the action (2.1), so is \(V(n)\). No proper nonzero submodule is possible for any other \(\lambda\), proving the complete assertion.

## What this lesson does not prove

Weyl's theorem, preservation of Jordan decomposition in finite-dimensional representations, and the enveloping-algebra universal property are the proved imports identified at the start. The Killing-form normalization and centrality of the two Casimir elements come from the preceding lessons.

Every classification, multiplicity, tensor-product and Verma-module assertion made here is proved. The basis of \(M(\lambda)\) is established directly, without importing full PBW. No statement about exponentiating infinite-dimensional modules, unitary representations or topological completions is needed. The group version for \(SU(2)\) belongs to *SU(2) and SO(3)*; general Verma modules and category \(\mathcal O\) belong to the later lessons with those titles.

## References

- **[Milne]** J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected 2021 text, published 2022, §§20g and 20k. These describe \(SL_2\) and its torus and root subgroups; the Lie-module proofs are provided here. [Author's corrected 2021 edition](https://www.jmilne.org/math/Books/AG.pdf).
- **[Kirillov]** A. Kirillov Jr., *An Introduction to Lie Groups and Lie Algebras*, §4.8, especially Theorems 4.59–4.60. The weight-reversal operator names in the latter are corrected in (3.2). [Author's notes](https://math.stonybrook.edu/~kirillov/liegroups/liegroups.pdf).
