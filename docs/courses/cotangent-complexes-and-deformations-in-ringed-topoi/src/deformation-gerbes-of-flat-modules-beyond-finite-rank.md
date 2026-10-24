# Deformation gerbes of flat modules beyond finite rank

*Written by Claude Opus 5.5 (Anthropic) on 23 October 2026. The question was posed by Claude while writing this course and solved by GPT-6 Astra (OpenAI) in ChatGPT's Pro mode; the solution was refereed by Claude Opus 5.5 in a separate session, and this lesson was written from it and refereed and revised by Claude Opus 5.5 in two further sessions. Public domain (CC0).*

For a flat module \(M\) over \(R=B/I\), the sign comparison of the lesson on the gerbe of local deformations holds as soon as the first two Ext sheaves of \(M\) into \(N=I\otimes_RM\) vanish. This lesson proves this and two related facts:
- the cohomology \(H^n(T,H)\) of the band \(H=\mathcal Hom_R(M,N)\) agrees with \(\operatorname{Ext}^n_R(M,N)\) for \(n\le2\), and the class of the gerbe is \(-\omega(B,M)\);
- in infinite rank, the band \(H\) need not be \(\mathcal End(M)\otimes I\).

**Prerequisites.**
- [*The gerbe of local deformations of a locally free module*](the-gerbe-of-local-deformations-of-a-locally-free-module.md): Conventions with Lemma 0.1, Lemma 1.1, Lemma 1.4, Definition 1.5, Section 2, and the proof of Theorem 3.1.
- [*Deformations of modules and of their morphisms*](deformations-of-modules-and-of-their-morphisms.md): Definition 2.2.
- From the AI-integrated Stacks project: [[Tag 05TG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-into-injective-complex)] and morphisms out of objects in degrees \(\le n\) [[Tag 06XS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-negative-exts)].

## Conventions

The notation of the lesson on the gerbe of local deformations is used, with \(N\xrightarrow{j}J^\bullet\) an injective resolution and \(\mathcal K^q=\mathcal Hom_R(M,J^q)\). Put
\[
\mathcal Ext^q_R(M,N)=H^q(\mathcal K^\bullet).
\]
This does not depend on \(J^\bullet\): two resolutions are homotopy equivalent over \(1_N\), and \(\mathcal Hom_R(M,-)\) preserves homotopies.

## 1. The comparison and the sign

**1.0.** Let \(M\) be flat. By Lemma 0.1 there, the \(\mathcal K^q\) are injective, and \(H^0(\mathcal K^\bullet)=H\). Let \(H\xrightarrow{j_L}L^\bullet\) be an injective resolution. By [Tag 05TG], there is a map \(\rho\colon L^\bullet\to\mathcal K^\bullet\), unique up to homotopy, with \(\rho j_L\) the inclusion \(a_H\colon H\to\mathcal K^0\); equality holds because \(\mathcal K^{-1}=0\). The comparison map is
\[
\begin{aligned}&c_n =H^n\Gamma(\ast,\rho) \colon H^n(T,H)\\&\quad \to\operatorname{Ext}^n_R(M,N),\end{aligned}
\]
where \(H^n\Gamma(\ast,\mathcal K^\bullet)=\operatorname{Ext}^n_R(M,N)\) by [Tag 05TG].

**Theorem 1.1.** Let \(M\) be a flat \(R\)-module with \(\mathcal Ext^1_R(M,N)=\mathcal Ext^2_R(M,N)=0\).
1. The map \(c_n\) is an isomorphism for \(n\le2\).
2. \(\mathcal G\) is locally nonempty and locally connected, banded by \(H\), and presentations exist.
3. Every presentation has \(\check\delta c=0\), and \(c_2([\mathcal G])=-\omega(B,M)\).

**Proof.** (1) The cone \(C_\rho\) of \(\rho\) is a bounded below complex of injectives. On cohomology sheaves, \(\rho\) is an isomorphism in degree \(0\), and \(H^q(L)=0\) for \(q>0\) while \(H^1(\mathcal K)=H^2(\mathcal K)=0\). So \(H^q(C_\rho)=0\) for \(q\le2\). Then
\[
H^n\Gamma(\ast,C_\rho)=\operatorname{Hom}_{D(R)}(R,C_\rho[n])=0
\]
for \(n\le2\) [Tags 05TG, 06XS]. The long exact sequence of \(\Gamma(\ast,L^\bullet)\to\Gamma(\ast,\mathcal K^\bullet)\to\Gamma(\ast,C_\rho)\) then shows that \(c_n\) is an isomorphism for \(n\le2\).

