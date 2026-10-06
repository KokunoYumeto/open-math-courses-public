# The right adjoint of derived pushforward

*Written by GPT-6.1 Sol (OpenAI), in Codex, at Ultra effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra effort. Public domain (CC0).*

The trace in Serre duality sends top cohomology of a canonical sheaf to the ground field. Its derived formulation is a counit: a map from the pushforward of a distinguished complex to the original complex on the base. This viewpoint puts finite maps, closed immersions and projective space into one construction. It also explains why a singular scheme may need a complex with several nonzero cohomology sheaves.

We use cohomological grading: \(H^i(C[r])=H^{i+r}(C)\). Write \(D_{\mathrm{QCoh}}(X)\) for the full subcategory of \(D(\mathcal O_X)\) whose cohomology sheaves are quasi-coherent. A perfect complex is locally represented by a bounded complex of finite locally free sheaves. All schemes in Sections 1–2 are quasi-compact and quasi-separated. No separation assumption is silently added to that convention.

The bounded-below injective machinery is taught in *Sheaves of modules and their derived categories*, Theorems 5.4 and 6.1 and Corollary 5.5. For the unbounded operations we use the exact open foundations identified in Section 8. Our two preceding lessons supply the complete classical projective duality proofs.

## 1. Representing maps out of pushforward

For a morphism \(f:X\to Y\), its derived pushforward has a right adjoint
\[
a_f:D_{\mathrm{QCoh}}(Y)\longrightarrow D_{\mathrm{QCoh}}(X),
\qquad
\operatorname{Hom}_X(L,a_fK)
 \simeq\operatorname{Hom}_Y(Rf_*L,K).
\tag{1}
\]
The bijection is natural in both variables. Existence in this exact generality has an open proof in [Stacks, Tag 0A9E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-twisted-inverse-image). Here is how its inputs fit together. The category \(D_{\mathrm{QCoh}}(X)\) has a perfect compact generator, and \(Rf_*\) preserves direct sums. For fixed \(K\), the right side of (1), viewed as a functor of \(L\), is cohomological and changes direct sums into products. Brown representability produces its representing object. Yoneda then produces the functor on maps. The exact compact-generation and representability proofs are linked in Section 8; the existence assertion is not an unsupported convention.

The **trace** is the counit
\[
\operatorname{Tr}_f(K):Rf_*a_fK\longrightarrow K,
\tag{2}
\]
corresponding to the identity of \(a_fK\). Thus the transpose of \(u:L\to a_fK\) is precisely \(\operatorname{Tr}_f(K)\circ Rf_*u\). This definition specifies the normalization of every computation below.

**Proposition 1.1.** The functor \(a_f\) is exact, commutes with shifts, and sends bounded-below objects to bounded-below objects. For composable morphisms \(X\xrightarrow fY\xrightarrow gZ\), there is a canonical isomorphism
\[
a_{gf}\simeq a_fa_g.
\tag{3}
\]
Under it, the composite trace is \(\operatorname{Tr}_g\circ Rg_*\operatorname{Tr}_f\).

**Proof.** Shifting both sides of (1) gives the shift isomorphism. Right adjoints of exact triangulated functors are exact: given a triangle on the target, transpose its first two maps, complete to a triangle, and test the third map by the adjunction and the long exact Hom sequences. The five lemma gives the required isomorphism with the third adjoint object. This is the usual derived adjunction construction, with its compatible shift maps.

Choose \(d\geq0\) such that \(Rf_*D^{\leq b}_{\mathrm{QCoh}}(X)\subset D^{\leq b+d}_{\mathrm{QCoh}}(Y)\) for every \(b\). The existence of such a uniform bound, including for unbounded complexes, is [Stacks, Tag 08D5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-quasi-coherence-direct-image); it follows by finite affine covers and truncation from quasi-coherent cohomological dimension. If \(K\in D^{\geq c}(Y)\), set \(T=\tau_{\leq c-d-1}a_fK\). Then \(Rf_*T\in D^{\leq c-1}(Y)\), so
\[
\operatorname{Hom}_X(T,a_fK)=\operatorname{Hom}_Y(Rf_*T,K)=0.
\]
In particular the truncation map \(T\to a_fK\) is zero. On every cohomology sheaf in degrees at most \(c-d-1\) that map is the identity identification, so those sheaves vanish. Hence \(a_fK\in D^{\geq c-d}(X)\).

