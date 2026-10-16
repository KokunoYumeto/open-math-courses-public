# A selection process with unbounded extinction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the algebraic input of the construction: one finitely presented complex algebra \(R\) with a central idempotent \(e\) and an automorphism \(\alpha\), and, for each \(m\), a finite-dimensional module that survives exactly \(m-1\) applications of the *selection* \(Y\mapsto{}_\alpha(eY)\) (Proposition 5.1). The algebra is the group algebra of a finitely presented group in which an automorphism shifts an infinite family of central involutions. The group is modelled on finitely presented soluble matrix groups of the kind studied by Abels and by Rego [Rego]; its presentation, its central elements and its finite quotients are established here. The construction follows [OpenAI-FD, Section 2].

Throughout, \(k\) is a field, algebras are associative and unital, and modules are left modules. Commutators are \([x,y]=xyx^{-1}y^{-1}\).

## 1. The selection functor

Let \(R\) be a \(k\)-algebra, \(e\in R\) a central idempotent and \(\alpha\colon R\to R\) an automorphism. For a module \(Y\), the subspace \(eY\) is a submodule, because \(e\) is central. Let \(H(Y)={}_\alpha(eY)\) be the vector space \(eY\) on which \(r\in R\) acts as the original operator of \(\alpha(r)\); this is a module because \(\alpha\) is a homomorphism of algebras. A module map \(f\colon Y\to Y'\) restricts to \(eY\to eY'\), and this restriction is \(R\)-linear for the twisted actions. So \(H\) is an additive functor, and \(\dim H(Y)\le\dim Y\). Write \(H^{\circ j}\) for the \(j\)-fold composite, with \(H^{\circ0}\) the identity, and \(e_q=\alpha^q(e)\) for \(q\ge0\); each \(e_q\) is a central idempotent, since \(\alpha^q\) is an automorphism.

**Lemma 1.1.** For every module \(Y\) and \(j\ge0\), the module \(H^{\circ j}(Y)\) is the subspace \(e_0e_1\cdots e_{j-1}Y\) of \(Y\), on which \(r\in R\) acts as the original operator of \(\alpha^j(r)\). The empty product is \(1\).

**Proof.** For \(j=0\) there is nothing to prove. Suppose the statement holds for \(j\), so \(Z=H^{\circ j}(Y)\) is the subspace \(V=e_0\cdots e_{j-1}Y\) with \(r\) acting as \(\alpha^j(r)\). In \(Z\) the element \(e\) acts as the operator \(\alpha^j(e)=e_j\), so \(eZ=e_jV=e_0\cdots e_jY\), using that the \(e_q\) commute. The functor \(H\) twists the action once more: \(r\) acts on \(H(Z)\) as \(\alpha(r)\) acts on \(Z\), that is as \(\alpha^j(\alpha(r))=\alpha^{j+1}(r)\). \(\square\)

Consequently, if the operators \(e_0,\dots,e_{m-2}\) act on \(Y\) as the identity and \(e_{m-1}\) acts as zero, then \(H^{\circ j}(Y)=Y\neq0\) as a vector space for \(j<m\) (when \(Y\neq0\)), while \(H^{\circ m}(Y)=0\). The rest of the lesson produces an algebra on which such modules exist for every \(m\).

## 2. A group and its finite presentation

Let \(I=\{1,2,3\}\) and let \(\varepsilon_1,\varepsilon_2,\varepsilon_3\) be the standard basis of \(\mathbb Z^3\). The group \(G\) has generators \(T_1,T_2,T_3\) and
\[
\begin{gathered}
U_i(r),\quad V_i(r),\quad W_{ij}(r)\\
(i,j\in I,\ i\neq j,\ r\in\mathbb Z).
\end{gathered}
\]
Each *type* \(S\in\{U_i,V_i,W_{ij}\}\) has a *weight* \(\lambda_S\in\mathbb Z^3\):
\[
\begin{gathered}
\lambda_{U_i}=-\varepsilon_i,\qquad\lambda_{V_i}=\varepsilon_i,\\
\lambda_{W_{ij}}=\varepsilon_i-\varepsilon_j .
\end{gathered}
\]
We also write \(\lambda_S(n)=\lambda_S\cdot n\) for \(n\in\mathbb Z^3\), and \(\lambda_{S,\ell}=\lambda_S(\varepsilon_\ell)\). The defining relations are, for all arguments in \(\mathbb Z\):

