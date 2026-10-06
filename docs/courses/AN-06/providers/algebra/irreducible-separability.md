# Irreducible polynomials and characteristic-zero separability

[Component notice and licence](NOTICE.md). Adapted from the exact [09H0 statement and proof](09H0-proof.tex). The division/Bézout prerequisites and root consequence are explicit elementary completions. Fields are nonzero commutative rings in which every nonzero element has an inverse; an irreducible polynomial is a nonconstant nonunit with no factorization into two nonunits.

<a id="irreducible-separability"></a>

## The statement

For a field $F$ and irreducible $P\in F[x]$, either $P$ and its formal derivative $P'$ are relatively prime, or $P'=0$. The latter case occurs only in characteristic $p>0$; then $P(x)=Q(x^{p^f})$ for some $f\geq1$, where $Q$ is irreducible and relatively prime to $Q'$. In particular every irreducible polynomial over a characteristic-zero field is separable, and for every root $\alpha$ in any extension field, $P'(\alpha)\ne0$.

<a id="algebra-polynomial-division"></a>

## Elementary completion: polynomial division and Bézout

For nonzero $D\in F[x]$ and arbitrary $A\in F[x]$, repeatedly subtract the multiple of $D$ that cancels the highest-degree term of the current remainder. The leading coefficient of $D$ is invertible, and the degree strictly decreases. This terminates with $A=QD+R$, $\deg R<\deg D$ (or $R=0$). Uniqueness follows because a nonzero multiple of $D$ has degree at least $\deg D$.

