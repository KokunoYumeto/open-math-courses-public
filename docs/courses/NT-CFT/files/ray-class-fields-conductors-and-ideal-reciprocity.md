# Ray class fields, conductors and ideal reciprocity

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

**Lesson 18.** A local uniformizer at an unramified prime acts by Frobenius. Multiplying these uniformizer idèles turns global reciprocity into a map on fractional ideals. The remaining idèle components record the congruences and signs that a principal generator must satisfy. Their quotient is the ray class group, and the global existence theorem constructs its class field.

We use [Global existence and the idèlic class field correspondence](global-existence-and-the-idelic-class-field-correspondence.md), [The global reciprocity law](the-global-reciprocity-law.md), and the local conductor criteria in [Abelian ramification, conductors and Hasse–Arf](abelian-ramification-conductors-and-hasse-arf.md), Proposition 10.4. The explicit quadratic Hilbert symbols of lesson 11 will determine the examples. Throughout sections 1–7, \(K\) is a number field. Section 8 explains the function-field degree distinction.

## 1. Moduli and ray classes

A **modulus** is a pair \(\mathfrak m=\mathfrak m_f\mathfrak m_\infty\), where \(\mathfrak m_f\) is a nonzero integral ideal and \(\mathfrak m_\infty\) is a set of real places, each occurring once. Complex places impose no additional condition. Divisibility means ideal divisibility together with inclusion of the selected real places. Write \(m_v=v(\mathfrak m_f)\) at finite places, and define
\[
U_v(\mathfrak m)=
\begin{cases}
1+\mathfrak p_v^{m_v}\mathcal O_v,&v\text{ finite},\ m_v>0,\\
\mathcal O_v^\times,&v\text{ finite},\ m_v=0,\\
\mathbf R_{>0},&v\in\mathfrak m_\infty,\\
K_v^\times,&v\mid\infty,\ v\notin\mathfrak m_\infty.
\end{cases}
\tag{1}
\]
Put \(U(\mathfrak m)=\prod_v U_v(\mathfrak m)\subset J_K\), and let \(C(\mathfrak m)\) be its image in \(C_K\).

Let \(I^{\mathfrak m}\) be the group of fractional ideals supported on finite primes not dividing \(\mathfrak m_f\). Define \(P_{\mathfrak m,1}\) to consist of the principal ideals \((a)\) for which
\[
a\in1+\mathfrak p_v^{m_v}\mathcal O_v\quad(v\mid\mathfrak m_f),
\qquad a_v>0\quad(v\in\mathfrak m_\infty).
\tag{2}
\]
The finite condition is a multiplicative local congruence, denoted \(a\equiv1\pmod{\mathfrak m_f}\); it forces \(a\) to be a unit at the primes in question, but does not require it to be integral everywhere. The **ray class group** is
\[
\operatorname{Cl}_{\mathfrak m}=I^{\mathfrak m}/P_{\mathfrak m,1}.
\tag{3}
\]

### From ideal classes to idèle classes

Choose a uniformizer \(\pi_{\mathfrak p}\) at each prime outside \(\mathfrak m_f\). An ideal \(\mathfrak a=\prod\mathfrak p^{e_{\mathfrak p}}\) gives the idèle with components \(\pi_{\mathfrak p}^{e_{\mathfrak p}}\) there and \(1\) elsewhere. Changing a uniformizer multiplies by units already in (1). This defines a canonical map
\[
I^{\mathfrak m}\longrightarrow C_K/C(\mathfrak m).
\]
It is onto. Given an idèle \(x\), weak approximation chooses \(a\in K^\times\) such that \(ax_v\) belongs to the deep unit group in (1) at each finite divisor of \(\mathfrak m_f\), and is positive at every selected real place. Outside these places, form the ideal with valuations \(v(ax_v)\). Removing its uniformizer idèle leaves an element of \(U(\mathfrak m)\).

Its kernel is \(P_{\mathfrak m,1}\). Indeed if a uniformizer idèle \(j\) equals \(a u\), with \(u\in U(\mathfrak m)\), its component \(1\) at each modulus prime forces \(a\) to satisfy (2), and its outside valuations give exactly the ideal \((a)\). The same argument at selected real places forces positivity. Conversely a generator satisfying (2) differs from its ideal's uniformizer idèle by an element of \(U(\mathfrak m)\). Hence
\[
\operatorname{Cl}_{\mathfrak m}\xrightarrow{\sim}C_K/C(\mathfrak m).
\tag{4}
\]