Finally, transpose twice:
\[
\operatorname{Hom}_X(L,a_fa_gK)
 \simeq\operatorname{Hom}_Y(Rf_*L,a_gK)
 \simeq\operatorname{Hom}_Z(Rg_*Rf_*L,K).
\]
Using the canonical composition of derived pushforwards, Yoneda proves (3). The displayed rule for transposes proves the trace formula. Repeating the argument three times shows associativity: both comparison maps induce the same bijection on every Hom set. \(\square\)

The bound need not be zero. For projective \(n\)-space, the adjoint of the field occurs in degree \(-n\), as Section 4 will show.

There are now three different operations to keep track of. Pullback is the left adjoint of pushforward; it transports sections and tensors them with the structure sheaf upstairs. The functor \(a_f\) is its right adjoint and represents maps from a pushforward into a prescribed target. The compactification construction \(f^!\), introduced later, uses the right adjoint of a proper map followed by restriction. Finite maps make the second operation concrete as coinduction; open immersions will show why the second and third operations require separate names.

## 2. What sheafified duality says

Distinguish internal \(R\mathcal H om_X\), which is a complex of sheaves, from global \(R\operatorname{Hom}_X\). Evaluation and the counit give a canonical morphism
\[
Rf_*R\mathcal H om_X(L,a_fK)
 \longrightarrow R\mathcal H om_Y(Rf_*L,K).
\tag{4}
\]
One construction first maps into \(R\mathcal H om_Y(Rf_*L,Rf_*a_fK)\), using evaluation and the projection-formula comparison, and then applies (2). Internal Hom of arbitrary unbounded quasi-coherent complexes need not have quasi-coherent cohomology. This prevents us from treating (4) as an isomorphism merely by applying (1).

Let \(DQ_Y:D(\mathcal O_Y)\to D_{\mathrm{QCoh}}(Y)\) be the right adjoint of the inclusion. Its exact open construction is [Stacks, Tag 0CR0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-better-coherator).

**Proposition 2.1.** Applying \(DQ_Y\) to (4) gives an isomorphism. Taking global sections of (4) gives
\[
R\operatorname{Hom}_X(L,a_fK)
 \simeq R\operatorname{Hom}_Y(Rf_*L,K).
\tag{5}
\]

**Proof.** Test (4) against \(M\in D_{\mathrm{QCoh}}(Y)\). The tensor–Hom and pullback–pushforward adjunctions identify its source Hom group with
\[
\operatorname{Hom}_X(Lf^*M\otimes^{\mathbf L}L,a_fK)
 \simeq
\operatorname{Hom}_Y(Rf_*(Lf^*M\otimes^{\mathbf L}L),K).
\]
The unbounded quasi-coherent projection formula identifies the last group with
\[
\operatorname{Hom}_Y(M\otimes^{\mathbf L}Rf_*L,K)
 \simeq
\operatorname{Hom}_Y(M,R\mathcal H om_Y(Rf_*L,K)).
\]
The projection formula holds for every qcqs morphism and both indicated quasi-coherent complexes, without a perfectness condition on \(M\); its open proof is [Stacks, Tag 08EU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-cohomology-base-change). The identifications just made are induced by evaluation and the counit, hence by (4). The defining adjunction of \(DQ_Y\) and Yoneda prove the first assertion. Testing with \(M=\mathcal O_Y[-r]\) proves that (4) induces an isomorphism on every global hypercohomology group. This gives (5), since global derived Hom is the derived global sections of internal Hom. \(\square\)

There is a second, distinct locality issue. If \(V\subset Y\) is quasi-compact open, \(U=f^{-1}(V)\), and \(f_V:U\to V\), there is a canonical comparison
\[
(a_fK)|_U\longrightarrow a_{f_V}(K|_V).
\tag{6}
\]
It comes from \(K\to Rj_*(K|_V)\) and the two adjunctions for the open inclusions. For \(K\in D^+_{\mathrm{QCoh}}(Y)\), (6) is an isomorphism if **\(f\) is proper** and either \(Y\) is Noetherian or \(f\) is flat of finite presentation. These precise cases have an open proof in [Stacks, Tags 0A9N and 0A9P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-proper-noetherian).

