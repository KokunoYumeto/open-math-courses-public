# Projective dimension and the Auslander–Buchsbaum formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A presentation describes a module by generators and relations. A resolution continues by describing relations among the relations. Projective dimension measures how long this process must continue. Over a Noetherian local ring, minimal resolutions make that length visible after reduction to the residue field. The Auslander–Buchsbaum formula then measures the same length as a loss of depth.

We use Regular sequences, depth and Cohen–Macaulay modules, particularly its Ext characterization of depth and its proof that regular local generators form a regular sequence. The resolution comparison, balanced Tor formalism and Ext exact sequences are proved in Resolutions, Tor and Ext, Theorem 1.1 and Sections 2–4, and used in Tor and flat modules. Nakayama and Noetherian finiteness retain their earlier hypotheses. All rings are commutative with identity. A local ring is nonzero and has one maximal ideal; it is not automatically Noetherian. A finite module is finitely generated.

Projective means that maps from the module lift along every surjection, equivalently that it is a direct summand of a free module. We set \(\operatorname{pd}_R(0)=0\). Depth still has the convention \(\operatorname{depth}(0)=\infty\). The depth formulas below concern nonzero modules; this distinction also matters for the residue-field formula for projective dimension.

## 1. Projective dimension over an arbitrary ring

The **projective dimension** \(\operatorname{pd}_R M\) is the least \(n\geq0\) for which there is an exact sequence
\[
0\longrightarrow P_n\longrightarrow\cdots\longrightarrow P_0
\longrightarrow M\longrightarrow0
\tag{1}
\]
with all \(P_i\) projective. It is infinity if there is no such \(n\). A zero module may appear among the projective terms. In particular, dimension zero means projective.

**Lemma 1.1 (Schanuel).** Suppose \(0\to K\to P\xrightarrow{\alpha}M\to0\) and \(0\to L\to Q\xrightarrow{\beta}M\to0\) are exact, with \(P,Q\) projective. Then
\[
K\oplus Q\cong L\oplus P.
\tag{2}
\]

**Proof.** Form \(T=\{(p,q)\in P\oplus Q:\alpha(p)=\beta(q)\}\). Projection onto \(Q\) gives \(0\to K\to T\to Q\to0\); projection onto \(P\) gives \(0\to L\to T\to P\to0\). Both projections are surjective because the original maps to \(M\) are. Both sequences split because their last terms are projective. These two decompositions of \(T\) prove (2). \(\square\)

We need the long exact Ext sequence in the **first** argument, with its arrows reversed. Here is the resolution construction that provides it and will also be used for global dimension.

**Lemma 1.2 (horseshoe construction).** Given \(0\to A\to B\to C\to0\) and projective resolutions of \(A,C\) of length at most \(n\), one can construct a resolution of \(B\) of length at most \(n\), in a short exact sequence of resolutions which splits in every degree. Its degree-\(i\) module is the direct sum of the chosen degree-\(i\) modules for \(A,C\).

**Proof.** For \(n=0\), the given sequence splits since \(C\) is projective. For \(n>0\), let \(P_0\to A\) and \(Q_0\to C\) be the first surjections. Lift \(Q_0\to C\) to \(B\) using projectivity. Together with \(P_0\to A\to B\), this gives a surjection \(P_0\oplus Q_0\to B\). Its kernel sits in
\[
0\longrightarrow K_A\longrightarrow K_B\longrightarrow K_C\longrightarrow0.
\tag{3}
\]
For surjectivity on kernels, lift an element of \(K_C\) to \(Q_0\); its image in \(B\) lies in \(A\), and a suitable element of \(P_0\) cancels it. The kernel on the left is exactly \(K_A\). The tails of the original resolutions resolve \(K_A,K_C\) in length \(n-1\). Apply induction to (3) and splice its resolution with the degree-zero surjection. This produces the asserted maps and degreewise splittings. With resolutions of unbounded length, the same kernel construction continues indefinitely. \(\square\)

Applying \(\operatorname{Hom}_R(-,N)\) to the degreewise split sequence of complexes gives a short exact sequence of Hom complexes. Its cohomology yields
\[
\cdots\to\operatorname{Ext}^i_R(C,N)\to\operatorname{Ext}^i_R(B,N)
\to\operatorname{Ext}^i_R(A,N)\to\operatorname{Ext}^{i+1}_R(C,N)\to\cdots.
\tag{4}
\]
Resolution comparison applies to projective resolutions as well as free ones, since the lifting and homotopy constructions only use projectivity.

