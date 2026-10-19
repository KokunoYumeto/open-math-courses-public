# Analytic realization and contraction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The preceding lessons produced finitely many changes of the gluing of a neighbourhood of \(C\) in the total space of \(L^{-1}\), together with two vector fields prescribed modulo terms of order nine. This lesson builds an actual complex surface \(Y\) from these gluing changes (Section 1), proves that the prescribed jets lift to holomorphic vector fields (Sections 2 and 3), and contracts \(C\) to a normal singular point \(x\) at which the two fields become a basis of the derivations (Section 4). Section 5 computes two invariants of the singularity.

The contraction and the lifting use four classical theorems of complex analytic geometry that the programme does not prove yet. They are stated precisely in Section 3 as named results N1–N4, with an extension theorem N5 used in Section 4, and every use is marked. The theorem of this course is proved conditionally on them; the course record lists them as open obligations.

**Prerequisites.** [*Gluing vector fields: higher orders and the determinant*](gluing-vector-fields-higher-orders-and-the-determinant.md), Proposition 3.1; [*Gluing vector fields: the first two orders*](gluing-vector-fields-the-first-two-orders.md), Sections 1 and 2; [*A curve of genus 21 with a fourth root of its canonical bundle*](a-curve-of-genus-21-with-a-fourth-root-of-its-canonical-bundle.md), Proposition 3.3 and Corollary 3.4. From *Complex analytic spaces and coherent sheaves*: [*Analytic germs, local parametrization and the Nullstellensatz*](course:complex-analytic-spaces-and-coherent-sheaves/analytic-germs-local-parametrization-and-the-nullstellensatz), Theorem 5.1; [*Cartan's coherence theorem and complex spaces*](course:complex-analytic-spaces-and-coherent-sheaves/cartans-coherence-theorem-and-complex-spaces), Theorem 1.1. From AG-CA: [*Completion*](course:AG-CA/completion) (completion of finite modules over a Noetherian local ring, and Nakayama's lemma). Existence of flows of holomorphic vector fields.

## 1. A Hausdorff surface

**Lemma 1.1 (realization).** The gluing changes of Proposition 3.1 of the preceding lesson define, after shrinking their domains, a complex surface \(Y\) that contains \(C\) as a smooth compact curve with conormal bundle \(L\); so \(C\cdot C=\deg(\mathcal O_Y(C)|_C)\), which is \(-\deg L=-10\). With \(\mathcal I=\mathcal O_Y(-C)\) and \(\mathcal F=\mathcal T_Y(-\log C)\), the sheaf of vector fields tangent to \(C\), the prescribed rows define two global sections
\[
\bar v_1,\bar v_2\in H^0(Y,\mathcal F/\mathcal I^9\mathcal F),
\]
lying in \(\mathcal I\mathcal F/\mathcal I^9\mathcal F\). In a chart \((t,z)\) with \(C=\{t=0\}\), any local lifts satisfy \(v_1\wedge v_2=t^5(1+O(t))\,\partial_t\wedge\partial_z\).

**Proof.** Let \(N\) be the total space of \(L^{-1}\). On the annulus at \(q_j\), the gluing change \(\Phi_j\) is a finite composite of time-one flows of fields \(t^k(bE_t+h\partial_z)\), \(k\ge1\), holomorphic on the punctured disc. Choose radii \(0<a_j<a'_j<b'_j<b_j\) such that the closed annulus \(a_j\le|z_j|\le b_j\) lies in the punctured coordinate disc at \(q_j\), the six discs \(|z_j|<b_j\) are disjoint, and the flows are defined on a neighbourhood of the zero section over a neighbourhood of the closed annulus: the fields vanish on the zero section, so their time-one flows and inverses exist on a sufficiently thin neighbourhood of the zero section over this compact set, and there are finitely many.

