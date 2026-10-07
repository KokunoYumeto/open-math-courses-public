# Idèles, ideals and ray class groups

*Original independently authored material written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the exact sequence of unit and class groups by Claude Opus 5.5 (Anthropic). Self-checked by the writing AI. Original text: [CC0](https://creativecommons.org/publicdomain/zero/1.0/).*

An idèle specifies a nonzero element at every completion. Its valuations form a fractional ideal; its unit components carry congruence information that the ideal forgets. A ray class group remembers a prescribed finite amount of this information, together with prescribed signs at real embeddings. We will construct these groups as finite discrete quotients of the idèle class group and prove that they detect every open subgroup.

Let \(K\) be a number field, \(\mathcal O_K\) its ring of integers, \(J_K\) its idèle group, and \(C_K=J_K/K^\times\). At a finite place \(v\) corresponding to \(\mathfrak p\), write \(\operatorname{ord}_v\) for the valuation with \(\operatorname{ord}_v(\varpi_v)=1\), and \(\mathcal O_v\) for the valuation ring. We use the topology and arithmetic proved in [Idèles and the idèle class group](NT-ADL-03.md), including the finiteness of the ordinary ideal class group. Simultaneous approximation at any finite set of places follows from Theorem 2.3 of [The adèle ring of a number field](NT-ADL-02.md), by omitting a place outside that set. For the conventions allowing a selected set of real places, compare [Milne CFT, Chapter V, §§1 and 4]. [Sutherland 21, Remark 21.5] gives the narrow case, with positivity at all real places. [Sutherland 26, §26.1] relates the idèle class group to the ideal class group.

## What the valuations retain

Let \(I_K\) be the group of nonzero fractional ideals of \(\mathcal O_K\), given the discrete topology. Unique ideal factorization identifies it with the direct sum of copies of \(\mathbb Z\) indexed by finite primes. Put

\[
J_{K,\infty}=\prod_{v\mid\infty}K_v^\times
\times\prod_{v<\infty}\mathcal O_v^\times.
\tag{1}
\]

This is an open subgroup of \(J_K\). The ordinary ideal class group is \(\operatorname{Cl}_K=I_K/\{(a):a\in K^\times\}\).

**Proposition 4.1 (the ideal attached to an idèle).** The map

\[
\mathfrak a:J_K\longrightarrow I_K,
\qquad x\longmapsto\prod_{v<\infty}\mathfrak p_v^{\operatorname{ord}_v(x_v)}
\tag{2}
\]

is a continuous surjective homomorphism with kernel \(J_{K,\infty}\). It induces a continuous surjection

\[
C_K\longrightarrow\operatorname{Cl}_K
\quad\text{with kernel }J_{K,\infty}K^\times/K^\times.
\tag{3}
\]

**Proof.** All but finitely many finite components of an idèle are units, so the product in (2) is finite. Additivity of the valuations makes the map a homomorphism. For an ideal \(\prod\mathfrak p^{n_{\mathfrak p}}\), take the component \(\varpi_v^{n_{\mathfrak p_v}}\) at the finitely many indicated primes and take \(1\) everywhere else. This idèle maps to the given ideal. The valuation is zero precisely on \(\mathcal O_v^\times\), proving the kernel statement. A homomorphism into a discrete group is continuous when its kernel is open: every fiber is then an open coset. This applies here.

For a diagonal element \(a\in K^\times\), (2) equals its principal fractional ideal \((a)\). Hence the map descends to (3), and surjectivity survives. If \(\mathfrak a(x)=(a)\), then \(xa^{-1}\) has zero valuation at every finite place and belongs to (1). Conversely, an element of \(J_{K,\infty}K^\times\) has principal ideal. The quotient topology on \(C_K\) gives continuity. \(\square\)

Let \(P_K\subseteq I_K\) be the subgroup of principal fractional ideals \((a)\), \(a\in K^\times\), so that \(\operatorname{Cl}_K=I_K/P_K\). As noted in the proof of Proposition 4.1, the map (2) sends a diagonal element \(a\in K^\times\) to \((a)\). It therefore maps the subgroup \(K^\times\) of \(J_K\) onto \(P_K\), and the map (3) sends the class of an idèle \(x\) to the ideal class of \(\mathfrak a(x)\). The unit group \(\mathcal O_K^\times\) and the subgroup (1) fit together with (3) into the sequence

\[
1\longrightarrow\mathcal O_K^\times
\longrightarrow J_{K,\infty}
\longrightarrow C_K
\longrightarrow\operatorname{Cl}_K
\longrightarrow1,
\]

which is exact. Its first map is the diagonal embedding, its second is the restriction of the quotient map \(q:J_K\to C_K\), and its third is (3).

The diagonal embedding is injective, because each map \(K\to K_v\) is injective. The kernel of the second map is \(J_{K,\infty}\cap K^\times\). Since \(J_{K,\infty}\) is the kernel of \(\mathfrak a\), a diagonal element \(a\) lies in it exactly when \((a)=\mathcal O_K\). Every unit generates \(\mathcal O_K\). Conversely, if \(a\mathcal O_K=\mathcal O_K\), then \(a\in\mathcal O_K\) and \(ab=1\) for some \(b\in\mathcal O_K\), so \(a\in\mathcal O_K^\times\). Thus \(J_{K,\infty}\cap K^\times=\mathcal O_K^\times\), which gives exactness at the first two terms. The image of the second map is \(J_{K,\infty}K^\times/K^\times\). Proposition 4.1 identifies this group with the kernel of (3) and proves that (3) is surjective.

Consequently, the kernel of (3) is isomorphic to \(J_{K,\infty}/\mathcal O_K^\times\). The isomorphism is a homeomorphism when the kernel carries the subspace topology from \(C_K\) and \(J_{K,\infty}/\mathcal O_K^\times\) carries the quotient topology. First, \(q\) is open: for open \(W\subseteq J_K\), the set \(q^{-1}(q(W))=\bigcup_{a\in K^\times}aW\) is a union of translates of \(W\) and is therefore open. Since \(J_{K,\infty}\) is open in \(J_K\), the restriction of \(q\) to \(J_{K,\infty}\) is a continuous open homomorphism onto \(J_{K,\infty}K^\times/K^\times\), with kernel \(\mathcal O_K^\times\). The induced bijection from \(J_{K,\infty}/\mathcal O_K^\times\) is continuous by the definition of the quotient topology. It is open because every open subset of \(J_{K,\infty}/\mathcal O_K^\times\) is the image of an open subset of \(J_{K,\infty}\).

Even when the ordinary class group is trivial, its kernel in (3) contains much information. The rational case already shows this: \(C_{\mathbb Q}\) has a positive real factor and a profinite unit factor. Congruences will give finite quotients of the latter.

## Finite congruences and real signs

A **modulus** is a pair \(\mathfrak m=\mathfrak m_f M\), where \(\mathfrak m_f\) is a nonzero integral ideal and \(M\) is a set of real places of \(K\). Write

\[
\mathfrak m_f=\prod_{\mathfrak p}\mathfrak p^{n_{\mathfrak p}},
\qquad n_{\mathfrak p}\geq0,
\]

with only finitely many positive exponents. A complex place never belongs to \(M\). Define

\[
U_v^{(0)}=\mathcal O_v^\times,
\qquad U_v^{(n)}=1+\mathfrak p_v^n\mathcal O_v\quad(n\geq1)
\tag{4}
\]

at a finite place. The congruence subgroup of idèles is

\[
U_{\mathfrak m}=
\prod_{v\in M}\mathbb R_{>0}
\times\prod_{\substack{v\text{ real}\\v\notin M}}\mathbb R^\times
\times\prod_{v\text{ complex}}\mathbb C^\times
\times\prod_{v<\infty}U_v^{(n_{\mathfrak p_v})}.
\tag{5}
\]

It is open in \(J_K\): at the finitely many primes dividing \(\mathfrak m_f\) we impose open principal-unit conditions, and the remaining finite factors are the usual unit subgroups. Each real positivity condition is open as well.

Write \(K_{\mathfrak m,1}^\times\) for the subgroup of \(a\in K^\times\) such that

\[
a-1\in\mathfrak p_v^{n_{\mathfrak p_v}}\mathcal O_v
\quad(\mathfrak p_v\mid\mathfrak m_f),
\qquad a_v>0\quad(v\in M).
\tag{6}
\]

The finite conditions automatically make \(a\) a unit at those primes. Let

\[
I_K^{\mathfrak m}=\left\{\mathfrak b\in I_K:
\operatorname{ord}_{\mathfrak p}(\mathfrak b)=0
\text{ for every }\mathfrak p\mid\mathfrak m_f\right\},
\qquad
P_{\mathfrak m,1}=\{(a):a\in K_{\mathfrak m,1}^\times\}.
\tag{7}
\]

These are fractional ideals prime to the finite part of the modulus; negative exponents at other primes are allowed. The **ray class group** is

\[
\operatorname{Cl}_{\mathfrak m}=I_K^{\mathfrak m}/P_{\mathfrak m,1}.
\tag{8}
\]

Two ideals in (7) represent the same ray class precisely when their ratio has a generator satisfying (6). With \(\mathfrak m_f=(1)\) and \(M=\varnothing\), (8) is the ordinary class group. With \(\mathfrak m_f=(1)\) and \(M\) all real places, it is the **narrow class group** \(\operatorname{Cl}_K^+\). Thus an absent infinite part does not impose positivity.

The selected set \(M\) is part of the modulus data, as in [Milne CFT, Definition 1.3, pp.148–149]. It affects only the real signs. The finite residue conditions are imposed in the completed valuation rings, and a complex component remains unrestricted. This distinction is necessary when comparing with the narrow convention, which imposes positivity at all real places [Sutherland 21, Remark 21.5]: an ordinary class group and a narrow class group need not agree.

For the proof, introduce another subgroup \(J_K^{\mathfrak m}\). Its components satisfy the conditions in (6) at primes dividing \(\mathfrak m_f\) and at places in \(M\), and are unrestricted elsewhere, subject to being an idèle. In particular, away from \(\mathfrak m_f\) they may have nonzero valuations. This distinguishes \(J_K^{\mathfrak m}\) from \(U_{\mathfrak m}\), whose every finite component is a unit.

In [Milne CFT, V, §4, pp.172–173], these two groups are \(I^{\mathfrak m}\) and \(W_{\mathfrak m}\), respectively. Proposition 4.6 there passes first from idèles satisfying the conditions at the modulus to ideals prime to its finite part, and then uses approximation to reach every idèle class. The proof below writes out both maps and their kernels. Keeping the two subgroups distinct avoids imposing unit conditions at primes where the representing ideal needs a nonzero exponent.

**Theorem 4.2 (the idèlic ray quotient).** There are canonical isomorphisms of discrete groups

\[
\operatorname{Cl}_{\mathfrak m}
\simeq J_K/(U_{\mathfrak m}K^\times)
\simeq C_K/C_{\mathfrak m},
\qquad
C_{\mathfrak m}=U_{\mathfrak m}K^\times/K^\times.
\tag{9}
\]

The first isomorphism sends the ideal of \(x\in J_K^{\mathfrak m}\) to the class of that idèle.

**Proof.** First we prove

\[
J_K=J_K^{\mathfrak m}K^\times.
\tag{10}
\]

For \(x\in J_K\), use simultaneous approximation to choose \(a\in K^\times\) close enough to \(x_v^{-1}\) at every prime dividing \(\mathfrak m_f\) that \(ax_v\in1+\mathfrak p_v^{n_{\mathfrak p_v}}\mathcal O_v\). At every real place in \(M\), require \(a_v\) to have the sign of \(x_v\). These are finitely many open conditions about nonzero targets. Approximation provides such an \(a\); if there are no conditions, choose \(a=1\). Then \(ax\in J_K^{\mathfrak m}\), proving (10).

Restriction of (2) gives a surjection \(J_K^{\mathfrak m}\to I_K^{\mathfrak m}\). Indeed, uniformizer powers at primes outside \(\mathfrak m_f\), with every other component \(1\), realize all these ideals. Its kernel is exactly \(U_{\mathfrak m}\). Moreover,

\[
J_K^{\mathfrak m}\cap K^\times=K_{\mathfrak m,1}^\times.
\tag{11}
\]

Consequently (8) identifies with \(J_K^{\mathfrak m}/(U_{\mathfrak m}K_{\mathfrak m,1}^\times)\). Inclusion in \(J_K\) maps this group onto \(J_K/(U_{\mathfrak m}K^\times)\) by (10). Its kernel is trivial: if \(x=ua\in J_K^{\mathfrak m}\), where \(u\in U_{\mathfrak m}\) and \(a\in K^\times\), then \(a=u^{-1}x\in J_K^{\mathfrak m}\cap K^\times\), which is (11). This proves the first isomorphism in (9). Quotienting first by \(K^\times\) proves the second. Since \(U_{\mathfrak m}K^\times\) is open, its quotient is discrete. All the maps just constructed therefore respect the indicated discrete topologies. \(\square\)

## The finite sequence behind a ray group

Let \(\mathcal O_{\mathfrak m,1}^\times=\mathcal O_K^\times\cap K_{\mathfrak m,1}^\times\). Put

\[
B_{\mathfrak m}=(\mathcal O_K/\mathfrak m_f)^\times
\times\{\pm1\}^{M}.
\tag{12}
\]

When \(\mathfrak m_f=(1)\), the first factor means the trivial group. A global unit has a residue in the finite factor and a sign at every selected real place. Denote this homomorphism by \(\delta\).

**Proposition 4.3 (residues, signs and ideal classes).** The following sequence is exact:

\[
1\longrightarrow\mathcal O_K^\times/\mathcal O_{\mathfrak m,1}^\times
\xrightarrow{\ \delta\ }B_{\mathfrak m}
\xrightarrow{\ \beta\ }\operatorname{Cl}_{\mathfrak m}
\xrightarrow{\ \gamma\ }\operatorname{Cl}_K
\longrightarrow1.
\tag{13}
\]

Here \(\gamma\) forgets the ray conditions. To define \(\beta\), choose \(a\in K^\times\) with the specified residues at \(\mathfrak m_f\) and signs at \(M\), and take the ray class of \((a)\). In particular, \(\operatorname{Cl}_{\mathfrak m}\) is finite. If \(h_K=\#\operatorname{Cl}_K\), then

\[
\#\operatorname{Cl}_{\mathfrak m}
=h_K\frac{2^{\#M}\#(\mathcal O_K/\mathfrak m_f)^\times}
{[\mathcal O_K^\times:\mathcal O_{\mathfrak m,1}^\times]}.
\tag{14}
\]

**Proof.** The kernel of the residue-and-sign map on units is exactly \(\mathcal O_{\mathfrak m,1}^\times\). Thus the displayed map \(\delta\) is injective.

For an element of (12), the Chinese remainder theorem identifies its finite residue with unit residues modulo each \(\mathfrak p^{n_{\mathfrak p}}\). These are also the residues in \(\mathcal O_v/\mathfrak p_v^{n_{\mathfrak p}}\mathcal O_v\): localization preserves this quotient because elements outside \(\mathfrak p\) become units modulo \(\mathfrak p^n\), and completion preserves it because the localized ring is dense and \(\mathfrak p_v^n\mathcal O_v\) is open. Choose local lifts, and impose the selected signs. Simultaneous approximation produces \(a\in K^\times\) meeting those finite congruences and signs. Each such \(a\) is a unit at primes dividing \(\mathfrak m_f\), so \((a)\in I_K^{\mathfrak m}\). If \(a'\) is a second choice, then \(a/a'\) is congruent to \(1\) at all those primes and positive at all places in \(M\). It belongs to \(K_{\mathfrak m,1}^\times\), so \((a)\) and \((a')\) have the same ray class. Products of choices give choices for products, making \(\beta\) a well-defined homomorphism.

If \(\beta(b)=1\), choose \(a\) representing its residues and signs. Then \((a)=(c)\) for some \(c\in K_{\mathfrak m,1}^\times\). Equality of their fractional ideals means \(a/c\in\mathcal O_K^\times\). The residues and signs of \(a/c\) are those of \(a\), because \(c\) has residue \(1\) and positive signs. Hence \(b\in\operatorname{im}\delta\). Conversely, a unit gives the unit ideal and maps to the identity under \(\beta\). This proves exactness at \(B_{\mathfrak m}\).

The map \(\gamma\) is well defined, since every ray-principal ideal is principal. If a ray class maps to the identity under \(\gamma\), represent it by \(\mathfrak b=(a)\in I_K^{\mathfrak m}\). The element \(a\) is a unit at each prime dividing \(\mathfrak m_f\). Its residues and selected signs give an element \(b\in B_{\mathfrak m}\) with \(\beta(b)=[\mathfrak b]\). Conversely, \(\beta\) produces principal ideals, so its image lies in \(\ker\gamma\).

Finally, let \(\mathfrak b\) be any fractional ideal. At every prime dividing \(\mathfrak m_f\), approximate a local element of valuation \(-\operatorname{ord}_{\mathfrak p}(\mathfrak b)\) by \(a\in K^\times\). A sufficiently small neighborhood fixes that valuation. The ideal \((a)\mathfrak b\) is then prime to \(\mathfrak m_f\), and has the same ordinary class as \(\mathfrak b\). This proves surjectivity of \(\gamma\).

The group \(B_{\mathfrak m}\) is finite, and \(\operatorname{Cl}_K\) is finite by Corollary 3.4. Exactness shows that the kernel of \(\gamma\) is the quotient of \(B_{\mathfrak m}\) by the indicated unit image. Therefore the middle ray group is finite, and counting gives (14). \(\square\)

For \(q_{\mathfrak p}=\#(\mathcal O_K/\mathfrak p)\), the finite residue factor has order

\[
\#(\mathcal O_K/\mathfrak m_f)^\times
=\prod_{\mathfrak p\mid\mathfrak m_f}
q_{\mathfrak p}^{n_{\mathfrak p}-1}(q_{\mathfrak p}-1).
\tag{15}
\]

Indeed, each successive quotient \(\mathfrak p^j/\mathfrak p^{j+1}\) has \(q_{\mathfrak p}\) elements: localization at \(\mathfrak p\) identifies it with the one-dimensional residue space in the discrete valuation ring, and localization does not change this module, which is killed by \(\mathfrak p\). Thus \(\mathcal O_K/\mathfrak p^n\) has \(q_{\mathfrak p}^n\) elements. The nonunits are exactly its ideal \(\mathfrak p/\mathfrak p^n\), with \(q_{\mathfrak p}^{n-1}\) elements. Subtract and apply the Chinese remainder theorem to get (15).

At the purely infinite modulus consisting of all real places, (14) becomes

\[
h_K^+=h_K\frac{2^{r_1}}
{[\mathcal O_K^\times:\mathcal O_K^{\times,+}]},
\tag{16}
\]

where \(\mathcal O_K^{\times,+}\) is the group of totally positive units. The difference between ordinary and narrow classes is therefore precisely the failure of unit signs to realize all sign patterns.

Say \(\mathfrak m\mid\mathfrak n\) if the finite exponents for \(\mathfrak n\) are at least those for \(\mathfrak m\) and its real-place set contains that of \(\mathfrak m\). Then \(U_{\mathfrak n}\subset U_{\mathfrak m}\), and (9) gives a surjection

\[
\operatorname{Cl}_{\mathfrak n}\longrightarrow\operatorname{Cl}_{\mathfrak m}.
\tag{17}
\]

On an ideal prime to \(\mathfrak n_f\), this simply forgets the extra congruences. Every ray class modulo \(\mathfrak m\) has such a representative: its idèle class lifts by (10) for \(\mathfrak n\), and the ideal of the resulting element of \(J_K^{\mathfrak n}\) is prime to \(\mathfrak n_f\).

## Which subgroups the moduli detect

**Proposition 4.4 (open subgroups).** A subgroup \(N\subset C_K\) is open of finite index if and only if it contains \(C_{\mathfrak m}\) for some modulus \(\mathfrak m\). In fact every open subgroup of \(C_K\) has finite index.

**Proof.** Suppose \(N\) is open. Its inverse image \(\widetilde N\) in \(J_K\) is an open subgroup containing \(K^\times\). Choose an identity neighborhood inside it of the form

\[
W=\prod_{v\mid\infty}W_v
\times\prod_{v\in S_f}W_v
\times\prod_{\substack{v<\infty\\v\notin S_f}}\mathcal O_v^\times,
\tag{18}
\]

where \(S_f\) is finite and every \(W_v\) is an open neighborhood of \(1\).

For each real place, \(\widetilde N\) contains the subgroup supported there that is generated by \(W_v\cap\mathbb R_{>0}\). That generated subgroup is all of \(\mathbb R_{>0}\): under the logarithm an identity neighborhood contains an interval about \(0\), and sums of that interval cover \(\mathbb R\). At a complex place the subgroup generated by an identity neighborhood is all of \(\mathbb C^\times\). To justify this, the generated subgroup is open, its complement is a union of open cosets, and \(\mathbb C^\times\) is connected; it must therefore be the whole group. Connectedness follows, for example, by joining a nonzero complex number to \(1\) through its polar radius and angle.

At each \(v\in S_f\), choose \(n_v\geq1\) sufficiently large that \(1+\mathfrak p_v^{n_v}\mathcal O_v\subset W_v\). These subgroups form an identity-neighborhood basis because the powers of the maximal ideal form an additive neighborhood basis, and translation by \(1\) preserves the topology. The complete product of unit groups outside \(S_f\), supported at those places, already lies in (18). Multiplying this tail by the finitely many supported principal-unit factors and the supported infinite factors shows that \(\widetilde N\) contains \(U_{\mathfrak m}\), where

\[
\mathfrak m_f=\prod_{v\in S_f}\mathfrak p_v^{n_v},
\qquad M=\{\text{all real places of }K\}.
\]

It also contains \(K^\times\), so \(N\supset C_{\mathfrak m}\).

Conversely, (5) is open, so its image \(C_{\mathfrak m}\) is open in the quotient \(C_K\). By (9) and Proposition 4.3 it has finite index. Any subgroup containing it is a union of its open cosets and has index at most \(\#\operatorname{Cl}_{\mathfrak m}\). It is therefore open of finite index. Applying this conclusion to the modulus constructed from an arbitrary open \(N\) proves the last assertion as well. \(\square\)

This gives a concrete way to locate a continuous finite quotient of \(C_K\). Its kernel is open because the target is discrete, and hence contains a ray congruence subgroup. Real positivity is enough at the infinite places because an open subgroup always contains their identity components. The assertion does not identify the connected component of \(C_K\) with a positive real line for a general number field.

[Milne CFT, Proposition 4.7, p.174] uses this same local argument to show that a continuous homomorphism to a finite discrete group kills some \(U_{\mathfrak m}\). Proposition 4.4 gives the subgroup formulation directly, including the entire compact unit tail; it also proves finite index for every open subgroup, rather than assuming it at the start.

## Reading the rational quotient explicitly

Use the decomposition from Proposition 3.6,

\[
C_{\mathbb Q}\simeq\mathbb R_{>0}\times\widehat{\mathbb Z}^{\times}.
\tag{19}
\]

Concretely, for an idèle \(x\), set

\[
q_0=\prod_p p^{\operatorname{ord}_p(x_p)},
\quad q=\operatorname{sgn}(x_\infty)q_0,
\quad t=x_\infty/q>0,
\quad u_p=x_p/q\in\mathbb Z_p^\times.
\tag{20}
\]

The pair \((t,u)\) is unchanged by multiplying \(x\) by a diagonal rational number. Write \(V_m=\ker(\widehat{\mathbb Z}^{\times}\to(\mathbb Z/m\mathbb Z)^\times)\). This reduction map is surjective: choose a unit lift at each prime dividing \(m\), and use \(1\) at other primes.

**Proposition 4.5 (rational ray groups).** For \(m\geq1\),

\[
C_{(m)\infty}=\mathbb R_{>0}\times V_m,
\qquad
C_{(m)}=\mathbb R_{>0}\times\bigl(\{\pm1\}V_m\bigr).
\tag{21}
\]

Here \(-1\) in the second formula is the same sign in every finite component. Consequently

\[
\operatorname{Cl}_{(m)\infty}(\mathbb Q)
\simeq(\mathbb Z/m\mathbb Z)^\times,
\qquad
\operatorname{Cl}_{(m)}(\mathbb Q)
\simeq(\mathbb Z/m\mathbb Z)^\times/\operatorname{im}\{\pm1\}.
\tag{22}
\]

Under (19), these are the maps given by reducing \(u\), and reducing it modulo the sign image, respectively.

**Proof.** Every element of \(U_{(m)\infty}\) has finite valuation zero, so \(q_0=1\); its infinite component is positive, so \(q=1\) in (20). Its finite components therefore form \(u\in V_m\), and its real component is an arbitrary \(t>0\). Conversely, every such pair is represented by an element of \(U_{(m)\infty}\). This proves the first formula of (21).

For \(U_{(m)}\) the infinite component may be negative. A positive component gives \(u\in V_m\); a negative one gives \(q=-1\), so its normalized finite component is the negative of an element of \(V_m\). Both possibilities occur for every \(t>0\). This proves the second formula. Theorem 4.2 and surjectivity of reduction now give (22). \(\square\)

There is an inverse in passing between the idèlic reduction convention and the common positive-generator convention for ideals. If \((a)\) is prime to \(m\), with \(a\in\mathbb Q_{>0}\), represent it by finite components \(p^{\operatorname{ord}_p(a)}\) and infinite component \(1\). The normalization in (20) divides by \(q=a\). At the primes dividing \(m\), those finite components were \(1\), so the normalized residue is \(a^{-1}\bmod m\). Thus the isomorphism in (22) compatible with idèlic reduction sends \([(a)]\) to \(a^{-1}\); sending it to \(a\) instead gives the equally valid isomorphism obtained by inversion. For the modulus without \(\infty\), changing a generator's sign has exactly the quotient effect in (22).

For \(m=5\), the group with \(\infty\) is cyclic of order \(4\), generated by residue \(2\). Omitting \(\infty\) identifies residues \(1\) and \(4\), and residues \(2\) and \(3\), leaving a cyclic group of order \(2\). For \(m=1\) or \(2\), the residue group is trivial. In general the order without \(\infty\) is

\[
\frac{\varphi(m)}{\#\operatorname{im}(\{\pm1\}\to(\mathbb Z/m\mathbb Z)^\times)}.
\tag{23}
\]

The denominator is \(1\) for \(m=1,2\), and \(2\) for \(m>2\).

## A narrow class that ordinary ideals cannot distinguish

Consider \(K=\mathbb Q(\sqrt3)\), with real embeddings \(\sigma_+(\sqrt3)=\sqrt3\) and \(\sigma_-(\sqrt3)=-\sqrt3\). We will compute both the ordinary and narrow class groups rather than presume the ordinary class number.

First, \(\mathcal O_K=\mathbb Z[\sqrt3]\). Here is a direct verification. Write an algebraic integer as \(a+b\sqrt3\), where \(a,b\in\mathbb Q\). Its trace gives \(2a=m\in\mathbb Z\), and its norm gives \(a^2-3b^2\in\mathbb Z\). Thus \(12b^2\in\mathbb Z\). The denominator of \(b\) in lowest terms has square dividing \(12\), so \(2b=l\in\mathbb Z\). Integrality of the norm now says \(m^2-3l^2\equiv0\pmod4\). If \(l\) were odd this would force a square to be \(3\) modulo \(4\), which is impossible. Hence \(l\), and then \(m\), are even; \(a,b\in\mathbb Z\). Conversely, every element of \(\mathbb Z[\sqrt3]\) satisfies a monic polynomial over \(\mathbb Z\).

The ring is Euclidean for the absolute norm. For \(\alpha,\beta\in\mathcal O_K\), \(\beta\ne0\), write \(\alpha/\beta=x+y\sqrt3\). Choose integers \(r,s\) with \(|x-r|,|y-s|\leq1/2\). Then

\[
\left|N_{K/\mathbb Q}\bigl(\alpha/\beta-(r+s\sqrt3)\bigr)\right|
=\left|(x-r)^2-3(y-s)^2\right|\leq\frac34<1.
\tag{24}
\]

Multiplying by \(|N(\beta)|\) gives a remainder of smaller absolute norm. Choosing a nonzero element of least absolute norm in an integral ideal and applying division shows that it generates the ideal: every remainder in that ideal must be zero. Every fractional ideal is therefore principal, and \(h_K=1\).

A unit \(a+b\sqrt3\) has norm \(a^2-3b^2=\pm1\). Norm \(-1\) would imply \(a^2\equiv2\pmod3\), impossible. Thus every unit has norm \(+1\), and its two signs agree. The units \(1\) and \(-1\) realize the sign patterns \((+,+)\) and \((-,-)\), so these are exactly the unit sign image. By (13) at the purely infinite modulus,

\[
\operatorname{Cl}_K^+
\simeq\{\pm1\}^2/\{(+,+),(-,-)\}
\simeq\mathbb Z/2\mathbb Z.
\tag{25}
\]

The ideal \((\sqrt3)\) represents its nontrivial class. Its generator has signs \((+,-)\); multiplying by any unit cannot make both signs positive. Its square is \((3)\), whose positive generator makes it narrow-principal. This realizes the order-two class concretely.

The unit \(\varepsilon=2+\sqrt3\) is totally positive and has norm \(+1\). In fact the totally positive units are exactly \(\varepsilon^{\mathbb Z}\). To see this, multiply a totally positive unit by a suitable power of \(\varepsilon\) so that its \(\sigma_+\)-value \(u\) lies in \([1,\varepsilon)\). Its other value is \(u^{-1}\), so its coefficient of \(\sqrt3\) is

\[
b=\frac{u-u^{-1}}{2\sqrt3}\in[0,1).
\]

This coefficient is an integer and hence zero. The reduced unit is \(1\). Every unit has equal signs, so the full unit group is \(\{\pm\varepsilon^n:n\in\mathbb Z\}\), in agreement with the sign calculation above.

## Exercises

1. **Easy.** Compute the rational ray class groups for the moduli \((12)\infty\) and \((12)\). Give their group structures and list the sign-identification classes.

2. **Medium.** Compute the narrow class group of \(\mathbb Q(\sqrt3)\) using idèles. Identify an idèle whose class gives the nontrivial narrow class, and explain which ideal represents it.

3. **Medium.** Reconstruct (13) without assuming the cardinality formula. Specify the map out of the residue-and-sign group, check both nontrivial kernels, and prove surjectivity onto the ordinary class group.

4. **Hard.** Show that the intersection over all rational moduli is

   \[
   \bigcap_{\mathfrak m}U_{\mathfrak m}\mathbb Q^\times/\mathbb Q^\times
   =\mathbb R_{>0}\times\{1\}\subset C_{\mathbb Q}.
   \]

   Prove that this is the connected component of the identity in \(C_{\mathbb Q}\).

## Solutions

**Solution 1.** The units modulo \(12\) are \(1,5,7,11\). Each of the three nonidentity elements has square \(1\), so the unit group is \((\mathbb Z/2\mathbb Z)^2\), generated, for instance, by \(5\) and \(7\). Proposition 4.5 gives this group for \((12)\infty\). Without \(\infty\), divide by the sign image \(\{1,11\}\). The two cosets are \(\{1,11\}\) and \(\{5,7\}\), so \(\operatorname{Cl}_{(12)}(\mathbb Q)\simeq\mathbb Z/2\mathbb Z\). This also follows from (14): the ordinary rational class number is \(1\), and the residue-and-sign contribution is divided by the image of its global units \(\{\pm1\}\).

**Solution 2.** Let \(M=\{\sigma_+,\sigma_-\}\) and \(\mathfrak m_f=(1)\). Then \(U_{\mathfrak m}=\mathbb R_{>0}^2\times\prod_{v<\infty}\mathcal O_v^\times\). The Euclidean argument (24) shows that every ordinary ideal class is trivial, so (2) allows any idèle to be multiplied by a diagonal element until all its finite components are units. The remaining obstruction to membership in \(U_{\mathfrak m}\) is its two real signs. Two such representatives differ by a diagonal element with unit finite components precisely when that element lies in \(\mathcal O_K^\times\). Its sign pattern is either \((+,+)\) or \((-,-)\), as the norm equation modulo \(3\) proves. Hence the quotient is the group in (25).

For an explicit idèle \(z\), take its infinite components to be \((1,-1)\) and every finite component to be \(1\). Its sign pattern is mixed, so its class is nontrivial. To compute its corresponding ideal under Theorem 4.2, multiply by the diagonal element \(\sqrt3\). The infinite components of \(\sqrt3 z\) are both positive, and the finite components are those of \(\sqrt3\). Thus \(\sqrt3 z\in J_K^{\mathfrak m}\), and (2) gives the ideal \((\sqrt3)\). Squaring \(z\) gives the identity idèle, consistent with the narrow class of \((\sqrt3)^2=(3)\) being trivial.

**Solution 3.** Send a unit to its residues modulo \(\mathfrak m_f\) and its signs at \(M\). The kernel consists of the units congruent to \(1\) and positive at the selected places, namely \(\mathcal O_{\mathfrak m,1}^\times\). This proves injectivity after dividing by that kernel. For a residue-and-sign tuple, choose a nonzero \(a\in K\) with these data by approximation, and send the tuple to \([(a)]\) in the ray group. The quotient of any two choices is in \(K_{\mathfrak m,1}^\times\), proving independence; multiplying choices proves the homomorphism property.

Its image is ray-principal exactly when \((a)=(c)\) for a \(c\) satisfying the ray conditions. Then \(a/c\) is a global unit with the original residue-and-sign data. Conversely such unit data give the unit ideal. Thus its kernel is precisely the unit image. The map from ray classes to ordinary classes forgets the conditions. A class in its kernel has a prime-to-modulus representative \((a)\); the residue-and-sign tuple of \(a\) maps back to that ray class. This proves the second kernel assertion. For an arbitrary fractional ideal \(\mathfrak b\), choose a nonzero \(a\in K\) whose valuations at primes dividing \(\mathfrak m_f\) cancel those of \(\mathfrak b\), using sufficiently close approximation to local elements with those valuations. Then \((a)\mathfrak b\) is prime to \(\mathfrak m_f\) and represents the same ordinary class. This proves the final surjectivity and every step of (13). Finiteness now follows from the finite residue-and-sign group and the finite ordinary class group, without using (14) in the proof.

This is the exact sequence of [Milne CFT, Theorem 1.7, pp.150–151], with the finite residues written before the selected real signs. Its unit term is an image in the finite group \(B_{\mathfrak m}\), even when \(\mathcal O_K^\times\) itself is infinite. The finite index in (14) therefore measures the realized residue-and-sign patterns. [Milne CFT, Example 1.8, pp.151–152] also separates the rational moduli with and without the real place; our formula (22) keeps track of the inversion required by the idèlic reduction convention.

**Solution 4.** Every congruence subgroup in (21) contains \(\mathbb R_{>0}\times\{1\}\). Conversely, suppose \((t,u)\) belongs to every rational congruence subgroup. In particular it belongs to \(C_{(p^n)\infty}\) for every prime \(p\) and every \(n\geq1\). By (21), \(u_p-1\in p^n\mathbb Z_p\) for every \(n\). The intersection \(\bigcap_n p^n\mathbb Z_p\) is \(\{0\}\): a nonzero element has a finite valuation. Hence \(u_p=1\) for every \(p\), proving the asserted intersection.

The group \(\mathbb R_{>0}\) is connected. The finite reduction maps separate distinct elements of \(\widehat{\mathbb Z}^{\times}\): if two units differ at \(p\), some reduction modulo \(p^n\) distinguishes them. Each finite discrete image of a connected subset is a singleton. Consequently any connected subset of \(\widehat{\mathbb Z}^{\times}\) containing the identity contains no other point. Projection of a connected subset of (19) to this factor is connected, so the identity component of \(C_{\mathbb Q}\) lies in \(\mathbb R_{>0}\times\{1\}\). The opposite inclusion follows from connectedness of that real factor. This completes the identification.

## Prerequisites and further directions

- Theorem 3.2 of [Discrete valuation rings and Dedekind domains](prerequisites/NT-ANT-03.md) proves unique fractional ideal factorization and its local valuation exponents; Proposition 3.3 proves Chinese remainders for distinct prime powers and their localization quotients. These are used in (2) and (15). The completion valuation rings are those of Theorem 2.1 and Proposition 2.3 of [Completions, the p-adic numbers and complete discretely valued fields](prerequisites/NT-LOC-02.md), with the number-field paragraph there, and Proposition 2.1 of [The adèle ring of a number field](NT-ADL-02.md). [Milne ANT, Theorems 1.14 and 3.20, Lemmas 3.9–3.10 and Example 3.26(c)] is the scholarly reference.
- The restricted-product topology on \(J_K\), the identification of a field element with a diagonal idèle, and finiteness of \(\operatorname{Cl}_K\). These are proved in [Idèles and the idèle class group](NT-ADL-03.md), especially Proposition 3.1 and Corollary 3.4.
- Simultaneous approximation at a finite set of places: given nonempty open subsets of finitely many completions, one element of \(K\) belongs to all of them. It follows by projection from Theorem 2.3 of [The adèle ring of a number field](NT-ADL-02.md), choosing an omitted place outside the finite set.
- The topological isomorphism (19), including its formula (20), is Proposition 3.6 of [Idèles and the idèle class group](NT-ADL-03.md). This lesson proves all of its stated ray-quotient consequences.

## References

- **[Milne CFT]** J. S. Milne, *Class Field Theory*, version 4.03 (6 August 2020), [author-hosted notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter V, §1, Definition 1.3, Theorem 1.7 and Example 1.8, pp.148–152; §4, especially 4.1–4.4 and Propositions 4.6–4.7, pp.170–174.
- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (19 July 2020), [author-hosted notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Theorems 1.14 and 3.20, Lemmas 3.9–3.10 and Example 3.26(c): Chinese remainders, prime-power quotients and their localizations, and fractional-ideal factorization with its valuations.
- **[Sutherland 21]** A. V. Sutherland, *Class field theory: ray class groups and ray class fields*, MIT 18.785, Lecture 21 (22 November 2021), [lecture notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes21.pdf), §21.3, Definitions 21.2–21.3 and Remark 21.5: moduli with a selected set of real places, ray class groups and the narrow case.
- **[Sutherland 26]** A. V. Sutherland, *The idele group, profinite groups, infinite Galois theory*, MIT 18.785, Lecture 26 (1 December 2021), [MIT OpenCourseWare notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/resources/mit18_785f21_lec26/), §26.1, p.2: the map from idèles to fractional ideals and the induced surjection of the idèle class group onto the ideal class group.
