# States detect the norm and positive functionals span the dual

The exact exports and hypotheses follow. OA-MOD-ST-02–07 prove these
statements first in the unital case and then for arbitrary C*-algebras.

Let \(A\) be an arbitrary complex C*-algebra, including nonunital and zero
algebras. A bounded positive functional is a bounded complex-linear map
\(\omega:A\to\mathbb C\) with \(\omega(a)\geq0\) for every \(a\in A_+\).
A state is such a functional of norm one. The following statements are
proved below.

1. If \(A\ne0\), for every \(a\in A_+\) there is a state \(\omega\) with
   \(\omega(a)=\|a\|\). For every \(h=h^*\in A\), there is a state with
   \(|\omega(h)|=\|h\|\). Thus bounded positive functionals separate positive
   elements and states determine the norm on the self-adjoint part.
   They also detect positivity: for arbitrary \(a\in A\),
   \(a\geq0\) if and only if \(\omega(a)\) is real and nonnegative for
   every state \(\omega\).
2. Every bounded hermitian functional \(g\), meaning
   \(g(a^*)=\overline{g(a)}\), has a decomposition

   \[
    g=p-q,\qquad p,q\in A^*_+,\qquad \|p\|+\|q\|=\|g\|.
    \tag{ST.1}
   \]

   This is an existence statement with a norm identity. No uniqueness,
   orthogonality, support-projection characterization, or lattice property
   of the decomposition is asserted.
3. Every \(f\in A^*\) can be written

   \[
    f=(p_1-p_2)+i(p_3-p_4),\qquad p_j\in A^*_+,\qquad
    \sum_{j=1}^4\|p_j\|\leq2\|f\|.
    \tag{ST.2}
   \]

   Consequently the complex span of the bounded positive functionals is
   all \(A^*\).

For \(A=0\), the decomposition conclusions hold with all functionals zero;
the state-separation claims are restricted to \(A\ne0\) because the zero
algebra has no norm-one functional.

The real and complex Hahn–Banach theorem is proved in NP1; strict real locally convex separation is proved in NP2. AB04 proves scalar and product compactness, closedness of compact subsets of Hausdorff spaces and preservation of compactness by continuous maps. AB05 proves Banach–Alaoglu for arbitrary real or complex normed spaces. These are written proofs of the exact inputs used below.

The required C*-spectral input is stated exactly: in an arbitrary nonzero
unital C*-algebra \(C\), every self-adjoint \(h\) has nonempty compact real
spectrum, the continuous calculus identifies \(C^*(1,h)\) isometrically and
unitally with \(C(\sigma(h))\), and
\(\|h\|=\max_{\lambda\in\sigma(h)}|\lambda|\). It preserves positivity and
gives \(0\leq a^*a\leq\|a\|^2 1\). These facts are proved in AC1–4, abstract self-adjoint calculus and positive order.
The CFC contract covers arbitrary unital complex C*-algebras, not only concrete operator algebras. No universal representation is invoked here.

The nonunital step needs an isometric *-embedding of \(A\) as a closed ideal
of a unital C*-algebra \(A^\dagger\), with the original positive cone
unchanged.
Here the named unitization is the forced unitization from OA-MOD-UZ-02–07: its construction is independent of states, and OA-MOD-UZ-07 identifies the original positive cone.

All arguments below are for arbitrary index sets and weak* topologies.
No separability, countable approximate identity, faithful state, normality
of functionals, or bidual is assumed.
The cyclic GNS construction for bounded functionals is OA-MOD-BG-01–03.

Mathematical antecedents: Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979, Chapter I, §9 for state existence, and Chapter III, §2, Proposition 2.1, printed pp. 120–121, for functional decomposition. The latter passage proves the existence and norm identity used here; its separate uniqueness assertion refers forward to another theorem. The state-extension argument and all separation and nonunital steps needed for our stated conclusions are proved below. The current prerequisite binding and proof-detail corrections are by GPT-6 Astra (OpenAI), Ultra, October 2026, CC0; earlier authorship is retained in the course records.

## Positive complexification and its norm

Let \(C\ne0\) be unital. Suppose \(u:C_{\rm sa}\to\mathbb R\) is a real
linear functional satisfying

\[
 \|u\|=u(1)=1.
 \tag{ST.3}
\]

For \(0\leq b\leq1\), continuous calculus gives \(\|1-b\|\leq1\).
Consequently \(u(b)=1-u(1-b)\geq0\). Scaling treats every positive \(b\).

Every \(a\in C\) has the unique expression

\[
 a=h+ik,\qquad h=(a+a^*)/2,\qquad k=(a-a^*)/(2i),
 \tag{ST.4}
\]