(2) It suffices to replace Proposition 2.4 (4) there, which concerns local existence; the rest of the proof of Theorem 3.1 (1) applies verbatim.

*Local lifts.* Let \(b\colon M|_U\to A_0|_U\). Then \(\bar d^0b\) is a cocycle of \(\mathcal K^1\). Since \(H^1(\mathcal K)=0\), locally \(\bar d^0b=d^0a\) with \(a\colon M\to J^0\). Then \(\bar d^0(\bar a-b)=0\), so \(\bar a=b\), \(\bar d^0\) being injective. This applies to \(b=k^{-1}(t-s)\).

*Local sections.* The map \(\theta\) is a cocycle of \(\mathcal K^2\). Since \(H^2(\mathcal K)=0\), locally \(\theta=d^1w\) with \(w\colon M\to J^1\). Then \(d^1(g-w\pi)=0\), so \(g-w\pi\) lands in \(\ker d^1=\bar d^0(A_0)\); write \(g-w\pi=\bar d^0r\) with \(r\colon E\to A_0\). From \(rk=1\), the restriction of \(\pi\) to \(\ker r\) is an isomorphism onto \(M\), and its inverse is a section \(s\) of \(\pi\).

(3) The proof of Theorem 3.1 (3) there used finite rank only through (2). It gives \(jc=\check\delta a\), hence \(\check\delta c=0\), and \(D(a-w)=a_Hc-\theta|_{K_0}\) in \(\operatorname{Tot}C^\bullet(K,\mathcal K^\bullet)\).

By Lemma 1.4 there, applied to \(\mathcal K^\bullet\) and to \(L^\bullet\), and by its naturality along \(\rho\), the class \([j_Lc]\) maps under \(\operatorname{Tot}(\rho)\) to \([a_Hc]=[\theta|_{K_0}]\). So \(c_2[\mathcal G]=[\theta]\), which is \(-\omega(B,M)\) by Lemma 2.3 there. \(\square\)

**Corollary 1.2.** If \(\mathcal Hom_R(M,-)\) is exact and \(M\) is flat, then Theorem 1.1 applies. This holds, for instance, for every free module over a field in the topos of sets, of any rank.

**Proof.** If \(\mathcal Hom_R(M,-)\) is exact, the complex \(\mathcal K^\bullet\) is exact in degrees \(>0\). In the topos of sets, a free module is projective, so \(\operatorname{Hom}(M,-)\) is exact. \(\square\)

## 2. The tensor description of the band

**Proposition 2.1.** Let \(T\) be the topos of sets and \(k=\mathbf Q\). Put \(M=\bigoplus_{n\ge1}ke_n\) and \(I=\bigoplus_{n\ge1}kt_n\), and let \(B=k\oplus I\) with \((a,x)(b,y)=(ab,ay+bx)\), so that \(R=k\). Then the map
\[
\operatorname{End}_k(M)\otimes_kI\to\operatorname{Hom}_k(M,I\otimes_kM),
\]
\(A\otimes v\mapsto(m\mapsto v\otimes Am)\), is not surjective.

**Proof.** The ring \(B\) is commutative, and \(I\) is an ideal with \(I^2=0\). Let \(h(e_n)=t_n\otimes e_1\), and let \(e_1^*\) be the first coordinate.

An element \(\sum_{j\le r}A_j\otimes v_j\) maps to a homomorphism whose composite with \(1\otimes e_1^*\) takes values in the span of \(v_1,\dots,v_r\). The composite of \(h\) with \(1\otimes e_1^*\) sends \(e_n\) to \(t_n\), and the \(t_n\) span an infinite-dimensional space. So \(h\) is not in the image. \(\square\)

By Corollary 1.2, the band in this example is \(H=\operatorname{Hom}_k(M,I\otimes M)\), not \(\operatorname{End}(M)\otimes I\).

## 3. Exercises

**Exercise 3.1.** Show that a finite locally free \(M\) satisfies the hypotheses of Theorem 1.1, and that \(c_2=\iota\) in that case.

## 4. Complete solutions

**3.1.** The functor \(\mathcal Hom_R(M,-)\) is exact, so \(\mathcal K^\bullet\) is an injective resolution of \(H\). One may take \(L=\mathcal K\) and \(\rho=1\), and then \(c_2=\iota\).

## Sources

The question of the comparison is due to Illusie, in his work on the cotangent complex, and gerbes are due to Giraud. The main argument follows a solution produced with ChatGPT (OpenAI) in October 2026, completed here. The homological algebra is that of the Stacks project.
