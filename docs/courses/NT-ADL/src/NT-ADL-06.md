# Quasi-characters and Hecke characters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Hecke character assigns compatible multiplicative data to all completions of a number field. The compatibility is the requirement that a diagonal nonzero field element have value one. This explains both the inverse on the ramified units of a Dirichlet character and the relation between an ideal character's infinity type and its actual archimedean idèlic component.

Let \(K\) be a number field, \(J_K\) its idèle group, and \(C_K=J_K/K^\times\). We use the normalized absolute values of [Idèles and the idèle class group](NT-ADL-03.md): at a finite place with residue cardinality \(q_v\), \(|\pi_v|_v=q_v^{-1}\), and at a complex place \(|z|_v=z\bar z\). Put \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). A **quasi-character** has values in \(\mathbb C^\times\); a **character** has values in \(\mathbb T\). Every homomorphism called a character or quasi-character here is continuous unless its domain is a discrete ideal group.

We use weak approximation, compactness of \(C_K^1\), and the ray class identifications from the preceding lessons. Local unit filtrations and the decomposition of a finite local multiplicative group are the prerequisites stated under *Prerequisites and further directions*. The ideal comparison below follows the classical definition of a Größencharakter, as in [Shurman, Definition 2.2], with its conventions translated explicitly.

## Local parameters and conductors

Let \(F\) be a finite extension of \(\mathbb Q_p\), with integral ring \(\mathcal O_F\), maximal ideal \(\mathfrak p\), and uniformizer \(\pi\). Define
\[
 U^{(0)}=\mathcal O_F^\times,\qquad
 U^{(n)}=1+\mathfrak p^n\quad(n\geq1).
 \tag{1}
\]
The value \(n=0\) is specified separately: \(1+\mathcal O_F\) is not the definition of \(U^{(0)}\).

**Proposition 6.1.** Every local quasi-character has the following form.

1. Over \(F\), choose \(A\in\mathbb C^\times\) and a finite-image continuous character \(\eta:\mathcal O_F^\times\to\mathbb T\). Then
   \[
   c(\pi^j u)=A^j\eta(u),\qquad j\in\mathbb Z,
   \quad u\in\mathcal O_F^\times,
   \tag{2}
   \]
   gives all quasi-characters, with unique parameters for the chosen \(\pi\). Its conductor exponent is
   \[
   a(c)=\min\{n\geq0:c(U^{(n)})=1\}.
   \tag{3}
   \]
   It is unramified exactly when \(a(c)=0\), equivalently when \(c=|\cdot|_F^s\) for some \(s\in\mathbb C\). Such an \(s\) is determined modulo \(2\pi i/\log q\).
2. Over \(\mathbb R\), the unique parameters are \(\epsilon\in\{0,1\}\) and \(s\in\mathbb C\), and
   \[
   c(x)=\operatorname{sgn}(x)^\epsilon |x|^s.
   \tag{4}
   \]
3. Over \(\mathbb C\), the unique parameters are \(n\in\mathbb Z\) and \(s\in\mathbb C\), and
   \[
   c(z)=\left(\frac{z}{|z|}\right)^n |z|_{\mathbb C}^s.
   \tag{5}
   \]
   In \(z/|z|\), the denominator is the ordinary complex modulus, so \(|z|_{\mathbb C}=|z|^2\).

In all three cases there is a unique real number \(\sigma(c)\) such that
\[
 |c(x)|=|x|_F^{\sigma(c)}.
 \tag{6}
\]
Consequently \(c=\omega|\cdot|_F^{\sigma(c)}\) with a unique unitary \(\omega\). One may instead use a complex exponent \(s\) with \(\operatorname{Re}s=\sigma(c)\), absorbing its imaginary part into \(\omega\); that decomposition is not unique.

*Proof.* We first record the small-neighborhood argument used several times below. The neighborhood
\[
 W=\{z\in\mathbb C^\times:1/2<|z|<2,
                  \ |\arg z|<\pi/2\}
 \tag{7}
\]
contains no nontrivial subgroup. Indeed, all positive and negative powers of a subgroup element lie in \(W\), forcing its modulus to be one. A nonidentity point of the circle has an integral power outside the indicated arc: represent its angle in \((-\pi,\pi]\); if its absolute value is smaller than \(\pi/2\), the least positive multiple reaching \(\pi/2\) has absolute value less than \(\pi\).

The image of the compact group \(\mathcal O_F^\times\) under \(|c|\) is a compact subgroup of \(\mathbb R_{>0}\). Taking logarithms shows it is trivial, since a nonzero real number has unbounded multiples. Thus \(\eta=c|_{\mathcal O_F^\times}\) is unitary. Continuity provides some \(U^{(n)}\) whose image lies in \(W\), and the subgroup argument makes that image trivial. The finite quotient \(\mathcal O_F^\times/U^{(n)}\) then gives finite image. The topological decomposition \(F^\times=\pi^{\mathbb Z}\times\mathcal O_F^\times\) proves (2), its converse, and the existence of (3).

