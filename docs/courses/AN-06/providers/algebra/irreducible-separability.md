# Irreducible polynomials and characteristic-zero separability

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

A derivation on a rational function field must respect every algebraic relation when it is extended to a larger field. We build the polynomial and field tools that make that requirement explicit. Fields are nonzero commutative rings in which each nonzero element has an inverse. The polynomial, quotient and fraction rings below are those constructed in [Noetherian polynomial rings and finite-type algebras](noetherian-permanence.md#algebra-rings-and-fractions).

<a id="irreducible-separability"></a>

**The separability theorem.** Let $P\in F[T]$ be irreducible; thus it is nonconstant and cannot be a product of two positive-degree polynomials. Either $P$ and its formal derivative $P'$ generate the whole polynomial ring, or $P'=0$. In the second case the field has prime characteristic $p>0$ and
$P(T)=Q(T^{p^f})$ for an integer $f\ge1$, where $Q$ is irreducible and $(Q,Q')=F[T]$. In characteristic zero, every root $a$ of $P$ in any extension field satisfies $P'(a)\ne0$ and is a simple root.

We will also prove that finitely many algebraic adjunctions give a finite-dimensional field extension; that a prescribed finite algebraically independent list in a finitely generated field can be completed to a transcendence basis with finite algebraic remainder; and that a derivation extends uniquely across every finite algebraic extension in characteristic zero.

<a id="algebra-polynomial-division"></a>

## 1. Division, greatest common divisors and a field quotient

For $A,B\in F[T]$ with $B\ne0$, there are unique $Q,R$ such that $A=BQ+R$ and either $R=0$ or $\deg R<\deg B$. Indeed, if the current remainder has degree at least $\deg B$, the invertible leading coefficient of $B$ lets us subtract a scalar times a power of $T$ times $B$ to cancel its top coefficient. The degree decreases at every step, so this process terminates. For uniqueness, a difference of two allowed remainders has degree below $\deg B$, whereas a nonzero multiple of $B$ has degree at least $\deg B$.

Apply division repeatedly to a pair of polynomials not both zero: divide the first by the second, then the second by the nonzero remainder, and continue. The degrees of the nonzero remainders decrease. The final nonzero remainder $d$, scaled to be monic, divides all the earlier remainders by working backwards through the division identities. Conversely any common divisor of the original pair divides every remainder, hence divides $d$. Each remainder is also a polynomial combination of the original pair, by induction through the same identities. Therefore
\[
 d=UA+VB
 \tag{FS1}
\]
for some $U,V\in F[T]$. This proves the greatest-common-divisor and Bézout assertions constructively, including a pair with one zero member. When both members vanish their generated ideal is zero.

For completeness, the ideal formulation follows directly as well. In any nonzero ideal choose a nonzero polynomial $d$ of smallest degree and scale it to be monic. Division of any element of that ideal by $d$ leaves a remainder in the ideal with smaller degree, which must be zero. Thus every ideal of $F[T]$ is principal. In particular $(A,B)=(d)$, and $A,B$ are relatively prime exactly when $d=1$, or equivalently when a polynomial combination equals $1$.

If $P$ is irreducible, $F[T]/(P)$ is a field. A nonzero class has a unique nonzero representative $g$ of degree below $\deg P$. A nonconstant common divisor of $g$ and $P$ would be a scalar multiple of $P$, which cannot divide such a $g$. Formula (FS1) consequently gives $ug+vP=1$. In the quotient the class of $u$ is the inverse of the class of $g$. This verifies the field property, and division shows that every class has a unique representative of degree below $\deg P$.

<a id="algebra-separability-proof"></a>

## 2. The derivative test in every characteristic

Formal differentiation sends $\sum a_jT^j$ to $\sum_{j\ge1} j a_jT^{j-1}$. The coefficient identity $(j+k)=j+k$ in $F$ verifies the product rule on two monomials, and distributivity verifies it on polynomials.

Suppose first that $P'\ne0$. Its degree is below $\deg P$, so its class in the field $F[T]/(P)$ is nonzero and invertible. Lift an inverse to a polynomial $V$. Then $1-VP'$ is a multiple of $P$, giving $UP+VP'=1$. This proves the relatively prime alternative. Equivalently, the principal-ideal argument of Section 1 says that a nonunit common divisor would be associated to $P$ and would divide the nonzero lower-degree polynomial $P'$, an impossibility.

If $P'=0$, the coefficient equations are $j a_j=0$ for all $j\ge1$. In characteristic zero, every nonzero integer has nonzero image in the field, so these equations would make $P$ constant. Thus the characteristic is positive. Its least positive value $p$ annihilating $1$ is prime: a factorization of $p$ into two smaller positive integers would give a product of two nonzero field elements equal to zero. An integer $j$ has zero image precisely when $p$ divides $j$, by integer division with remainder and minimality of $p$. Hence every nonzero exponent in $P$ is divisible by $p$, and $P(T)=P_1(T^p)$.

The polynomial $P_1$ is nonconstant and irreducible, since a factorization into positive-degree polynomials would give one for $P$ by substitution. If $P_1'=0$, repeat the same argument. At every repetition the positive degree is divided by $p\ge2$, so after finitely many steps we obtain $Q'\ne0$. The number of steps is some $f\ge1$, and $P(T)=Q(T^{p^f})$. Apply the preceding nonzero-derivative proof to $Q$. This proves the full characteristic-$p$ alternative without assuming the field is perfect.

In characteristic zero, evaluate $UP+VP'=1$ at any root $a$ in any extension field. It gives $V(a)P'(a)=1$. To identify this with simplicity of the root, division in that extension field gives $P=(T-a)H$ because $P(a)=0$. The product rule gives $P'(a)=H(a)$. Another division by $T-a$ shows $H(a)=0$ exactly when $(T-a)^2$ divides $P$. Thus a repeated root is impossible. All these statements hold in an arbitrary field containing the particular root; no algebraic closure is needed.

<a id="algebra-finite-extensions"></a>

## 3. Finite algebraic towers and a prescribed independent list

Let $a$ in a field extension of $E$ be algebraic. Among nonzero polynomials vanishing at $a$, choose one of least degree and normalize it to be monic, denoting it by $h$. If $h$ factored into two positive-degree factors, one factor would vanish at $a$ because the extension is a field. This contradicts the least degree. Therefore $h$ is irreducible.

Divide any polynomial vanishing at $a$ by $h$. The remainder also vanishes at $a$, so minimality makes it zero. Consequently the kernel of evaluation is precisely $(h)$; the same observation proves uniqueness of the monic minimal polynomial. Evaluation identifies $E[a]$ with $E[T]/(h)$, which is a field by Section 1. It follows that $E[a]=E(a)$ and that
\[
 1,a,\ldots,a^{d-1},\qquad d=\deg h,
 \tag{FS2}
\]
is an $E$-basis. Division proves spanning, and any linear dependence would be a nonzero polynomial of degree below $d$ vanishing at $a$.

For a tower $E\subset L\subset M$ with finite bases $b_1,\ldots,b_j$ of $L/E$ and $c_1,\ldots,c_k$ of $M/L$, the products $b_i c_l$ are an $E$-basis of $M$. Expand first in the $c_l$ and then expand each coefficient in the $b_i$ to prove spanning. In a zero linear combination of the products, independence of the $c_l$ forces each $L$-coefficient to vanish; independence of the $b_i$ then forces every $E$-coefficient to vanish. Induction proves finiteness for any tower obtained by adjoining finitely many algebraic elements.

Every element $v$ of a field of finite dimension $d$ over $E$ is algebraic over $E$. Express $1,v,\ldots,v^d$ in an $E$-basis. A homogeneous system with their $d$ coordinates has $d+1$ unknown coefficients. Row elimination chooses at most $d$ pivot columns; a nonpivot variable can be set to $1$, the other free variables to $0$, and backward substitution determines the pivots. The resulting nonzero solution is a polynomial relation for $v$. All elimination operations use only inverses of nonzero field elements.

Now let $M=k(x_1,\ldots,x_n)$, and fix any finite algebraically independent list $u_1,\ldots,u_r$ in $M$, including the empty list. Independence means that evaluation embeds $k[U_1,\ldots,U_r]$ in $M$. The field generated by the list is its fraction field: all rational expressions in the variables lie in any containing field, and the fraction-field construction supplies such a field inside $M$.

Process $x_1,\ldots,x_n$ in order, adjoining $x_j$ to the independent list if the longer list is independent. Otherwise a nonzero polynomial relation in the list and $x_j$, collected in powers of $x_j$, has at least one coefficient that is a nonzero polynomial in the independent list. Its value is nonzero by independence. The relation therefore proves that $x_j$ is algebraic over the current rational function field. That relation remains nonzero over every later field, since field inclusions do not turn a nonzero coefficient into zero.

The final list is finite and independent; let $E$ be its rational function field. Every $x_j$ is algebraic over $E$ (those in the list already belong to $E$), and $E(x_1,\ldots,x_n)=M$ because the starting list was in $M$. The finite-tower proof makes $M/E$ finite. This constructs the required transcendence basis while retaining every element prescribed at the start.

<a id="algebra-derivations"></a>

## 4. Fractions and infinitesimal algebraic relations

A derivation $D$ is additive and obeys $D(ab)=aD(b)+bD(a)$. The identity at $1\cdot1$ implies $D(1)=0$. If it vanishes on a subfield $k$, the product rule gives $k$-linearity. On a polynomial algebra over $k$, prescribe the derivative of each variable, differentiate a monomial by the product rule and extend by addition. Expanding products of monomials verifies that this is a derivation. Algebraic independence therefore defines partial derivatives on the polynomial algebra generated by an independent list.

A derivation on a domain $A$ with values in its fraction field extends uniquely by
\[
 D(a/s)=\frac{D(a)}s-\frac{aD(s)}{s^2}.
 \tag{FS3}
\]
For well-definedness, take $a/s=b/t$, so $at=bs$. Differentiating that equality yields
$tD(a)+aD(t)=sD(b)+bD(s)$. After putting the difference of the two proposed values over $s^2t^2$, its numerator is
$st(tD(a)-sD(b))-at^2D(s)+bs^2D(t)$.
Substitution of the differentiated equality and $at=bs$ makes this zero. A common denominator and expansion verify additivity and the product rule for fractions. Conversely differentiating $s\cdot s^{-1}=1$ forces (FS3), so the extension is unique. In particular the partial derivatives just constructed extend to the rational function field.

Let $E$ have characteristic zero, let $D:E\to E$ be a derivation and let $a$ be algebraic over $E$ with minimal polynomial $h(T)=\sum h_jT^j$. Section 2 gives $h'(a)\ne0$. Put
\[
 b=-\frac{\sum_j D(h_j)a^j}{h'(a)}.
 \tag{FS4}
\]
We prove existence of the extension by realizing the product rule inside a small ring. In
$B=E(a)[\varepsilon]/(\varepsilon^2)$, every element is uniquely $z+\varepsilon y$, by polynomial division. Multiplication is
$(z+\varepsilon y)(v+\varepsilon w)=zv+\varepsilon(zw+vy)$.
Thus $c\mapsto c+\varepsilon D(c)$ is a unital ring homomorphism from $E$ to $B$.

Extend this homomorphism to $E[T]$ by sending $T$ to $a+\varepsilon b$. The finite binomial identity, with $\varepsilon^2=0$, gives for $g(T)=\sum g_jT^j$ the image
\[
 \begin{gathered}
 \delta g=\sum_jD(g_j)a^j+g'(a)b,\\
 g\longmapsto g(a)+\varepsilon\,\delta g.
 \end{gathered}
 \tag{FS5}
\]
For $g=h$ both coefficients vanish: $h(a)=0$, and the second coefficient is zero by (FS4). Hence every multiple of $h$ maps to zero. The map descends to $E[T]/(h)=E(a)$. Its constant coefficient is the identity on $E(a)$, so it has the form $z\mapsto z+\varepsilon\widetilde D(z)$. Additivity and multiplication in $B$ prove that $\widetilde D$ is a derivation. Its values on $E$ agree with $D$, and its value on $a$ is $b$.

This also provides a direct coefficient verification: the coefficient $\delta g$ in (FS5) satisfies
$\delta(gq)=g(a)\delta q+q(a)\delta g$. Since $\delta h=0$, it vanishes on the evaluation kernel $(h)$ and is well-defined on $E[a]$. Thus the coefficient formula and the infinitesimal-ring construction give the same extension.

Any extension must differentiate $h(a)=0$ to obtain (FS4). Polynomial evaluation, and then the fraction rule if needed, determines its other values. The extension is therefore unique. A finite-dimensional extension is generated as a field by a finite vector-space basis, because a field containing that basis contains its linear span. Each basis element is algebraic by Section 3. Apply the simple-extension construction successively to these generators. This proves existence and uniqueness on every finite algebraic extension of a characteristic-zero field. If the original derivation vanishes on $k\subset E$, its extension still vanishes there. Taking a partial derivative with respect to a prescribed transcendental element in Section 3 gives exactly the derivation used in the critical-values argument.

## Further reading

The Stacks Project authors, with the AI Integrated Stacks Project, [*Fields*, irreducible polynomials and their derivatives, tag 09H0](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/fields.tex#L1167), give the irreducible-polynomial alternatives. The historical source excerpts and their licence retain their own terms.