with \(h,k\) self-adjoint. Define \(\omega(a)=u(h)+iu(k)\).
Real linearity and the transformation \((h,k)\mapsto(-k,h)\) under
multiplication by \(i\) show that \(\omega\) is complex linear.
It is hermitian and positive, and the bound
\(|\omega(a)|\leq2\|u\|\|a\|\) already makes it bounded.

We record the exact sharper norm statement without using a bidual or
representation. For any positive complex-linear functional \(\rho\) on
\(C\), positivity makes \(\rho(h)\) real for self-adjoint \(h\), since
\(h\) is a difference of two positive elements by continuous calculus.
Thus \(\rho(a^*)=\overline{\rho(a)}\). The form

\[
 Q(a,b)=\rho(b^*a)
\]

is a positive semidefinite hermitian sesquilinear form, linear in its first
argument. Expanding \(Q(a+zb,a+zb)\geq0\), for \(z\in\mathbb C\), proves

\[
 |\rho(b^*a)|^2\leq\rho(a^*a)\rho(b^*b).
 \tag{ST.5}
\]

If \(Q(b,b)>0\), minimize the scalar quadratic in \(z\). If \(Q(b,b)=0\),
a nonzero mixed term would give a negative value after choosing its phase
and sufficiently large modulus, so the mixed term is zero. This covers
the degenerate case as well.

Taking \(b=1\) and using \(a^*a\leq\|a\|^2 1\) gives

\[
 |\rho(a)|^2\leq\rho(a^*a)\rho(1)
                  \leq\|a\|^2\rho(1)^2.
 \tag{ST.6}
\]

If \(\rho(1)=0\), this forces \(\rho=0\). Otherwise it proves boundedness,
and testing at \(1\), whose norm is one, gives

\[
 \|\rho\|=\rho(1).
 \tag{ST.7}
\]

In particular the complexification of \(u\) in (ST.3) is a state.

We will also use a norm identity for arbitrary hermitian \(g\in C^*\),
valid equally on a nonunital C*-algebra:

\[
 \|g\|=\|g|_{C_{\rm sa}}\|_{\mathbb R}.
 \tag{ST.8}
\]

The restriction norm is at most \(\|g\|\). For the reverse bound on \(\|g\|\), it suffices to test its real restriction: Given \(a\), choose
a scalar \(\zeta\) of modulus one with
\(\zeta g(a)=|g(a)|\), with any \(\zeta\) if the value vanishes. Then

\[
 |g(a)|=\operatorname{Re}g(\zeta a)
        =g(\operatorname{Re}(\zeta a)),\qquad
 \|\operatorname{Re}(\zeta a)\|\leq\|a\|.
\]

This proves (ST.8). The same reasoning shows that complexifying any bounded
real functional on the self-adjoint part is hermitian and preserves its
norm; no positivity is needed for this last statement.

## States attain self-adjoint spectral endpoints

Let \(h=h^*\in C\), with \(C\ne0\) unital. Choose
\(\lambda\in\sigma(h)\) such that \(|\lambda|=\|h\|\).
In the continuous calculus algebra \(C^*(1,h)\), evaluation at \(\lambda\)
is a unital positive functional of norm one. Restrict this evaluation to
the real self-adjoint part. It has real norm one, since evaluation is
contractive and takes the value one at \(1\).

Real Hahn--Banach extends it to a real functional \(u\) on \(C_{\rm sa}\)
of norm one. Its value at \(1\) remains one. By OA-MOD-ST-02, its complexification
is a state \(\omega\) on \(C\), and

\[
 \omega(h)=\lambda,\qquad |\omega(h)|=\|h\|.
 \tag{ST.9}
\]

If \(h\geq0\), its spectrum is nonnegative and we choose
\(\lambda=\|h\|\), so \(\omega(h)=\|h\|\).
For \(h=0\), the same construction on \(C^*(1,0)=\mathbb C1\) supplies
a state. Thus the state set of every nonzero unital C*-algebra is nonempty,
without presupposing a representation on a Hilbert space.

The same extension construction works for **every** \(\lambda\in\sigma(h)\),
not just one with maximal absolute value: evaluation still has norm one
and takes value one at the identity. This gives the exact positivity test.
If every state has a real nonnegative value at \(a=h+ik\), then
\(\omega(k)=0\) for every state; (ST.9) applied to \(k=k^*\) forces \(k=0\).
Now \(a=h\) is self-adjoint. If it were not positive, the positive-spectrum
criterion in the C*-order/calculus input would give some
\(\lambda\in\sigma(h)\) with \(\lambda<0\). A state extending evaluation
at that \(\lambda\) would have \(\omega(h)=\lambda<0\), a contradiction.
Conversely positive elements have nonnegative state values by definition.
This proves the exact OA-MOD-DEP-STATES positivity contract for arbitrary
nonzero unital C*-algebras, including initially nonself-adjoint test elements.