The mechanism is useful: the comparison is equivalent to saying that \(a_f\) carries complexes supported outside \(V\) to complexes supported outside \(U\). Properness makes pushforwards of perfect complexes pseudo-coherent in these cases. A map from such a pushforward into a supported complex can be killed by a perfect factor which is the identity on \(V\); the projection formula brings this factor back to \(X\). Perfect generators then detect the claimed support. Section 6 exhibits the failure of unrestricted locality.

## 3. Finite maps and closed immersions

Let \(f:X\to Y\) be finite between Noetherian schemes, and put \(B=f_*\mathcal O_X\), a coherent sheaf of \(\mathcal O_Y\)-algebras. Quasi-coherent sheaves on \(X\) correspond to quasi-coherent \(B\)-modules on \(Y\). In the derived category this correspondence is given by exact affine pushforward; it preserves and detects quasi-isomorphisms.

**Theorem 3.1.** For \(K\in D^+_{\mathrm{QCoh}}(Y)\), the object \(a_fK\), expressed as a \(B\)-complex on \(Y\), is
\[
R\mathcal H om_{\mathcal O_Y}(B,K),
\qquad (b\varphi)(b')=\varphi(bb').
\tag{7}
\]
For a closed immersion \(i:Z\hookrightarrow Y\), this is the derived functor of the annihilator sheaf
\[
i^bK=\mathcal H om_Y(i_*\mathcal O_Z,K),
\]
regarded as a sheaf on \(Z\). Its derived value is often denoted \(Ri^bK\).

**Proof.** The sheaf-level coinduction identity is
\[
\operatorname{Hom}_B(M,\mathcal H om_Y(B,J))
 \simeq\operatorname{Hom}_{\mathcal O_Y}(M,J).
\tag{8}
\]
Evaluation at \(1\) gives the forward map; the inverse sends \(v\) to \(m\mapsto[b\mapsto v(bm)]\). This works on every open subset and glues. Restriction of scalars is exact, so its right adjoint sends injectives to injectives. Resolve \(K\) by a bounded-below injective complex \(J\). Formula (8), applied to complexes, identifies the derived adjunction with coinduction into \(\mathcal H om_Y(B,J)\).

This complex has quasi-coherent cohomology. Locally on the Noetherian base, resolve the finite module \(B\) by finite free modules in nonpositive degrees. The bounded-below hypothesis on \(K\) makes each fixed total degree involve only finitely many terms. Hom therefore commutes with localization and computes quasi-coherent Ext sheaves. The equivalence for affine pushforward now transports the complex back to \(X\). It represents exactly the Hom functor (1), proving (7). For \(B=\mathcal O_Y/\mathcal I\), its terms are annihilated by \(\mathcal I\), so they are the asserted sheaves on \(Z\). \(\square\)

The \(B\)-action in (7) is essential. An ambient internal Hom complex without its algebra action has not yet specified an object on \(X\). The trace in this model is evaluation at \(1\), not an unspecified ring trace.

**Example 3.2 (an effective Cartier divisor).** If \(Z=D\) is an effective Cartier divisor in \(Y\), resolve \(\mathcal O_D\) by
\[
0\longrightarrow\mathcal O_Y(-D)\longrightarrow\mathcal O_Y
 \longrightarrow\mathcal O_D\longrightarrow0.
\]
Applying Hom into \(\mathcal O_Y\) gives \(\mathcal O_Y\to\mathcal O_Y(D)\) in degrees 0 and 1. The map is injective, and its cokernel is the normal line \(N_{D/Y}=\mathcal O_D(D)\). Thus
\[
a_i(\mathcal O_Y)=N_{D/Y}[-1].
\tag{9}
\]
The minus sign in the shift places the normal line in cohomological degree 1.

## 4. Projective space and the classical trace

**Theorem 4.1.** For \(\pi:P=\mathbf P^n_k\to\operatorname{Spec}k\),
\[
a_\pi(k)\simeq\mathcal O_P(-n-1)[n]=\omega_P[n].
\tag{10}
\]
The counit is the trace whose ordered Čech representative extracts the coefficient of \(T_0^{-1}\cdots T_n^{-1}\).

**Proof.** The projective-space calculation gives \(R\Gamma(P,\omega_P[n])\simeq k\), with the specified trace. Transpose that map to obtain \(c:\omega_P[n]\to a_\pi(k)\). For a coherent sheaf \(F\), testing \(c\) against every shift of \(F\) gives the maps
\[
\operatorname{Ext}^{n+r}_P(F,\omega_P)
 \longrightarrow\operatorname{Hom}_{D(k)}(R\Gamma(P,F),k[r])
 \simeq H^{-r}(P,F)^\vee.
\]
These are precisely the Yoneda trace pairings proved in Serre duality on projective space, Theorem 5.1. They are isomorphisms for all \(r\), including the zero groups outside the cohomological range.

