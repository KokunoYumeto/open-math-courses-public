# General tail supports and controlled tunnels

We construct the larger-depth full corner inside an actual ordinary tunnel, compute both of its support traces, and retain the old physical operators after cutting. We then prove an exact criterion for replacing a whole-stage cell by a tail-supported cell through an actual corner tunnel. Exact retention of the entire selected finite block can fail at every finite length, even in an explicit amenable tensor inclusion. Controlled approximation in that same physical corner supplies a valid quantitative return. The unrestricted finite-partition theorem remains unproved by these constructions and is not refuted.

## The original finite-partition theorem

Popa4.4.1(1), printed p.222, assumes an amenable proper finite-index inclusion \(N\subsetneq M\) of II₁ factors. For every finite \(Y\subset M\) and \(\varepsilon>0\), it asserts unital finite-dimensional \(Q_*\subset P_*\subset M\), \(Q_*\subset N\), satisfying

\[
 E_{P_*}E_N=E_NE_{P_*}=E_{Q_*},\qquad
 \|y-E_{P_*}(y)\|_2<\varepsilon\quad(y\in Y),
 \tag{GTB.0}
\]

and a finite orthogonal partition \(\sum_i s_i=1\), with an individual actual whole-inclusion finite tunnel for every cell, such that

\[
\begin{gathered}
 s_i\in (N_{k_i}^{(i)})'\cap N,\\
 P_*=\bigoplus_i s_i((N_{k_i}^{(i)})'\cap M)s_i,\\
 Q_*=\bigoplus_i s_i((N_{k_i}^{(i)})'\cap N)s_i.
\end{gathered}
\tag{GTB.1}
\]

The source prints the first expectation order; its \(L^2\) adjoint gives the other. Orthogonality follows from the projection sum, as in [FP.0–FP.1](finite-residual-cells-and-canonical-overlap.md). No separability, finite depth, extremality, factorial core or unique norm trace is added. A common stage, retention of an arbitrary ordinary prefix and generation are separate obligations. The original residual must be covered by finitely many actual cells, not left as an arbitrary finite-dimensional summand.

Popa's §1.3.2 states the skipped basic construction; the complete finite representation proof is [14.1–14.2 and 14.8](reflected-traces-and-uniform-bounds.md). The preceding §4.4 argument selects supports in tail **factors**, compresses their tunnels and uses actual corner-tunnel uniqueness. Its unrestricted finite-partition statement does not identify the whole-stage supports of [76.2](whole-relative-commutant-blocks.md) with tail-factor supports. [OT.1](tail-supports-and-compressed-tunnel-depth.md) gives the finite completion once an actual tail-supported near-cover is available. We examine the missing change of support class.

## Earlier proofs used in this reading

| Proof scope | Earlier reading |
| --- | --- |
| 1.2, actual basic construction and strong generation | [The projection and basic construction](projection-and-basic-construction.md) |
| 2.1, 2.4 and 2.9, module restriction, two local traces and common compression | [Module dimension and local index](module-dimension-and-local-index.md) |
| 4.4–4.5, actual downward construction and finite marked uniqueness | [Towers and tunnels](towers-and-tunnels.md) |
| 14.1–14.2 and 14.8, finite reflected representations and skipped triples | [Reflected traces and uniform bounds](reflected-traces-and-uniform-bounds.md) |
| 53.1, both expectation orders | Bounded frames with central support |
| 57.3, finite marked tunnel alignment | [Actual supported local approximation](actual-supported-local-approximation.md) |
| 61.1–61.2, complete nondegenerate expected and smooth representation definitions | [Smooth representations and tower compression](smooth-representations-and-tower-compression.md) |
| 76.2–76.4, whole-stage near-covers and exact residual scope | [Whole relative-commutant blocks](whole-relative-commutant-blocks.md) |
| OT.1–OT.2, finite tail-family return and both whole-support traces | [Tail supports and compressed tunnel depth](tail-supports-and-compressed-tunnel-depth.md) |
| FP.0–FP.1, the original full finite-partition scope | [Finite residual cells and canonical overlap](finite-residual-cells-and-canonical-overlap.md) |
| HB2.1–HB2.3 and WT2.1–WT3.1, complete state extension and dual compactness | [Finite algebras and normal traces: supporting proofs](finite-algebras-and-normal-traces.md) |

## A full-corner identity, with its actual maps

**Lemma GTB.1 — common-corner comparison.** Let \(A\subset B\) be II₁ factors of finite index \(I\), and \(0\ne r\in A\) a projection. Common compression gives \([rBr:rAr]=I\). If \(A\subset B\subset B_1\subset\cdots\) is its canonical Jones tower, then \(rAr\subset rBr\subset rB_1r\subset\cdots\), with projections \(re_j\), is its canonical common-corner tower. On every higher relative commutant the map

\[
 A'\cap B_j\longrightarrow (rAr)'\cap rB_jr,
 \qquad x\longmapsto rxr=rx,
 \tag{GTB.2}
\]

is a normal unital trace-preserving *-isomorphism. It carries the actual Jones projections to their common compressions and commutes with the inherited expectations. The same assertion holds for rectangles of this tower when \(r\) belongs to their smaller factor.

**Proof.** Right compression of \(L^2(B)\) by \(r\) multiplies its left-\(B\) dimension by \(\tau(r)\). Restriction to \(A\) multiplies this by \(I\). Left algebra compression by \(r\in A\) divides by \(\tau(r)\), giving \(I\). These are the actual module maps and trace normalizations of2.1/2.9, so this argument does not equate two different relative-commutant traces.

For the commutant assertion, choose finitely many partial isometries \(v_a\in A\) with \(v_a^*v_a\le r\) and mutually orthogonal final projections summing to1. Such a finite cover follows from projection comparison in a finite factor: split1 into finitely many projections of trace at most \(\tau(r)\), then compare each with a subprojection of \(r\). If \(z\in(rAr)'\cap rB_jr\), define

\[
 \widetilde z=\sum_a v_a z v_a^*\in B_j.
 \tag{GTB.3}
\]

For \(a\in A\), each \(v_i^*av_j\in rAr\) commutes with \(z\); inserting the covering sum on both sides proves \(a\widetilde z=\widetilde z a\). Furthermore, using \(rv_a\in rAr\) and the same covering sum gives \(r\widetilde z r=z\). Conversely, any \(x\in A'\cap B_j\) obeys \(\sum_a v_a(rxr)v_a^*=x\). Thus(GTB.2) has the displayed inverse. It is a *-homomorphism because \(x\) commutes with \(r\); the constructions are normal. For positive \(x\) commuting with the factor \(A\), the normal functional \(a\mapsto\tau(ax)\) on \(A\) is tracial, so \(\tau(rx)=\tau(r)\tau(x)\). This proves the normalized corner-trace assertion.

Every Jones projection commutes with \(A\), hence with \(r\). Compressing \(e_jbe_j=E_{B_{j-1}}(b)e_j\) gives the corner identity, and the compressed expectation is \(b\mapsto rE_{B_{j-1}}(b)r\) on the corner, by bimodularity and trace pairing. The compressed projection has its original Jones weight: \(\tau(re_j)/\tau(r)=\tau(e_j)\). The spanning identity survives: insert the finite covering sum \(\sum_a v_av_a^*=1\) on both sides of each uncompressed middle-algebra multiple of \(e_j\), and move \(v_a\) past \(e_j\). This expresses the whole larger corner as the weak span of corner-middle multiples of \(re_j\). Basic-construction recognition now fixes all projections and expectations. Iteration proves the tower and rectangle assertions. \(\square\)

## The correct skipped full corner does not change the compressed local index

Fix an actual ordinary tunnel \(N=N_0\supset N_1\supset\cdots\), with \(d=[M:N]>1\). Write \(A_m=N_m'\cap M\), \(B_m=N_m'\cap N\). Take \(m\ge1\), \(F=N_m\), and a nonzero projection \(p\in B_m\). Let \(\rho_F\) denote the intrinsic left-\(F\) commutant dimension trace on \(L^2(N)\), normalized to total mass1. Put

\[
 t=\tau(p),\quad u=\rho_F(p),\quad
 \theta=tu,\quad I_p=d^m\theta=[pNp:Fp].
 \tag{GTB.4}
\]

The factor \(Fp\subset pNp\), its normalized trace, and the exact identities \((Fp)'\cap pMp=pA_mp\), \((Fp)'\cap pNp=pB_mp\), are established in [OT.2](tail-supports-and-compressed-tunnel-depth.md). The two numbers \(t,u\) are not silently identified. The trace \(T_F\) is the intrinsic faithful normal finite trace on \(F'\subset B(L^2(N))\), with \(T_F(1)=d^m\); \(\rho_F=T_F/d^m\) is its normalized trace. These traces are evaluated on the actual left support projection, not on an abstract matrix rank.

**Theorem GTB.2 — actual cup padding.** For \(h\ge1\), set \(S=N_{m+h}\), \(T=N_{m+2h}\). The actual skipped triple \(T\subset S\subset F\) has a Jones projection \(q_h\in F\) such that

\[
\begin{gathered}
 q_h\in T'\cap F,\quad
 q_h x q_h=E_T^S(x)q_h\quad(x\in S),\\
 E_S^F(q_h)=d^{-h}1,\quad
 \tau(q_h)=d^{-h},\quad q_hFq_h=Tq_h.
\end{gathered}
\tag{GTB.5}
\]

For the actual support \(r=pq_h\), all of the following hold:

\[
\begin{gathered}
 0\ne r\in T'\cap N,\quad r\le p,\quad
 \tau(r)=td^{-h},\\
 \rho_T(r)=ud^{-h},\quad
 \tau(r)\rho_T(r)=\theta d^{-2h},\\
 r(Fp)r=Tr,\quad
 [rNr:Tr]=I_p,\quad [rMr:rNr]=d,\\
 rA_mr\subset r(T'\cap M)r,\quad
 rB_mr\subset r(T'\cap N)r.
\end{gathered}
\tag{GTB.6}
\]

Both the standard invariant of \(Fp\subset pNp\), with index \(I_p\), and that of the physical inclusion \(pNp\subset pMp\), with index \(d\), are preserved by their respective common-corner maps. These are two different towers; neither is being identified with the other, even when their index values happen to agree.

**Proof.** The finite proof of14.8 uses the tracial standard representation at the middle level \(S\). Its coherently identified larger level is \((J_STJ_S)'\), the basic construction of \(T\subset S\), by1.2. Lemma14.1 and the repeated finite identifications14.2 match the marked ordinary Jones triples of the given tunnel with this representation. They preserve the factor traces and actual marked projections, rather than merely the index. This supplies the actual skipped projection \(q_h\), its compression identity, its middle expectation and the spanning identity \(F=\overline{Sq_hS}^{\,w}\). Compressing that span and using \(q_hSq_h=Tq_h\) proves the last equality in(GTB.5). This finite argument uses no finite-depth/trace-uniqueness part of14.3–14.7 and no assertion about an infinite representation. For \(h=1\), \(q_h\) is the specified ordinary marked cup at this triple.

Since \(p\) commutes with all of \(F\), \(r=pq_h\) is a projection and commutes with \(T\). The functional \(x\mapsto\tau(px)\) is normal tracial on the factor \(F\); hence \(\tau(px)=t\tau(x)\). This gives \(\tau(r)=td^{-h}>0\). The map \(F\to Fp\), \(x\mapsto xp\), is an actual faithful normal trace-preserving factor isomorphism, so

\[
 r(Fp)r=pq_hFq_hp=T(pq_h)=Tr.
 \tag{GTB.7}
\]

Here \(r\in Fp\). Apply GTB.1 to \(Fp\subset pNp\): its common corner is exactly \(Tr\subset rNr\), with index \(I_p\), and with the marked tower/trace identifications proved there. Also apply GTB.1 to \(pNp\subset pMp\), using \(r\in pNp\), to retain its physical index \(d\) and its own marked tower.

The larger inclusion \(T\subset N\) has index \(d^{m+2h}\). Local formula2.4 at its actual relative-commutant projection \(r\) therefore reads

\[
 d^{m+2h}\tau(r)\rho_T(r)
 =[rNr:Tr]=d^mtu.
 \tag{GTB.8}
\]

Substitution of \(\tau(r)=td^{-h}\) and cancellation of the strictly positive \(t\) prove \(\rho_T(r)=ud^{-h}\). Thus the second support trace is computed through the proved actual corner construction, not guessed by a tensor model or an assumed extremality. Finally \(A_m\subset T'\cap M\), \(B_m\subset T'\cap N\), and \(r\) commutes with \(pA_mp\). This proves the physical operator inclusions in(GTB.6). \(\square\)

If \(p\) is proper, OT.2 gives \(\theta<1\). For the padded smaller factor \(Tr\) to be a terminal factor at length \(k\ge0\) in an actual tunnel of \(rNr\subset rMr\), it is necessary that

\[
 I_p=d^k,
 \qquad\theta=d^{-(m-k)}.
 \tag{GTB.9}
\]

This condition is independent of \(h\). In the padded whole stage the support product becomes \(\theta d^{-2h}\), while its level becomes \(m+2h\); the two changes cancel in the compressed index. A larger-depth full-corner cup does not repair a failed resonance. If(GTB.9) holds, it is still insufficient: the actual corner chain and its marked Jones identities remain necessary. Nothing here infers such a chain from equality of two numerical traces.

## Arbitrarily small physical mass loss is possible, but the support class stays whole-stage

**Corollary GTB.3 — actual finite orthogonal refinement.** For one \(p\) as above, let \(L=\lfloor d^h\rfloor\). Inside the factor \(F\), choose mutually orthogonal projections \(q_1,\ldots,q_L\) of trace \(d^{-h}\). Each is unitarily conjugate in \(F\) to the actual \(q_h\). Conjugate the continuation separately for each \(q_a\), fixing the older prefix, and put \(r_a=pq_a\). These are actual whole-stage cells with individual continuations, and

\[
\begin{gathered}
 \sum_{a=1}^Lr_a\le p,\qquad
 0\le\tau\left(p-\sum_a r_a\right)<td^{-h},\\
 [r_aNr_a:T_a r_a]=I_p,\qquad
 r_aA_mr_a\subset r_a(T_a'\cap M)r_a.
\end{gathered}
\tag{GTB.10}
\]

If \(d^h\) is an integer, this refinement covers \(p\) exactly. This assertion covers an already realized whole cell, not the original arbitrary residual.

**Proof.** Prescribe the projections successively in \(F\), using \(Ld^{-h}\le1\), and use finite-factor unitary comparison. If \(q_a=v_aq_hv_a^*\), \(v_a\in\mathcal U(F)\), rotate all future factors and cups by this specified unitary. It fixes \(p\), \(A_m\), \(B_m\) and the older tunnel factors, since \(p,A_m,B_m\) commute with \(F\) and \(v_a\) belongs to those older factors. The new terminal factor is \(T_a=v_aTv_a^*\). GTB.2 applies literally to it and \(q_a\); orthogonality is physical because the \(q_a\) commute with \(p\). The residual trace is \(t(1-Ld^{-h})<td^{-h}\). Its vanishing in the integer case gives exact coverage by faithfulness. \(\square\)

For a finite old family \(p_i\), these refinements may discard total additional trace less than any prescribed \(\kappa>0\), by selecting finite \(h_i\) with \(\sum_i\tau(p_i)d^{-h_i}<\kappa\). If its old finite algebra has residual \(fA_0\), \(A_0=N'\cap M\), let \(b_y=E_{P_0}(y)\), \(R=\max(\{1\}\cup\{\|y\|:y\in Y\})\). All \(r_{ia}\) commute with \(b_y\). The retained candidate \(c_y=\sum_{i,a}r_{ia}b_yr_{ia}\) lies in the enlarged full supported relative-commutant cells, and

\[
 \|y-c_y\|_2
 \le\|y-E_{P_0}(y)\|_2
       +R\sqrt{\tau(f)+\kappa}.
 \tag{GTB.11}
\]

Indeed the difference from \(b_y\) is exactly \(f'b_yf'\), with \(\tau(f')<\tau(f)+\kappa\). Both expectation orders hold for the refined square with its displayed residual summand, by53.1 and trace pairing. Its supported \(A_0\) pieces reconstruct \(A_0\). This is a proved fixed-operator estimate with actual finite cells, but \(f'\) has not acquired a full finite origin. Nor have the new good cells acquired tail-factor membership. Thus(GTB.11) does not settle(GTB.0)–(GTB.1).

## The exact finite operator/tower criterion for a tail reclassification

For a physical projection \(0\ne p\in N\), let \(G\subset pMp\) be finite dimensional with unit \(p\), and set \(C_G=G'\cap pNp\). No factoriality of \(C_G\) is inferred.

**Theorem GTB.4 — exact tail-retention equivalence at a finite length.** For an integer \(k\ge0\), the following two actual constructions are equivalent:

1. An ordinary finite whole tunnel \(M\supset N\supset T_1\supset\cdots\supset T_k\), with \(p\in T_k\) and \(G\subset p(T_k'\cap M)p\).
2. An actual finite corner tunnel \(pMp\supset pNp\supset S_1\supset\cdots\supset S_k\), with every ordinary Jones projection, expectation and generation identity, such that \(S_k\subset C_G\).

At \(k=0\), these mean \(G\subset pA_0p\). In direction2→1 the lifted supported algebra contains the **same physical operators** of \(G\). Equal indices or an abstract isomorphism of standard invariants alone are not the input in2.

**Proof.** For1→2, compress the actual whole chain by its common smaller-factor projection \(p\in T_k\). GTB.1 proves all the corner Jones identities and gives

\[
 (pT_kp)'\cap pMp=p(T_k'\cap M)p.
 \tag{GTB.12}
\]

Thus \(S_j=pT_jp\) is the required actual chain and commutes with \(G\).

For2→1 with \(k\ge1\), choose any ordinary whole tunnel to length \(k\). Its terminal factor is II₁, so prescribe a projection there of trace \(\tau(p)\). A unitary in \(N\) sends that projection to the physical \(p\); conjugating this reference tunnel makes \(p\) belong to every factor of the finite chain. GTB.1 compresses it to an actual corner tunnel of the **fixed** physical inclusion \(pNp\subset pMp\).

The finite uniqueness4.5, iterated as in57.3, supplies one unitary \(w\in\mathcal U(pNp)\) aligning that compressed chain with the specified chain in2, including its marked Jones projections. This is a comparison of two already constructed actual tunnels of the same physical inclusion, not a comparison inferred from their index. Extend \(w\) to \(w+(1-p)\in\mathcal U(N)\) and conjugate the reference whole tunnel. Denote its terminal factor by \(T_k\). It still contains \(p\), and satisfies \(pT_kp=S_k\) exactly. Apply(GTB.12), proved by the explicit common-corner map, to conclude

\[
 G\subset S_k'\cap pMp=p(T_k'\cap M)p.
 \tag{GTB.13}
\]

The comparison is the identity on the physical operators in(GTB.13): the tunnel was changed and the candidates were kept fixed. The placement unitary need not be close to1. The case \(k=0\) is immediate. \(\square\)

**Corollary GTB.5 — one concrete sufficient missing input.** Suppose the actual finite nonempty near-cover of76.4 at zero prefix has \(\tau(f)<\varepsilon^2/(16R^2)\), and has its displayed residual \(fA_0\) and candidates \(b_y\in P_0\) with \(\|y-b_y\|_2<\varepsilon/2\), \(\|b_y\|\le R\). For each good cell \(p_i\), let \(G_i\) be the finite algebra with unit \(p_i\) generated by its blocks \(p_ib_yp_i\) and their adjoints. If actual corner tunnels as in GTB.4(2) are supplied in every \(C_{G_i}\), then the original full finite conclusion(GTB.0)–(GTB.1) follows.

**Proof.** Lift each of these finitely many chains by GTB.4. The physical supports \(p_i\) now belong to individual actual tail factors. Their full supported relative-commutant algebras contain all the retained blocks \(p_ib_yp_i\), while the residual \(fA_0\) retains \(fb_yf\). Thus the new tail-supported square has the same candidates \(b_y\), so its expectation errors are below \(\varepsilon/2\). Its \(A_0\) is retained: every \(p_iA_0p_i\) commutes with \(p_iNp_i\), and hence belongs to the lifted supported algebra by(GTB.12); \(A_0\) commutes with all physical support projections. The inherited expectation onto \(N\) maps each good algebra \(p_i(T_i'\cap M)p_i\) onto \(p_i(T_i'\cap N)p_i\), by bimodularity and finite-stage trace pairing; it maps \(fA_0\) onto \(\mathbb Cf\). Taking \(L^2\) adjoints proves the other order. This checks the entire actual tail-family input of [OT.1](tail-supports-and-compressed-tunnel-depth.md). Apply that established construction, with its unchanged strict error constants, to cut only controlled physical mass, place its finite cup-certified residual, and obtain the exact finite full partition. The physical \(y\) have never been conjugated. \(\square\)

A sufficient stronger version of this input would give the actual corner chains inside \(N_{m_i}^{(i)}p_i\), since that factor commutes with the whole old supported algebra. GTB.2 shows that simply padding that factor by skipped cups does not furnish such a chain: it preserves its actual local index \(I_{p_i}\). More generally GTB.4 allows another actual terminal factor inside \(C_{G_i}\), and therefore does not declare the numerical resonance necessary for every conceivable construction of the original theorem.

## A genuine Jones calculation where padding preserves a nonresonant index

This example tests the proposed padding mechanism, not the unrestricted theorem. Let \(\mathcal R\) be any II₁ factor, take \(n=3\), and label four matrix legs \(a,b,c,e\). Set

\[
\begin{gathered}
 M=\operatorname{Mat}_3^{(a)}\bar\otimes
   \operatorname{Mat}_3^{(b)}\bar\otimes
   \operatorname{Mat}_3^{(c)}\bar\otimes
   \operatorname{Mat}_3^{(e)}\bar\otimes\mathcal R,\\
 N=1_a\bar\otimes\operatorname{Mat}_3^{(b)}\bar\otimes
   \operatorname{Mat}_3^{(c)}\bar\otimes
   \operatorname{Mat}_3^{(e)}\bar\otimes\mathcal R,\\
 F=N_1=1_a\bar\otimes1_b\bar\otimes
   \operatorname{Mat}_3^{(c)}\bar\otimes
   \operatorname{Mat}_3^{(e)}\bar\otimes\mathcal R,\\
 S=N_2=1_a\bar\otimes1_b\bar\otimes1_c\bar\otimes
   \operatorname{Mat}_3^{(e)}\bar\otimes\mathcal R,
 \qquad T=N_3=\mathcal R.
\end{gathered}
\tag{GTB.14}
\]

For each adjacent pair of legs define its actual marked cup

\[
 e_{uv}=\frac13\sum_{i,j=1}^3E_{ij}^{(u)}\otimes E_{ij}^{(v)}.
 \tag{GTB.15}
\]

Each is the rank-one Bell projection. Matrix multiplication gives \(e_{uv}^2=e_{uv}=e_{uv}^*\), middle expectation \(1/9\), and the Jones compression identity. For the generic triple \(\mathcal R\subset\operatorname{Mat}_3\otimes\mathcal R\subset\operatorname{Mat}_3\otimes\operatorname{Mat}_3\otimes\mathcal R\), the spanning identity is

\[
 3(E_{ui}\otimes1)e(E_{jv}\otimes1)
 =E_{uv}\otimes E_{ij}.
 \tag{GTB.16}
\]

Thus the three consecutive triples in(GTB.14), with cups \(e_{ab},e_{bc},e_{ce}\), are actual basic constructions, with \(d=9\). This supplies their marked projections, expectations and generation; it is not a numerical index assignment.

Take \(p=(E_{11}^{(b)}+E_{22}^{(b)})\otimes1\in F'\cap N\), \(q=e_{ce}\in F\), and \(r=pq\). The actual supported factors are

\[
\begin{gathered}
 pNp\cong\operatorname{Mat}_2\bar\otimes F,
 \qquad Fp\cong F,\qquad [pNp:Fp]=4,\\
 rNr\cong\operatorname{Mat}_2\bar\otimes\mathcal R,
 \qquad Tr\cong\mathcal R,\qquad [rNr:Tr]=4,\\
 rMr\cong\operatorname{Mat}_3\bar\otimes
                  \operatorname{Mat}_2\bar\otimes\mathcal R,
 \qquad [rMr:rNr]=9.
\end{gathered}
\tag{GTB.17}
\]

The indices4 and9 can also be checked by restricting the standard modules: \(L^2(\operatorname{Mat}_2)\) has dimension4 over its scalar base, and the removed \(\operatorname{Mat}_3\) leg contributes9. On the original standard \(F\)-module, left \(p\) has normalized rank \(2/3\), so \(\tau(p)=\rho_F(p)=2/3\). On the standard \(T\)-module, left \(r\) has normalized rank \(2/27\), so \(\tau(r)=\rho_T(r)=2/27\). Consequently

\[
 9\cdot\frac49=4,
 \qquad 9^3\cdot\frac4{729}=4.
 \tag{GTB.18}
\]

The old physical supported pair is retained **exactly**:

\[
 rA_1r=rA_3r\cong\operatorname{Mat}_3\otimes\operatorname{Mat}_2,
 \qquad rB_1r=rB_3r\cong\operatorname{Mat}_2.
 \tag{GTB.19}
\]

These equalities follow from the rank-one \(ce\)-corner, not a conjectural transfer. Yet4 is not \(9^k\) for any integer \(k\ge0\) (the value is1 at \(k=0\), and at least9 thereafter), so neither \(Fp\) nor \(Tr\) can be the stipulated terminal factor of an actual ordinary tunnel of its physical corner inclusion. They are nevertheless perfectly valid whole-stage cells of the displayed original tunnel. This is an actual example of the failure of that **particular tail reclassification**, not a Jones counterexample to(GTB.0)–(GTB.1), not a claim that every possible \(S_k\subset C_G\) fails, and not an extra general amenability assumption.

## Exact retention can fail at every finite depth in the same Jones example

**Theorem GTB.6 — the finite matrix divisibility obstruction.** In the actual example (GTB.14)–(GTB.19), choose \(\mathcal R\) to be the tracial von Neumann closure of \(\bigotimes_{j\ge1}\operatorname{Mat}_3\). Retain the same rank-two projection \(p\), and let

\[
\begin{gathered}
 D=pNp=\operatorname{Mat}_2\bar\otimes F,\\
 C=pMp=\operatorname{Mat}_3\bar\otimes D,\\
 G=pA_1p=\operatorname{Mat}_3\otimes\operatorname{Mat}_2\otimes1_F,
 \qquad [C:D]=9.
\end{gathered}
\tag{GTB.20}
\]

There is no actual finite tunnel of \(D\subset C\), of any length \(j\ge0\), whose terminal factor commutes with all of the same physical \(G\). Equivalently, GTB.4's exact input fails for this \(p,G\) at every finite length. This strengthens the analysis of the **same** marked Jones example; it is not a second counterexample, nor a refutation of the original global approximation theorem.

**Proof.** The finite tensor expectations of \(\mathcal R\) converge in \(L^2\). A central element has scalar expectation at every finite tensor stage, hence is scalar. The unbounded matrix sizes exclude a finite-dimensional factor. Thus \(\mathcal R\) is an actual II₁ factor. Removing its first tensor leg identifies it as \(\operatorname{Mat}_3\bar\otimes\mathcal R_1\), with the product trace and an explicitly specified remaining tail. The same holds after any finite number of legs. No abstract isomorphism is used to move a fixed target.

For the fixed corner inclusion \(D\subset C\), choose the reference downward tunnel by successively removing the actual \(\operatorname{Mat}_3\) legs of \(F=\operatorname{Mat}_3^{(c)}\bar\otimes\operatorname{Mat}_3^{(e)}\bar\otimes\mathcal R\), leaving the \(\operatorname{Mat}_2\) leg in its terminal factor. The Bell cups (GTB.15), at each successive pair of removed legs, satisfy compression, scalar expectation and generation by (GTB.16). Hence this is an actual marked tunnel of index nine. If \(D_j\) is its terminal factor at length \(j\), its smaller relative commutant is

\[
 D_j'\cap D\cong\operatorname{Mat}_{3^j},\qquad j\ge0,
\tag{GTB.21}
\]

with the normalized matrix trace. The identification sends matrix units to the actual first \(j\) removed legs; it is a unital trace-preserving *-isomorphism. Here \(\operatorname{Mat}_{3^0}=\mathbb C\).

Every other actual tunnel of this fixed physical inclusion through length \(j\) is carried to this reference tunnel by a unitary in \(D\), by the complete finite uniqueness proof 4.5/57.3. Taking commutants transfers (GTB.21) to its terminal factor \(S_j\). If \(G\subset S_j'\cap C\), then its physical unital \(\operatorname{Mat}_2\subset D\) is contained in \(S_j'\cap D\). This would give a unital *-embedding

\[
 \operatorname{Mat}_2\longrightarrow\operatorname{Mat}_{3^j}.
\tag{GTB.22}
\]

The images of the two diagonal matrix units are orthogonal equal-rank projections summing to the identity: their ranks agree because the off-diagonal matrix unit is a partial isometry between them. Therefore \(3^j\) would be even. It is odd for every \(j\), a contradiction. The argument covers \(j=0\) too.

The tensor-strip core has a compatible relative hypertrace, but that one-core calculation alone does not prove Popa's full amenability hypothesis, which quantifies every smooth representation. The full hypothesis for this example is established by the explicit smooth-representation construction below. The obstruction refutes only the additional universal exact-retention input for arbitrary already selected whole cells, and does not refute the original global theorem. \(\square\)

## Full amenability of this explicit tensor model

**Lemma GTB.6a — every smooth representation has the required hypertrace.** Let \(D\) be a II₁ factor with an increasing sequence of unital finite matrix factors \(F_l\) whose union is \(L^2\)-dense. Let \(C=\operatorname{Mat}_n\bar\otimes D\), \(n\ge2\), with its normalized product trace and smaller inclusion \(D=1_n\otimes D\). Then \(D\subset C\) satisfies **full** amenability as defined in Popa3.1.1, not only amenability relative to its tensor-strip core.

**Proof.** Fix an arbitrary smooth representation \(\mathcal A\subset\mathcal B\) of this physical inclusion, with conditional expectation \(\mathscr E:\mathcal B\to\mathcal A\). Thus \(D\subset\mathcal A\), \(C\subset\mathcal B\), \(\mathscr E|_C=E_D\), the weak span of \(C\mathcal A\) equals \(\mathcal B\), and smoothness at the first level gives

\[
 C\cap D'=\operatorname{Mat}_n\otimes1
 \subset\mathcal A'\cap\mathcal B.
\tag{GTB.32}
\]

The higher smoothness conditions need not be weakened or omitted: they are assumed, while these first-level consequences already suffice for the construction. Denote the actual matrix units of this commuting \(\operatorname{Mat}_n\) by \(e_{uv}\).

The multiplication map

\[
 \Xi:\operatorname{Mat}_n\bar\otimes\mathcal A\longrightarrow\mathcal B,
 \qquad [a_{uv}]\longmapsto\sum_{u,v}e_{uv}a_{uv}
\tag{GTB.33}
\]

is a normal unital *-isomorphism. Here finite matrices over \(\mathcal A\) use their ordinary von Neumann matrix-algebra topology. Products and adjoints are preserved because the matrix units commute with \(\mathcal A\). Its actual inverse coefficients are

\[
 a_{uv}(T)=\sum_{k=1}^n e_{ku}T e_{vk},\qquad T\in\mathcal B.
\tag{GTB.34}
\]

For \(T=\sum e_{rs}a_{rs}\), matrix multiplication proves that (GTB.34) recovers exactly \(a_{uv}\). The coefficient maps are ultraweakly continuous. Since \(C\mathcal A=\operatorname{Mat}_n\mathcal A\) has weakly dense span, the coefficients lie in the ultraweakly closed \(\mathcal A\) for every \(T\in\mathcal B\); the finite recombination identity then passes to that weak closure. This proves surjectivity, injectivity and normality of both maps without an abstract invariant identification. Bimodularity and \(\mathscr E(e_{uv})=\delta_{uv}1/n\) give the actual expectation

\[
 \mathscr E\Xi([a_{uv}])=\frac1n\sum_u a_{uu}.
\tag{GTB.35}
\]

Construct a \(D\)-central state \(\psi\) on the arbitrary \(\mathcal A\). First extend \(\tau_D\) to a state \(\psi_0\) on \(\mathcal A\). Explicitly extend its norm-one real functional on \(D_{\rm sa}\) to \(\mathcal A_{\rm sa}\) by Hahn–Banach, keeping value one at the identity. For \(0\le x\le1\), the extension's value is \(1-\psi_0(1-x)\ge0\), since \(\|1-x\|\le1\). Scaling gives positivity, and complexification gives a unital positive linear state. Positivity's elementary Cauchy–Schwarz inequality proves boundedness and norm one.

Write \(F_l=\operatorname{Mat}_{m_l}\). In its actual matrix units choose the clock and cyclic shift unitaries \(U_l,V_l\), with \(U_lV_l=\zeta_lV_lU_l\), \(\zeta_l=\exp(2\pi i/m_l)\). Define states

\[
 \psi_l(T)=\frac1{m_l^2}\sum_{r,s=0}^{m_l-1}
 \psi_0\bigl(U_l^rV_l^s T V_l^{-s}U_l^{-r}\bigr),
 \qquad T\in\mathcal A.
\tag{GTB.36}
\]

The sum is finite. Conjugation by \(U_l\) or \(V_l\) permutes its terms, with scalar phases cancelling. Hence \(\psi_l\) is invariant under those conjugations, and central for their powers and products. The \(m_l^2\) Weyl matrices span \(F_l\): diagonal clock powers separate the diagonal coordinates by the finite Fourier sum, and shift powers then give every off-diagonal matrix unit. Thus \(\psi_l(xT)=\psi_l(Tx)\) for all \(x\in F_l\). Also \(\psi_l|_D=\tau_D\), because \(\tau_D\) is invariant under these unitaries.

The state extension uses the full Hahn–Banach proofs HB2.1–HB2.3. Compactness uses the complete ultrafilter/Tychonoff and Banach–Alaoglu arguments WT2.1–WT3.1. The earlier [finite-algebra reading](finite-algebras-and-normal-traces.md) identifies these programme prerequisites and their full proofs. The states lie in the weak-star compact state space in \(\mathcal A^*\), by Banach–Alaoglu and closed positivity/unitality. Take a cluster subnet of the sequence, with indices tending to infinity. Its state \(\psi\) restricts to \(\tau_D\) and is central for every \(F_l\). For arbitrary \(x\in D\), put \(x_l=E_{F_l}^D(x)\). Increasing orthogonal expectation ranges give \(\|x-x_l\|_{2,\tau_D}\to0\). Cauchy–Schwarz for this possibly nonnormal state, using its **exact** restriction to \(D\), gives

\[
\begin{gathered}
 |\psi(xT)-\psi(Tx)|\le
 2\|T\|\|x-x_l\|_{2,\tau_D}\longrightarrow0,
 \qquad T\in\mathcal A.
\end{gathered}
\tag{GTB.37}
\]

Indeed bound each term involving \(x-x_l\) by \(\|T\|\|x-x_l\|_2\); traciality of \(\psi|_D\) equates the two possible squared trace norms. This extends centrality to all of \(D\), without passing an ultraweak limit through \(\psi\) or asserting its normality.

Finally define a state on the original smooth representation by

\[
 \varphi\bigl(\Xi([a_{uv}])\bigr)=\frac1n\sum_u\psi(a_{uu}).
\tag{GTB.38}
\]

A positive matrix has positive diagonal entries, so the formula is positive and unital. It restricts to \(\tau_C\). For \(x\in D\), matrix multiplication and \(\psi(xa)=\psi(ax)\) prove
\(\varphi((e_{uv}x)T)=\varphi(T(e_{uv}x))\). Every element of the physical \(C\) is a finite sum of these matrix entries, so \(\varphi\) is \(C\)-central. Equation (GTB.35) gives \(\varphi\mathscr E=\varphi\) on every \(T\in\mathcal B\). This is the required compatible hypertrace for the **arbitrary** smooth representation. Therefore the full definition holds.

For (GTB.14), \(N\) has the concrete increasing matrix factors \(\operatorname{Mat}_{3^{l+3}}\). Its rank-two corner \(D=pNp=\operatorname{Mat}_2\bar\otimes F\) has \(F_l=\operatorname{Mat}_{2\cdot3^{l+2}}\). Apply this proof directly, with \(n=3\), to both physical inclusions. The exact all-depth rank obstruction of GTB.6 thus satisfies the original full amenability hypothesis. \(\square\)

Compatibility in one generating core does not by itself establish full amenability. Equations (GTB.32)–(GTB.38) give the universal representation argument. No converse from one-core amenability in Popa's Theorem4.1.1 is used.

## A controlled approximation in that actual corner

**Lemma GTB.7 — odd matrix stages can approximate the retained block.** Keep the fixed inclusion (GTB.20) and its normalized corner trace \(\tau_D\). For every \(j\ge1\), put \(L=3^j\), \(q=(L-1)/2\). There is an actual finite tunnel of \(D\subset C\) whose full stage pair \(Q_j\subset P_j\) has

\[
\begin{gathered}
 Q_j\cong\operatorname{Mat}_L,\qquad
 P_j=\operatorname{Mat}_3\otimes Q_j,\\
 E_D E_{P_j}=E_{P_j}E_D=E_{Q_j},\\
 \operatorname{dist}_{2,\tau_C}
 (E_{uv}^{(a)}\otimes E_{ab}^{(b)},P_j)
 \le (6L)^{-1/2}
\end{gathered}
\tag{GTB.23}
\]

for every \(1\le u,v\le3\), \(1\le a,b\le2\), with the identity on all unlisted factors. The physical targets remain fixed. No exact embedding (GTB.22) is asserted.

**Proof.** In the diffuse factor \(F\), choose \(z\) of trace \(1-1/L\). Split it into \(q\) equivalent projections of trace \(2/L\), and complete matrix units \((h_{rs})\) with unit \(z\). Then
\(E_{ab}^{(b)}\otimes h_{rs}\), indexed by \((a,r),(b,s)\), are actual \(L-1\) matrix units in \(D\), each diagonal of normalized trace \(1/L\), with sum \(1_2\otimes z\). The residual \(t=1_2\otimes(1-z)\) also has trace \(1/L\). Factor comparison supplies partial isometries connecting it to these diagonal projections. Explicitly, label them \(f_1,\ldots,f_{L-1}\), choose \(v_1=f_1\), \(v_i^*v_i=f_1,v_iv_i^*=f_i\) realizing the existing units, and choose \(v_L^*v_L=f_1,v_Lv_L^*=t\). The units \(v_iv_l^*\) extend the existing units and generate a unital \(Q_j\cong\operatorname{Mat}_L\) in the **same physical** \(D\).

The candidates \(E_{ab}^{(b)}\otimes z=\sum_{r=1}^q E_{ab}^{(b)}\otimes h_{rr}\) belong to \(Q_j\). Their differences from the fixed \(E_{ab}^{(b)}\otimes1\) have squared \(D\)-norm

\[
 \tau_D\bigl((E_{ab}\otimes(1-z))^*
                    (E_{ab}\otimes(1-z))\bigr)=\frac1{2L}.
\tag{GTB.24}
\]

The physical \(\operatorname{Mat}_3\) matrix unit has squared norm \(1/3\), giving (GTB.23)'s \(1/(6L)\). In the original inherited \(M\)-norm the squared error is \(\tau(p)/(6L)=1/(9L)\), because \(\tau(p)=2/3\).

Both \(Q_j\) and the reference smaller stage of (GTB.21) are unital matrix factors of size \(L\) in \(D\). An actual unitary in \(D\) sends the reference matrix units to those just constructed: compare their first diagonal projections, use a partial isometry between them, and sum the resulting matrix-unit transports over their \(L\) diagonal supports. Conjugate the **reference tunnel**, including its Bell cups, by this unitary. Its full smaller stage becomes \(Q_j\). Its full larger stage is exactly \(\operatorname{Mat}_3\otimes Q_j\), since the unitary belongs to \(D\) and commutes with the physical first matrix leg. This proves actual tunnel origin, not merely an abstract matrix-algebra fit. The inherited expectation onto \(D\) removes that first leg and maps \(P_j\) onto \(Q_j\); trace pairing and adjoints give both displayed orders.

This realizes a controlled return for this explicit amenable corner. The whole-corner lifting of GTB.4 applies to these **approximating candidates**, not to all of the exact \(G\). It gives a tail-supported near-cover when combined with the other selected cells and their error budgets. No universal construction for a general centered standard invariant follows from this tensor calculation. \(\square\)

## Quantitative return to the original full partition

**Proposition GTB.8 — approximate corner-chain input is sufficient.** Take an actual finite nonempty near-cover supplied by 76.4 at zero prefix. Such a nonempty finite selection can always be taken from its nonempty maximal orthogonal family. When the target set is empty, adjoin the target1 for the construction; its conclusion also answers the original empty target request. Write its orthogonal good supports as \(p_i\), residual as \(f=1-\sum_i p_i\), and its norm-contracting candidates as \(b_y=E_{P_0}(y)\), \(y\in Y\). Put \(R=\max(\{1\}\cup\{\|y\|:y\in Y\})\). Suppose

\[
 \tau(f)<\frac{\varepsilon^2}{16R^2},\qquad
 \max_{y\in Y}\|y-b_y\|_2<\varepsilon_0.
\tag{GTB.25}
\]

For each good support, suppose an **actual** finite tunnel of the fixed corner inclusion \(p_iNp_i\subset p_iMp_i\) is constructed, with terminal factor \(S_i\). Let

\[
 \mathcal P_i=S_i'\cap p_iMp_i,\qquad
 \mathcal Q_i=S_i'\cap p_iNp_i.
\tag{GTB.26}
\]

The corner expectations have these finite-dimensional ranges. Assume actual physical error bounds

\[
\begin{gathered}
 \|p_i b_yp_i-E_{\mathcal P_i}(p_i b_yp_i)\|_2
 \le\delta_i(y),\\
 \varepsilon_0+
 \max_{y\in Y}\Bigl(\sum_i\delta_i(y)^2\Bigr)^{1/2}
 <\varepsilon/2.
\end{gathered}
\tag{GTB.27}
\]

Then the original finite full conclusion (GTB.0)–(GTB.1) follows. The norms in (GTB.25)–(GTB.27) are the inherited physical \(M\)-norms, not normalized corner norms. A normalized corner bound \(\eta_i(y)\) gives \(\delta_i(y)=\sqrt{\tau(p_i)}\eta_i(y)\).

**Proof.** Each \(\mathcal P_i\) commutes with its actual terminal factor \(S_i\). Use GTB.4 with \(G=\mathcal P_i\): it lifts this already constructed corner tunnel to a whole tunnel retaining the physical \(p_i\) in its terminal factor \(T_i\). The explicit common-corner comparison gives equalities of the **same** finite algebras

\[
 \mathcal P_i=p_i(T_i'\cap M)p_i,\qquad
 \mathcal Q_i=p_i(T_i'\cap N)p_i.
\tag{GTB.28}
\]

The equality follows from \(p_iT_ip_i=S_i\) and GTB.1's typed commutant map; no trace-product or abstract invariant fit is used in place of the actual chain.

Define the tail-family algebras and candidates

\[
\begin{gathered}
 P'=\bigoplus_i\mathcal P_i\ \oplus\ fA_0,\\
 Q'=\bigoplus_i\mathcal Q_i\ \oplus\mathbb Cf,\\
 c_y=\sum_iE_{\mathcal P_i}(p_i b_yp_i)+fb_yf.
\end{gathered}
\tag{GTB.29}
\]

Omit a zero residual summand. The supports remain the original orthogonal physical projections, and the candidates have norm at most \(R\) by positivity and unitality in each block. On \(p_iMp_i\), the normalized corner expectation onto \(p_iNp_i\) is \(x\mapsto p_iE_N(x)p_i\). Its bimodularity over \(S_i\) makes its image on \(\mathcal P_i\) exactly \(\mathcal Q_i\). Multiplying normalized corner traces by \(\tau(p_i)\) identifies these expectations with the inherited-trace block restrictions. The residual expectation maps \(fA_0\) onto \(\mathbb Cf\). Trace pairing and self-adjointness of the \(L^2\) projections therefore give

\[
 E_NE_{P'}=E_{P'}E_N=E_{Q'}.
\tag{GTB.30}
\]

Every physical \(p_iA_0p_i\) commutes with all of \(p_iNp_i\), hence with \(S_i\), and belongs to \(\mathcal P_i\). Since \(A_0\) commutes with all the projections in \(N\), the good pieces and \(fA_0\) sum to each element of \(A_0\). Thus \(A_0\subset P'\), as required by OT.1.

The old \(b_y\) is block diagonal for these same supports. Its residual block is unchanged. Orthogonality of the good block differences proves

\[
\begin{gathered}
 \|b_y-c_y\|_2^2
 =\sum_i\|p_i b_yp_i-E_{\mathcal P_i}(p_i b_yp_i)\|_2^2,\\
 \|y-c_y\|_2
 \le\|y-b_y\|_2+\Bigl(\sum_i\delta_i(y)^2\Bigr)^{1/2}
 <\varepsilon/2.
\end{gathered}
\tag{GTB.31}
\]

The first identity concerns only mutually orthogonal block supports. It does not incorrectly assert that the old expectation error is orthogonal to the new finite algebras. Best approximation bounds the new expectation error by the candidate error. Equations (GTB.25), (GTB.28)–(GTB.31) supply every actual tail-family hypothesis of [OT.1](tail-supports-and-compressed-tunnel-depth.md). Apply its already proved finite cup-budget cutting and residual placement to obtain an exact finite whole-cell partition of one with both expectation orders and strict final target error. The physical \(y\) were kept fixed throughout. \(\square\)

GTB.6 refutes the universal **exact** version of the input for arbitrary selected blocks. GTB.7 verifies the **approximate** version in one explicit amenable tensor model. Deriving (GTB.26)–(GTB.27) from unrestricted amenability for the general selected near-cover, or selecting another construction that proves (GTB.0)–(GTB.1), remains substantive unfinished mathematics. The sufficient input is not substituted for the original theorem.

## Two checks with complete solutions

**Exercise GTB.1 — padding and physical error.** Suppose actual whole-stage cells have \(d=9\), \(\tau(p_1)=2/3\), \(\tau(p_2)=1/3-1/10000\), residual trace \(1/10000\), and old target error below \(1/20\) for targets of norm at most two. Refine both cells by GTB.3 using \(h=3\). Determine the extra discarded mass and prove a strict \(1/10\) target-error bound. Does this make the supports tail-factor projections?

**Solution.** There are \(L=9^3=729\) equal-trace full-corner projections in each relevant tail factor. Their sum is exactly one there, so each realized cell is covered exactly and no extra mass is discarded. Thus GTB.11 gives
\(\|y-c_y\|_2<1/20+2\sqrt{1/10000}=7/100<1/10\).
The original residual remains \(1/10000\). The projections are still whole-stage supports, with the original compressed indices. No tail membership or exact finite origin for that residual has been produced. The traces describe a conditional test of already realized cells, not an existence claim for an arbitrary proposed numerical family.

**Exercise GTB.2 — exact versus controlled retention.** In (GTB.20), can a length-three actual corner tunnel retain all of \(G\) exactly? At that length, give the errors from (GTB.23)–(GTB.24), and prove that every one of the 36 displayed physical matrix-unit targets is approximated strictly within \(1/10\).

**Solution.** Its smaller full stage is \(\operatorname{Mat}_{27}\), for any actual tunnel by finite marked uniqueness. A unital \(\operatorname{Mat}_2\) in it would split 27 into two equal integer ranks, so exact retention is impossible. For \(j=3\), choose \(\tau_F(z)=26/27\), split it into 13 projections of trace \(2/27\), and complete the 26 old corner units with the residual of trace \(1/27\). The two-leg target \(E_{ab}^{(b)}\otimes1\) has error \(1/\sqrt{54}\) in \(D\). Each complete target \(E_{uv}^{(a)}\otimes E_{ab}^{(b)}\) has error \(1/\sqrt{162}<1/10\), since \(162>100\). The specified unitary rotates the tunnel, while these 36 targets are kept fixed. Approximation does not create an exact unital \(M_2\) inside \(M_{27}\).

## The remaining general implication

The general whole-stage near-cover and its fixed operators are established inputs. GTB.2 constructs the correct larger-depth full corner and both trace identifications. GTB.3 makes arbitrarily cheap actual whole-cell refinements, retaining physical operators. GTB.4 proves the exact return map from an **actual constructed corner tunnel** to a whole tail-supported cell. GTB.5 then invokes the already proved OT.1 conversion to obtain a full finite partition if those actual corner chains are supplied.

GTB.6 proves that unrestricted amenability cannot supply those exact corner chains for every already selected finite block: the same rank-two example prevents them at every length. What remains is an unrestricted amenability-derived approximate candidate/corner-chain construction with an explicit physical error budget, a selection of different cells, or another construction proving the original finite full partition with its original residual. Index equality, physical factoriality, core passage, common-corner stability and cup padding do not supply that implication. The stronger sufficient input in GTB.5 is not substituted for the original theorem. The small-\(K\), singular-state, canonical-cost-zero, above-four expectation and general ergodicity implications remain separate mathematical questions.

Human sources: Sorin Popa, *Classification of amenable subfactors of type II*, Acta Mathematica 172 (1994), 163–255, [source paper](https://doi.org/10.1007/BF02392646): §1.3.2, printed p.178; Definitions3.1.1–3.1.2, printed pp.203–204; Theorems4.1.1–4.1.2, printed pp.209–210; §4.4 and Theorem4.4.1, printed pp.220–222. Jan van Neerven, *Functional Analysis*, [arXiv:2112.11166v7](https://arxiv.org/abs/2112.11166v7), Theorems4.7–4.9 and4.50, supplies the human context for Hahn–Banach and dual compactness. The complete programme proofs and independently expressed constructions above retain their stated hypotheses.

![Actual common-corner maps and both support traces; the all-depth odd-rank obstruction; and the equal-trace matrix completion with exact target errors](figures/general-tail-support-and-controlled-tunnel-v4.svg)

Figure GTB.1. The upper panels show the actual full-corner and skipped-cup maps, both support traces, and the conditional finite return. The lower panels show the same rank-two index-nine example at every depth and the controlled matrix completion at length three. Areas are schematic; the labels state exact traces and ranks. Proofs: GTB.1–GTB.8, including the full smooth-representation argument GTB.6a; Exercises GTB.1–GTB.2. Human context: Popa's §§1.3 and4.4, cited above. On a narrow screen, scroll the figure horizontally or [open the full-size figure](figures/general-tail-support-and-controlled-tunnel-v4.svg). [Editable figure source](figures/general-tail-support-and-controlled-tunnel-v4.py).

Original independently written programme text and SVG: public domain, CC0 1.0.