**Theorem 1.3 (Ext test and syzygies).** For every ring, module and integer \(n\geq0\),
\[
\operatorname{pd}_R M\leq n
\quad\Longleftrightarrow\quad
\operatorname{Ext}^{n+1}_R(M,N)=0\text{ for every }N.
\tag{5}
\]
These conditions also imply vanishing in every degree greater than \(n\). In any projective resolution, write \(\Omega^0M=M\) and
\[
0\longrightarrow\Omega^{i+1}M\longrightarrow P_i
\longrightarrow\Omega^iM\longrightarrow0.
\tag{6}
\]
Then \(\operatorname{pd}M\leq n\) precisely when \(\Omega^nM\) is projective.

**Proof.** A length-\(n\) projective resolution computes Ext by a complex with no terms above degree \(n\), giving all the asserted vanishings.

First prove the converse at \(n=0\). Choose \(0\to K\to F\to M\to0\) with \(F\) free. If \(\operatorname{Ext}^1_R(M,K)=0\), (4) makes \(\operatorname{Hom}(F,K)\to\operatorname{Hom}(K,K)\) surjective. The identity of \(K\) extends to a retraction \(F\to K\), so the sequence splits and \(M\) is projective. Thus vanishing of Ext in degree one for every second argument detects projectivity.

For general \(n\), (4) applied repeatedly to (6), using positive-degree Ext vanishing for each \(P_i\), gives
\[
\operatorname{Ext}^1_R(\Omega^nM,N)
\cong\operatorname{Ext}^{n+1}_R(M,N).
\tag{7}
\]
For \(n=0\) this is the identity. Condition (5) therefore makes \(\Omega^nM\) projective. Truncating at that module supplies (1). This also proves the criterion for any chosen resolution. \(\square\)

**Corollary 1.4 (short exact sequences).** If \(0\to A\to B\to C\to0\) is exact, then
\[
\begin{aligned}
\operatorname{pd}A&\leq\max(\operatorname{pd}B,\operatorname{pd}C-1,0),\\
\operatorname{pd}B&\leq\max(\operatorname{pd}A,\operatorname{pd}C),\\
\operatorname{pd}C&\leq\max(\operatorname{pd}B,\operatorname{pd}A+1).
\end{aligned}
\tag{8}
\]

**Proof.** If a right side is infinite its inequality is immediate. Otherwise, for the first inequality (4) places \(\operatorname{Ext}^{n+1}(A,N)\) between \(\operatorname{Ext}^{n+1}(B,N)\) and \(\operatorname{Ext}^{n+2}(C,N)\), both zero at the indicated bound. For the second, the surrounding groups are those for \(C\) and \(A\) in degree \(n+1\). For the third, use \(\operatorname{Ext}^{n}(A,N)\) and \(\operatorname{Ext}^{n+1}(B,N)\), where the indicated \(n\) is at least one. Apply Theorem 1.3. The extra zero in the first bound respects our convention on projective and zero modules. \(\square\)

The **global dimension** \(\operatorname{gl.dim}R\) is \(\sup_M\operatorname{pd}_R M\), allowing infinity. It includes arbitrary modules, not just finite ones.

**Theorem 1.5 (cyclic test for global dimension).** For every ring,
\[
\operatorname{gl.dim}R=\sup_{I\subset R}\operatorname{pd}_R(R/I).
\tag{9}
\]
In particular, a uniform bound on projective dimensions of finite modules bounds the dimensions of all modules.

**Proof.** The right side is at most the left side. If it is infinite, equality follows. Suppose every cyclic quotient has dimension at most a finite \(n\). We show that every module \(M\) has such a resolution.

Well-order a set of generators \(m_\alpha\), indexed by an ordinal \(\lambda\). Let \(M_\alpha\) be generated by the elements with index less than \(\alpha\), so \(M_0=0\), \(M_\lambda=M\), and at a limit index the module is the union of the earlier ones. Each successor quotient \(M_{\alpha+1}/M_\alpha\) is cyclic, possibly zero, and has a chosen length-\(n\) projective resolution.