The group is finite. More explicitly, with \(E_K=\mathcal O_K^\times\), there is an exact sequence
\[
E_K\longrightarrow
(\mathcal O_K/\mathfrak m_f)^\times\times\{\pm1\}^{|\mathfrak m_\infty|}
\longrightarrow\operatorname{Cl}_{\mathfrak m}
\longrightarrow\operatorname{Cl}_K\longrightarrow1.
\tag{5}
\]
When \(\mathfrak m_f=(1)\), the residue factor means the trivial group. The first map is reduction and the selected real signs. For the second, use weak approximation to choose an element with the specified residue units and signs and take its principal ideal class. Changing this element changes the ideal by a generator satisfying (2). Its ray class is trivial exactly when its residues and signs come from a global unit: divide by a ray-principal generator and use equality of the principal ideals. Finally every ordinary ideal class has a representative prime to \(\mathfrak m_f\), by weak approximation at those finitely many primes. The kernel of forgetting the ray condition is precisely the principal ideals just described. This proves (5), and finiteness follows from the finite residue and sign groups and the finite ordinary class group.

Under our convention \(\operatorname{Cl}_{(1)}=\operatorname{Cl}_K\). Selecting all real places, with finite modulus \((1)\), gives the narrow class group. Some accounts build total positivity into every modulus; converting their convention requires adding all the real places to ours. Keeping this choice explicit prevents exchanging the ordinary and narrow class fields.

## 2. Frobenius and the ideal Artin map

Let \(L/K\) be finite abelian and unramified at every finite prime outside \(\mathfrak m_f\). Define
\[
\psi_{L/K}:I^{\mathfrak m}\longrightarrow\operatorname{Gal}(L/K),
\qquad
\mathfrak p\longmapsto\operatorname{Frob}_{\mathfrak p},
\tag{6}
\]
extended multiplicatively, allowing negative ideal exponents. Arithmetic Frobenius acts on the residue field by \(z\mapsto z^{N\mathfrak p}\). Since the extension is abelian, the automorphism is independent of the prime chosen above \(\mathfrak p\).

**Proposition 18.1.** The ideal symbol of \(\mathfrak a\) in (6) is the global reciprocity symbol of its uniformizer idèle.

**Proof.** At an unramified prime, local reciprocity takes any uniformizer to arithmetic Frobenius, and takes units to \(1\). Theorem 16.4 identifies insertion of this local symbol with the global symbol. Multiplying over the support of \(\mathfrak a\) gives (6). Negative exponents give inverse Frobenius powers, as required for fractional ideals. \(\square\)

If \(C(\mathfrak m)\) is contained in the norm group of \(L\), (4) and global reciprocity therefore make (6) onto and kill \(P_{\mathfrak m,1}\). We next determine exactly when that containment holds.

## 3. The conductor, including real places

For a finite place \(v\), choose \(w\mid v\) and let \(a_v\) be the least integer \(a\geq0\) such that
\[
U_v^{(a)}\subseteq N_{L_w/K_v}L_w^\times,
\qquad U_v^{(0)}=\mathcal O_v^\times.
\tag{7}
\]
This is the local conductor exponent of Proposition 10.4. It is finite by continuity, independent of \(w\), and zero at unramified places. At a real place put \(a_v=1\) if it becomes complex, and \(a_v=0\) otherwise; complex places have exponent zero.

**Proposition 18.3 (local description of the global conductor).** The smallest modulus \(\mathfrak f(L/K)\) satisfying \(C(\mathfrak m)\subseteq N_{L/K}C_L\) is
\[
\mathfrak f(L/K)=
\prod_{v\text{ finite}}\mathfrak p_v^{a_v}
\prod_{v\text{ real},\ L_w=\mathbf C}v.
\tag{8}
\]
More precisely,
\[
C(\mathfrak m)\subseteq N_{L/K}C_L
\quad\Longleftrightarrow\quad\mathfrak f(L/K)\mid\mathfrak m.
\tag{9}
\]
A place ramifies in \(L\) exactly when it occurs in (8), where real ramification means complexification.

**Proof.** A local element inserted at a single place has trivial global symbol exactly when its local symbol is trivial: the local decomposition group embeds in the global Galois group. Thus containment on the left of (9) forces every group \(U_v(\mathfrak m)\) into its local norm group. Conversely, if this holds at every place, all the local symbols of an idèle in \(U(\mathfrak m)\) are trivial, and its global product symbol is trivial. The norm-kernel theorem gives the containment. The least finite level is precisely (7). At a complexified real place the norm group is \(\mathbf R_{>0}\), so that place must be selected; at every other infinite place all local elements are norms. This proves (8)–(9). Proposition 10.4 identifies positive finite conductor with nontrivial inertia, proving the final assertion. \(\square\)