Finite truncation triangles extend this assertion from coherent sheaves to every bounded complex with coherent cohomology. In particular it holds for a perfect generator \(G\) of \(D_{\mathrm{QCoh}}(P)\), which is bounded coherent because \(P\) is Noetherian and quasi-compact. If \(C\) is the cone of \(c\), then \(\operatorname{Hom}(G,C[r])=0\) for every \(r\). The generator property forces \(C=0\). Thus the map is an isomorphism in the full unbounded category, not merely on coherent test objects. When \(n=0\), this is the identity adjunction on the field; every twist on the point is the same line. \(\square\)

The corresponding relative formula, for a locally free \(E\) of rank \(n+1\geq1\) on a qcqs base and the quotient convention for \(\mathbf P(E)\), is
\[
a_\pi(\mathcal O_Y)\simeq
\pi^*(\det E)\otimes\mathcal O_{\mathbf P(E)}(-n-1)[n].
\tag{11}
\]
Its exact open proof is [Stacks, Tag 0A9W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-upper-shriek-P1): transpose the relative top-cohomology trace and test on the generating twists \(\mathcal O,\ldots,\mathcal O(-n)\) locally on the base. In the rank-one case \(\mathcal O(1)=\pi^*E\), so the two line factors cancel, as they must.

## 5. Proper duality over a field

Let \(p:X\to\operatorname{Spec}k\) be proper, and define
\[
\omega_X^\bullet=a_p(k).
\]

**Theorem 5.1.** For every \(K\in D_{\mathrm{QCoh}}(X)\) and every integer \(i\), the trace induces
\[
H^i(X,K)^\vee\simeq
\operatorname{Ext}^{-i}_X(K,\omega_X^\bullet).
\tag{12}
\]
If \(X\) is projective, Cohen–Macaulay and equidimensional of dimension \(n\), then
\[
\omega_X^\bullet\simeq\omega_X^\circ[n],
\]
where \(\omega_X^\circ\) is the dualizing sheaf of the preceding lesson.

**Proof.** Formula (1) gives
\[
\operatorname{Hom}_X(K,\omega_X^\bullet[-i])
 \simeq\operatorname{Hom}_{D(k)}(R\Gamma(X,K),k[-i]).
\]
Over a field, every complex splits into its cohomology complex and a contractible complex: choose complements to boundaries inside cycles and to cycles inside each term. Its maps to \(k[-i]\) in the derived category are consequently exactly the linear functionals on \(H^i\). This remains valid for unbounded complexes and infinite-dimensional cohomology; no finite-dimensional biduality has been used. It proves (12). For bounded coherent \(K\), proper coherence gives the familiar finite-dimensional interpretation.

For the last assertion embed \(i:X\hookrightarrow P=\mathbf P^N_k\). Composition and Theorems 3.1 and 4.1 identify
\[
\omega_X^\bullet=Ri^b(\omega_P[N]).
\]
The preceding lesson proves that \(Ri^b\omega_P\) has only one cohomology sheaf, in degree \(c=N-n\), and that this sheaf is \(\omega_X^\circ\). Thus it is \(\omega_X^\circ[-c]\); shifting by \(N\) gives \(\omega_X^\circ[n]\). The classical representing trace was defined from the same ambient pairing, so this identification respects traces. \(\square\)

For a general proper scheme, the further assertion that \(\omega_X^\bullet\) is a bounded coherent dualizing complex, with cohomology in \([-\dim X,0]\), has the exact open proof [Stacks, Tag 0FVV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-duality-proper-over-field). The construction here does not assume projectivity to define \(a_p(k)\) or to prove (12).

The embedded-point example \(X=V(T_0^2,T_0T_1)\subset\mathbf P^2\) from the preceding lesson has \(H^{-1}(\omega_X^\bullet)=\mathcal O_{\mathbf P^1}(-2)\) and \(H^0(\omega_X^\bullet)=k_p\). Dropping its second cohomology sheaf was exactly what made the single-sheaf duality formula fail.

## 6. Coinduction versus restriction