Construct compatible resolutions of \(M_\alpha\) by transfinite induction. At a successor index, Lemma 1.2 extends the previously constructed resolution using that of the cyclic quotient. The inclusion of old resolution terms into new terms splits in every degree. At a limit index, take their unions in every degree, with the induced differential and augmentation. The resulting augmented complex is exact: a cycle occurs at some earlier index, where exactness supplies its preimage; surjectivity of the augmentation follows the same way. Each degree module is a direct sum of the projective pieces added at successor stages, since all the inclusions were constructed as direct-sum inclusions. Such a direct sum is projective: lift a map from it along a surjection by lifting the maps from its individual summands. There are no terms above degree \(n\).

This produces a length-\(n\) projective resolution of \(M\), proving the reverse bound in (9). Every cyclic module is finite, giving the last assertion. For the zero ring, all modules are zero and both sides are zero under our convention. \(\square\)

## 2. Minimal resolutions over a local ring

**Proposition 2.1.** A finite projective module over any local ring is finite free.

**Proof.** Lift a basis of \(P/\mathfrak mP\) to obtain \(R^r\to P\), surjective by Nakayama. Projectivity splits it, so \(R^r=K\oplus P\), with \(K\) finite as a direct summand of a finite free module. Reduction modulo \(\mathfrak m\) makes the map an isomorphism, hence \(K/\mathfrak mK=0\). Nakayama gives \(K=0\). This includes \(P=0\), with rank zero. \(\square\)

A free resolution over \((R,\mathfrak m)\) is **minimal** if
\[
d_i(F_i)\subset\mathfrak mF_{i-1}\quad(i\geq1),
\qquad F_0/\mathfrak mF_0\xrightarrow{\sim}M/\mathfrak mM.
\tag{10}
\]

**Theorem 2.2 (minimal resolution and Tor).** Over a Noetherian local ring, every finite module has a minimal resolution by finite free modules. For nonzero finite \(M\),
\[
\operatorname{pd}_R M
=\sup\{i\geq0:\operatorname{Tor}^R_i(\kappa,M)\ne0\}.
\tag{11}
\]
If this value is finite, the supremum is a maximum. More precisely, for every \(n\geq0\),
\[
\operatorname{pd}_R M\leq n
\quad\Longleftrightarrow\quad
\operatorname{Tor}^R_{n+1}(\kappa,M)=0.
\tag{12}
\]
This last criterion also holds for \(M=0\).

**Proof.** Lift a basis of \(M/\mathfrak mM\) to a surjection \(F_0\to M\). Its kernel \(\Omega^1M\) is finite by Noetherianity and contained in \(\mathfrak mF_0\), since the induced residue map is an isomorphism. Repeat with a minimal-generator surjection \(F_i\to\Omega^iM\). Each kernel is finite and lies in \(\mathfrak mF_i\). The resulting resolution satisfies (10). Once a kernel is zero, take all subsequent terms zero.

After tensoring with \(\kappa\), every differential is zero. The balanced Tor formalism therefore gives
\[
\operatorname{Tor}^R_i(\kappa,M)\cong F_i/\mathfrak mF_i,
\qquad \beta_i(M):=\dim_\kappa\operatorname{Tor}^R_i(\kappa,M)
=\operatorname{rank}F_i.
\tag{13}
\]
These ranks, the **Betti numbers**, consequently do not depend on the choices of generators.

If \(\operatorname{pd}M\leq n\), Theorem 1.3 makes \(\Omega^nM\) projective, hence finite free by Proposition 2.1. Its minimal-generator surjection \(F_n\to\Omega^nM\) is an isomorphism by the same splitting-and-Nakayama argument. Thus \(F_{n+1}=0\). Conversely, (13) makes vanishing of \(\operatorname{Tor}_{n+1}\) equivalent to \(F_{n+1}=0\). Exactness then truncates the resolution at \(F_n\), giving dimension at most \(n\). This proves (12).

For nonzero \(M\), Nakayama gives nonzero \(\operatorname{Tor}_0= M/\mathfrak mM\). If projective dimension is finite \(p\), the minimal resolution terminates in degree \(p\), and its last term cannot be zero when \(p>0\), since that would give a shorter resolution. If the dimension is infinite, no stage can vanish by (12), so the nonzero Tor degrees are unbounded. This proves (11). For the zero module, all Tor groups vanish, and its projective dimension zero is handled separately. \(\square\)

