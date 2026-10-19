# Ampleness of the power family

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the algebraic half of the theorem of [Hermitian metrics and Griffiths positivity](hermitian-metrics-and-griffiths-positivity.md): every bundle \(E_m=f_m^*G\otimes P\) is ample, where \(G\) is the bundle of [A bundle glued along three graphs](a-bundle-glued-along-three-graphs.md), \(f_m\) the \(m\)th power map of \(S=\mathbb P^1\times\mathbb P^1\) and \(P=\mathcal O_S(1,1)\). The proof is explicit: it shows that \(\mathcal O_{\mathbb P(E_m)}(n)\) is very ample for every even \(n\) with \(n-1\ge3m\). The two quotient sequences of \(G\) are used alternately to filter the symmetric powers by line bundles. Each kernel alone has a negative degree, but their product is positive in both directions.

- Symmetric powers of an extension (Lemma 1.1).
- A filtration of \(\operatorname{Sym}^nf_m^*G\) by line bundles (Lemma 2.1).
- Global generation after a twist (Lemma 3.1, Proposition 3.2).
- The embedding (Theorem 4.1).

The lesson follows [OpenAI-GP, Section 3], within the symmetric-power framework of [Ha66].

## 1. Symmetric powers of an extension

**Lemma 1.1.** Let \(0\to K'\to V'\to L'\to0\) be an exact sequence of vector bundles on a scheme, with \(K'\) and \(L'\) line bundles. For every \(r\ge1\), multiplication gives an exact sequence of vector bundles
\[
\begin{aligned}
0&\to K'\otimes\operatorname{Sym}^{r-1}V'\\
&\to\operatorname{Sym}^rV'\to(L')^{\otimes r}\to0 .
\end{aligned}
\]

**Proof.** The question is local, and locally the sequence splits: \(V'\) has a basis \(k',e'\) with \(k'\) generating \(K'\) and \(e'\) mapping to a generator of \(L'\). Then \(\operatorname{Sym}^rV'\) has the basis of monomials \(k'^ie'^{r-i}\), the monomials with \(i\ge1\) form a basis of the image of \(K'\otimes\operatorname{Sym}^{r-1}V'\), and \(e'^r\) maps to a generator of \((L')^{\otimes r}\). \(\blacksquare\)

## 2. A filtration by line bundles

Fix \(m\ge1\) and write
\[
\begin{gathered}
V=f_m^*G,\quad\widetilde L_i=f_m^*L_i,\quad\widetilde D=f_m^*D,\\
K_i=\widetilde L_i(-\widetilde D),\qquad K=K_1\otimes K_2 .
\end{gathered}
\]
Pulling back the quotient sequences of Proposition 3.1 of the lesson on the glued bundle gives exact sequences
\[
0\to K_i\to V\to\widetilde L_j\to0 ,
\]
for \(\{i,j\}=\{1,2\}\), exact because the original sequences consist of vector bundles and are locally split. Since \(\mathcal O_S(D)=\mathcal O_S(3,3)\), \(L_1=\mathcal O_S(24,0)\), \(L_2=\mathcal O_S(0,24)\) and \(f_m^*\mathcal O_S(r,t)=\mathcal O_S(mr,mt)\),
\[
\begin{gathered}
K_1=\mathcal O_S(21m,-3m),\\
K_2=\mathcal O_S(-3m,21m),\\
K=\mathcal O_S(18m,18m) .
\end{gathered}
\]
Powers of line bundles are tensor powers.

**Lemma 2.1** ([OpenAI-GP, Section 3]). For even \(n\ge2\), \(\operatorname{Sym}^nV\) has a filtration by subbundles whose successive quotients are the line bundles
\[
\begin{gathered}
K^j\otimes\widetilde L_2^{\,n-2j},\\
K^j\otimes\widetilde L_1^{\,n-2j}(-\widetilde D)
\end{gathered}
\]
for \(0\le j<n/2\), and \(K^{n/2}\).