The argument tests *each local group* inside the subgroup. One particular global norm class need not have each of its components a local norm, since its local symbols can cancel. For example the principal idèle \(-1\) in \(\mathbf Q(i)/\mathbf Q\) has nontrivial symbols at \(2\) and infinity, whose product is \(1\). Testing single-place insertions is what makes (9) valid.

Equivalently, the finite exponent \(a_v\) is the maximum of the conductor exponents of the restrictions of all characters of \(\operatorname{Gal}(L/K)\) to its local decomposition group. Characters separate that finite abelian group, so killing all these restrictions is exactly killing the group-valued local symbol. Proposition 10.4 proves the character formula and its upper-ramification interpretation, including wild ramification.

## 4. Artin reciprocity for ideals

Let \(I_L^{\mathfrak m}\) denote fractional ideals of \(L\) prime to every prime above \(\mathfrak m_f\). Its norm is the usual ideal norm; in particular
\(N_{L/K}\mathfrak q=\mathfrak p^{f(\mathfrak q/\mathfrak p)}\).

**Theorem 18.2 (ideal reciprocity).** If \(\mathfrak f(L/K)\mid\mathfrak m\), then
\[
\ker\psi_{L/K}=P_{\mathfrak m,1}\,N_{L/K}I_L^{\mathfrak m},
\qquad
I^{\mathfrak m}/\bigl(P_{\mathfrak m,1}N_{L/K}I_L^{\mathfrak m}\bigr)
\xrightarrow{\sim}\operatorname{Gal}(L/K).
\tag{10}
\]

**Proof.** By (9), the global symbol factors through (4); Proposition 18.1 identifies that factor with the ideal symbol, which is therefore onto. It remains to identify the image of the norm subgroup in the ray quotient.

Take \(y\in J_L\). Multiplying by a principal element of \(L\), weak approximation makes its components above \(\mathfrak m_f\) sufficiently close to \(1\) that their local norms belong to (1). It also makes its real components above the selected real places positive; norms from complex components are positive automatically. This normalization is possible simultaneously at these finitely many places, and does not change its norm class. The ideal
\(\mathfrak b=\prod_{\mathfrak q\nmid\mathfrak m_f}\mathfrak q^{v_{\mathfrak q}(y_{\mathfrak q})}\)
is now prime to \(\mathfrak m_f\). The local valuation formula
\[
v_{\mathfrak p}\bigl((Ny)_{\mathfrak p}\bigr)
=\sum_{\mathfrak q\mid\mathfrak p}f(\mathfrak q/\mathfrak p)
v_{\mathfrak q}(y_{\mathfrak q})
\tag{11}
\]
shows that the image of \(Ny\) under (4) is the ray class of \(N\mathfrak b\). Conversely a uniformizer idèle for any \(\mathfrak b\in I_L^{\mathfrak m}\) has norm with exactly that ray class, by (11), and with component \(1\) at the modulus primes and at infinity. Thus the image of \(NC_L\) is
\(P_{\mathfrak m,1}NI_L^{\mathfrak m}/P_{\mathfrak m,1}\).
Applying the norm-kernel theorem proves (10). \(\square\)

In particular, if \(\mathfrak p\nmid\mathfrak m_f\), its residue degree in \(L\) is the order of its class in the quotient in (10); it has \([L:K]/f\) primes above it. Its Frobenius is trivial exactly when it splits completely. This converts a splitting problem into a test in an explicit ideal group.

## 5. Ray class fields and Takagi’s formulation

**Theorem 18.4.** For every modulus \(\mathfrak m\) there is a unique finite abelian **ray class field** \(K_{\mathfrak m}/K\) with norm group \(C(\mathfrak m)\), and
\[
\operatorname{Gal}(K_{\mathfrak m}/K)\simeq\operatorname{Cl}_{\mathfrak m}.
\tag{12}
\]
A finite abelian \(L/K\) lies in \(K_{\mathfrak m}\) exactly when its conductor divides \(\mathfrak m\). If \(\mathfrak m\mid\mathfrak n\), then \(K_{\mathfrak m}\subseteq K_{\mathfrak n}\).