**Theorem 2.3 (the residue field detects global dimension).** For every Noetherian local ring,
\[
\operatorname{gl.dim}R=\operatorname{pd}_R\kappa.
\tag{14}
\]

**Proof.** One inequality follows by including \(\kappa\) among all modules. If its projective dimension is infinite, equality follows. Otherwise write it as \(d\). A length-\(d\) projective resolution of \(\kappa\) gives \(\operatorname{Tor}_{d+1}^R(\kappa,M)=0\) for every \(M\). Theorem 2.2 makes every finite module have projective dimension at most \(d\). In particular this holds for every \(R/I\). The arbitrary-ring cyclic test in Theorem 1.5 now bounds the dimensions of all modules by \(d\). \(\square\)

## 3. The Auslander–Buchsbaum formula

**Theorem 3.1 (Auslander–Buchsbaum).** If \((R,\mathfrak m,\kappa)\) is Noetherian local and \(M\ne0\) is finite with finite projective dimension, then
\[
\boxed{\operatorname{pd}_R M+\operatorname{depth}_R M
=\operatorname{depth}R.}
\tag{15}
\]

**Proof.** Put \(t=\operatorname{depth}R\) and \(p=\operatorname{pd}M\). We induct on \(p\) using the minimal resolution. If \(p=0\), Proposition 2.1 makes \(M\cong R^r\) with \(r>0\). Ext from \(\kappa\) commutes with finite direct sums, so its first nonzero degree is \(t\) on both modules. Theorem 2.3 of *Regular sequences, depth and Cohen–Macaulay modules* gives depth \(t\), proving (15).

For \(p=1\), the minimal resolution is
\[
0\longrightarrow K\xrightarrow{a}F\longrightarrow M\longrightarrow0,
\tag{16}
\]
with \(K,F\) nonzero finite free and every matrix entry of \(a\) in \(\mathfrak m\). Section 2 of the preceding lesson proves that \(\mathfrak m\) kills every \(\operatorname{Ext}^i_R(\kappa,R)\). Hence the map induced by \(a\) on \(\operatorname{Ext}^t\) is zero. Its source is nonzero, since \(K\) has positive rank and depth \(t\).

If \(t=0\), this would be the zero map \(\operatorname{Hom}(\kappa,K)\to\operatorname{Hom}(\kappa,F)\), contradicting its injectivity in the long exact sequence of (16). Thus \(t\geq1\). The surrounding Ext groups vanish below degree \(t\), and that sequence gives
\[
\operatorname{Ext}^{t-1}_R(\kappa,M)
\cong\operatorname{Ext}^{t}_R(\kappa,K)\ne0,
\quad
\operatorname{Ext}^i_R(\kappa,M)=0\quad(0\leq i<t-1).
\tag{17}
\]
Therefore \(\operatorname{depth}M=t-1\). This is the case where minimality supplies more information than the three depth inequalities alone.

Now suppose \(p\geq2\). In \(0\to K\to F_0\to M\to0\), the tail of the minimal resolution is a minimal resolution of \(K\) of length \(p-1\), so Theorem 2.2 gives \(\operatorname{pd}K=p-1\). Induction gives
\[
s:=\operatorname{depth}K=t-p+1\geq0.
\tag{18}
\]
If \(s=0\), then \(t=p-1\geq1\). But the nonzero group \(\operatorname{Hom}(\kappa,K)\) injects into \(\operatorname{Hom}(\kappa,F_0)=0\), impossible. Consequently \(1\leq s<t\). The long exact sequence now makes \(\operatorname{Ext}^i(\kappa,M)\) vanish for \(i<s-1\), since the adjacent groups for \(F_0\) and \(K\) vanish. In degree \(s-1\) it gives
\[
\operatorname{Ext}^{s-1}_R(\kappa,M)
\cong\operatorname{Ext}^{s}_R(\kappa,K)\ne0,
\]
because both \(\operatorname{Ext}^{s-1}(\kappa,F_0)\) and \(\operatorname{Ext}^{s}(\kappa,F_0)\) vanish. Thus depth \(M=s-1=t-p\), completing the induction. \(\square\)