Every nonzero ideal of $F[x]$ is principal: choose a nonzero element $D$ of least degree in the ideal and divide any other element by it. The remainder belongs to the same ideal and must vanish. Apply this to the ideal $(P,P')$. Its generator $D$ divides both polynomials, and being in that ideal has the form $D=UP+VP'$ for polynomials $U,V$. Relatively prime means that this ideal is the whole ring, equivalently that one can take $D=1$.

<a id="algebra-separability-proof"></a>

## Proof, including the positive-characteristic alternative

Suppose $P'\ne0$. Then $\deg P'<\deg P$. If $(P,P')=(D)$ were a proper ideal, $D$ would be a nonunit divisor of $P$, so irreducibility makes $D$ associate to $P$. Since it also divides the nonzero $P'$, one would have $\deg P\leq\deg P'<\deg P$, a contradiction. Thus $P$ and $P'$ are relatively prime.

If $P'=0$ and $P=\sum_{j=0}^d a_jx^j$, all $j a_j$ for $j\geq1$ vanish. In characteristic zero this forces $P$ to be constant, a contradiction. A field of positive characteristic has prime characteristic $p$: if the least positive integer annihilating $1$ factored into two smaller positive integers, their nonzero images would multiply to zero in a field. It follows that $a_j=0$ whenever $p$ does not divide $j$. Thus $P(x)=P_1(x^p)$ with $P_1$ nonconstant. A factorization of $P_1$ would give one of $P$, so $P_1$ is irreducible. Its degree is strictly smaller. Repeat while the derivative vanishes; natural-number induction gives $P(x)=Q(x^{p^f})$ with $Q'\ne0$. The first paragraph then makes $Q,Q'$ relatively prime. This proves the full source alternative.

## Root consequence needed in AN06-U008

In characteristic zero, $UP+VP'=1$. If $P(\alpha)=0$ in any extension field, evaluation gives $V(\alpha)P'(\alpha)=1$, hence $P'(\alpha)\ne0$. To see that this is precisely the simple-root conclusion, divide by $x-\alpha$ in the extension field and write $P=(x-\alpha)R$. The product rule for the formal derivative, obtained term by term from the polynomial coefficients, gives $P'(\alpha)=R(\alpha)$. Therefore $P'(\alpha)=0$ holds exactly when $(x-\alpha)^2$ divides $P$. No construction of an algebraic closure is needed: the assertion holds in every field where a root is being considered.

<a id="algebra-finite-extensions"></a>

## Elementary completion: algebraic and rational function fields

The [ring and fraction-field construction](noetherian-permanence.md#algebra-rings-and-fractions) supplies the ambient fields. If $a$ in a field extension is algebraic over $E$, choose a nonzero polynomial of least degree vanishing at $a$ and divide by its leading coefficient. This gives a monic polynomial $h$. A factorization of $h$ into positive-degree factors would make one factor vanish at $a$, since the extension is a field, contradicting minimal degree. Thus $h$ is irreducible. Polynomial division shows that every polynomial vanishing at $a$ is a multiple of $h$: the remainder also vanishes and has smaller degree. In particular the monic minimal polynomial is unique.

Evaluation therefore identifies $E[a]$ with $E[T]/(h)$. This quotient is a field. For a nonzero class represented by $g$, the principal-ideal and Bézout proof above gives $(g,h)=E[T]$: a nonunit common divisor would be associated to the irreducible $h$, whereas $h$ does not divide $g$. Thus $ug+vh=1$ for some $u,v$, and the class of $u$ is an inverse. Consequently $E[a]=E(a)$, with basis $1,a,\ldots,a^{d-1}$ over $E$, where $d=\deg h$. Division proves spanning; minimality of $h$ proves linear independence.

If $b_1,\ldots,b_j$ is a basis of a field $L$ over $E$, and $c_1,\ldots,c_k$ a basis of $F$ over $L$, then the products $b_i c_l$ form a basis of $F$ over $E$. Expand coefficients in the two bases to prove spanning. In a relation among the products, independence of the $c_l$ first makes each $L$ coefficient zero, and independence of the $b_i$ makes every $E$ coefficient zero. It follows by induction that adjoining finitely many algebraic elements produces a finite-dimensional extension. Every element $v$ of a finite-dimensional extension is algebraic, since sufficiently many powers $1,v,v^2,\ldots$ are linearly dependent. Explicitly, write these powers in a basis of size $d$ and perform row elimination on the resulting $d$-by-$(d+1)$ coefficient matrix. There are at most $d$ pivot columns; assigning a nonzero value to one free variable and solving for the pivots gives a nontrivial relation. Elimination uses only division by nonzero field elements.

Elements $u_1,\ldots,u_r$ are algebraically independent over $k$ if evaluating polynomials in them is injective on $k[T_1,\ldots,T_r]$. Their generated field is consequently its fraction field, denoted $k(u_1,\ldots,u_r)$. Suppose $F=k(x_1,\ldots,x_n)$, and begin with any finite algebraically independent list already in $F$. Examine the $x_j$ in order, adding $x_j$ precisely when independence is preserved. If it is not added, a nonzero polynomial relation can be collected in powers of $x_j$; at least one coefficient remains nonzero on the independent list. Thus $x_j$ is algebraic over the field generated by that list. It remains algebraic as the independent list is enlarged, because its nonzero coefficients remain nonzero under field inclusions. The final independent list is finite; all the generators are algebraic over its rational function field $E$. Since the initial list was in $F$, adjoining the $x_j$ to $E$ recovers $F$. The preceding finite-tower argument proves that $F/E$ is finite. This proves the precise transcendence-basis assertion used in AN06-U008, including a prescribed initial transcendental element.

<a id="algebra-derivations"></a>

## Elementary completion: extending derivations

A derivation $D$ is an additive map satisfying $D(ab)=aD(b)+bD(a)$. It has $D(1)=0$, by applying this identity to $1\cdot1$. If it is zero on a subfield $k$, the product rule makes it $k$-linear. On a polynomial ring over $k$, prescribing the derivatives of its variables and differentiating each monomial defines a derivation: expansion verifies the product rule on two monomials and finite distributivity extends it to arbitrary polynomials. Algebraic independence therefore defines the usual partial derivation on the polynomial algebra generated by an independent list.

A derivation on a domain $A$, with values in its fraction field, extends uniquely to that field by

$$
 D(a/s)=\frac{D(a)}s-\frac{aD(s)}{s^2},\qquad s\ne0.
$$

For well-definedness, if $a/s=b/t$, then $at=bs$. Differentiate that equality and multiply out the difference of the proposed formulas with denominator $s^2t^2$; using $at=bs$ reduces the numerator to zero. Expansion with a common denominator proves additivity and the product rule. Conversely the product rule applied to $s\cdot s^{-1}=1$ forces this formula, proving uniqueness. This supplies a derivation on each rational function field, without choosing representations of its elements.

Let now $E$ have characteristic zero, $D:E\to E$ be a derivation, and $a$ be algebraic over $E$ with monic minimal polynomial $h(T)=\sum h_jT^j$. Separability, proved above, gives $h'(a)\ne0$. Define

$$
 b=-\frac{\sum_jD(h_j)a^j}{h'(a)}.
$$

For $g(T)=\sum g_jT^j$ define
$\delta g=\sum D(g_j)a^j+g'(a)b$.
Expanding polynomial products shows
$\delta(gq)=g(a)\delta q+q(a)\delta g$.
The choice of $b$ gives $\delta h=0$, and hence $\delta(qh)=0$ for every $q$. The evaluation kernel is exactly $(h)$, by the minimal-polynomial proof. Thus $\delta$ descends to a derivation of $E[a]=E(a)$ extending $D$ and sending $a$ to $b$. Any extension must have that value, by differentiating $h(a)=0$, and the polynomial and quotient rules then give uniqueness. Adjoining finitely many algebraic generators successively proves existence and uniqueness over every finite algebraic extension in characteristic zero. Such an extension is generated as a field by any finite vector-space basis, since a field containing the basis contains all its linear combinations. If the original derivation vanishes on $k$, each extension still does. These arguments justify both the rational-function derivative and its algebraic extension in the critical-values proof.