For a finite \(k\)-algebra \(B\), Theorem 3.1 gives \(a_p(k)=\operatorname{Hom}_k(B,k)\) in degree zero. This is coinduction; \(k\) is injective as a vector space, so there is no higher cohomology.

Now take \(A=k[t]\), \(B=k[x]\), with \(t=x^2\). As an \(A\)-module, \(B=A\oplus Ax\) is free. Let \(\lambda:B\to A\) extract the coefficient of \(x\). The pairing \((b,b')\mapsto\lambda(bb')\) has matrix
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
in the basis \(1,x\), so \(B\to\operatorname{Hom}_A(B,A)\), \(b\mapsto b\lambda\), is a \(B\)-linear isomorphism in every characteristic. Hence \(a_f(\mathcal O_Y)\simeq\mathcal O_X\). Under this chosen trivialization the counit sends \(a+bx\) to \(b\). The algebraic trace of multiplication is a different functional: it sends \(1\) to \(2\), and in characteristic 2 it vanishes identically.

For an open immersion \(j:U\hookrightarrow X\), the compactification functor \(j^!\) discussed below is restriction, but the right adjoint \(a_j\) of \(Rj_*\) generally differs. An explicit affine example is
\[
j:\operatorname{Spec}A[t^{-1}]\hookrightarrow\operatorname{Spec}A,
\qquad A=k[t].
\]
Here \(a_j(A)=R\operatorname{Hom}_A(A[t^{-1}],A)\), with its \(A[t^{-1}]\)-action. In degree zero this is zero: the image of \(1\) under an \(A\)-linear map must lie in every \(t^mA\), whose intersection is zero; the same argument applies to each \(t^{-r}\). But \(j^!A=A[t^{-1}]\) has nonzero degree zero. Thus restriction cannot be the general right adjoint of pushforward.

More precisely, the free telescope resolution has map \(e_r\mapsto e_r-te_{r+1}\) on \(\bigoplus_{r\geq0}A\). Its cokernel is \(A[t^{-1}]\), with \(e_r\) mapping to \(t^{-r}\); its injectivity follows by examining the last nonzero coefficient in a finite sum. Dualizing computes \(a_j(A)\) by
\[
\prod_{r\geq0}A\longrightarrow\prod_{r\geq0}A,
\qquad (b_r)\longmapsto(b_r-tb_{r+1})
\tag{13}
\]
in degrees 0 and 1. Its cokernel is \(k[[t]]/k[t]\). Indeed, sending \((c_r)\) to \(\sum t^rc_r\) modulo \(A\) is surjective. A sequence is in its kernel exactly when that sum is a polynomial \(s\); then \(b_r=(s-\sum_{j<r}t^jc_j)/t^r\) is a polynomial and solves (13). This calculation makes the failure visible in both degrees.

For a separated finite type morphism of Noetherian schemes, choose a compactification \(f=\bar f j\), with \(j\) open and \(\bar f\) proper. On bounded-below quasi-coherent complexes set
\[
f^!K=j^*a_{\bar f}K.
\tag{14}
\]
Compactification existence and the independence and composition of (14) are the exact open constructions in [Stacks, Tag 0A9Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-section-upper-shriek). Common proper refinements compare the compactifications; proper restriction compatibility and the canonical adjunction composition identify their functors. The resulting comparison maps satisfy the cocycle condition. Its properties, including \(j^!=j^*\) for open immersions and \(f^!=a_f\) for proper \(f\), are proved in [Stacks, Tag 0ATZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-section-upper-shriek-properties). These statements concern the compactification construction, whose domain and locality differ from the general unbounded adjoint.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Compute the adjoint of \(k\) for \(B=k[\epsilon]/(\epsilon^2)\), its \(B\)-action and the counit.

**Solution.** Let \(\lambda\) extract the coefficient of \(\epsilon\). The two functionals \(\lambda,\epsilon\lambda\) form a basis of \(B^\vee\), because \(\epsilon\lambda\) extracts the constant coefficient. Thus \(B^\vee=B\lambda\), and \(\epsilon\) sends \(\lambda\) to \(\epsilon\lambda\) and the latter to zero. The counit is evaluation at \(1\): it sends \(a\lambda+b\epsilon\lambda\) to \(b\). This is a degree-zero complex.

**Exercise 7.2 (easy).** Derive the composite adjunction and verify its counit on a map \(u:L\to a_fa_gK\).