In particular, finite projective dimension of a nonzero finite module is at most \(\operatorname{depth}R\). The finiteness hypothesis is essential: the periodic example in Section 5 has infinite projective dimension and cannot satisfy (15).

## 4. Koszul resolutions

Let \(R\) be any ring and \(f_1,\ldots,f_r\in R\). With basis \(e_1,\ldots,e_r\) of \(R^r\), the **Koszul complex** has
\[
K_i=\bigwedge^iR^r\cong R^{\binom ri},\qquad 0\leq i\leq r,
\]
and its differential is defined on the increasing exterior basis by
\[
d(e_{j_1}\wedge\cdots\wedge e_{j_i})
=\sum_{a=1}^i(-1)^{a-1}f_{j_a}
e_{j_1}\wedge\cdots\wedge\widehat{e_{j_a}}\wedge\cdots\wedge e_{j_i}.
\tag{19}
\]
The hat means omission. For each pair of omitted indices, the two contributions to \(d^2\) have opposite signs and the same commuting coefficient product. Thus \(d^2=0\), also in characteristic two. In degree one, \(d(e_j)=f_j\), so \(H_0(K)=R/(f_1,\ldots,f_r)\).

**Theorem 4.1 (Koszul exactness).** If \(f_1,\ldots,f_r\) is regular on \(R\), its augmented Koszul complex is a finite free resolution of \(R/(f_1,\ldots,f_r)\). More generally, if the list is \(M\)-regular, then \(K_\bullet\otimes_RM\) has no positive homology and has degree-zero homology \(M/(f_1,\ldots,f_r)M\).