**Proof.** The group \(U(\mathfrak m)\) is open in the restricted product, so its image \(C(\mathfrak m)\) is open. Equation (4) and finiteness from (5) give finite index. Theorem 17.1 constructs its unique class field, and Theorem 16.4 gives (12). The reversed-inclusion correspondence and (9) prove the conductor criterion. Finally (1) gives \(C(\mathfrak n)\subseteq C(\mathfrak m)\), so field inclusion reverses that subgroup inclusion. \(\square\)

The conductor of \(K_{\mathfrak m}\) divides \(\mathfrak m\); equality need not hold. Different moduli can give the same ray class field. For instance \(\operatorname{Cl}_{2\infty}(\mathbf Q)\) is trivial, as (5) or the unit decomposition of lesson 17 shows, so this modulus gives \(\mathbf Q\) itself.

**Proposition 18.5 (Takagi’s congruence subgroups).** For fixed \(\mathfrak m\), the subgroups
\[
P_{\mathfrak m,1}\subseteq H\subseteq I^{\mathfrak m}
\tag{13}
\]
correspond with reversed inclusions to the subextensions of \(K_{\mathfrak m}/K\). Their class field \(L\) has ideal Artin kernel \(H\) and
\[
\operatorname{Gal}(L/K)\simeq I^{\mathfrak m}/H.
\tag{14}
\]
Every finite abelian extension appears for some modulus.

**Proof.** Use (4) to regard \(H/P_{\mathfrak m,1}\) as a subgroup of the finite quotient \(C_K/C(\mathfrak m)\). Its inverse image \(\widetilde H\subset C_K\) is open of finite index and contains \(C(\mathfrak m)\). Theorem 17.1 gives a unique class field \(L\), and reversed inclusion places it in \(K_{\mathfrak m}\). Proposition 18.1 and finite reciprocity show that its ideal kernel is exactly \(H\), giving (14). Conversely each subextension yields such a subgroup. A finite abelian extension has the finite conductor (8), hence lies in its conductor ray field. This proves the final assertion and equivalence with the idèlic formulation. \(\square\)

For a larger modulus \(\mathfrak n\) divisible by \(\mathfrak m\), the same field is represented by \(H\cap I^{\mathfrak n}\). Indeed the ideal Artin map for \(\mathfrak n\) is the restriction of (6), and its kernel is this intersection. The surjection \(\operatorname{Cl}_{\mathfrak n}\to\operatorname{Cl}_{\mathfrak m}\) is equally the quotient map from \(C(\mathfrak n)\subseteq C(\mathfrak m)\). Thus changing the modulus preserves the field when the congruence subgroup is changed compatibly.

## 6. Quadratic conductors over the rationals

Let \(d\ne1\) be a nonzero squarefree integer and \(L=\mathbf Q(\sqrt d)\). Its fundamental discriminant is
\[
D=\begin{cases}d,&d\equiv1\pmod4,\\4d,&d\not\equiv1\pmod4.\end{cases}
\tag{15}
\]
We claim
\[
\mathfrak f(L/\mathbf Q)=
\begin{cases}
|D|,&d>0,\\
|D|\infty,&d<0.
\end{cases}
\tag{16}
\]
Here \(\infty\) is the real place, a factor of the modulus, not a numeric multiplier.

We verify every local factor, independently of a later global conductor–discriminant formula. The quadratic local norm character on \(\mathbf Q_p^\times\) is \(b\mapsto(b,d)_p\). At an odd prime dividing \(d\), the odd-place formula of Theorem 11.4 restricts on units to \(u\mapsto(u/p)\). It is nontrivial on all units and trivial on \(1+p\mathbf Z_p\), so its conductor exponent is \(1\). At an odd prime not dividing \(d\), the formula is trivial on units and the exponent is \(0\).

For an odd \(2\)-adic unit write
\[
\epsilon(u)=\frac{u-1}{2}\pmod2,
\qquad\omega(u)=\frac{u^2-1}{8}\pmod2.
\]
If \(d\) is odd, the unit character is
\[
(u,d)_2=(-1)^{\epsilon(u)\epsilon(d)}.
\tag{17}
\]
For \(d\equiv1\pmod4\) this is trivial, giving exponent \(0\). For \(d\equiv3\pmod4\) it is nontrivial on units, including \(u=3\), but trivial on \(1+4\mathbf Z_2\). Its exponent is \(2\), since \(U_2^{(1)}=\mathbf Z_2^\times\).

