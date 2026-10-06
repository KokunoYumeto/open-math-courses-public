# Abelian number fields and Dirichlet L-functions at \(s=1\)

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. No independent full-lesson review is claimed. Public domain (CC0).*

Characters turn the prime decomposition of a cyclotomic subfield into a product of one-dimensional Euler factors. At ramified primes, some characters lose their Euler factor, while the others retain the residue-field Frobenius. Keeping each character at its primitive conductor makes the product exact.

We first work with
\[
E=\mathbf Q(\zeta_m),\quad G=\operatorname{Gal}(E/\mathbf Q)
\simeq(\mathbf Z/m\mathbf Z)^\times,\quad
K=E^H,\quad A=G/H.
\tag{1}
\]
The cyclotomic groups, integral bases, inertia and arithmetic Frobenius come from [*Cyclotomic fields*](cyclotomic-fields.md). The zeta residue comes from [*The Dedekind zeta function and the analytic class number formula*](the-dedekind-zeta-function-and-the-analytic-class-number-formula.md).

## Characters, conductors and subfields

A character of a finite abelian group is a homomorphism to \(\mathbf C^\times\); its values are roots of unity. The characters form a group \(\widehat G\) under multiplication.

We recall the finite duality facts with their proofs. Writing \(G\) as a product of cyclic groups shows that \(|\widehat G|=|G|\) and that characters separate points. A character of a subgroup \(B\) extends to \(G\): choose \(g\notin B\), let \(d\) be the order of its class modulo \(B\), and choose a complex \(d\)-th root \(z\) of the character's value on \(g^d\). Setting the value on \(g\) to \(z\) defines a character on \(B\langle g\rangle\); the relation \(g^d\in B\) makes it well-defined. Repeat until the finite group is exhausted. Thus restriction to any subgroup is onto.

For \(H\leq G\), its annihilator is
\[
H^\perp=\{\chi\in\widehat G\mid\chi|_H=1\}
\simeq\widehat{G/H},\qquad |H^\perp|=[G:H].
\tag{2}
\]
Conversely, for \(X\leq\widehat G\), let
\(X^\perp=\{g\mid\chi(g)=1\text{ for all }\chi\in X\}\).
The evaluation map identifies \(G\) with its double dual. Applying the surjective restriction map from \(\widehat{\widehat G}\) to \(\widehat X\) gives \(|X^\perp|=|G|/|X|\); hence \((X^\perp)^\perp=X\). Together with Galois correspondence this proves the bijection
\[
K\longleftrightarrow X(K)=H^\perp.
\tag{3}
\]
Inclusions of fields correspond to inclusions of character groups.

An ambient character modulo \(m\) has a unique primitive conductor. Indeed, the Chinese remainder theorem writes its group as a product of the groups modulo \(p^a\). In each factor, choose the least \(b\), \(0\leq b\leq a\), through which the local character factors. The reduction maps are onto and their kernels are nested. Their least exponents therefore give
\[
f(\chi)=\prod_p p^{b_p},
\tag{4}
\]
and a uniquely determined primitive character modulo \(f(\chi)\). This includes the trivial character of conductor \(1\) and the trivial group modulo \(2\).

We identify each member of \(X(K)\) with that primitive character. Its value on an integer is zero exactly when that integer is not coprime to its conductor. The group operation still means multiplication after inflation to a common modulus, followed by passage to the primitive representative. Multiplying the two zero-extended functions directly would not give that operation.