Let \(V_j\) be a thin open neighbourhood of the zero section over \(|z_j|<b'_j\), and \(V_0\) a thin open neighbourhood of the zero section over \(C\setminus\bigcup_j\{|z_j|\le a'_j\}\). Since \(\Phi_j\) is the identity on the zero section, after thinning,
\[
\begin{aligned}
&\bigl|z_j(\Phi_j(p))-z_j(p)\bigr|\\
&\quad<\tfrac12(a'_j-a_j)
\end{aligned}
\tag{1.1}
\]
for \(p\) over the closed annulus, and \(\Phi_j(p)\) lies over the disc \(|z_j|<b_j\). Let \(A_j\) be the open set of points \(p\in V_j\) with \(a_j<|z_j(p)|<b_j\) and \(\Phi_j(p)\in V_0\), and identify \(p\in A_j\) with \(\Phi_j(p)\in V_0\). Let \(Y\) be the quotient of \(V_0\sqcup V_1\sqcup\cdots\sqcup V_6\).

*The relation is closed.* Its graph is the diagonal together with the graphs of the \(\Phi_j|_{A_j}\) and their inverses; a point of \(V_0\) lies in the image of at most one \(A_j\), because these images lie over disjoint discs. Suppose \(p_\nu\in A_j\), \(p_\nu\to p\in V_j\) and \(\Phi_j(p_\nu)\to q\in V_0\). Then \(a_j\le|z_j(p)|\le b'_j<b_j\), the flow is defined at \(p\), and \(q=\Phi_j(p)\). If \(|z_j(p)|=a_j\), then (1.1) gives \(|z_j(q)|<a'_j\), contradicting \(q\in V_0\). So \(p\in A_j\), and the graph is closed in \(V_j\times V_0\).

*Hausdorff.* The quotient map is open, because the identifications are biholomorphisms between open sets. For an open quotient map with closed relation, two inequivalent points have product neighbourhoods disjoint from the relation, whose images are disjoint open sets. The quotient map is injective and open on each \(V_i\), so the complex structures of the pieces give \(Y\) the structure of a complex surface, and the zero sections give a compact curve, \(C\) with its own complex structure.

*Conormal bundle.* Each flow fixes \(C\) pointwise and changes the fibre coordinate by \(t\mapsto t+O(t^2)\) (Section 2 of the lesson on the first two orders), so \(\mathcal I/\mathcal I^2\cong L\) as for \(N\). Hence \(\mathcal O_Y(C)|_C\cong L^{-1}\), of degree \(-10\).

*The sections.* In the logarithmic frame \((t\partial_t,\partial_z)\), a field (1.4) of the lesson on the first two orders has coefficients \(tA\) and \(tB\), so the rows of index \(0\) to \(7\) prescribe the coefficients modulo \(t^9\). Matching through index seven on the actual gluing maps is matching modulo \(\mathcal I^9\mathcal F\), and gives the global sections. The logarithmic determinant is \(t^2(A\wedge B)=t^4(1+O(t))\), and replacing \(t\partial_t\) by \(\partial_t\) multiplies it by \(t\). Changing the lifts by sections of \(\mathcal I^9\mathcal F\) changes the wedge by a section of \(\mathcal I^{10}\det\mathcal F\). \(\square\)

## 2. Graded vanishing

The sheaf \(\mathcal F\) is locally free of rank two, with local basis \(t\partial_t,\partial_z\). Restriction to \(C\) gives the exact sequence
\[
0\to\mathcal O_C\to\mathcal F|_C\to\mathcal T_C\to0,\qquad(2.1)
\]
where \(1\) maps to the class of the Euler field \(t\partial_t\), and the second map restricts a field tangent to \(C\) to \(C\). The class of \(t\partial_t\) does not change when \(t\) is multiplied by a unit, so (2.1) is intrinsic.

**Lemma 2.1.** For every \(n\ge9\), \(H^1(C,\mathcal F|_C\otimes L^n)=0\). Consequently, for \(\mathcal E=\mathcal I^9\mathcal F\) and every \(r\ge1\), \(H^1(Y,\mathcal E/\mathcal I^r\mathcal E)=0\).

**Proof.** Since \(\mathcal T_C=K_C^{-1}\cong L^{-4}\), tensoring (2.1) with \(L^n\) gives \(0\to L^n\to\mathcal F|_C\otimes L^n\to L^{n-4}\to0\). By Serre duality, \(H^1(C,L^m)\) is dual to \(H^0(C,L^{4-m})\), which vanishes for \(m\ge5\) because \(\deg L>0\). For \(n\ge9\) both \(m=n\) and \(m=n-4\) are at least \(5\), and the cohomology sequence gives the first claim. Since \(C\) is a Cartier divisor and \(\mathcal F\) is locally free, \(\mathcal I^n\mathcal F/\mathcal I^{n+1}\mathcal F\cong\mathcal F|_C\otimes L^n\). The sheaf \(\mathcal E/\mathcal I^r\mathcal E=\mathcal I^9\mathcal F/\mathcal I^{9+r}\mathcal F\) is supported on \(C\) and has a finite filtration with these quotients for \(9\le n<9+r\); the cohomology sequences give the second claim. \(\square\)

## 3. Contraction and lifting

The following theorems are used and not proved in the programme. Each is stated in the form used.

**N1 (Grauert's contraction theorem).** Let \(Y\) be a complex surface and \(C\subset Y\) a compact connected smooth curve with \(C\cdot C<0\). After replacing \(Y\) by a suitable open neighbourhood of \(C\), there are a normal complex space \(X\) of dimension two, a point \(x\in X\), and a proper surjective holomorphic map \(\pi:Y\to X\) with \(\pi^{-1}(x)=C\) as sets, \(\pi:Y\setminus C\to X\setminus\{x\}\) biholomorphic, and \(\pi_*\mathcal O_Y=\mathcal O_X\). [H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Math. Ann. 146 (1962), §4.8(e), pp. 366–367, with the reduction and contraction statements of §2, p. 337, and Definition 3, pp. 339–340.]

**N2 (Grauert's direct image theorem).** For a proper holomorphic map \(\pi:Y\to X\) of complex spaces and a coherent analytic sheaf \(\mathcal E\) on \(Y\), every \(R^q\pi_*\mathcal E\) is coherent. [H. Grauert, *Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*, Publ. Math. IHÉS 5 (1960), §6, Hauptsatz I.]

**N3 (theorem on formal functions, analytic case).** In the situation of N2, for \(x\in X\) and \(\mathcal J=\mathfrak m_x\mathcal O_Y\),
\[
\widehat{(R^q\pi_*\mathcal E)_x}\cong\varprojlim_rH^q(Y,\mathcal E/\mathcal J^r\mathcal E).
\]
[Grauert, loc. cit., §6, Hauptsatz IIa, p. 59. No flatness of \(\pi\) is needed.]

**N4 (Stein neighbourhoods and Theorem B).** Every point of a complex space has a basis of Stein open neighbourhoods, and on a Stein space every coherent analytic sheaf has vanishing cohomology in positive degrees. [H. Cartan, *Faisceaux analytiques sur les variétés de Stein*, Séminaire Henri Cartan 4 (1951/52), exposé 18; for Stein manifolds the programme proves Theorem B in [*Theorems A and B on Stein manifolds*](course:complex-analytic-spaces-and-coherent-sheaves/theorems-a-and-b-on-stein-manifolds), Theorem 4.1.]

**Lemma 3.1 (lifting).** Assume N1–N4. After shrinking \(Y\) around \(C\), the sections \(\bar v_1,\bar v_2\) lift to holomorphic sections \(v_1,v_2\) of \(\mathcal F\), and \(v_1,v_2\) is a frame of the tangent bundle of \(Y\setminus C\).

**Proof.** Since \(C\cdot C=-10<0\), N1 gives a contraction \(\pi:Y\to X\) onto a normal surface \(X\) with \(\pi^{-1}(x)=C\). By N4, we may replace \(X\) by a Stein open neighbourhood of \(x\) and \(Y\) by its inverse image; for a proper map, every neighbourhood of the compact fibre \(C\) contains the inverse image of a neighbourhood of \(x\).

*The direct image vanishes.* Let \(\mathcal E=\mathcal I^9\mathcal F\) and \(\mathcal J=\mathfrak m_x\mathcal O_Y\). Both \(\mathcal J\) and \(\mathcal I\) have zero set \(C\), and \(\mathcal I\) is the ideal of all holomorphic functions vanishing on \(C\). By the analytic Nullstellensatz (Theorem 5.1 of the lesson on analytic germs), at each point of \(C\) some power of \(\mathcal I\) lies in \(\mathcal J\), the ideal \(\mathcal I\) being finitely generated; by compactness one exponent \(a\) works along \(C\), and after shrinking,
\[
\mathcal I^{ar}\subseteq\mathcal J^r\subseteq\mathcal I^r\qquad(r\ge1).
\]
So \(\mathcal J^{ar}\mathcal E\subseteq\mathcal I^{ar}\mathcal E\subseteq\mathcal J^r\mathcal E\), and the transition map from index \(ar\) to index \(r\) in the inverse system \(H^1(Y,\mathcal E/\mathcal J^r\mathcal E)\) factors through \(H^1(Y,\mathcal E/\mathcal I^{ar}\mathcal E)\), which is zero by Lemma 2.1. Hence the inverse limit is zero. By N2, \((R^1\pi_*\mathcal E)_x\) is a finite module over the Noetherian local ring \(\mathcal O_{X,x}\), and by N3 its completion is zero; so it is zero, a finite module over a Noetherian local ring injecting into its completion. Away from \(x\), \(\pi\) is an isomorphism. So \(R^1\pi_*\mathcal E=0\).

*Lifting.* \(\pi_*\mathcal E\) is coherent by N2, so \(H^1(X,\pi_*\mathcal E)=0\) by N4. The exact sequence of low degrees of the Leray spectral sequence of \(\pi\), \(0\to H^1(X,\pi_*\mathcal E)\to H^1(Y,\mathcal E)\)\(\to H^0(X,R^1\pi_*\mathcal E)\), gives \(H^1(Y,\mathcal E)=0\). The cohomology sequence of \(0\to\mathcal E\to\mathcal F\to\mathcal F/\mathcal I^9\mathcal F\to0\) lifts \(\bar v_1,\bar v_2\) to sections \(v_1,v_2\) of \(\mathcal F\).

*Frame.* By Lemma 1.1, in each chart \(v_1\wedge v_2=t^5u(t,z)\,\partial_t\wedge\partial_z\) with \(u(0,z)=1\). So \(u\) is nonzero on a neighbourhood of \(C\); by compactness and properness we may shrink \(X\) so that its inverse image \(Y\) lies in that neighbourhood. Off \(C\), \(t\ne0\), and \(v_1\wedge v_2\ne0\). \(\square\)

## 4. The singular point and its derivations

**N5 (extension across a point of a normal surface).** If \(X\) is a normal complex space of dimension two and \(x\in X\), every holomorphic function on \(U\setminus\{x\}\), for \(U\) an open neighbourhood of \(x\), extends holomorphically to \(U\); that is, \(\mathcal O_X\cong j_*\mathcal O_{X\setminus\{x\}}\) for the inclusion \(j\). [J.-P. Demailly, *Complex analytic and differential geometry*, Chapter II, Corollary 7.8 (free at the author's web page).]

**Proposition 4.1 (an analytic counterexample).** Assume N1–N5. There is a normal complex surface germ \((X,x)\), smooth away from \(x\) and singular at \(x\), whose sheaf of derivations \(\mathcal T_X=\mathcal Hom_{\mathcal O_X}(\Omega^1_X,\mathcal O_X)\) is free of rank two. It has a resolution \(\pi:Y\to X\) whose exceptional set is the curve \(C\) of genus \(21\), with \(C\cdot C=-10\).

**Proof.** Take \(\pi:Y\to X\) from Lemma 3.1; \(X\setminus\{x\}\cong Y\setminus C\) is smooth.

*The point is singular.* By the adjunction formula on \(Y\), \(K_C\cong(K_Y+C)|_C\), through the residue as in Lemma 1.3 of the lesson on the elliptic curve; so \(K_Y\cdot C:=\deg(K_Y|_C)\) equals \(2g(C)-2-C\cdot C=40+10=50\). If \(x\) were a smooth point, a small neighbourhood of \(x\) would carry a nowhere vanishing holomorphic two-form \(\omega\). Its pullback \(\pi^*\omega\) is a holomorphic section of \(K_Y\) without zeros off \(C\), so its divisor is \(aC\) with \(a\ge0\), as \(C\) is irreducible. Then \(K_Y\cong\mathcal O_Y(aC)\) near \(C\), and \(K_Y\cdot C=a\,C\cdot C\le0\), a contradiction.

*The derivations are free.* Put \(X^\circ=X\setminus\{x\}\) and \(j:X^\circ\to X\). The fields \(v_1,v_2\) of Lemma 3.1 give a frame \(w_1,w_2\) of the tangent bundle of \(X^\circ\). Embed a representative of \((X,x)\) in an open set of \(\mathbb C^e\) with coordinates \(x_1,\ldots,x_e\). By N5, each function \(w_i(x_\alpha)\) on \(X^\circ\) extends to a holomorphic function \(a_{i\alpha}\) on \(X\). For every local equation \(f\) of \(X\), \(\sum_\alpha a_{i\alpha}\,\partial f/\partial x_\alpha\) vanishes on the dense open set \(X^\circ\) (Theorem 3.3 of the lesson on Cartan's coherence theorem: the regular locus is dense), hence on the reduced space \(X\). So \((a_{i\alpha})_\alpha\) defines a derivation of \(\mathcal O_X\), that is, a section of \(\mathcal T_X\), extending \(w_i\); call it \(w_i\) again.

Let \(w\) be a local section of \(\mathcal T_X\). On \(X^\circ\), \(w=h_1w_1+h_2w_2\) with unique holomorphic \(h_1,h_2\). By N5 they extend to \(X\), and \(w-h_1w_1-h_2w_2\) applied to the coordinates gives holomorphic functions vanishing on \(X^\circ\), hence zero. So \((h_1,h_2)\mapsto h_1w_1+h_2w_2\) maps \(\mathcal O_X^{\oplus2}\) onto \(\mathcal T_X\). If \(h_1w_1+h_2w_2=0\), then \(h_1=h_2=0\) on \(X^\circ\), where \(w_1,w_2\) is a frame, hence on \(X\). So \(\mathcal T_X\cong\mathcal O_X^{\oplus2}\). \(\square\)

## 5. Two invariants

**The discrepancy.** Let \(\omega^\circ\) be the two-form on \(X^\circ\) dual to the frame \(w_1,w_2\), so \(\omega^\circ(w_1,w_2)=1\). In a chart of \(Y\), \(v_1\wedge v_2=t^5u\,\partial_t\wedge\partial_z\), so
\[
\pi^*\omega^\circ=t^{-5}u^{-1}\,dt\wedge dz,
\]
a meromorphic two-form on \(Y\) with divisor \(-5C\). So \(K_Y=\pi^*K_X-5C\) with \(K_X\) the divisor of \(\omega^\circ\), which is zero: the *discrepancy* of \(C\) is \(-5\), and \(\omega^\circ\) trivializes the canonical sheaf of \(X^\circ\).

**The geometric genus.** Put \(\mathcal O_{nC}=\mathcal O_Y/\mathcal I^n\). From \(0\to L\to\mathcal O_{2C}\to\mathcal O_C\to0\), in which the constant \(1\) of \(\mathcal O_C\) lifts, and \(H^2(C,L)=0\),
\[
\begin{aligned}
h^1(\mathcal O_{2C})&=h^1(C,L)+h^1(C,\mathcal O_C)\\
&=12+21=33,
\end{aligned}
\]
by Corollary 3.4 of the lesson on the curve of genus 21. The sequences \(0\to L^n\to\mathcal O_{(n+1)C}\to\mathcal O_{nC}\to0\) make every map \(H^1(\mathcal O_{(n+1)C})\to H^1(\mathcal O_{nC})\) surjective. By N2 and N3 (with \(\mathcal E=\mathcal O_Y\) and the comparison of the two filtrations in the proof of Lemma 3.1), the inverse limit of the \(H^1(\mathcal O_{nC})\) is the completion of \((R^1\pi_*\mathcal O_Y)_x\), a module of finite length, so equal to its completion; it maps onto \(H^1(\mathcal O_{2C})\). Hence
\[
p_g(X,x)=\dim_{\mathbb C}(R^1\pi_*\mathcal O_Y)_x\ge33 .
\]

## 6. Exercises

**6.1** (easy). Show that the gluing changes do not change the degree of the normal bundle of \(C\), and that \(C\cdot C=-10\) in \(Y\) as in the total space of \(L^{-1}\).

**6.2** (medium). Show that \(H^1(C,\mathcal F|_C\otimes L^8)\) is one-dimensional, so the bound nine in Lemma 2.1 is the least for which the argument works.

**6.3** (medium). For the contraction of the zero section of the total space of \(L^{-1}\) itself, compute \(K_Y\cdot C\) and the discrepancy of \(C\), and compare with Section 5.

**6.4** (medium). Show that in the proof of Proposition 4.1 the extension of \(w_i\) is a derivation of \(\mathcal O_X\), that is, it maps \(f\cdot g\) to \(fw_i(g)+gw_i(f)\).

## 7. Solutions

**6.1.** \(\mathcal I/\mathcal I^2\cong L\) on \(Y\) by Lemma 1.1, as on the total space; the normal bundle is the dual \(L^{-1}\), of degree \(-10\), and \(C\cdot C\) is its degree.

**6.2.** For \(n=8\), the sequence \(0\to L^8\to\mathcal F|_C\otimes L^8\to L^4\to0\) and \(H^1(C,L^8)=0\), \(H^2=0\), give \(H^1(\mathcal F|_C\otimes L^8)\cong H^1(C,L^4)\), and \(H^1(C,L^4)=H^1(C,K_C)\cong\mathbb C\).

**6.3.** The computation of Section 4 applies: \(K_Y\cdot C=2g-2-C\cdot C=50\). Writing \(K_Y\equiv\pi^*K_X+\delta C\) numerically near \(C\) and intersecting with \(C\) gives \(\delta\,C\cdot C=50\), so \(\delta=-5\), the value of Section 5. The discrepancy depends only on \(K_Y\cdot C\) and \(C\cdot C\), which the gluing changes do not alter. The two surfaces differ in their analytic structure: the contraction of the zero section is the cone \(\operatorname{Spec}\bigoplus_{n\ge0}H^0(C,L^n)\), a graded ring, and for graded rings a free derivation module forces regularity, a known positive case of the problem listed in the first lesson.

**6.4.** On \(X^\circ\), \(w_i\) is a vector field, so the Leibniz rule holds there; both sides are holomorphic on \(X\) and agree on the dense set \(X^\circ\), so they agree on \(X\).

## Sources

- [OpenAI-048] OpenAI, *A singular normal affine surface with free tangent sheaf* (manuscript, 23 September 2026), in the release github.com/openai/math, family 048. Section 5: realization, graded vanishing, lifting, the singular point and its invariants.
- H. Grauert, *Über Modifikationen und exzeptionelle analytische Mengen*, Math. Ann. 146 (1962), 331–368; freely readable through the Göttingen digitization centre (gdz.sub.uni-goettingen.de, volume PPN235181684_0146). Result N1.
- H. Grauert, *Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*, Publ. Math. IHÉS 5 (1960); freely readable on Numdam. Results N2, N3.
- H. Cartan, *Séminaire Henri Cartan*, volume 4 (1951/52); freely readable on Numdam. Result N4.
- J.-P. Demailly, *Complex analytic and differential geometry*, https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf. Result N5, and coherence of analytic structure sheaves.