If \(\eta=1\), choose \(s\) with \(e^{-s\log q}=A\). Conversely a norm power is trivial on the units. Equality of two exponents is equivalent to \(e^{-(s-s')\log q}=1\), giving the stated period. Taking
\[
 \sigma(c)=-\frac{\log|A|}{\log q}
 \tag{8}
\]
proves (6) in the finite case.

A continuous homomorphism \(h:(\mathbb R,+)\to\mathbb C^\times\) has the form \(h(t)=e^{(a+ib)t}\), for unique real \(a,b\). To see this, \(\log|h(t)|\) is continuous additive, hence equals \(at\), first on rational multiples of a fixed real argument and then by continuity. For the unitary part, choose a continuous argument near zero. On a sufficiently small interval the homomorphism law makes that argument additive, because the discrepancy is an integral multiple of \(2\pi\), continuous and zero at the origin. It is therefore \(bt\) there; subdivision extends the formula to every \(t\). Uniqueness follows by varying \(t\) over an interval.

Apply this to \(t\mapsto c(e^t)\). Since \(c(-1)^2=1\), the decomposition \(\mathbb R^\times=\{\pm1\}\times\mathbb R_{>0}\) gives (4). For \(\mathbb C^\times=\mathbb T\times\mathbb R_{>0}\), compactness again makes the restriction to the circle unitary. Pulled back along \(t\mapsto e^{it}\), that restriction is \(e^{ibt}\); period \(2\pi\) forces \(b\in\mathbb Z\). The radial homomorphism is \(r\mapsto r^{2s}\). This proves (5) and uniqueness. Taking real parts proves (6), and division by that norm power gives the unique unitary factor. ∎

Finite-order archimedean characters are especially simple. Connectedness of \(\mathbb R_{>0}\) and \(\mathbb C^\times\) makes their image in a finite group trivial. Thus they are sign characters at real places and trivial at complex places. The integer \(n\) in (5) is an angular parameter, not a finite conductor exponent.

## A global character and its local restrictions

For a place \(v\), let \(j_v:K_v^\times\to J_K\) insert its argument at \(v\) and one elsewhere. Define \(c_v=c\circ j_v\).

**Proposition 6.2.** A quasi-character \(c\) of \(J_K\) is uniquely a product
\[
 c(x)=\prod_v c_v(x_v),
 \qquad c_v|_{\mathcal O_v^\times}=1
       \text{ for almost every finite }v.
 \tag{9}
\]
Conversely any such family defines a continuous quasi-character of \(J_K\). It is a Hecke quasi-character precisely when the product is one on every diagonal \(a\in K^\times\).

Every Hecke quasi-character has a unique decomposition
\[
 c(x)=\omega(x)|x|^{\sigma},\qquad
 \sigma\in\mathbb R,
 \tag{10}
\]
with \(\omega\) a unitary Hecke character. In particular it can be written \(\omega_s|\cdot|^s\) for any \(s\) with \(\operatorname{Re}s=\sigma\).

*Proof.* Continuity at one and (7) give a basic restricted-product neighborhood whose image lies in \(W\). Outside a finite set \(S\) of places, that neighborhood contains the entire subgroup
\[
 H_S=\prod_{v\notin S}\mathcal O_v^\times,
 \tag{11}
\]
embedded with coordinates one on \(S\). Consequently \(c(H_S)=1\). This proves almost-all unramifiedness and, more strongly, triviality on the whole compact tail. Given \(x\), enlarge \(S\) to contain its nonunit coordinates. The idèle splits into finitely many supported local factors and an element of \(H_S\), proving (9). This also proves uniqueness. Conversely (9) is a finite product on each open restricted-product chart containing all exceptional places. It is continuous on that chart and hence on \(J_K\). Triviality on \(K^\times\) is exactly the condition for descent through the quotient map to \(C_K\).

Now suppose \(c\) descends to \(C_K\). Its absolute value on compact \(C_K^1\) is a compact subgroup of \(\mathbb R_{>0}\), hence trivial. The norm therefore induces a homomorphism \(|c|:\mathbb R_{>0}\to\mathbb R_{>0}\). It is continuous: the norm has the continuous section constructed in Proposition 3.5. Its logarithm is continuous additive and equals \(\sigma\log t\). Thus \(|c(x)|=|x|^\sigma\). The norm is onto, so \(\sigma\) is unique. The product formula makes \(|\cdot|^\sigma\) trivial on \(K^\times\), and division proves (10). Finally set \(\omega_s=\omega|\cdot|^{\sigma-s}\), a unitary character whenever \(\operatorname{Re}s=\sigma\). ∎

All local absolute-value exponents of a Hecke quasi-character equal this same \(\sigma\): apply (10) to a supported idèle. This equality is a global consequence of compactness, rather than a condition one may omit when assembling arbitrary local quasi-characters.

Its **finite conductor** is the integral ideal
\[
 \mathfrak f(c)=\prod_{v\nmid\infty}\mathfrak p_v^{a(c_v)}.
 \tag{12}
\]
Only finitely many factors are nontrivial. Norm twists do not change it. For an integral ideal \(\mathfrak m\), write
\[
 U_f(\mathfrak m)=\prod_{v\mid\infty}\{1\}
          \times\prod_{v\nmid\infty}U_v^{(\operatorname{ord}_v\mathfrak m)}.
 \tag{13}
\]
Then \(c(U_f(\mathfrak m))=1\) if and only if \(\mathfrak f(c)\mid\mathfrak m\). Necessity follows from the supported unit groups. For sufficiency, (9) makes the value on any element of (13) a finite product of values one. This finite-conductor subgroup has archimedean coordinates one; it must be distinguished from a ray subgroup that includes archimedean identity components.

## From ideals to idèles, with the inverse fixed

Let \(I^{\mathfrak m}\) be the group of fractional ideals having valuation zero at primes dividing \(\mathfrak m\). Let
\[
 B_f(\mathfrak m)=(\mathcal O_K/\mathfrak m)^\times,
 \qquad K^{(\mathfrak m)}=
 \{a\in K^\times:\operatorname{ord}_v(a)=0\text{ for }v\mid\mathfrak m\}.
 \tag{14}
\]
For \(a\in K^{(\mathfrak m)}\), its residue in \(B_f(\mathfrak m)\) is defined by the local unit residues and the Chinese remainder theorem. This includes fractions whose denominator is coprime to \(\mathfrak m\).

A **Größencharakter modulo \(\mathfrak m\)** is a homomorphism \(\chi:I^{\mathfrak m}\to\mathbb T\) for which there are characters \(\chi_f:B_f(\mathfrak m)\to\mathbb T\) and \(\chi_\infty:K_\infty^\times\to\mathbb T\) satisfying
\[
 \chi((a))=\chi_f(a)\chi_\infty(a)
 \quad(a\in K^{(\mathfrak m)}).
 \tag{15}
\]
Here \(K_\infty^\times=\prod_{v\mid\infty}K_v^\times\). The identity for coprime integral \(a\) already implies (15) for fractions, by dividing the two identities.

**Theorem 6.3.** Größencharaktere modulo \(\mathfrak m\) correspond bijectively to unitary Hecke characters \(\omega\) with \(\mathfrak f(\omega)\mid\mathfrak m\), under the normalization
\[
 \chi(\mathfrak p_v)=\omega_v(\pi_v)
                  \quad(v\nmid\mathfrak m\infty).
 \tag{16}
\]
The auxiliary characters in (15) are uniquely determined by \(\chi\). In this correspondence
\[
 \chi_f=\left(\omega\big|_{\prod_{v\mid\mathfrak m}\mathcal O_v^\times}\right)^{-1},
 \qquad \chi_\infty=\omega_\infty^{-1},
 \tag{17}
\]
where the first restriction factors through \(B_f(\mathfrak m)\). Finite conductor exponents agree. The conductor is the smallest finite modulus to which the ideal character extends with the same infinity type.

The inverse in (17) is also the convention in Shurman, §6: the classical formula on principal ideals uses the inverse of the infinite component of the corresponding idèlic character. Thus the auxiliary ideal infinity type and the actual idèlic infinity type are inverse characters. Equation (18) below derives that inversion directly from diagonal triviality, so it also fixes the finite unit convention for Dirichlet characters.

*Proof.* Given \(\omega\), define \(\chi\) multiplicatively by (16). At these places \(\omega_v\) is unramified, so the value is independent of the uniformizer. Formula (13) ensures the restriction in (17) factors through the residue group. For diagonal \(a\in K^{(\mathfrak m)}\), (9) and \(\omega(a)=1\) give
\[
 1=\chi((a))\prod_{v\mid\mathfrak m}\omega_v(a)
                           \prod_{v\mid\infty}\omega_v(a).
 \tag{18}
\]
Rearrangement gives (15) and (17).

To prove uniqueness of \(\chi_f,\chi_\infty\), divide two candidate pairs. Their product is one on the image of \(K^{(\mathfrak m)}\) in \(B_f(\mathfrak m)\times K_\infty^\times\). That image is dense: prescribe any unit residue at the finitely many primes dividing \(\mathfrak m\) and any sufficiently small neighborhoods of nonzero archimedean targets; weak approximation supplies an element meeting all of them. Continuity makes the quotient character trivial on the whole product. Testing each factor gives uniqueness separately.

Conversely suppose (15) holds. Use the open subgroup
\[
 H^{(\mathfrak m)}=K_\infty^\times
      \times\prod_{v\mid\mathfrak m}\mathcal O_v^\times
      \times\prod_{v\nmid\mathfrak m\infty}'K_v^\times
 \tag{19}
\]
of \(J_K\), with the usual integral unit subgroups in the last restricted product. For \(x\in H^{(\mathfrak m)}\), put
\[
 \mathfrak a(x)=\prod_{v\nmid\mathfrak m\infty}
                       \mathfrak p_v^{\operatorname{ord}_v(x_v)},\qquad
 b(x)=(x_v\bmod\mathfrak p_v^{\operatorname{ord}_v\mathfrak m})_{v\mid\mathfrak m},
\]
and define
\[
 \omega_H(x)=\chi(\mathfrak a(x))
                 \chi_f(b(x))^{-1}\chi_\infty(x_\infty)^{-1}.
 \tag{20}
\]
The ideal map is continuous to a discrete group: its fibers are translates of the open subgroup with every finite coordinate a unit. The residue map is continuous to a finite group. Thus (20) is a continuous unitary homomorphism. On \(H^{(\mathfrak m)}\cap K^\times=K^{(\mathfrak m)}\), (15) makes it one.

Weak approximation gives \(J_K=H^{(\mathfrak m)}K^\times\). For each \(x\in J_K\), choose \(a\in K^\times\) with \(\operatorname{ord}_v(a)=\operatorname{ord}_v(x_v)\) at all \(v\mid\mathfrak m\); then \(h=x/a\in H^{(\mathfrak m)}\). Set \(\omega(x)=\omega_H(h)\). Two choices have ratio in \(H^{(\mathfrak m)}\cap K^\times\), so this is well-defined. Multiplying decompositions proves multiplicativity and triviality on \(K^\times\). On every open coset of \(H^{(\mathfrak m)}\), the extension is a translate of \(\omega_H\), so it is continuous. Formula (20) gives (16), (17), and triviality on (13). The two constructions agree on \(H^{(\mathfrak m)}\) and on \(K^\times\), proving they are inverse.

By the Chinese remainder theorem, \(\chi_f\) is a product of characters of \((\mathcal O_v/\mathfrak p_v^{e_v})^\times\). The least \(n\in\{0,\ldots,e_v\}\) through which its \(v\)-factor descends is exactly the least \(n\) for which \(\omega_v(U_v^{(n)})=1\), because those restrictions are inverses. Their exponents therefore match. Removing excess prime powers, or an entire prime with exponent zero, is possible by applying the first construction to the same \(\omega\) at its smaller conductor. Conversely any such ideal extension gives the same \(\omega\), by the proved uniqueness on (19) and \(K^\times\), so its modulus is divisible by (12). ∎

In particular the pair \((\chi_f,\chi_\infty)\) necessarily satisfies
\[
 \chi_f(\varepsilon)\chi_\infty(\varepsilon)=1
                  \quad(\varepsilon\in\mathcal O_K^\times).
 \tag{21}
\]
This is also sufficient for a pair to occur. Indeed it makes \((a)\mapsto\chi_f(a)\chi_\infty(a)\) a well-defined character of the principal ideals in \(I^{\mathfrak m}\). Their quotient in \(I^{\mathfrak m}\) is the ordinary class group, finite by Corollary 3.4 and the coprime-representative argument in Proposition 4.3. A character of a subgroup with finite quotient extends to the whole abelian group with values in \(\mathbb T\): adjoin a lift \(g\) of a quotient generator, let \(d\) be its order modulo the subgroup, choose a \(d\)-th root of the prescribed value on \(g^d\), and define the value on \(hg^j\) multiplicatively. The only relation to check is \(g^d\) in the subgroup, which the chosen root satisfies. Finitely many adjoining steps finish the extension. Different extensions can differ by class group characters.

## Finite order and the rational case

For a modulus \(\mathfrak m=\mathfrak m_f\mathfrak m_\infty\), with \(\mathfrak m_\infty\) a set of real places, retain the ray subgroup \(U_{\mathfrak m}\) of Theorem 4.2: its archimedean factor is \(\mathbb R_{>0}\) at selected real places, all of \(\mathbb R^\times\) at other real places, and all of \(\mathbb C^\times\) at complex places. Its finite factor is that of (13).

**Proposition 6.4.** The finite-order Hecke characters are exactly the pullbacks of characters of ray class groups
\[
 C_K/(U_{\mathfrak m}K^\times/K^\times)
           \simeq\operatorname{Cl}_{\mathfrak m}(K).
 \tag{22}
\]
Their smallest ray modulus consists of the finite conductor (12) and exactly the real places where the local sign character is nontrivial.

For \(K=\mathbb Q\), primitive Dirichlet characters \(\chi\) correspond bijectively to finite-order Hecke characters \(\omega_\chi\), normalized by
\[
 \omega_\chi(j_\ell(\ell))=\chi(\ell)\quad(\ell\nmid m),
 \qquad \omega_{\chi,\infty}=\operatorname{sgn}^{\epsilon},
 \quad \chi(-1)=(-1)^\epsilon,
 \tag{23}
\]
and by triviality on \(\mathbb R_{>0}\). On the finite unit factors at primes dividing \(m\), its restriction is \(\chi^{-1}\). Its finite conductor is the primitive Dirichlet conductor \(m\).

*Proof.* A finite-order character has finite image, so its kernel is open: choose a neighborhood of one excluding all other image points. Proposition 4.4 places a ray subgroup in that kernel, giving (22). Conversely ray class groups are finite by Proposition 4.3, so their characters have finite order.

More precisely, Proposition 6.1 shows that a finite-order character is trivial on archimedean identity components. At a real place it is either one or the sign, and at a complex place it is one. Formula (9) then proves that it kills \(U_{\mathfrak m}\) exactly when its finite conductor divides \(\mathfrak m_f\) and every nontrivial real sign occurs in \(\mathfrak m_\infty\). Necessity follows by supported factors; sufficiency follows from the entire product formula. This proves the minimality assertion.

For \(\mathbb Q\), Proposition 3.6 gives \(C_{\mathbb Q}=\mathbb R_{>0}\times\widehat{\mathbb Z}^{\times}\). Explicitly, for an idèle \(x\), put
\[
 q_x=\operatorname{sgn}(x_\infty)\prod_p p^{\operatorname{ord}_p(x_p)},
 \quad t_x=x_\infty/q_x>0,
 \quad u_{x,p}=x_p/q_x\in\mathbb Z_p^\times.
 \tag{24}
\]
The product is finite. Multiplication by a diagonal rational number does not change \((t_x,u_x)\). Define
\[
 \omega_\chi(x)=\chi(u_x\bmod m)^{-1}.
 \tag{25}
\]
This is a continuous finite-order character and trivial on diagonal rationals. At \(j_\ell(\ell)\), for \(\ell\nmid m\), one has \(q_x=\ell\) and \(u_x\bmod m=\ell^{-1}\), proving the first formula in (23). A supported positive real coordinate changes only \(t_x\); a negative one has \(q_x=-1\) and residue \(-1\), proving the second formula. A supported finite unit changes exactly that unit coordinate, giving the inverse restriction.

For completeness these conditions determine the ramified uniformizer values too. Factor the Dirichlet character by the Chinese remainder theorem as
\[
 \chi=\prod_{p\mid m}\chi_p,
 \qquad \chi_p:(\mathbb Z/p^{e_p}\mathbb Z)^\times\to\mathbb T.
 \tag{26}
\]
At \(p\mid m\), for \(x_p=p^j u\), (24) gives \(q_x=p^j\), unit coordinate \(u\) at \(p\), and unit \(p^{-j}\) at every other prime dividing \(m\). Hence
\[
 \omega_{\chi,p}(p^j u)=
       \left(\prod_{r\mid m,\ r\ne p}\chi_r(p)\right)^j
                                      \chi_p(u)^{-1}.
 \tag{27}
\]
At \(p\nmid m\), the formula is instead \(\omega_{\chi,p}(p^j u)=\chi(p)^j\). Thus ramified uniformizers need not all have value one. Their unit conductors are the least exponents through which \(\chi_p\) factors, so the product of their prime powers is \(m\) when \(\chi\) is primitive.

Conversely a finite-order character of \(C_{\mathbb Q}\) kills the connected factor \(\mathbb R_{>0}\). Its restriction to \(\widehat{\mathbb Z}^{\times}\) has open kernel and hence contains
\[
 V_m=\prod_{p\mid m}(1+p^{e_p}\mathbb Z_p)
                \times\prod_{p\nmid m}\mathbb Z_p^\times
 \tag{28}
\]
for some \(m\), with the displayed factors interpreted as the units congruent to one. Reduction identifies the quotient with \((\mathbb Z/m\mathbb Z)^\times\). The inverse of its quotient character is \(\chi\) in (25). At each prime choose the least possible exponent; (26) then produces the unique primitive Dirichlet character. This includes the trivial character of conductor one and the absence of a primitive nontrivial character of conductor two. ∎

For example, if \(p\) is odd and \(\chi(a)=(a/p)\) is the Legendre symbol, (27) becomes
\[
 \omega_{\chi,p}(p^j u)=\left(\frac{\bar u}{p}\right),\qquad
 \omega_{\chi,\ell}(\ell)=\left(\frac{\ell}{p}\right)\ (\ell\ne p),\qquad
 \omega_{\chi,\infty}=\operatorname{sgn}^{(p-1)/2\bmod2}.
 \tag{29}
\]
The parity in (29) can be checked directly. Pairing each nonzero residue with its inverse shows that \((p-1)!\equiv-1\pmod p\), since only \(1,-1\) are their own inverses. Pairing \(a\) with \(p-a\) then gives \(((p-1)/2)!^2\equiv(-1)^{(p+1)/2}\). If \(p\equiv1\pmod4\), this exhibits a square root of \(-1\). If \(p\equiv3\pmod4\), a square root \(b\) would give \(b^{p-1}=(-1)^{(p-1)/2}=-1\), contradicting Lagrange's theorem in the multiplicative group of the finite field. Thus \(\chi(-1)=(-1)^{(p-1)/2}\).

The inverse on the units is invisible for this quadratic character, but remains essential for higher-order Dirichlet characters. For a concrete composite example, modulo \(15\) take the nontrivial quadratic \(\chi_3\) and the character \(\chi_5\) with \(\chi_5(2)=i\). Since \(2\) has order four modulo \(5\), this defines \(\chi_5\). Both factors are primitive, so their product has conductor \(15\). Formula (27) gives
\[
 \omega_{\chi,3}(3)=\chi_5(3)=-i,
 \qquad \omega_{\chi,5}(5)=\chi_3(5)=-1.
 \tag{30}
\]
Here \(\chi(-1)=(-1)(-1)=1\), so the real component is trivial. On diagonal \(3\), the other ramified local value is \(\chi_5(3)^{-1}=i\), canceling \(-i\); on diagonal \(5\), the two ramified values are both \(-1\). These checks exhibit why the local uniformizer values and the inverse unit values belong to the same construction.

## Angular characters over the Gaussian field

The integral ring of \(\mathbb Q(i)\) is \(\mathbb Z[i]\), as checked in Solution 2 of *The adèle ring of a number field*. It is Euclidean for \(N(a)=|a|^2\): round both coordinates of \(a/b\) to integers to obtain \(q\in\mathbb Z[i]\) with \(N(a-bq)\leq N(b)/2<N(b)\). Euclidean division makes every ideal principal. The units have norm one, hence are \(\{1,-1,i,-i\}\). Therefore, for \(k\in\mathbb Z\),
\[
 \chi_k((a))=\left(\frac{a}{|a|}\right)^{4k}
                    \quad(a\in\mathbb Q(i)^\times)
 \tag{31}
\]
is a well-defined multiplicative character of all fractional ideals. Multiplying a generator by a unit changes its angular factor by a fourth root of unity, which disappears in the exponent \(4k\). Equation (15) holds with finite part one and ideal infinity type \((z/|z|)^{4k}\).

Here is its full idèlic form. For \(x\in J_{\mathbb Q(i)}\), choose a generator \(a_x\) of
\[
 \mathfrak a(x_f)=\prod_{v\nmid\infty}
                          \mathfrak p_v^{\operatorname{ord}_v(x_v)}.
\]
Then Theorem 6.3 gives
\[
 \omega_k(x)=
       \left(\frac{a_x}{|a_x|}\right)^{4k}
       \left(\frac{x_\infty}{|x_\infty|}\right)^{-4k}.
 \tag{32}
\]
It is independent of the choice of generator, continuous because the ideal map is locally constant, and multiplicative because generators multiply up to a unit. Multiplication by diagonal \(b\in\mathbb Q(i)^\times\) multiplies the two factors by inverse angular powers of \(b\); hence it is trivial on the field. Every finite unit has value one, so its finite conductor is one. For \(k\ne0\), its archimedean circle image is all of \(\mathbb T\), so it has infinite order.

The **actual idèlic** infinity type \((z/|z|)^4\) belongs to \(\omega_{-1}\), the inverse of \(\omega_1\). Its ideal character is \(\chi_{-1}\). Equation (31) has positive ideal angular exponent, while (32) has negative idèlic angular exponent. Recording which one is meant prevents an inversion when these examples enter local functional equations.

An ideal-theoretic \(\mathbb C^\times\)-valued Hecke character is called **algebraic** if its auxiliary infinity type in (15) is
\[
 \chi_\infty(x)=
 \prod_{v\text{ real}}x_v^{m_v}
 \prod_{v\text{ complex}}z_v^{m_v}\bar z_v^{m_{\bar v}},
 \qquad m_v,m_{\bar v}\in\mathbb Z.
 \tag{33}
\]
We choose one complex embedding for each complex place. Equivalently, use integral exponents for all embeddings of \(K\) into \(\mathbb C\). Its actual archimedean idèlic component is the inverse of (33). The comparison proof works unchanged with \(\mathbb C^\times\) in place of \(\mathbb T\); finite residue characters still have finite image. This definition imposes a condition on an existing Hecke character and does not assert that arbitrary exponent lists satisfy the unit condition (21).

The angular infinity type in (31) is algebraic:
\[
 (z/|z|)^{4k}=z^{2k}\bar z^{-2k}.
 \tag{34}
\]
Algebraic Hecke characters also occur in the description of elliptic curves with complex multiplication. Their associated Hecke \(L\)-functions describe the curve's \(L\)-function; this is the separate complex-multiplication theory discussed in [Milne, *Elliptic Curves*, second edition, IV §10, discussion preceding Remark 10.4](https://www.jmilne.org/math/Books/EC2.pdf). No association to a particular elliptic curve is asserted for (31).

## Exercises

1. **Easy.** Find every quasi-character of \(\mathbb Q_p^\times\) trivial on \(1+p\mathbb Z_p\), including the case \(p=2\). Give its conductor and its real absolute-value exponent.
2. **Medium.** For an odd prime \(p\), construct the Hecke character attached to the Legendre symbol, derive all local components, and verify directly on every diagonal rational number that their product is one.
3. **Medium.** Prove that every finite-order Hecke character of \(\mathbb Q\), trivial on \(\mathbb R_{>0}\), arises from a unique primitive Dirichlet character with the normalization (23). Explain why the positive-real condition is automatic.
4. **Hard.** Construct a Hecke character of \(\mathbb Q(i)\) with actual idèlic infinity type \((z/|z|)^4\), directly on idèles. Check continuity, independence of ideal generators, triviality on \(\mathbb Q(i)^\times\), finite conductor, and the sign of its associated ideal infinity type.

## Solutions

**Solution 1.** Reduction gives \(\mathbb Z_p^\times/(1+p\mathbb Z_p)\simeq\mathbb F_p^\times\). Thus all answers are
\[
 c(p^j u)=A^j\eta(\bar u),\qquad
 A\in\mathbb C^\times,\quad
 \eta\in\operatorname{Hom}(\mathbb F_p^\times,\mathbb T).
\]
Every finite group character is continuous, and the valuation is locally constant, so these formulas give continuous quasi-characters. Uniqueness follows by evaluating at \(p\) and at units. Their conductor is zero for \(\eta=1\) and one otherwise, and \(\sigma=-\log|A|/\log p\). Equivalently the finite residue characters, together with the arbitrary uniformizer value, are the two parameters. At \(p=2\), \(\mathbb F_2^\times\) is trivial and \(1+2\mathbb Z_2=\mathbb Z_2^\times\); only unramified answers occur. No character of conductor exponent one exists there.

**Solution 2.** Set \(\chi(a)=(a/p)\) on \((\mathbb Z/p\mathbb Z)^\times\). This is a nontrivial quadratic character: in \(\mathbb F_p^\times\) the squaring homomorphism has kernel \(\{\pm1\}\), so its image has index two. For an idèle use (24) and define \(\omega(x)=(\bar u_{x,p}/p)\). Continuity and multiplicativity follow from the rational idèle decomposition. Evaluating supported idèles yields (29); in particular the supported uniformizer at the ramified prime \(p\) has value one. The parity evaluation \(\chi(-1)=(-1)^{(p-1)/2}\) was proved following (29).

A direct diagonal check also follows without the decomposition. Write
\[
 r=(-1)^e p^j\prod_{\ell\ne p}\ell^{j_\ell}
 \quad(e\in\{0,1\},\ j,j_\ell\in\mathbb Z),
\]
with finitely many nonzero \(j_\ell\). At \(p\), the unit part is \((-1)^e\prod_{\ell\ne p}\ell^{j_\ell}\), giving value
\(\chi(-1)^e\prod_{\ell\ne p}\chi(\ell)^{j_\ell}\). The other finite components give \(\prod_{\ell\ne p}\chi(\ell)^{j_\ell}\), and the infinite component gives \(\chi(-1)^e\). Their product is one because each value is \(\pm1\). The ramified unit restriction is nontrivial but kills \(1+p\mathbb Z_p\), proving finite conductor \(p\).

**Solution 3.** A finite subgroup of \(\mathbb C^\times\) is discrete. A continuous map from the connected group \(\mathbb R_{>0}\) into it is constant, so the condition is automatic. Proposition 3.6 therefore reduces the character to a continuous finite-image character \(\theta\) of \(\widehat{\mathbb Z}^{\times}\). Its open kernel contains a product subgroup as in (28): choose a basic product neighborhood, and shrink the finitely many exceptional factors to principal-unit subgroups. Hence \(\theta\) descends through reduction modulo some \(m\). Let \(\chi\) be the inverse of that quotient character. Equation (25) reconstructs the original Hecke character. For each prime, the local unit restriction has a least conductor exponent by Proposition 6.1. Taking their product gives the least possible finite modulus, and CRT makes the corresponding character primitive. Any second primitive character giving the same \(\theta\) has the same local exponents and inverse local unit characters, so it is identical. Evaluating the supported prime and the negative real factor proves (23), rather than choosing those signs separately.

**Solution 4.** For the finite ideal \(\mathfrak a(x_f)=(a_x)\), define
\[
 \Omega(x)=
 \left(\frac{x_\infty}{|x_\infty|}\right)^4
 \left(\frac{a_x}{|a_x|}\right)^{-4}.
\]
Replacing \(a_x\) by a Gaussian unit times \(a_x\) leaves the expression unchanged. For \(x,y\), a generator for the product ideal differs from \(a_xa_y\) by a unit, so \(\Omega(xy)=\Omega(x)\Omega(y)\). On a fiber of the finite ideal map the second factor is constant, and that fiber is open; the first factor is continuous. This proves continuity. For diagonal \(b\), the ideal generator can be chosen as \(b\), making \(\Omega(b)=1\). More generally multiplying any idèle by \(b\) leaves the value unchanged. The supported complex coordinate has value \((z/|z|)^4\). Every finite supported unit has value one, and the whole finite unit tail is killed; hence the conductor is one. A supported uniformizer at a finite prime whose ideal generator is \(a\) has value \((a/|a|)^{-4}\). Thus the ideal infinity type is \((z/|z|)^{-4}\), with algebraic exponents \((-2,2)\); the actual idèlic type has exponents \((2,-2)\). Its circle image is all of \(\mathbb T\), which also proves infinite order.

## Prerequisites and further directions

- The local multiplicative decomposition \(F^\times=\pi^{\mathbb Z}\times\mathcal O_F^\times\), compactness of \(\mathcal O_F^\times\), and its principal-unit neighborhood basis are imported from [The multiplicative group of a local field](prerequisites/NT-LOC-11.md), Proposition 1.1 and its proof. The quasi-character classification using them is proved in Proposition 6.1.
- Weak approximation follows from this course's strong approximation, Theorem 2.3: for a finite set of prescribed coordinates, omit any place outside it and use density in the resulting restricted product. Norm-one idèle-class compactness, the topological rational idèle decomposition, ordinary class-group finiteness, and the idèlic ray class isomorphism are imported from Theorem 3.3, Proposition 3.6, Corollary 3.4, and Theorem 4.2 respectively. No class field reciprocity is needed for the comparison theorem.
- The complex-multiplication association between elliptic curves and algebraic Hecke characters, and its identification of \(L\)-functions, is mentioned with the Milne locator above. No part of its proof is needed here.
- Weil groups and local reciprocity are outside this lesson. [Deligne 1973, §§2.2–2.3, 3.2, 3.6] relate local quasi-characters to one-dimensional Weil-group representations and normalize geometric Frobenius to a uniformizer. The Euler factors and functional equations are developed in the next lessons; none are imported here as proved consequences.

## References

- J. Shurman, [*Hecke characters classically and idèlically*](https://people.reed.edu/~jerry/361/lectures/heckechar.pdf), Reed College number theory notes, Definitions 2.1, 2.2 and 6.1 and §§3, 5 and 6: the classical and idèlic definitions, conductor and infinity type, Dirichlet characters, the angular characters of \(\mathbf Q(i)\) and the ideal/idèle comparison. Its classical formula uses the inverse of the infinite component, as in (15)–(18).
- Bjorn Poonen, [*Tate’s Thesis*, MIT 18.786, Spring 2015](https://math.mit.edu/~poonen/786/notes.pdf), §§4.6 and 5.8, especially Example 5.13; and James-Michael Leahy, [*An introduction to Tate’s Thesis* (2010)](https://www.math.mcgill.ca/darmon/theses/leahy/thesis.pdf), §4.8, Proposition 4.8.1 and Example 4.8.3: local character classification, the norm split and rational profinite characters. Equations (23)–(27) specify the finite unit inverse and uniformizer values for our ideal-character convention.
- P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, IAS edition](https://publications.ias.edu/sites/default/files/Number20.pdf), 1973, §§2.2–2.3, 3.2 and 3.6, printed pages 521–529: the one-dimensional Weil-group comparison mentioned above. Local reciprocity is a further direction.
- J. S. Milne, [*Elliptic Curves*, second edition](https://www.jmilne.org/math/Books/EC2.pdf), 2021, IV §10 discussion preceding Remark 10.4 and Remark 10.4(a): the separate complex-multiplication motivation.