- (G1) the \(T_\ell\) commute, and \(T_\ell S(r)T_\ell^{-1}=S(r+\lambda_{S,\ell})\) for every type \(S\);
- (G2) \(U_i(r)^2=1\);
- (G3) for \(i\neq j\), generators of types \(U_i\) and \(U_j\) commute, so do those of types \(V_i\) and \(V_j\), and those of types \(U_i\) and \(V_j\);
- (G4) \(W_{ij}(r)\) commutes with \(U_h(s)\) for \(h\neq i\) and with \(V_h(s)\) for \(h\neq j\);
- (G5) for \(i\neq j\), \([U_i(r),W_{ij}(s)]=U_j(r+s)\) and \([W_{ij}(s),V_j(r)]=V_i(s+r)\).

Generators of the same type with different arguments are not required to commute. For \(n\in\mathbb Z^3\) write \(T^n=T_1^{n_1}T_2^{n_2}T_3^{n_3}\). Iterating (G1) gives the identity (2.1):
\[
T^nS(r)T^{-n}=S\bigl(r+\lambda_S(n)\bigr).
\]

**Lemma 2.1.** The group \(G\) is isomorphic to the group \(G'\) with the fifteen generators \(T_\ell\), \(u_i\), \(v_i\), \(w_{ij}\) and the following finitely many relations: the \(T_\ell\) commute; \(u_i\) and \(v_i\) commute with \(T_h\) for \(h\neq i\); \(w_{ij}\) commutes with \(T_iT_j\) and with \(T_h\) for \(h\notin\{i,j\}\); and the relations (G2)–(G5) with all arguments equal to \(0\), written with \(u_i,v_i,w_{ij}\) in place of \(U_i(0),V_i(0),W_{ij}(0)\). In particular \(G\) is finitely presented.

**Proof.** *Step 1: the generators of \(G'\) for nonzero arguments.* For a type \(S\), let \(s\) be the corresponding generator of \(G'\) and \(K_S=\{n\in\mathbb Z^3:\lambda_S(n)=0\}\). The relations of \(G'\) say that \(s\) commutes with \(T^n\) for \(n\) in a basis of \(K_S\): for \(U_i\) and \(V_i\) the basis \(\varepsilon_h\), \(h\neq i\), of \(K_{U_i}=K_{V_i}=\{n_i=0\}\), and for \(W_{ij}\) the basis \(\varepsilon_i+\varepsilon_j\), \(\varepsilon_h\) of \(K_{W_{ij}}=\{n_i=n_j\}\). Since the \(T_\ell\) commute, \(s\) commutes with \(T^n\) for every \(n\in K_S\). Each \(\lambda_S\colon\mathbb Z^3\to\mathbb Z\) is surjective; for \(r\in\mathbb Z\) choose \(n\) with \(\lambda_S(n)=r\) and put
\[
S(r)=T^nsT^{-n}\in G'.
\]
This does not depend on \(n\): if \(\lambda_S(n)=\lambda_S(n')\), then \(n-n'\in K_S\), so \(T^{n-n'}\) commutes with \(s\), and \(T^nsT^{-n}=T^{n'}sT^{-n'}\). Then \(T_\ell S(r)T_\ell^{-1}=T^{n+\varepsilon_\ell}sT^{-n-\varepsilon_\ell}\), and the latter equals \(S(r+\lambda_{S,\ell})\), which is (G1) in \(G'\).

*Step 2: the relations (G2)–(G5) hold in \(G'\) for all arguments.* Each relation involves one or two input types \(S,S'\) with arguments \(r,s\), and the relation with arguments \(0\) holds in \(G'\). Conjugating it by \(T^n\) with \(\lambda_S(n)=r\) and \(\lambda_{S'}(n)=s\) gives the relation with arguments \(r,s\). Such an \(n\) exists for every pair of types that occurs: the following table lists one, with unlisted coordinates \(0\) and \(h\notin\{i,j\}\).

| types \(S,S'\) | \(n\) with \(\lambda_S(n)=r\), \(\lambda_{S'}(n)=s\) |
|---|---|
| \(U_i,U_j\) | \(n_i=-r\), \(n_j=-s\) |
| \(V_i,V_j\) | \(n_i=r\), \(n_j=s\) |
| \(U_i,V_j\) | \(n_i=-r\), \(n_j=s\) |
| \(W_{ij},U_j\) | \(n_j=-s\), \(n_i=r-s\) |
| \(W_{ij},U_h\) | \(n_i=r\), \(n_h=-s\) |
| \(W_{ij},V_i\) | \(n_i=s\), \(n_j=s-r\) |
| \(W_{ij},V_h\) | \(n_i=r\), \(n_h=s\) |
| \(U_i,W_{ij}\) | \(n_i=-r\), \(n_j=-r-s\) |
| \(W_{ij},V_j\) | \(n_j=s\), \(n_i=r+s\) |

For the square relation (G2), one type suffices. In (G5) the output types have weights \(\lambda_{U_j}=\lambda_{U_i}+\lambda_{W_{ij}}\) and \(\lambda_{V_i}=\lambda_{W_{ij}}+\lambda_{V_j}\), so the conjugated output generator is \(U_j(r+s)\), respectively \(V_i(s+r)\), as required.

*Step 3: the isomorphism.* By Steps 1 and 2, the assignment \(T_\ell\mapsto T_\ell\), \(S(r)\mapsto S(r)\) respects the relations of \(G\), so it defines a homomorphism \(\phi\colon G\to G'\) (by the universal properties of free groups and of presented groups: [Words, free groups and Cayley graphs](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs), Lemma 1.2 and Section 2). Conversely, the relations of \(G'\) hold in \(G\) for \(u_i=U_i(0)\), \(v_i=V_i(0)\), \(w_{ij}=W_{ij}(0)\): the relations with argument \(0\) are instances of (G2)–(G5), and the centralizer relations follow from (2.1), since \(\lambda_S\) vanishes on the listed vectors. This gives \(\psi\colon G'\to G\). On generators, \(\psi\phi(S(r))=T^nS(0)T^{-n}=S(r)\) by (2.1), and \(\phi\psi\) fixes the fifteen generators. So \(\phi\) and \(\psi\) are inverse isomorphisms. \(\square\)

## 3. Central involutions and a shift

**Lemma 3.1.** For each \(N\in\mathbb Z\), the element
\[
z_N=[U_i(a),V_i(b)]\qquad(a+b=N)
\]
does not depend on \(i\in I\) or on the splitting \(N=a+b\). Each \(z_N\) is central in \(G\) and satisfies \(z_N^2=1\).

**Proof.** Fix \(i\neq j\) and integers \(r,q,s\). Put \(x=U_i(r)\), \(y=W_{ij}(q)\), \(v=V_j(s)\), and, by (G5),
\[
\begin{gathered}
u=[x,y]=U_j(r+q),\\
w=[y,v]=V_i(q+s).
\end{gathered}
\]
By (G3), \(x\) commutes with \(v\), \(w\) commutes with \(u\) (types \(V_i\), \(U_j\) with \(i\neq j\)), and \(w\) commutes with \(v\). From \(u=[x,y]\) and \(w=[y,v]\) we get \(xy=uyx\) and \(yv=wvy\). Compute \(xyv\) in two ways:
\[
\begin{aligned}
xyv&=uyxv=uyvx=uwvyx,\\
xyv&=xwvy=(xwx^{-1})xvy\\
&=(xwx^{-1})vxy=(xwx^{-1})vuyx .
\end{aligned}
\]
Cancelling \(yx\) gives \(uwv=(xwx^{-1})vu\). With \(c=[x,w]\), that is \(xwx^{-1}=cw\), this reads \(uwv=cwvu\), so
\[
\begin{aligned}
c&=uwvu^{-1}v^{-1}w^{-1}\\
&=w\,(uvu^{-1}v^{-1})\,w^{-1}=[u,v],
\end{aligned}
\]
because \(w\) commutes with \(u\) and \(v\), hence with \([u,v]\). We have shown the identity (3.1): for \(i\neq j\) and \(r,q,s\in\mathbb Z\),
\[
\begin{aligned}
&[U_i(r),V_i(q+s)]\\
&\quad=[U_j(r+q),V_j(s)].
\end{aligned}
\]
Let \(a+b=a'+b'=N\) and \(i\neq j\). Taking \(r=a\), \(s=b'\) and \(q=a'-a=b-b'\) in (3.1) gives \([U_i(a),V_i(b)]=[U_j(a'),V_j(b')]\). Two splittings at the same index \(i\) are compared through a third index. This proves the independence.

To see that \(z_N\) commutes with \(U_h(r)\) or \(V_h(r)\), write \(z_N\) with an index \(i\neq h\); both factors commute with the given generator by (G3). For \(W_{hj}(r)\), use the index \(i\notin\{h,j\}\): both factors commute with it by (G4). By (2.1), \(T_\ell z_NT_\ell^{-1}=[U_i(a-\delta_{\ell i}),V_i(b+\delta_{\ell i})]\), another splitting of \(N\), so \(T_\ell\) commutes with \(z_N\). So \(z_N\) is central. For central \(c=[x,y]\) one has \([x^2,y]=x[x,y]yx^{-1}y^{-1}\), which equals \([x,y]\,xyx^{-1}y^{-1}=c^2\); with \(x=U_i(a)\), (G2) gives \(1=[x^2,y]=z_N^2\). \(\square\)

**Lemma 3.2.** There is an automorphism \(\alpha_G\) of \(G\) fixing the \(T_\ell\), \(V_i(r)\), \(W_{ij}(r)\) and sending \(U_i(r)\) to \(U_i(r+1)\). It satisfies \(\alpha_G(z_N)=z_{N+1}\).

**Proof.** Shifting every \(U\)-argument by \(1\) maps each relation (G1)–(G5) to another relation of the same list: (G1) because the conjugation rule shifts arguments additively, and the first relation of (G5) because \([U_i(r+1),W_{ij}(s)]=U_j(r+s+1)\) is again an instance. So the shift defines an endomorphism of \(G\), and the shift by \(-1\) is its inverse. Finally \(\alpha_G(z_N)=[U_i(a+1),V_i(b)]=z_{N+1}\). \(\square\)

## 4. Finite quotients that separate the involutions

**Lemma 4.1.** For every \(m\ge1\) there is a finite quotient \(\pi_m\colon G\to F_m\) such that \(\pi_m(z_0),\dots,\pi_m(z_{m-1})\) generate a central subgroup of \(F_m\) isomorphic to \((\mathbb Z/2)^m\).

**Proof.** Let \(S_m=\mathbb F_2[t]/(t^m-1)\), a finite ring in which \(t\) is a unit (\(t\cdot t^{m-1}=1\)), so \(t^r\) is defined for all \(r\in\mathbb Z\). Index \(5\times5\) matrices by \(0,1,2,3,4\), and let \(E_{ab}\) be the matrix units, \(E_{ab}E_{cd}=\delta_{bc}E_{ad}\). Send \(T_\ell\) to the diagonal matrix with \(t\) at position \(\ell\) and \(1\) elsewhere, and
\[
\begin{aligned}
U_i(r)&\mapsto1+t^rE_{0i},\\
V_i(r)&\mapsto1+t^rE_{i4},\\
W_{ij}(r)&\mapsto1+t^rE_{ij}.
\end{aligned}
\]
These matrices are invertible: \((1+cE_{ab})(1-cE_{ab})=1\) for \(a\neq b\), and \(-c=c\) in characteristic two. We check the relations. Conjugating \(E_{ab}\) by a diagonal matrix with entries \(d_0,\dots,d_4\) multiplies it by \(d_a/d_b\); for the image of \(T_\ell\) this factor is \(t^{\lambda_{S,\ell}}\) for the unit of type \(S\), which gives (G1). For a pair of units \(E_{ab},E_{cd}\) with \(E_{ab}E_{cd}=E_{cd}E_{ab}=0\), the matrices \(1+xE_{ab}\) and \(1+yE_{cd}\) commute; the pairs in (G3) and (G4) are \(E_{0i},E_{0j}\); \(E_{i4},E_{j4}\); \(E_{0i},E_{j4}\) with \(i\neq j\); \(E_{ij},E_{0h}\) with \(h\neq i\); and \(E_{ij},E_{h4}\) with \(h\neq j\), and all these products vanish. (G2) holds since \((1+cE_{0i})^2=1+2cE_{0i}=1\). For (G5), if \(E_{ab}E_{cd}=E_{ad}\) with \(a\neq d\) and all other products among \(E_{ab},E_{cd},E_{ad}\) vanish, then
\[
[1+xE_{ab},1+yE_{cd}]=1+xyE_{ad}.
\]
This applies to \(E_{0i}E_{ij}=E_{0j}\) and to \(E_{ij}E_{j4}=E_{i4}\), with \(t^rt^s=t^{r+s}\). So the assignment defines a homomorphism from \(G\) to the finite group of invertible \(5\times5\) matrices over \(S_m\); let \(F_m\) be its image.

The image of \(z_N=[U_1(a),V_1(b)]\) is \(1+t^NE_{04}\), by the same commutator formula with \(E_{01}E_{14}=E_{04}\). The unit \(E_{04}\) has zero product, in both orders, with every unit \(E_{0i},E_{i4},E_{ij}\) above, and the diagonal images of the \(T_\ell\) have equal entries at positions \(0\) and \(4\); so \(1+t^NE_{04}\) commutes with all generators of \(F_m\) and is central. For \(c_0,\dots,c_{m-1}\in\{0,1\}\),
\[
\prod_{q=0}^{m-1}(1+t^qE_{04})^{c_q}=1+\Bigl(\sum_{q=0}^{m-1}c_qt^q\Bigr)E_{04},
\]
since \(E_{04}^2=0\). The classes of \(1,t,\dots,t^{m-1}\) form an \(\mathbb F_2\)-basis of \(S_m\), because \(t^m-1\) is monic of degree \(m\). So the product is \(1\) only if all \(c_q\) vanish: the images of \(z_0,\dots,z_{m-1}\) are independent involutions, and they generate a central subgroup isomorphic to \((\mathbb Z/2)^m\). \(\square\)

## 5. The algebra and the test modules

**Proposition 5.1** (OpenAI). Let \(R=\mathbb CG\), let \(\alpha\) be the automorphism of \(R\) extending \(\alpha_G\) linearly, and let \(e=\frac12(1+z_0)\). Then \(R\) is a finitely presented complex algebra, \(e\) is a central idempotent, and for every \(m\ge1\) there is a finite-dimensional \(R\)-module \(Y_m\) with
\[
\begin{gathered}
H^{\circ j}(Y_m)\neq0\quad(0\le j<m),\\
H^{\circ m}(Y_m)=0,
\end{gathered}
\]
where \(H(Y)={}_\alpha(eY)\). The algebra, the idempotent and the automorphism do not depend on \(m\).

**Proof.** *Finite presentation.* Let \(\Sigma\) be the fifteen generators and \(\mathcal R\) the finite set of relators of Lemma 2.1. Let \(R'\) be the complex algebra generated by symbols \(g\) and \(\bar g\) for \(g\in\Sigma\), with the relations \(g\bar g=\bar gg=1\) and \(w(g,\bar g)=1\) for \(w\in\mathcal R\), where \(\bar g\) replaces \(g^{-1}\). The map \(g\mapsto g\), \(\bar g\mapsto g^{-1}\) defines an algebra homomorphism \(R'\to\mathbb CG\). Conversely, the images of the \(g\) in \(R'\) are units satisfying the relators, so they define a group homomorphism \(G'\to R'^\times\), which extends linearly to an algebra homomorphism \(\mathbb CG'\to R'\). The two homomorphisms are inverse on generators, so \(R\cong R'\) is finitely presented by Lemma 2.1.

*The idempotent.* By Lemma 3.1, \(z_0\) is a central involution, so \(e^2=\frac14(1+2z_0+z_0^2)=e\), and \(e\) is central. By Lemma 3.2, \(e_q=\alpha^q(e)=\frac12(1+z_q)\).

*The modules.* Fix \(m\ge1\), take \(\pi_m\colon G\to F_m\) from Lemma 4.1, and let \(\bar z_q=\pi_m(z_q)\) and \(Z=\langle\bar z_0,\dots,\bar z_{m-1}\rangle\cong(\mathbb Z/2)^m\). Since the \(\bar z_q\) are independent, there is a homomorphism \(\chi\colon Z\to\{\pm1\}\) with \(\chi(\bar z_q)=1\) for \(q<m-1\) and \(\chi(\bar z_{m-1})=-1\). In the group algebra \(\mathbb CF_m\) put
\[
p=\frac1{|Z|}\sum_{z\in Z}\chi(z)\,z,\qquad Y_m=\mathbb CF_m\,p ,
\]
a finite-dimensional module, regarded as an \(R\)-module through \(\pi_m\). It is nonzero: \(p\in Y_m\), and the coefficient of the identity in \(p\) is \(1/|Z|\). For \(z\in Z\), reindexing the sum gives \(zp=\chi(z)p\), since \(\chi(z)^{-1}=\chi(z)\). Every element of \(Y_m\) has the form \(xp\), and \(z(xp)=x(zp)=\chi(z)xp\) because \(z\) is central in \(F_m\). So \(z_q\) acts on \(Y_m\) as the scalar \(\chi(\bar z_q)\), and \(e_q=\frac12(1+z_q)\) acts as \(1\) for \(q<m-1\) and as \(0\) for \(q=m-1\). Lemma 1.1 gives \(H^{\circ j}(Y_m)=Y_m\) as a vector space for \(j<m\), and \(H^{\circ m}(Y_m)=e_0\cdots e_{m-1}Y_m=0\). For \(m=1\) the statement reads \(Y_1\neq0\) and \(H(Y_1)=0\). \(\square\)

Each application of \(H\) uses the same vector space with its action precomposed by an automorphism of \(R\); the argument never needs \(\alpha\) to be compatible with the quotient \(\pi_m\) (compare Exercise 6.4).

## 6. Exercises

**Exercise 6.1** (easy). Show that \(z_N\neq1\) for every \(N\in\mathbb Z\).

**Exercise 6.2** (medium). Show that the elements \(z_N\), \(N\in\mathbb Z\), generate a central subgroup of \(G\) isomorphic to a direct sum of countably many copies of \(\mathbb Z/2\).

**Exercise 6.3** (easy). Describe \(Y_1\), \(H(Y_1)\), \(Y_2\), \(H(Y_2)\) and \(H^{\circ2}(Y_2)\) in terms of the scalars by which \(z_0\) and \(z_1\) act.

**Exercise 6.4** (medium). Let \(D=\operatorname{diag}(t,1,1,1,1)\). Show that \(\pi_m\circ\alpha_G=c_D\circ\pi_m\), where \(c_D\) is conjugation by \(D\), and deduce that \(\alpha_G\) maps the kernel of \(\pi_m\) onto itself.

**Exercise 6.5** (medium). In Lemma 4.1, explain why the coefficient ring must have characteristic two for the images of the \(U_i(r)\), and why a field would not do in place of \(S_m\) when \(m\ge2\) and one wants the images of \(z_0,\dots,z_{m-1}\) to be independent with \(t\) of finite multiplicative order \(m\).

## 7. Solutions

**6.1.** By Lemma 3.2, \(z_N=\alpha_G^N(z_0)\), and \(\alpha_G\) is an automorphism; so it suffices that \(z_0\neq1\). In \(F_1\) the image of \(z_0\) is \(1+E_{04}\neq1\).

**6.2.** The \(z_N\) commute and square to \(1\) (Lemma 3.1), so the subgroup they generate is an \(\mathbb F_2\)-vector space, and it suffices to show that finitely many of them are independent. A relation \(z_{N_1}\cdots z_{N_s}=1\) with distinct \(N_l\) can be shifted by a power of \(\alpha_G\) so that all indices lie in \(\{0,\dots,m-1\}\) for some \(m\); Lemma 4.1 then shows that the relation is empty.

**6.3.** On \(Y_1\), \(z_0\) acts as \(-1\), so \(e_0=0\) and \(H(Y_1)=0\). On \(Y_2\), \(z_0\) acts as \(1\) and \(z_1\) as \(-1\); so \(H(Y_2)=Y_2\) as a vector space with the action twisted by \(\alpha\), on which \(z_0\) acts as \(z_1\) did, namely as \(-1\); hence \(H^{\circ2}(Y_2)=0\).

**6.4.** Conjugation by \(D\) multiplies \(E_{ab}\) by \(d_a/d_b\): it sends \(E_{0i}\) to \(tE_{0i}\) and fixes \(E_{i4}\), \(E_{ij}\) and the diagonal matrices. So \(c_D(\pi_m(U_i(r)))=1+t^{r+1}E_{0i}\), which is \(\pi_m(\alpha_G(U_i(r)))\), and both sides agree on the other generators. If \(\pi_m(g)=1\), then \(\pi_m(\alpha_G(g))=D\cdot1\cdot D^{-1}=1\); the same argument with \(\alpha_G^{-1}\) and \(D^{-1}\) gives the reverse inclusion.

**6.5.** The relation \(U_i(r)^2=1\) forces \((1+cE_{0i})^2=1+2cE_{0i}=1\), so \(2c=0\) for the unit \(c=t^r\), which needs characteristic two. In a field of characteristic two, if \(t^m=1\) then the elements \(1,t,\dots,t^{m-1}\) span the subfield \(\mathbb F_2[t]\), of dimension at most the degree of the minimal polynomial of \(t\); since \(t^m-1=(t-1)\bigl(1+t+\dots+t^{m-1}\bigr)\), this minimal polynomial has degree less than \(m\) when \(m\ge2\). So the powers \(1,\dots,t^{m-1}\) are dependent over \(\mathbb F_2\), and the product formula of Lemma 4.1 gives a relation among the images of \(z_0,\dots,z_{m-1}\). The ring \(S_m\) avoids this because \(t^m-1\) itself is the defining relation.

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [Rego] Y. Santos Rego, *On the finiteness length of some soluble linear groups*, Canadian Journal of Mathematics (2022); arXiv:1901.06704. https://arxiv.org/abs/1901.06704