If \(d=2e\) with \(e\) odd, the character is
\[
(u,2e)_2=(-1)^{\epsilon(u)\epsilon(e)+\omega(u)}.
\tag{18}
\]
It is trivial on \(1+8\mathbf Z_2\), while \(u=5\in1+4\mathbf Z_2\) gives \(-1\). Its exponent is \(3\). These are exactly the \(2\)-adic exponents of \(|D|\) in (15). Finally the real extension is trivial for \(d>0\) and complex for \(d<0\). Proposition 18.3 now proves (16), including its sign condition.

For instance \(\mathbf Q(\sqrt5)\) has conductor \(5\), \(\mathbf Q(i)\) has conductor \(4\infty\), and \(\mathbf Q(\sqrt{-3})\) has conductor \(3\infty\). Keeping the real factor distinguishes the latter two fields from the corresponding real ray fields.

## 7. A ray field over the Gaussian rationals

Take \(K=\mathbf Q(i)\) and modulus \((3)\). The ring \(\mathbf Z[i]\) is Euclidean: approximate the real and imaginary parts of a complex quotient by integers, leaving remainder norm at most one half the divisor norm. Thus its class group is trivial. Since \(X^2+1\) is irreducible over \(\mathbf F_3\),
\[
\mathbf Z[i]/(3)\simeq\mathbf F_9,
\qquad (\mathbf Z[i]/(3))^\times\simeq\mathbf Z/8.
\]
The four units \(\{\pm1,\pm i\}\) have distinct reductions. Sequence (5) gives
\[
\operatorname{Cl}_{(3)}\simeq
\mathbf F_9^\times/\{\pm1,\pm i\}\simeq\mathbf Z/2.
\tag{19}
\]
Its ray field is
\[
K_{(3)}=\mathbf Q(i,\sqrt3)=\mathbf Q(\zeta_{12}).
\tag{20}
\]

To identify it, not merely predict its degree, let \(L=K(\sqrt3)\). The element \(3\) is not a square in \(K\): squaring \(a+bi\), with \(a,b\in\mathbf Q\), forces \(ab=0\), and neither remaining rational square equation is possible. Thus \([L:K]=2\). At the prime \((3)\), \(X^2-3\) is Eisenstein over the unramified quadratic completion of \(\mathbf Q_3\), and the quadratic extension is tame. Its conductor exponent is \(1\), by Proposition 10.4 and the tame unit symbol of Proposition 11.3.

At the prime above \(2\), adjoining \(\sqrt3\) is the same as adjoining \(\sqrt{-3}\), since \(i\in K\). The field \(\mathbf Q_2(\sqrt{-3})=\mathbf Q_2(\sqrt5)\) is the unramified quadratic extension: their defining units differ by a square because \(-3/5\equiv1\pmod8\). The odd-unit square criterion and unramified quadratic field were proved in lessons 10–11. Base change of an unramified local extension remains unramified or split, by lifting its separable residue-field polynomial. Hence the prime over \(2\) contributes no conductor. At every other finite prime, the unit radical of order \(2\) gives an unramified or split extension; the archimedean places of \(K\) are complex. Thus \(\mathfrak f(L/K)=(3)\).

Theorem 18.4 places \(L\) in \(K_{(3)}\). Both have degree \(2\), by (19), so they coincide. Finally
\(\zeta_{12}=(\sqrt3+i)/2\), while \(i=\zeta_{12}^3\) and \(\sqrt3=\zeta_{12}+\zeta_{12}^{-1}\); this proves the second equality in (20).

## 8. What changes over a function field

For a function field over full constants \(\mathbf F_q\), use divisors instead of fractional ideals, and finite place powers instead of an archimedean sign set. The uniformizer map and weak-approximation proof of (4) give the divisor ray group as \(C_K/C(\mathfrak m)\). Here \(C(\mathfrak m)\) has degree zero. Consequently there is an exact sequence
\[
0\longrightarrow C_K^1/C(\mathfrak m)
\longrightarrow C_K/C(\mathfrak m)
\xrightarrow{\deg}\mathbf Z\longrightarrow0.
\tag{21}
\]
The left group is finite because \(C_K^1\) is compact and \(C(\mathfrak m)\) is open. The right group is infinite. Thus this entire divisor ray group does not correspond to a finite ray extension: constant extensions of every degree satisfy the same unit conditions. To specify a finite class field, impose an additional finite-index degree condition. For example, choose a degree-one class \(c\) and take the subgroup generated by \(C(\mathfrak m)\) and \(c^d\), with \(d>0\); (21) shows that its index is \(d\,|C_K^1/C(\mathfrak m)|\), so Theorem 17.1 applies. Other subgroups of finite index give the corresponding general extensions.