**Proof.** Induct on \(r\). For the empty list there is just the degree-zero module. Write \(K'\) for the complex on the first \(r-1\) entries. In degree \(i\), decompose
\[
K_i=K'_i\oplus(K'_{i-1}\wedge e_r).
\]
For \(v\in K'_{i-1}\), formula (19) gives
\[
d(v\wedge e_r)=d'v\wedge e_r+(-1)^{i-1}f_rv.
\tag{20}
\]
Thus the inclusion of \(K'\) and projection onto the second component give a short exact sequence of complexes with quotient \(K'[1]\), the complex having \(K'_{i-1}\) in degree \(i\) and differential \(-d'\). The projection includes the sign \((-1)^{i-1}\), which makes it commute with differentials. Its homology connecting map is multiplication by \(f_r\): a cycle \(w\) of degree \(i-1\) lifts as \((-1)^{i-1}w\wedge e_r\), whose differential has first component \(f_rw\).

Tensor this degreewise split sequence with \(M\). The homology exact sequence contains
\[
\cdots\to H_i(K'\otimes M)\to H_i(K\otimes M)
\to H_{i-1}(K'\otimes M)\xrightarrow{f_r}H_{i-1}(K'\otimes M)\to\cdots.
\tag{21}
\]
Induction makes all the positive homology groups of \(K'\otimes M\) zero, and its degree-zero homology is \(M/(f_1,\ldots,f_{r-1})M\). Regularity says that \(f_r\) is injective on this last module. Equation (21) therefore kills \(H_1\), kills every higher homology group, and identifies \(H_0\) with the quotient by all entries. Taking \(M=R\) proves the resolution assertion. \(\square\)

**Corollary 4.2 (exact projective dimension).** For any ring and regular sequence of length \(r\), with \(J=(f_1,\ldots,f_r)\),
\[
\operatorname{pd}_R(R/J)=r,
\qquad \operatorname{Ext}^r_R(R/J,R)\cong R/J.
\tag{22}
\]

**Proof.** The Koszul resolution gives dimension at most \(r\). In its dual Hom complex, the degree-\(r\) term is \(R\), and the image of the preceding differential is exactly \(J\): its coefficients are the signed entries \(f_i\). Hence the top Ext is \(R/J\), nonzero by the definition of a regular sequence. If \(r>0\), Theorem 1.3 makes this incompatible with projective dimension at most \(r-1\). For \(r=0\), the quotient is \(R\ne0\), its dimension is zero and \(\operatorname{Hom}_R(R,R)=R\). \(\square\)

**Corollary 4.3 (regular local upper bound).** For a regular local ring \(R\) of dimension \(D\),
\[
\operatorname{gl.dim}R=\operatorname{pd}_R\kappa=D.
\tag{23}
\]
Every nonzero finite module satisfies
\[
\operatorname{pd}_R M=D-\operatorname{depth}_R M,
\qquad
M\text{ is free}\ \Longleftrightarrow\ \operatorname{depth}_R M=D.
\tag{24}
\]

**Proof.** Theorem 6.1 of the preceding lesson makes a minimal generating list of the maximal ideal a regular sequence of length \(D\). Its Koszul complex resolves \(\kappa\), and (22) gives projective dimension \(D\). Equation (14) proves (23), including the field case \(D=0\). Thus every finite module has finite projective dimension, and the ring has depth \(D\) by the same earlier theorem. Apply Auslander–Buchsbaum and Proposition 2.1 to obtain (24). \(\square\)

This proves the regular-local consequence needed here. The converse, finite projective dimension of the residue field implying regularity, belongs to the later lesson *Regular local rings* and is not used above. The zero module is free of rank zero but has depth infinity, so it is excluded from the equivalence in (24).

## 5. Calculations and the finiteness boundary

**The plane origin.** In \(R=k[x,y]_{(x,y)}\), the coordinate pair is regular: the ring is a domain, and modulo \(x\) multiplication by \(y\) is injective in \(k[y]_{(y)}\). The Koszul resolution is
\[
0\longrightarrow R\xrightarrow{\binom{-y}{x}}R^2
\xrightarrow{(x\ \ y)}R\longrightarrow k\longrightarrow0.
\tag{25}
\]
All entries lie in the maximal ideal, so the Betti numbers are \(1,2,1\). Projective dimension of \(k\) is two. The ring is regular of dimension two by the polynomial height and embedding-dimension results, hence has depth two; the field quotient has depth zero. Formula (15) reads \(2+0=2\).

**A periodic resolution.** Let \(R=k[\epsilon]/(\epsilon^2)\), with residue field \(k\). The annihilator of \(\epsilon\) is exactly \((\epsilon)\), as the basis \(1,\epsilon\) shows. Consequently
\[
\cdots\xrightarrow{\epsilon}R\xrightarrow{\epsilon}R
\xrightarrow{\epsilon}R\longrightarrow k\longrightarrow0
\tag{26}
\]
is exact and minimal. Tensoring with \(k\) gives zero differentials and one copy of \(k\) in each degree. Thus \(\operatorname{Tor}^R_i(k,k)=k\) for every \(i\geq0\), and \(\operatorname{pd}_R k=\infty\). The ring and its residue field both have depth zero; the finite-projective-dimension hypothesis in (15) cannot be discarded.

**One regular equation.** If \(x\in\mathfrak m\) is injective on a Noetherian local ring, then \(0\to R\xrightarrow{x}R\to R/(x)\to0\) is minimal and nontrivial. It gives projective dimension one, while the preceding lesson gives depth \(\operatorname{depth}R-1\). This is the first dimension-loss case of Auslander–Buchsbaum. If \(x\) is a unit instead, its quotient is zero, so this conclusion would not apply.

## 6. Exercises

**Exercise 6.1 (easy).** Prove that a finite projective module over a Noetherian local ring is free. Identify which part of the proof can be made without Noetherianity, and include rank zero.

**Exercise 6.2 (easy).** Compute the projective dimension of \(k[x,y]/(x,y)\) over \(k[x,y]\). Write its resolution and check Auslander–Buchsbaum after localization at the origin.

**Exercise 6.3 (medium).** For \(R=k[\epsilon]/(\epsilon^2)\), compute \(\operatorname{Tor}^R_i(k,k)\) for every \(i\geq0\), and deduce that the residue field has infinite projective dimension.

**Exercise 6.4 (medium).** For a regular local ring and a nonzero finite module \(M\), prove that \(M\) is free precisely when its depth equals the ring's dimension. Explain why the finite-projective-dimension hypothesis is available, and what happens for \(M=0\).

**Exercise 6.5 (medium).** For \(A=k[x,y]_{(x,y)}\) and positive integers \(a,b\), compute projective dimension, depth, Betti numbers and \(\operatorname{Ext}^2_A(A/(x^a,y^b),A)\). Compute the length of the quotient.

**Exercise 6.6 (hard).** In the same \(A\), let \(I=(x,y)\). Construct minimal free resolutions of \(I\) and \(I^2\), prove exactness directly, and calculate their depths and projective dimensions. Then calculate these invariants for \(A/I\) and \(A/I^2\). Explain how an ideal with full support can have depth less than \(\dim A\).

## 7. Complete solutions

**Solution 6.1.** Lift a basis of \(M/\mathfrak mM\) to a surjection \(R^r\to M\). Projectivity splits it, with kernel \(K\) a direct summand of \(R^r\), hence finite even without Noetherianity. The induced residue map is an isomorphism, and the splitting makes \(K/\mathfrak mK=0\). Nakayama gives \(K=0\), so the chosen lifts form a free basis. The entire argument works over any local ring. For the zero module, use \(r=0\).

**Solution 6.2.** The pair \(x,y\) is regular already over the polynomial ring: \(x\) is injective, and its quotient is the domain \(k[y]\), on which \(y\) is injective. The final quotient is \(k\). Formula (25), over \(k[x,y]\) before localization, is therefore a free resolution. It has length two, and its dual top Ext group is \(k\ne0\) by (22), so projective dimension is exactly two. At the origin the localized resolution is minimal, the regular local ring has dimension and depth two, and the residue field has depth zero. Auslander–Buchsbaum gives the equality \(2+0=2\).

**Solution 6.3.** Every element of \(R\) has a unique expression \(u+v\epsilon\), with \(u,v\in k\). Multiplication by \(\epsilon\) has kernel and image both \(k\epsilon=(\epsilon)\). The kernel of \(R\to k\) is the same ideal, so (26) is a free resolution. Modulo \(\epsilon\), all differentials are zero, giving one copy of \(k\) as homology in every nonnegative degree. A finite-length projective resolution would make all Tor groups above its length zero. The computed groups exclude this, proving infinite projective dimension. This also proves \(\operatorname{gl.dim}R=\infty\) by (14).

**Solution 6.4.** If the dimension is \(D\), the preceding lesson makes the \(D\) minimal generators of the maximal ideal regular. Their Koszul complex resolves the residue field, with projective dimension \(D\). The local global-dimension theorem therefore bounds the projective dimension of every module by \(D\). The ring has depth \(D\). For nonzero finite \(M\), Auslander–Buchsbaum says \(\operatorname{pd}M=D-\operatorname{depth}M\). Depth \(D\) is equivalent to projective dimension zero, hence to finite projectivity and to freeness. Conversely, a nonzero finite free module has the same first nonzero Ext degree as the ring, so depth \(D\). The zero module is free, but its depth is infinity under the course convention, so it must be excepted from this characterization.

**Solution 6.5.** The coordinate list is regular, and Proposition 1.3 of *Regular sequences, depth and Cohen–Macaulay modules* makes \(x^a,y^b\) regular. Its minimal Koszul resolution has modules \(A,A^2,A\), with matrices \((x^a\ \ y^b)\) and \(\binom{-y^b}{x^a}\). Thus the Betti numbers are \(1,2,1\), with all subsequent ones zero. Projective dimension is two and top Ext is \(A/(x^a,y^b)\) by (22).

The quotient is already an Artinian local ring before localization: the positive-degree ideal is nilpotent and the residue is \(k\). A basis consists of \(x^iy^j\), \(0\leq i<a\), \(0\leq j<b\), because membership in the monomial ideal is termwise divisibility. Localization at the origin changes nothing: a nonzero constant plus a nilpotent element is a unit by a finite geometric series. The length is its \(k\)-dimension \(ab\), since all simple factors are \(k\). Its support dimension and depth are zero, and Auslander–Buchsbaum again reads \(2+0=2\).

**Solution 6.6.** The ideal \(I\) has a resolution
\[
0\longrightarrow A\xrightarrow{\binom{-y}{x}}A^2
\xrightarrow{(u,v)\mapsto ux+vy}I\longrightarrow0.
\tag{27}
\]
For direct exactness, if \(ux+vy=0\), reduce modulo \(x\). The quotient is a domain in which \(y\) is nonzero, so \(v=xh\). Cancel \(x\) in \(A\) to obtain \(u=-yh\). Thus every kernel element is in the image, and that first map is injective because \(A\) is a domain.

For \(I^2\), use
\[
0\longrightarrow A^2
\xrightarrow{\begin{pmatrix}-y&0\\x&-y\\0&x\end{pmatrix}}A^3
\xrightarrow{(u,v,w)\mapsto ux^2+vxy+wy^2}I^2
\longrightarrow0.
\tag{28}
\]
The matrix's columns are relations. If \(ux^2+vxy+wy^2=0\), reduction modulo \(x\) gives \(w=xw_1\). Cancel \(x\), obtaining \(ux+(v+w_1y)y=0\). Reduction modulo \(y\) gives \(u=yu_1\). Cancel \(y\) in the resulting equality to get \(v=-xu_1-yw_1\). Hence
\[
(u,v,w)=-u_1(-y,x,0)+w_1(0,-y,x),
\]
as required. The matrix is injective: its first row kills the first coefficient only if that coefficient is zero, and its last row then kills the second only if it is zero.

Both resolutions are minimal. The displayed ideal generators are bases modulo \(\mathfrak mI\) and \(\mathfrak mI^2\): their degree-one or degree-two monomials are linearly independent in \(\operatorname{gr}_{\mathfrak m}A=k[X,Y]\). Every differential entry is in \(\mathfrak m\). Thus \(I\) has Betti numbers \(2,1\) and \(I^2\) has \(3,2\), and both have projective dimension one. Auslander–Buchsbaum gives depth one to both.

Appending their inclusions into \(A\) turns (27) and (28) into minimal resolutions of \(A/I\) and \(A/I^2\). Their Betti numbers are respectively \(1,2,1\) and \(1,3,2\); both have projective dimension two and depth zero. The quotients have lengths one and three, with the latter represented by \(1,x,y\).

Each ideal is nonzero in a domain, so its annihilator is zero and its support is the whole dimension-two spectrum of \(A\). Nevertheless each has depth one. Full support and absence of torsion do not force a finite module to be CM or free; the relation modules in (27) and (28) account for the lost depth.

## What this lesson does not prove

All the projective-dimension tests, the cyclic global-dimension theorem, local residue-field test, Auslander–Buchsbaum formula and Koszul resolution asserted here are proved. Resolution comparison, balanced Tor and homology long exact sequences are proved in Resolutions, Tor and Ext, Theorems 1.1 and 3.2 and Section 2. The first-variable Ext sequence is constructed in Section 1; the second-variable sequence and scalar annihilation used in Section 3 are those established in the preceding lesson. The converse homological characterization of regular local rings is deferred to *Regular local rings*, without being assumed here. No classification of projective modules over polynomial rings or proof of the Hilbert syzygy theorem is asserted.

## References

The [official Stacks project](https://stacks.math.columbia.edu/) is the maintained reference. Tag links here use [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), an edition with AI-proposed corrections and AI-written additions that have not been reviewed by the Stacks project maintainers. The proof organization and solutions above are independent expressions.

- Projective dimension, Schanuel, Ext tests and short exact sequences: [Stacks, Tag 00O3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Schanuel), [Stacks, Tag 00O4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-finite-proj-dim), [Stacks, Tag 065R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-projective-dimension-ext), [Stacks, Tag 065S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-exact-sequence-projective-dimension), [Stacks, Tag 065P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-reverse-long-exact-seq-ext).
- Global dimension and resolutions: [Stacks, Tag 00O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-finite-gl-dim), [Stacks, Tag 065T](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-gl-dim), [Stacks, Tag 0D1U](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-colimit-projective-dimension), [Stacks, Tag 0CXF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-what-kind-of-resolutions-Noetherian-local).
- The general local formula is [Stacks, Tag 090V](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-Auslander-Buchsbaum). The regular-local resolution bound is also [Stacks, Tag 00O7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-regular-finite-gl-dim).
- Koszul definitions and exactness: [Stacks, Tag 0622](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-koszul), [Stacks, Tag 0623](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-definition-koszul-complex), [Stacks, Tag 062F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-koszul-regular).
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, §24.4 on Koszul complexes and resolutions; §§26.1–26.2 on depth and Cohen–Macaulay rings.