**Proof.** For \(r\ge2\), Lemma 1.1 applied to \(0\to K_1\to V\to\widetilde L_2\to0\) gives
\[
\begin{aligned}
0&\to K_1\otimes\operatorname{Sym}^{r-1}V\\
&\to\operatorname{Sym}^rV\to\widetilde L_2^{\,r}\to0 ,
\end{aligned}
\]
and Lemma 1.1 applied to \(0\to K_2\to V\to\widetilde L_1\to0\), with \(r-1\), tensored with \(K_1\), gives
\[
\begin{aligned}
0&\to K\otimes\operatorname{Sym}^{r-2}V\to K_1\otimes\operatorname{Sym}^{r-1}V\\
&\quad\to K_1\otimes\widetilde L_1^{\,r-1}\to0 .
\end{aligned}
\]
Here \(K_1\otimes\widetilde L_1^{\,r-1}=\widetilde L_1^{\,r}(-\widetilde D)\). These two steps pass from \(\operatorname{Sym}^rV\) to the subbundle \(K\otimes\operatorname{Sym}^{r-2}V\), with the two quotients \(\widetilde L_2^{\,r}\) and \(\widetilde L_1^{\,r}(-\widetilde D)\). Apply them with \(r=n\) to \(\operatorname{Sym}^nV\), then with \(r=n-2\) to \(\operatorname{Sym}^{n-2}V\) tensored with \(K\), and so on. After \(j\) pairs of steps the remaining subbundle is \(K^j\otimes\operatorname{Sym}^{n-2j}V\), the next two quotients are the displayed ones, and at the end \(K^{n/2}\otimes\operatorname{Sym}^0V=K^{n/2}\) remains. Each inclusion has a locally free quotient, so all members are subbundles. \(\blacksquare\)

Each step uses one of the two sequences only. So the filtration exists although the two kernels \(K_1\) and \(K_2\) have the same image in the fibers over \(\widetilde D\) (Exercise 5.1 makes this explicit for \(n=2\)).

## 3. Global generation after a twist

**Lemma 3.1.** For \(c,t\ge0\), the line bundle \(\mathcal O_S(c,t)\) is globally generated and \(H^1(S,\mathcal O_S(c,t))=0\).