## The compact state set and its polar inequalities

Put \(V=C_{\rm sa}\), regarded as a real Banach space. Identify a state
with its restriction to \(V\), and let \(S\subseteq V^*\) be this set.
OA-MOD-ST-02 shows exactly that

\[
 S=\{u\in V^*:u(b)\geq0\ (b\in C_+),\ u(1)=1\}.
 \tag{ST.10}
\]

Each such positive real functional complexifies positively, and (ST.7)
shows that both its real norm and its complexified norm equal one.
Thus \(S\) lies in the real dual unit ball. Positivity and normalization
in (ST.10) are weak* closed conditions, being intersections of closed
evaluation conditions. Banach--Alaoglu makes \(S\) weak* compact.
It is also convex and nonempty.

By OA-MOD-ST-03 and the state norm bound,

\[
 \sup_{u\in S}|u(h)|=\|h\|\qquad(h\in V).
 \tag{ST.11}
\]

These facts are asserted here only for the unital algebra \(C\).
For a nonunital algebra its norm-one state set need not itself be weak*
closed or compact; OA-MOD-ST-07 will pass through the unitization instead.

## The signed convex hull is the full real dual ball

Define

\[
 K=\{t\omega-(1-t)\nu:
          0\leq t\leq1,\ \omega,\nu\in S\}\subseteq V^*.
 \tag{ST.12}
\]

This set lies in the dual unit ball. It is the continuous image, for the
weak* topology, of the compact space \([0,1]\times S\times S\);
hence it is compact and closed. The weak* topology is Hausdorff because two different functionals differ on some element of the predual. Its defining evaluation seminorms also make it locally convex, as required for separation below.

It is convex. Indeed, a convex combination of two displayed expressions
has nonnegative total positive coefficient \(T\) and negative coefficient
\(1-T\). If \(T>0\), normalize the positive coefficients to obtain a
convex combination of their states; if \(T=0\), choose any fixed state
for that unused term. Do the same for the negative coefficients.
The result is another expression in (ST.12). Swapping \(\omega,\nu\)
and replacing \(t\) by \(1-t\) shows \(K=-K\). Since it contains zero,
convexity and symmetry also make it balanced over the real scalars.

For each \(h\in V\),

\[
 \sup_{k\in K} k(h)=\sup_{\omega\in S}|\omega(h)|=\|h\|.
 \tag{ST.13}
\]

For the first equality, every value of an element of \(K\) is bounded above
by the supremum on the right. Conversely \(S\) and \(-S\) are contained
in \(K\) by taking \(t=1\) and \(t=0\), respectively.
The second equality is (ST.11).

For use of separation, every weak* continuous real-linear functional
\(L:V^*\to\mathbb R\) is evaluation at an element of \(V\).
Here is the finite-coordinate proof. Continuity at zero gives
\(h_1,\ldots,h_n\in V\) and a bound

\[
 |L(g)|\leq C\max_{1\leq j\leq n}|g(h_j)|\qquad(g\in V^*).
 \tag{ST.14}
\]

To obtain the bound explicitly, take \(\delta>0\) so that \(\max_j|g(h_j)|<\delta\) implies \(|L(g)|<1\). If the maximum is \(p>0\), apply this implication to \(\delta g/(2p)\), giving (ST.14) with \(C=2/\delta\). If the maximum is zero, apply it to every positive multiple of \(g\), forcing \(L(g)=0\). Thus a functional annihilating all \(h_j\) is annihilated by \(L\). Therefore \(L\) factors through the linear map
\(g\mapsto(g(h_1),\ldots,g(h_n))\) into \(\mathbb R^n\).
A real linear functional on its range extends linearly to \(\mathbb R^n\).
Writing that extension as a dot product with coefficients \(c_j\) yields

\[
 L(g)=\sum_j c_jg(h_j)=g\left(\sum_jc_jh_j\right).
 \tag{ST.15}
\]

The zero functional is evaluation at zero.

Suppose \(g\) is in the real dual unit ball but not in \(K\).
Strict separation of this point from the nonempty closed convex set \(K\)
in the real locally convex weak* topology gives \(h\in V\) with

\[
 g(h)>\sup_{k\in K}k(h)=\|h\|.
 \tag{ST.16}
\]

This contradicts \(\|g\|\leq1\). Consequently

\[
 K=\{g\in V^*:\|g\|\leq1\}.
 \tag{ST.17}
\]