**Solution.** Its two transposes are \(Rf_*L\xrightarrow{Rf_*u}Rf_*a_fa_gK\xrightarrow{\operatorname{Tr}_f}a_gK\) and then \(Rg_*Rf_*L\to Rg_*a_gK\xrightarrow{\operatorname{Tr}_g}K\). This is the transpose under \(a_{gf}\), giving (3) and the asserted composite counit. Naturality in \(u\) proves equality of the transformations.

**Exercise 7.3 (medium).** For a closed immersion of Noetherian schemes, explain why ordinary annihilators do not generally compute the derived adjoint. Compute the example \(A=k[t]\), \(A\to k=A/(t)\), with input \(A\).

**Solution.** The ordinary annihilator is \(\operatorname{Hom}_A(k,A)=0\). The free resolution \(A\xrightarrow tA\) in degrees \(-1,0\) gives the dual complex \(A\xrightarrow tA\) in degrees \(0,1\). Its only cohomology is \(k\) in degree 1, so the adjoint is \(k[-1]\). The derived annihilator construction of Theorem 3.1 supplies the missing Ext term.

**Exercise 7.4 (medium).** Recover classical Serre duality for a coherent sheaf \(F\) on \(\mathbf P^n_k\) from (10) and the adjunction, including its signs.

**Solution.** Taking \(K=F\) in (12) gives
\[
H^i(F)^\vee=\operatorname{Hom}(F,\omega_P[n-i])
 =\operatorname{Ext}^{n-i}(F,\omega_P).
\]
The pairing sends a cohomology class and its Ext partner to their composite into \(\omega_P[n]\), followed by the trace. This agrees with the ordered Čech normalization in Theorem 4.1. For \(n=0\) it is the vector-space evaluation pairing.

**Exercise 7.5 (medium).** In the squaring map example, compute the action of \(x\) on the dual basis \(\lambda_0,\lambda_1\), which extracts the coefficients of \(1,x\). Identify a generator and its counit.

**Solution.** For \(a+bx\), multiplying by \(x\) gives \(bt+ax\), so \(x\lambda_0=t\lambda_1\) and \(x\lambda_1=\lambda_0\). Hence \(\lambda_1\) generates the dual as a free \(B\)-module; its two \(A\)-basis vectors are \(\lambda_1,x\lambda_1=\lambda_0\). Evaluation at \(1\) takes them to \(0,1\), respectively. This computation remains valid at the branch point and in characteristic 2.

**Exercise 7.6 (hard).** Verify that the degree-one module in the open-immersion calculation is nonzero, and that multiplication by \(t\) on \(k[[t]]/k[t]\) is invertible.

**Solution.** The series \(\sum_{r\geq1}t^{r!}\) is not a polynomial, so gives a nonzero class. If \(ts\) is a polynomial, then the formal series \(s\) is a polynomial, proving injectivity. For any series \(s\), remove its constant term; \((s-s(0))/t\) is a formal series whose class maps to \([s]\), proving surjectivity. Thus the module has the required \(A[t^{-1}]\)-action. Together with its zero degree-zero cohomology this explicitly distinguishes \(a_j(A)\) from \(j^!A\).

## 8. Proof dependencies

The trace, formal adjunction properties, coherator comparison, finite and closed computations, projective-space identification in the unbounded category, and the proper-field duality formula were proved here. The following larger foundational constructions are supplied by exact open proofs:

- Compact generation for every qcqs scheme: [Stacks, Tag 09IS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-theorem-bondal-van-den-Bergh). Brown representability and its adjoint consequence: [Tags 0A8F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-brown) and [0A8G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-proposition-brown).
- Affine unbounded module comparison: [Tag 06Z0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-affine-compare-bounded). Preservation of direct sums by qcqs pushforward: [Tag 08DZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-quasi-coherence-pushforward-direct-sums). Unbounded derived pullback and tensor–Hom adjunctions: [Cohomology, the derived adjunction proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-adjoint) and [the internal Hom proof](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-internal-hom).
- The coherator, unbounded cohomological-dimension and projection-formula foundations, proper restriction theorem, relative projective-bundle computation, and bounded coherent proper dualizing-complex theorem are identified at their precise uses above. Compactification and upper shriek are imported with the exact hypotheses of (14).

These links point to the GNU FDL 1.2 AI Integrated Stacks Project edition. They identify proof providers for the stated generality; the exposition and calculations in this lesson are independent. There is no assumption that every right adjoint is local or that a dualizing complex is a shifted line bundle.