The least cyclotomic modulus containing \(K\) is
\[
f_K=\operatorname{lcm}_{\chi\in X(K)}f(\chi).
\tag{5}
\]
For divisors \(f\mid m\), the field lies in \(\mathbf Q(\zeta_f)\) precisely when every character factors modulo \(f\), by (2) and the kernel of reduction. This gives the least divisor \(f_K\). If \(K\) also lies in \(\mathbf Q(\zeta_{m'})\), the cyclotomic intersection formula from *Cyclotomic fields* puts it in \(\mathbf Q(\zeta_{\gcd(m,m')})\). Thus \(f_K\mid m'\), proving the global assertion.

## Recovering all three decomposition numbers

For a rational prime \(p\), define subgroups of \(X=X(K)\) by
\[
Y=\{\chi\in X\mid p\nmid f(\chi)\},\qquad
Z=\{\chi\in Y\mid\chi(p)=1\}.
\tag{6}
\]
Equivalently \(Y\) consists of the characters with \(\chi(p)\ne0\).

**Proposition 17.0.** If \(pO_K=(\mathfrak p_1\cdots\mathfrak p_g)^e\) and every \(\mathfrak p_i\) has residue degree \(f\), then
\[
e=[X:Y],\qquad f=[Y:Z],\qquad g=|Z|.
\tag{7}
\]

**Proof.** Write \(m=p^ab\), \((p,b)=1\). In the full cyclotomic field, its inertia group is
\[
I_E=(\mathbf Z/p^a\mathbf Z)^\times\times\{1\}
\]
in the Chinese remainder decomposition; when \(a=0\) this is the trivial group. Its image in \(A\) is the inertia group \(I\) of \(K/\mathbf Q\). A character's conductor is prime to \(p\) exactly when its \(p\)-component is trivial, so
\[
Y=\widehat{A/I},\qquad |Y|=|A|/|I|.
\tag{8}
\]
Here \(|I|=e\) by the inertia theorem.

The arithmetic Frobenius of the residue extension is the image in \(A/I\) of the cyclotomic action \(p\bmod b\). For \(\chi\in Y\), evaluation on this element \(F\) is exactly its primitive value \(\chi(p)\). The subgroup \(\langle F\rangle=D/I\) has order \(f\), where \(D\) is the decomposition group. By character restriction surjectivity, the evaluation map
\[
Y\longrightarrow\widehat{\langle F\rangle}
\]
is onto and has kernel \(Z\). Therefore \([Y:Z]=f\) and
\[
|Z|=\frac{|A|}{|I|f}=\frac{|A|}{|D|}=g.
\]
Together with \(|X|=|A|\), this proves all of (7), including ramified primes. \(\square\)

## Factoring the zeta function

For a primitive character, put
\[
L(s,\chi)=\sum_{a\geq1}\chi(a)a^{-s}
=\prod_p(1-\chi(p)p^{-s})^{-1},\qquad \Re s>1.
\tag{9}
\]
Absolute convergence follows from \(|\chi(a)|\leq1\); multiplicativity and integer prime factorization prove the product by finite expansion and absolute exhaustion. For the conductor-one character \(1\), this is the Riemann zeta function.

**Theorem 17.1.** For every cyclotomic subfield \(K\),
\[
\zeta_K(s)=\prod_{\chi\in X(K)}L(s,\chi),\qquad \Re s>1,
\tag{10}
\]
where every factor uses the primitive character.

**Proof.** Fix \(p\), and put \(T=p^{-s}\). The characters outside \(Y\) have value zero and contribute the factor \(1\). By the proof of Proposition 17.0, the values \(\chi(p)\), \(\chi\in Y\), run through every \(f\)-th root of unity exactly \(g=|Y|/f\) times. Thus
\[
\prod_{\chi\in X}(1-\chi(p)T)
=\left(\prod_{\omega^f=1}(1-\omega T)\right)^g
=(1-T^f)^g.
\tag{11}
\]
The reciprocal is \((1-p^{-fs})^{-g}\), which is precisely the product of the \(g\) prime-ideal factors above \(p\). This argument includes \(p\mid f_K\). Taking the absolutely convergent product over all \(p\) proves (10). \(\square\)

For example, \(K=\mathbf Q(\zeta_5)\) has four characters. The three nontrivial ones have conductor \(5\), while the trivial one has conductor \(1\). At \(5\), only the latter contributes, giving \((1-5^{-s})^{-1}\), the factor of the single totally ramified prime. If all characters were instead extended by zero modulo \(5\), even the trivial factor would disappear: that product would equal \((1-5^{-s})\zeta_K(s)\).

For \(K=\mathbf Q(\zeta_{12})\),
\[
X(K)=\{1,\chi_{-3},\chi_{-4},\chi_{12}\}.
\tag{12}
\]
At \(2\), \(Y=\{1,\chi_{-3}\}\) and \(\chi_{-3}(2)=-1\); hence \(e=2,f=2,g=1\). At \(3\), the same calculation uses \(\{1,\chi_{-4}\}\), again giving \(2,2,1\). These give the factors \((1-2^{-2s})^{-1}\) and \((1-3^{-2s})^{-1}\). At \(5\), evaluation has order two and kernel of size two, so \(e=1,f=2,g=2\). These agree with the earlier direct prime decomposition.

## Continuation and nonvanishing at one

**Proposition 17.2.** If \(\chi\ne1\), its series \(L(s,\chi)\) converges for \(\Re s>0\) and is holomorphic there.

**Proof.** If \(q=f(\chi)\), then
\(\sum_{a=1}^q\chi(a)=0\): multiplication by a unit \(u\) with \(\chi(u)\ne1\) permutes the residues and multiplies this sum by \(\chi(u)\). Therefore
\[
B_\chi(x)=\sum_{a\leq x}\chi(a)
\]
is bounded by a constant depending on \(q\). Finite Abel summation gives
\[
\sum_{a\leq T}\chi(a)a^{-s}
=B_\chi(T)T^{-s}
 +s\int_1^T B_\chi(x)x^{-s-1}\,dx.
\]
On a compact subset of \(\Re s>0\), take \(\sigma_0>0\) below the real parts and bound \(|s|\). The endpoint and integral tail tend uniformly to zero, with bounds \(O(T^{-\sigma_0})\). The limiting integral
\[
L(s,\chi)=s\int_1^\infty B_\chi(x)x^{-s-1}\,dx
\tag{13}
\]
is holomorphic: \(x^{-\sigma_0-1}(\log x)^j\) dominates each derivative on the compact set and is integrable. \(\square\)

**Theorem 17.3.** Every nontrivial primitive Dirichlet character satisfies
\[
L(1,\chi)\ne0.
\tag{14}
\]

**Proof.** Take the full field \(E=\mathbf Q(\zeta_m)\), where \(m=f(\chi)\). Its character group includes the inflation of \(\chi\) and the conductor-one trivial character. Equation (10) gives
\[
\frac{\zeta_E(s)}{\zeta(s)}
=\prod_{\psi\in X(E),\,\psi\ne1}L(s,\psi).
\]
All factors on the right are holomorphic at \(1\) by Proposition 17.2. On the left, the simple-pole residues proved in the preceding lesson give the nonzero limit
\[
\lim_{s\downarrow1}\frac{\zeta_E(s)}{\zeta(s)}
=\frac{2^{r_1}(2\pi)^{r_2}h_ER_E}
 {w_E\sqrt{|d_E|}}>0.
\]
The finite product of their values at \(1\) is therefore nonzero, so each value is nonzero. \(\square\)

For a nonprincipal character presented at an imprimitive modulus, its usual series differs from the primitive one by finitely many factors \(1-\chi^*(p)p^{-s}\). None vanishes at \(s=1\), since \(|\chi^*(p)|\leq1<p\). Nonvanishing therefore holds for that convention too.

## Quadratic class numbers as finite sums

Let \(D\) be the fundamental discriminant of a quadratic field \(F\), put \(q=|D|\), and write \(\chi=\chi_D\). Set
\[
\zeta_q=e^{2\pi i/q},\qquad
\tau_D=\sum_{a=1}^{q-1}\chi(a)\zeta_q^a.
\]
The finite quadratic Gauss-transform identity was proved in *Cyclotomic fields*, including its zero values at nonunits:
\[
\sum_{a=1}^{q-1}\chi(a)\zeta_q^{an}
=\chi(n)\tau_D,\qquad \tau_D^2=D.
\tag{15}
\]
The additional **sign theorem** is proved in *Gauss sums*, Theorem 5.1, with the Gaussian and branch argument of sections 3–4 (source). In our notation it says
\[
\tau_D=
\begin{cases}
\sqrt D,&D>0,\\
i\sqrt{|D|},&D<0,
\end{cases}
\tag{16}
\]
where both real square roots are positive. The provider defines \(e(x)=\exp(2\pi i x)\), exactly as here, and covers every real primitive character, including all fundamental discriminants with a factor at \(2\). Thus no conjugation or exponential-sign conversion is needed.

Here is how the cited proof determines the phase. The Gaussian transformation uses the holomorphic square root positive on the positive real axis. Its limit at \(t-2i/q\), as \(t\downarrow0\), gives the exact quadratic sum for every positive integer modulus; for an odd prime this is \(\sqrt p\) or \(i\sqrt p\) according to \(p\bmod4\). Theorem 5.1 then combines these prime evaluations with the direct sums for \(-4,8,-8\). Its Chinese-remainder product formula includes the cross-character factors; quadratic reciprocity shows that their signs turn the product phase into \(1\) for positive fundamental discriminant and \(i\) for negative fundamental discriminant. These are the full Gaussian-limit and conductor-product proofs of (16), rather than a choice between the two square roots in (15). For historical comparison, the exact classical sign theorem is Hecke VIII §58, Satz 164, printed p.242.

**Theorem 17.4.** The ordinary ideal class number is
\[
h_F=-\frac{w_F}{2|D|}
\sum_{a=1}^{|D|-1}\chi_D(a)a,\qquad D<0.
\tag{17}
\]
For \(D>0\), if \(\varepsilon>1\) is the fundamental unit in the chosen real embedding, of either norm, then
\[
h_F\log\varepsilon
=-\frac12\sum_{a=1}^{D-1}
\chi_D(a)\log\sin\frac{\pi a}{D}.
\tag{18}
\]

**Proof.** For \(0<r<1\), insert (15) into the absolutely convergent damped series:
\[
\sum_{n\geq1}\frac{\chi(n)r^n}{n}
=-\frac1{\tau_D}\sum_{a=1}^{q-1}
\chi(a)\log(1-r\zeta_q^a).
\tag{19}
\]
The logarithm is the branch reached from \(r=0\); all these arguments have positive real part.

To justify the limit on the left, put \(U_N=\sum_{n=1}^N\chi(n)/n\). Proposition 17.2 gives \(U_N\to L(1,\chi)\). Summation of the geometric weights yields
\[
\sum_{n\geq1}\frac{\chi(n)r^n}{n}
=(1-r)\sum_{N\geq1}U_Nr^N.
\]
Split the last sum at a fixed large \(N_0\). The finite initial part tends to zero after multiplication by \(1-r\), and the tail differs from its limiting constant by at most \(\sup_{N\geq N_0}|U_N-L(1,\chi)|\). Thus the limit is \(L(1,\chi)\). Every logarithm on the finite right side of (19) also has a finite limit, since \(1\leq a<q\).

For these indices,
\[
\log(1-\zeta_q^a)
=\log\left(2\sin\frac{\pi a}{q}\right)
 +i\pi\left(\frac aq-\frac12\right).
\tag{20}
\]
This follows from
\(1-e^{2\pi ia/q}=2\sin(\pi a/q)e^{i(\pi a/q-\pi/2)}\);
the displayed argument lies between \(-\pi/2\) and \(\pi/2\).

If \(D<0\), then \(\chi(q-a)=-\chi(a)\), so the real logarithms cancel in pairs. Also \(\sum_a\chi(a)=0\). Equations (16), (19) and (20) give
\[
L(1,\chi_D)
=-\frac{\pi}{q\sqrt q}\sum_{a=1}^{q-1}\chi_D(a)a.
\tag{21}
\]
The previous residue formula and quadratic factorization give
\(L(1,\chi_D)=2\pi h_F/(w_F\sqrt q)\), because \(R_F=1\). Comparing proves (17), including \(D=-3,-4\) with their larger \(w_F\).

If \(D>0\), then \(\chi(D-a)=\chi(a)\); the imaginary parts in (20) cancel. The constant \(\log2\) cancels because the character sum is zero. Therefore
\[
L(1,\chi_D)
=-\frac1{\sqrt D}\sum_{a=1}^{D-1}
\chi_D(a)\log\sin\frac{\pi a}{D}.
\tag{22}
\]
Now \(R_F=\log\varepsilon,\ w_F=2\), and the residue formula is
\(L(1,\chi_D)=2h_F\log\varepsilon/\sqrt D\). This proves (18). \(\square\)

The ordinary and narrow conventions agree after their constants are matched. If \(h_F^+\) is the narrow class number and \(\varepsilon^+>1\) the least unit of norm \(+1\), the unit-sign sequence from [*Quadratic fields: ideal classes and binary quadratic forms*](quadratic-fields-ideal-classes-and-binary-quadratic-forms.md) gives
\[
h_F^+\log\varepsilon^+=2h_F\log\varepsilon.
\tag{23}
\]
When \(N\varepsilon=-1\), one has \(h_F^+=h_F\) and \(\varepsilon^+=\varepsilon^2\). When \(N\varepsilon=+1\), one has \(h_F^+=2h_F\) and \(\varepsilon^+=\varepsilon\).

For \(D=-4\), the weighted sum is \(1-3=-2\), and (17) gives \(h=1\). For \(D=-23\), the positive quadratic residues sum to \(92\), while all residues \(1,\ldots,22\) sum to \(253\). Thus the weighted sum is \(184-253=-69\), giving \(h=3\).

For \(D=5\), the values on \(1,2,3,4\) are \(1,-1,-1,1\). Equation (18) reduces to
\[
h\log\varphi
=\log\frac{\sin(2\pi/5)}{\sin(\pi/5)}
=\log\left(2\cos\frac\pi5\right)=\log\varphi,
\quad\varphi=\frac{1+\sqrt5}{2}.
\tag{24}
\]
Here \(2\cos(\pi/5)\) is the positive root of \(t^2-t-1\), from the fifth-root identity, and \(\varphi\) is the previously proved fundamental unit. Consequently \(h=1\).

## Abelian fields and their conductor–discriminant formula

The next two theorems use the exact written programme proofs in *Kronecker–Weber and the maximal abelian extension of the rationals* (source).

**Theorem 17.5 (Kronecker–Weber).** Every finite abelian extension of \(\mathbf Q\) is contained in a cyclotomic field. Consequently (3), (7) and (10) apply to every abelian number field.

**Proof from the programme result.** The provider's Theorem 20.2 proves the finite assertion using its earlier global conductor and ray-field containment theorems. A finite abelian extension has a conductor bounded by some modulus \(m\infty\), so it lies in the rational ray field for that modulus. Proposition 20.1 identifies this ray field with \(\mathbf Q(\zeta_m)\): its ray group is \((\mathbf Z/m\mathbf Z)^\times\), the local cyclotomic symbols annihilate the modulus subgroup, and cyclotomic irreducibility gives the same degree as the ray group. This includes \(m=1,2\). After choosing the resulting cyclotomic embedding, the finite character, decomposition and Euler-factor proofs above apply unchanged. \(\square\)

**Theorem 17.6 (conductor–discriminant).** For every finite abelian number field \(K\),
\[
|d_K|=\prod_{\chi\in X(K)}f(\chi).
\tag{25}
\]
The conductors are those of the primitive representatives in (4); the trivial character contributes \(1\). The infinity part of a global conductor is not an integer factor in (25).

**Proof from the programme result.** Proposition 20.5 in the cited class-field lesson identifies the finite Dirichlet conductor of each character with its local conductor: their exponents are the least exponents at which the corresponding local unit groups lie in its kernel. The inversion relating the idèle character to the cyclotomic exponent character preserves that kernel. Thus its Theorem 20.6 uses exactly our conductors, rather than conductors at a chosen larger modulus.

For completeness, its local-to-global argument is as follows. Fix \(p\), let \(D_p\) be the decomposition group in \(A=\operatorname{Gal}(K/\mathbf Q)\), and let \(E/\mathbf Q_p\) be the corresponding completion. There are \(g=[A:D_p]\) primes above \(p\). The character-extension argument preceding (2) makes restriction \(\widehat A\to\widehat{D_p}\) onto, with every fibre of size \(g\). The earlier local conductor–discriminant theorem, class-field Theorem 10.5, therefore gives
\[
\sum_{\chi\in X(K)}v_p(f(\chi))
=g\sum_{\eta\in\widehat{D_p}}a(\eta)
=g\,v_p(\mathfrak d_{E/\mathbf Q_p}),
\]
where \(a(\eta)\) is the local conductor exponent and \(\mathfrak d_{E/\mathbf Q_p}\) is the local discriminant ideal. The last term is \(v_p(d_K)\): the completed integral algebra is the product of the integral rings at all primes over \(p\), and its trace matrix is block diagonal, with one local trace matrix per factor. The Galois hypothesis makes those \(g\) factors isomorphic. Equality of every prime exponent proves (25), with the absolute value removing the archimedean sign. \(\square\)

The class-field proof uses only the finite character duality already established before (3), together with its own earlier local conductor theorem. Its proof of Kronecker–Weber precedes that use. Therefore these imports do not use (25), Theorem 17.4 or the general abelian conclusion as their own prerequisites. Equation (25) was not used to prove the zeta factorization or the quadratic formulas.

As a consistency check, (12) has conductors \(1,3,4,12\), whose product is \(144\), the independently computed discriminant of \(\mathbf Q(\zeta_{12})\).

## Exercises and complete solutions

**Exercise 1.** Determine \(X(\mathbf Q(\sqrt{-3}))\).

**Solution 1.** This field is \(\mathbf Q(\zeta_3)\), because \(\zeta_3=(-1+\sqrt{-3})/2\). Its Galois group is the order-two unit group modulo \(3\). Its two characters are the conductor-one trivial character and the primitive quadratic character
\[
\chi_{-3}(a)=
\begin{cases}
0,&3\mid a,\\
1,&a\equiv1\pmod3,\\
-1,&a\equiv2\pmod3.
\end{cases}
\]
The latter has order two and cannot factor modulo \(1\). Thus \(X=\{1,\chi_{-3}\}\).

**Exercise 2.** Prove the zeta factorization for a quadratic field directly from its decomposition law.

**Solution 2.** Its group is \(\{1,\chi_D\}\). At \(\chi_D(p)=1\), the product of the two factors is \((1-p^{-s})^{-2}\), matching two degree-one primes. At \(-1\), it is
\((1-p^{-s})^{-1}(1+p^{-s})^{-1}=(1-p^{-2s})^{-1}\), matching one degree-two prime. At \(0\), the nontrivial factor is \(1\), while the trivial factor remains \((1-p^{-s})^{-1}\), matching one ramified degree-one prime. Absolute convergence proves
\(\zeta_F(s)=\zeta(s)L(s,\chi_D)\) after multiplication over all primes.

**Exercise 3.** Compute \(h(-23)\) and \(h(-47)\) and compare them with reduced forms.

**Solution 3.** For \(D=-p\), \(p=23,47\), one has \(w=2\) and \(\chi_D(a)=(a/p)\). Write \(R_p\) for the sum of the nonzero quadratic residues as their representatives in \(1,\ldots,p-1\). Enumerating the squares of \(1,\ldots,(p-1)/2\) gives
\[
R_{23}=92,\qquad R_{47}=423.
\]
Hence the weighted character sums are
\[
2R_{23}-\frac{23\cdot22}{2}=-69,\qquad
2R_{47}-\frac{47\cdot46}{2}=-235.
\]
Equation (17) gives \(h(-23)=3\) and \(h(-47)=5\).

For the independent form comparison, the earlier reduction theorem requires
\(|b|\leq a\leq c\), \(b^2-4ac=D\), primitivity, and \(b\geq0\) on either equality boundary. It gives \(a\leq\sqrt{|D|/3}\). Thus \(a\leq2\) for \(-23\) and \(a\leq3\) for \(-47\). Substituting those values and checking the parity of \(b\) gives exactly
\[
\begin{array}{c|l}
D&\text{reduced representatives }(a,b,c)\\ \hline
-23&(1,1,6),\ (2,1,3),\ (2,-1,3)\\
-47&(1,1,12),\ (2,1,6),\ (2,-1,6),\
(3,1,4),\ (3,-1,4).
\end{array}
\]
They are primitive and satisfy every boundary convention; the bound excludes further values of \(a\). The form-to-ideal bijection therefore gives the same class numbers.

**Exercise 4.** For \(p>3\), \(p\equiv3\pmod4\), derive Dirichlet's half-sum formula
\[
h(\mathbf Q(\sqrt{-p}))
=\frac1{2-(2/p)}\sum_{0<a<p/2}\left(\frac ap\right).
\tag{26}
\]

**Solution 4.** Put \(\chi(a)=(a/p)\),
\(S=\sum_{a=1}^{p-1}a\chi(a)\), and
\(T=\sum_{a=1}^{(p-1)/2}\chi(a)\).
Since \(p>3\), \(w=2\), so (17) says \(S=-ph\). Oddness gives
\(\sum_{a>p/2}\chi(a)=-T\). Multiplication by \(2\) permutes the nonzero residues, and its representative is \(2a\) in the lower half and \(2a-p\) in the upper half. Therefore
\[
S=\chi(2)\sum_{a=1}^{p-1}
 \chi(a)(2a-p\,\mathbf1_{a>p/2})
=\chi(2)(2S+pT).
\]
Since \(\chi(2)^2=1\), rearranging gives
\(pT=(\chi(2)-2)S=p(2-\chi(2))h\).
The denominator \(2-\chi(2)\) is \(1\) or \(3\), so division proves (26).

**Exercise 5.** Express the analytic class number constant of an abelian field as a product of \(L\)-values.

**Solution 5.** The conductor-one trivial character occurs once in \(X(K)\). Divide (10) by its factor \(\zeta(s)\); all other factors are holomorphic at \(1\) by Proposition 17.2. Taking the limit and using the residues from the preceding lesson yields
\[
\frac{2^{r_1}(2\pi)^{r_2}h_KR_K}
 {w_K\sqrt{|d_K|}}
=\prod_{\chi\in X(K),\,\chi\ne1}L(1,\chi).
\tag{27}
\]
For \(K=\mathbf Q\) the product is empty and equals \(1\), consistent with \(R=1,h=1,w=2,d=1\). For a general abelian field, Theorem 17.5 supplies the cyclotomic embedding through the cited programme proof.

## Proof dependencies and further topics

The cyclotomic arithmetic, quadratic character classification and finite quadratic Gauss transform are imported from *Cyclotomic fields*. The analytic class number residue is imported from the preceding lesson. Finite abelian group decomposition and Galois correspondence are algebra prerequisites; their character consequences used here were proved above.

The sign theorem (16) imports the written Dirichlet-course Theorem 5.1, whose earlier inputs are real primitive-character classification, supplementary quadratic laws and the elementary analytic prerequisites used in its Gaussian proof. Theorems 17.5–17.6 import the written class-field Theorems 20.2 and 20.6 and Proposition 20.5; their earlier inputs include local reciprocity, global conductor and ray-field existence, and local conductor–discriminant. These receiving arguments retain those programme dependencies and do not certify their entire earlier proof chains. General finite \(L(1,\chi)\) formulas, full Dirichlet \(L\)-function continuation and functional equations, and Dirichlet's theorem on arithmetic progressions are further topics in the dedicated courses.

## References

- *Gauss sums*, sections 3–5, especially Theorems 4.1 and 5.1, for the full signed sum (16), including its Gaussian branch and all fundamental discriminants.
- *Kronecker–Weber and the maximal abelian extension of the rationals*, Proposition 20.1, Theorem 20.2, Proposition 20.5 and Theorem 20.6, for the programme proofs of Theorems 17.5–17.6 with primitive finite conductors.
- Erich Hecke, [*Vorlesungen über die Theorie der algebraischen Zahlen*](https://archive.org/details/vorlesungenber00heckuoft), 1923, VII §§49–52, printed pp.197–209, especially Satz 150–152, pp.208–209, for the historical finite quadratic formulas; VIII §58, Satz 164, p.242, for the classical signed sum. The sign used here is supplied by the linked programme proof.
- J. S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 6, “The basic results,” printed pp.95–100, for freely readable cyclotomic background; the arithmetic imported here is proved in the earlier programme lesson *Cyclotomic fields*.