This proves the polar consequence directly; no bidual, GNS representation,
or Jordan theorem is hidden in it.

## Decompositions in the unital case

Let \(g\in C^*\) be hermitian. If \(g=0\), choose both positive summands
zero. Otherwise set \(m=\|g\|>0\). By (ST.8) and (ST.17),

\[
 m^{-1}g|_V=t\omega-(1-t)\nu
\]

for \(0\leq t\leq1\) and states \(\omega,\nu\), first as real restrictions.
Complexification gives the same equation on \(C\).
Thus \(p=mt\omega\), \(q=m(1-t)\nu\) are positive and
\(\|p\|+\|q\|=m\), proving (ST.1) in the unital case.

For \(f\in C^*\), put

\[
 f^\sharp(a)=\overline{f(a^*)},\qquad
 g=(f+f^\sharp)/2,\qquad h=(f-f^\sharp)/(2i).
 \tag{ST.18}
\]

The map \(f^\sharp\) is complex linear and bounded with norm \(\|f\|\).
Both \(g,h\) are hermitian, \(f=g+ih\), and
\(\|g\|,\|h\|\leq\|f\|\). Applying the preceding paragraph separately to
\(g\) and \(h\) gives the four positive summands of (ST.2), with

\[
 \sum_{j=1}^4\|p_j\|=\|g\|+\|h\|\leq2\|f\|.
 \tag{ST.19}
\]

The bound two is sufficient here; no optimal four-term constant is claimed.

## Passage to a nonunital algebra

Assume now the explicit unitization input in the introductory theorem, and identify \(A\)
isometrically with its closed *-ideal in a unital C*-algebra \(A^\dagger\).
If \(A\ne0\), its unitization is nonzero.

Take \(0\ne h=h^*\in A\). Apply OA-MOD-ST-03 inside \(A^\dagger\) to obtain a
state \(\Omega\) with \(|\Omega(h)|=\|h\|\). The restriction
\(\omega=\Omega|_A\) is positive and has norm at most one. Evaluation at
\(h/\|h\|\) shows its norm is at least one; hence it is a state of \(A\).
For \(h\geq0\) the value is \(\|h\|\), with no absolute value required.
If \(h=0\), choose any nonzero \(a\in A\); then \(a^*a\ne0\), and the
preceding positive case supplies a state, which of course vanishes at
zero. This proves the norming assertion of the introductory theorem for every nonzero \(A\).

The positivity test extends as well. If all states of \(A\) take real
nonnegative values at \(a=h+ik\), their norming property forces \(k=0\).
If \(h\) were not positive, equality of the original and inherited cones
from OA-MOD-UZ-07 would make it nonpositive in \(A^\dagger\). Choose a negative
spectral value \(\lambda\) and the corresponding state \(\Omega\) on
\(A^\dagger\), as in OA-MOD-ST-03. Its positive restriction \(\rho\) to \(A\)
is nonzero because \(\rho(h)=\lambda<0\). Therefore
\(\rho/\|\rho\|\) is a state of \(A\) with negative value at \(h\),
contradicting the hypothesis. The converse again follows from positivity.

The norm-additive hermitian decomposition also descends. Let
\(g\in A^*\) be hermitian. Its real restriction to \(A_{\rm sa}\) has norm
\(\|g\|\) by (ST.8). Real Hahn--Banach extends it to a real functional
on \((A^\dagger)_{\rm sa}\) of the same norm. Complexification, again by
the norm argument in (ST.8), yields a hermitian
\(G\in(A^\dagger)^*\), with \(G|_A=g\) and \(\|G\|=\|g\|\).
The unital case gives \(G=P-Q\), where \(P,Q\) are positive and
\(\|P\|+\|Q\|=\|G\|\). Restrict them to \(A\), writing \(p,q\).
Then \(g=p-q\), and

\[
 \|g\|\leq\|p\|+\|q\|
          \leq\|P\|+\|Q\|=\|G\|=\|g\|.
 \tag{ST.20}
\]

All inequalities are therefore equalities, proving (ST.1) without a
unit. No uniqueness claim is needed.

Finally split an arbitrary \(f\in A^*\) as in (ST.18), which uses only
the involution and the norm. Apply the just-proved nonunital hermitian
case to \(g\) and \(h\). Equations (ST.2) and (ST.19) follow unchanged.
In particular every element of the full Banach dual belongs to the
complex span of its bounded positive cone.

An alternative sufficient route for the four-term statement alone is to
extend \(f\) by complex Hahn--Banach to \(A^\dagger\), decompose there by
OA-MOD-ST-06, and restrict the four positive terms. The real-extension argument
above records the additional norm-additive hermitian existence statement.