**Proof.** The products of a monomial of degree \(c\) in \(z_0,z_1\) and a monomial of degree \(t\) in \(w_0,w_1\) are sections, and at every point one of them is nonzero. For the cohomology, cover \(S\) by the four affine products of the standard charts of the two factors. The Čech complex of \(\mathcal O_S(c,t)\) for this cover is the tensor product over \(\mathbb C\) of the Čech complexes of \(\mathcal O(c)\) and \(\mathcal O(t)\) on \(\mathbb P^1\) for the two standard charts, and Čech cohomology of affine covers computes sheaf cohomology (Theorem 3.1 of [Affine cohomology and Serre's criterion](course:AG-QC/affine-cohomology-and-serres-criterion), course *Cohomology of quasi-coherent sheaves*, with Theorems 3.2 and 4.1 of [Čech cohomology](course:AG-QC/cech-cohomology)). Over a field, the cohomology of a tensor product of complexes is the tensor product of the cohomologies. Since \(H^1(\mathbb P^1,\mathcal O(c))=H^1(\mathbb P^1,\mathcal O(t))=0\) for \(c,t\ge0\) (Theorem 2.2 of [Cohomology of projective space](course:AG-QC/cohomology-of-projective-space)), \(H^1(S,\mathcal O_S(c,t))=0\). \(\blacksquare\)

**Proposition 3.2.** Let \(n\) be even with \(n-1\ge3m\). Then \(W=\operatorname{Sym}^nV\otimes P^{n-1}\) is globally generated.

**Proof.** The quotients of the filtration of Lemma 2.1, twisted by \(P^{n-1}=\mathcal O_S(n-1,n-1)\), have the bidegrees
\[
\begin{aligned}
&\bigl(18mj+n-1,\\
&\qquad18mj+24m(n-2j)+n-1\bigr),\\
&\bigl(18mj+24m(n-2j)-3m+n-1,\\
&\qquad18mj-3m+n-1\bigr),\\
&\bigl(9mn+n-1,\ 9mn+n-1\bigr),
\end{aligned}
\]
for \(0\le j<n/2\). Each entry is nonnegative: the only negative contribution is \(-3m\), and \(n-1\ge3m\). By Lemma 3.1 each quotient is globally generated with vanishing \(H^1\).

If \(0\to U\to Z\to Q\to0\) is exact with \(U\) and \(Q\) globally generated and \(H^1(U)=H^1(Q)=0\), then the long exact sequence gives \(H^1(Z)=0\) and the surjectivity of \(H^0(Z)\to H^0(Q)\). The lifts of generating sections of \(Q\), together with generating sections of \(U\), generate \(Z\) at every point. Starting from the innermost member of the filtration and adding one quotient at a time proves that \(W\) is globally generated. \(\blacksquare\)

## 4. The embedding

**Theorem 4.1** ([OpenAI-GP, Proposition 3.1]). For every \(m\ge1\), \(E_m=f_m^*G\otimes P\) is ample; more precisely, \(\mathcal O_{\mathbb P(E_m)}(n)\) is very ample for every even \(n\) with \(n-1\ge3m\).

**Proof.** Let \(\pi\colon\mathbb P(V)\to S\) be the projective bundle of one-dimensional quotients, and \(H=H^0(S,W)\) with \(W\) as in Proposition 3.2.

*Three closed immersions.* A surjection of vector bundles \(V_1\to V_2\) induces a closed immersion \(\mathbb P(V_2)\to\mathbb P(V_1)\) under which \(\mathcal O_{\mathbb P(V_1)}(1)\) restricts to \(\mathcal O_{\mathbb P(V_2)}(1)\) (Theorem 4.1 of [Projective space, relative Proj and maps to projective space](course:AG-SS/projective-space-relative-proj-and-maps-to-projective-space), course *Sheaves and schemes*). Applied to the evaluation \(H\otimes\mathcal O_S\to W\), surjective by Proposition 3.2, it gives a closed immersion \(\mathbb P(W)\to\mathbb P(H)\times S\) under which the hyperplane bundle of \(\mathbb P(H)\) restricts to \(\mathcal O_{\mathbb P(W)}(1)\). The relative Veronese map \(\mathbb P(V)\to\mathbb P(\operatorname{Sym}^nV)\), which sends a quotient line \(\ell\) to \(\ell^{\otimes n}\), is a closed immersion pulling back \(\mathcal O(1)\) to \(\mathcal O_{\mathbb P(V)}(n)\): locally on \(S\) it is the base change of the Veronese map of Theorem 4.1 of [Very ample sheaves and embeddings](course:AG-MO/very-ample-sheaves-and-embeddings) (course *Morphisms of schemes*). Finally \(\mathbb P(\operatorname{Sym}^nV)=\mathbb P(W)\), with \(\mathcal O_{\mathbb P(W)}(1)=\mathcal O_{\mathbb P(\operatorname{Sym}^nV)}(1)\otimes\pi^*P^{n-1}\).

*The composite.* The composite closed immersion \(\mathbb P(V)\to\mathbb P(H)\times S\) pulls the hyperplane bundle of \(\mathbb P(H)\) back to \(\mathcal O_{\mathbb P(V)}(n)\otimes\pi^*P^{n-1}\). Embed \(S\) into \(\mathbb P^3\) by the Segre embedding, which pulls \(\mathcal O(1)\) back to \(P\), and then \(\mathbb P(H)\times\mathbb P^3\) into projective space by the Segre embedding (Theorem 3.1 of the lesson on very ample sheaves). The resulting closed immersion of \(\mathbb P(V)\) pulls the hyperplane bundle back to
\[
\begin{aligned}
&\bigl(\mathcal O_{\mathbb P(V)}(n)\otimes\pi^*P^{n-1}\bigr)\otimes\pi^*P\\
&\quad=\bigl(\mathcal O_{\mathbb P(V)}(1)\otimes\pi^*P\bigr)^{\otimes n} ,
\end{aligned}
\]
which is therefore very ample.

*Conclusion.* \(\mathbb P(E_m)=\mathbb P(V\otimes P)=\mathbb P(V)\) with \(\mathcal O_{\mathbb P(E_m)}(1)=\mathcal O_{\mathbb P(V)}(1)\otimes\pi^*P\). So \(\mathcal O_{\mathbb P(E_m)}(n)\) is very ample, and \(E_m\) is ample by Section 4 of [Hermitian metrics and Griffiths positivity](hermitian-metrics-and-griffiths-positivity.md). \(\blacksquare\)

Every \(E_m\) is ample, for every \(m\). The metric half of the theorem, proved in [A quadratic limit of dual norms](a-quadratic-limit-of-dual-norms.md) and [An invariant measure and the proof](an-invariant-measure-and-the-proof.md), concerns large \(m\) only.

## 5. Exercises

**5.1.** For \(n=2\), use the local basis \(e=(1,h)\), \(f=(0,d)\) of \(G\) from the lesson on the glued bundle. Show that the kernels of the two projections are generated by \(k=de-hf\) and \(f\), and that the filtration of \(\operatorname{Sym}^2V\) is \(\mathcal O(kf)\subset kV\subset\operatorname{Sym}^2V\), with locally free quotients, also at points of \(D\).

**5.2.** For \(m=1\) and \(n=4\), list the bidegrees of the five quotients of Proposition 3.2 and check that they are nonnegative.

**5.3.** Show that the condition \(n-1\ge3m\) is exactly the condition that the quotient \(\widetilde L_1^{\,n}(-\widetilde D)\otimes P^{n-1}\) (the case \(j=0\) of the second family) has nonnegative bidegree.

**5.4.** Show that the subbundle \(L_2(-D)=\mathcal O_S(-3,21)\) of \(G\) has no nonzero section, and explain why the argument of Proposition 3.2 needs the twist by \(P^{n-1}\).

**5.5.** Show that \(\det E_m=\mathcal O_S(21m+2,21m+2)\), and compute \(c_2(E_m)\).

## 6. Solutions

**5.1.** The kernel of \(\rho_2\) consists of \(u_1e+kf\) with \(u_1h+kd=0\); since \(h\) is a unit, it is generated by \(de-hf\). The kernel of \(\rho_1\) is generated by \(f\). Since \(e,k\) is again a basis of \(V\), \(kV\) has the basis \(ke,k^2\) and is a direct summand of \(\operatorname{Sym}^2V\), with complement spanned by \(e^2\). Further \(f=(de-k)/h\), so \(kf=\frac dhke-\frac1hk^2\); the coefficient \(-1/h\) is a unit, so \(kf\) is part of a basis of \(kV\). Both quotients are free, also where \(d=0\).

**5.2.** With \(m=1\), \(n=4\): for \(j=0\): \((3,99)\) and \((96,0)\); for \(j=1\): \((21,69)\) and \((66,18)\); and \((39,39)\). All entries are nonnegative.

**5.3.** For \(j=0\) the second family gives \(\bigl(24mn-3m+n-1,\ -3m+n-1\bigr)\); the second entry is nonnegative exactly when \(n-1\ge3m\), and all other entries are then nonnegative.

**5.4.** By the Čech computation of Lemma 3.1, the space of sections of \(\mathcal O_S(-3,21)\) is the tensor product of \(H^0(\mathbb P^1,\mathcal O(-3))=0\) and \(H^0(\mathbb P^1,\mathcal O(21))\), so it is zero. Without the twist, the quotients of the filtration include \(\widetilde L_1^{\,n}(-\widetilde D)=\mathcal O_S(24mn-3m,-3m)\), which has no nonzero section, so the lifting of sections through the filtration cannot work; the twist by \(P^{n-1}\) makes every bidegree nonnegative once \(n-1\ge3m\).

**5.5.** \(\det(f_m^*G)=f_m^*\mathcal O_S(21,21)\), which is \(\mathcal O_S(21m,21m)\), and twisting a rank-two bundle by \(P\) adds \(2P\): \(\det E_m=\mathcal O_S(21m+2,21m+2)\). Since \(f_m\) has degree \(m^2\), \(c_2(V)=m^2\,c_2(G)=504m^2\), and \(c_2(E_m)=c_2(V\otimes P)\) equals \(c_2(V)+c_1(V)\cdot P+P^2\), which is \(504m^2+42m+2\).

## References

- [OpenAI-GP] OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
- [Ha66] R. Hartshorne, *Ample vector bundles*, Publ. Math. IHÉS 29 (1966), 63–94. https://www.numdam.org/item/PMIHES_1966__29__63_0/