The local conductor and ideal-symbol arguments remain valid in this setting, with no real factors and with divisors prime to the finite modulus. This degree condition is why the number-field finiteness proof of a ray class group should not simply be repeated for the full function-field divisor group.

## 9. Exercises and complete solutions

### Exercise 1 — Quadratic conductors (easy)

Determine the conductor of \(\mathbf Q(\sqrt d)/\mathbf Q\) for a nontrivial squarefree \(d\).

**Solution.** Each odd divisor of \(d\) has unit character \((u/p)\), giving exponent \(1\); every other odd prime gives exponent \(0\). At \(2\), formula (17) gives exponent \(0\) when \(d\equiv1\pmod4\) and exponent \(2\) when \(d\equiv3\pmod4\). For even \(d\), formula (18) kills \(U_2^{(3)}\) and is nontrivial on \(5\in U_2^{(2)}\), giving exponent \(3\). Their product is \(|D|\), with \(D\) as in (15). Add the real place exactly when \(d<0\). This is (16); omitting that place for an imaginary quadratic extension would violate the local norm condition at infinity.

### Exercise 2 — The Gaussian ray group (medium)

Compute \(\operatorname{Cl}_{(3)}(\mathbf Q(i))\) and identify its class field.

**Solution.** Euclideanity gives ordinary class number \(1\). The residue unit group at the inert prime \((3)\) has order \(8\), and the global units have four distinct residues. Sequence (5) gives a cyclic quotient of order \(2\). The quadratic extension \(K(\sqrt3)/K\) has tame conductor exponent \(1\) at \((3)\), is unramified at \(2\) because it is the base change of the unramified extension \(\mathbf Q_2(\sqrt{-3})\), and is unramified at every other finite prime. There are no real places. Its conductor is \((3)\), so it lies in the degree-two ray field and equals it. The explicit identities following (20) identify it with \(\mathbf Q(\zeta_{12})\).

### Exercise 3 — Increasing the modulus (medium)

Prove \(K_{\mathfrak m}\subseteq K_{\mathfrak n}\) for \(\mathfrak m\mid\mathfrak n\), and describe the resulting map on ray groups.

**Solution.** Increasing finite exponents shrinks the principal-unit groups, and adding a real place replaces \(\mathbf R^\times\) by \(\mathbf R_{>0}\). Thus \(U(\mathfrak n)\subseteq U(\mathfrak m)\) and \(C(\mathfrak n)\subseteq C(\mathfrak m)\). The class field correspondence reverses that inclusion. Restriction of Galois automorphisms is the surjective quotient map
\(C_K/C(\mathfrak n)\to C_K/C(\mathfrak m)\).
Under (4) this is the ideal map induced by \(I^{\mathfrak n}\subseteq I^{\mathfrak m}\). Its surjectivity is already proved by the idèle quotient description; no unsupported assertion about moving ideals past new modulus primes is needed.

### Exercise 4 — Congruence subgroups (hard)

Prove Proposition 18.5, including its converse and its compatibility with the idèlic correspondence.

**Solution.** Given \(P_{\mathfrak m,1}\subseteq H\subseteq I^{\mathfrak m}\), use the isomorphism (4) to lift \(H/P_{\mathfrak m,1}\) to a subgroup \(\widetilde H\) of \(C_K\) containing \(C(\mathfrak m)\). It has finite index and is open, since the quotient ray group is finite and \(C(\mathfrak m)\) is open. Existence gives its unique abelian class field \(L\). Containment of norm groups puts \(L\) inside \(K_{\mathfrak m}\). On a prime away from the modulus the quotient map is the Frobenius map, by Proposition 18.1; therefore its ideal kernel is exactly \(H\), and its quotient is (14). Conversely for a subextension \(L\), take its norm group, pass to the quotient by \(C(\mathfrak m)\), and pull back through (4); these operations reverse the construction. They also reverse inclusions and agree with restriction and norm. Every finite abelian \(L\) has conductor (8), so the construction includes it after choosing that modulus.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The local conductor criterion, optional real modulus, idèle-to-ideal ray identification, norm kernel, Takagi correspondence and decomposition law are proved with the stated fractional-ideal conventions.

- [Jürgen Neukirch, Class Field Theory — The Bonn Lectures, Online Edition 2.0 (May 2015), edited by Alexander Schmidt](https://www.mathi.uni-heidelberg.de/~schmidt/Neukirch-en/Neukirch_cft_02_may15.pdf).
- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
