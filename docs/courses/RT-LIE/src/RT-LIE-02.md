# Nilpotent and solvable Lie algebras: Engel's and Lie's theorems

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An algebra of upper-triangular operators preserves a flag. An algebra of strictly upper-triangular operators does more: every sufficiently long product of its operators is zero. Engel's and Lie's theorems recover these matrix pictures from intrinsic conditions. Their conclusions look similar, but their hypotheses and their dependence on the ground field differ.

The prerequisite is [Lie algebras: definitions, examples and first constructions](RT-LIE-01.md). We use its ideals, quotients, adjoint representation and module operations. All Lie algebras and representation spaces in this lesson are finite-dimensional unless a paragraph explicitly says otherwise. Engel's theorem works over every field. Lie's theorem will require an algebraically closed field of characteristic zero. The basic reference is [Milne, Lie algebras].

## 1. Two ways brackets can run out

For a Lie algebra \(\mathfrak g\), define the lower central series and the derived series by

\[
C^1\mathfrak g=\mathfrak g,\qquad
C^{r+1}\mathfrak g=[\mathfrak g,C^r\mathfrak g],\qquad
D^0\mathfrak g=\mathfrak g,\qquad
D^{r+1}\mathfrak g=[D^r\mathfrak g,D^r\mathfrak g].
\]

Each term is an ideal. For the lower central series this follows inductively from Jacobi:
\([x,[y,z]]=[[x,y],z]+[y,[x,z]]\).
For the derived series the same identity applies with both bracket arguments in the preceding ideal. The series are decreasing.

The algebra is **nilpotent** if \(C^{c+1}\mathfrak g=0\) for some \(c\), and **solvable** if \(D^r\mathfrak g=0\) for some \(r\). The zero algebra satisfies both definitions. The inclusion \(D^r\mathfrak g\subseteq C^{r+1}\mathfrak g\), proved by induction using the decreasing central series, shows that nilpotence implies solvability. The reverse implication fails.

For example, in the algebra with basis \(x,y\) and \([x,y]=y\),

\[
D^1\mathfrak g=ky,\qquad D^2\mathfrak g=0,\qquad
C^r\mathfrak g=ky\quad(r\ge2).
\]

It is solvable but not nilpotent. Its centre is zero. In contrast, the Heisenberg algebra has \(C^2=kz\) and \(C^3=0\).

There is a useful way to count matrix brackets. Let \(F^r\) be the space of \(n\times n\) matrices whose possibly nonzero entries satisfy \(j-i\ge r\). Then

\[
F^rF^s\subseteq F^{r+s},\qquad
[F^r,F^s]\subseteq F^{r+s}.
\]

Indeed, a nonzero summand \(X_{ik}Y_{kj}\) requires \(k-i\ge r\) and \(j-k\ge s\). The strictly upper-triangular algebra is \(F^1\), so \(C^r\mathfrak n_n\subseteq F^r\) and \(C^n\mathfrak n_n=0\). Its nilpotence class is \(n-1\) when \(n\ge2\): successive brackets of \(E_{12},E_{23},\ldots,E_{n-1,n}\) produce \(E_{1n}\ne0\).

The upper-triangular algebra \(\mathfrak b_n\) satisfies
\([\mathfrak b_n,\mathfrak b_n]\subseteq F^1\), because a commutator has zero diagonal. Consequently
\(D^r\mathfrak b_n\subseteq F^{2^{r-1}}\) for \(r\ge1\); it is solvable. For \(n\ge2\) it is not nilpotent, since it contains \(E_{11},E_{12}\) with \([E_{11},E_{12}]=E_{12}\).

For \(\mathfrak b_2\), this is an exact calculation:
\(D^1=kE_{12}\), \(D^2=0\), and \(C^r=kE_{12}\) for every \(r\ge2\).
The first equality follows from the zero diagonal of every commutator and the displayed bracket. Bracketing \(E_{12}\) again with \(E_{11}\) proves that the central series never terminates.

**Proposition 1.1 (passing to smaller algebras).** Subalgebras and quotients of nilpotent algebras are nilpotent. Subalgebras and quotients of solvable algebras are solvable. If \(I\) is a solvable ideal and \(\mathfrak g/I\) is solvable, then \(\mathfrak g\) is solvable.

**Proof.** The relevant series of a subalgebra lies in the series of the ambient algebra. A surjective homomorphism maps each series term onto the corresponding quotient term, by induction from bracket preservation. Finally, if \(D^a(\mathfrak g/I)=0\), then \(D^a\mathfrak g\subseteq I\). If \(D^bI=0\), repeated bracketing gives \(D^{a+b}\mathfrak g\subseteq D^bI=0\). \(\square\)

An extension of nilpotent algebras need not be nilpotent: the preceding two-dimensional example has nilpotent ideal \(ky\) and nilpotent quotient \(kx\).

**Proposition 1.2 (extending the field).** For a field extension \(K/k\), the algebra \(K\otimes_k\mathfrak g\) is nilpotent, respectively solvable, exactly when \(\mathfrak g\) is.

**Proof.** Bilinearity gives
\([K\otimes U,K\otimes W]=K\otimes[U,W]\).
Induction identifies both series after extending the field. A nonzero vector space remains nonzero under field extension, as any basis shows, so termination before and after extension is equivalent. \(\square\)

## 2. Engel's theorem: a common zero vector

An endomorphism \(X\) is nilpotent if \(X^r=0\) for some \(r\). This says something about an action, whereas nilpotence of a Lie algebra says something about its brackets. The adjoint action connects the two.

We first need an elementary observation. On \(\operatorname{End}(V)\), write
\(\operatorname{ad}X=L_X-R_X\), where \(L_X(T)=XT\) and \(R_X(T)=TX\). These two operators commute. If \(X^r=0\), then

\[
(\operatorname{ad}X)^{2r-1}
=\sum_{j=0}^{2r-1}(-1)^j
\binom{2r-1}{j}L_X^{\,2r-1-j}R_X^j=0.
\]

Every summand has at least \(r\) copies of \(L_X\) or \(R_X\). This proof uses no division, so it is valid in every characteristic. Restrictions to invariant subspaces and induced maps on quotients are also nilpotent.

**Theorem 2.1 (Engel, linear form).** Let \(V\ne0\) and let
\(\mathfrak l\subseteq\mathfrak{gl}(V)\) be a Lie subalgebra all of whose elements are nilpotent endomorphisms. There is \(v\ne0\) such that \(Xv=0\) for every \(X\in\mathfrak l\). There is a basis in which all elements of \(\mathfrak l\) are strictly upper-triangular.

**Proof.** Induct on \(\dim\mathfrak l\). The zero algebra is immediate. Assume the assertion about a common zero vector is known for smaller-dimensional operator algebras.

For every proper subalgebra \(\mathfrak k\subsetneq\mathfrak l\), let \(\mathfrak k\) act on \(\mathfrak l/\mathfrak k\) by brackets. This action is well-defined because \([\mathfrak k,\mathfrak k]\subseteq\mathfrak k\). Every acting operator is nilpotent by the observation above. Its image has dimension at most \(\dim\mathfrak k<\dim\mathfrak l\), so induction supplies a nonzero class \(Z+\mathfrak k\) killed by \(\mathfrak k\). Thus \([\mathfrak k,Z]\subseteq\mathfrak k\), and the normalizer of \(\mathfrak k\) strictly contains \(\mathfrak k\).

Choose a maximal proper subalgebra \(\mathfrak k\). Its normalizer is therefore \(\mathfrak l\), so it is an ideal. It has codimension one: if \(\dim(\mathfrak l/\mathfrak k)>1\), a one-dimensional subspace of this quotient is a proper nonzero subalgebra, contradicting maximality after taking its inverse image.

Induction on \(\mathfrak k\subseteq\mathfrak{gl}(V)\) gives

\[
W=\{v\in V:Kv=0\text{ for all }K\in\mathfrak k\}\ne0.
\]

This subspace is \(\mathfrak l\)-invariant. Indeed,
\(K(Xw)=X(Kw)+[K,X]w=0\), since \(\mathfrak k\) is an ideal. Write \(\mathfrak l=\mathfrak k+kZ\). The nilpotent operator \(Z|_W\) has nonzero kernel: otherwise all its powers would be injective, contrary to a power being zero. A nonzero vector in that kernel is killed by all of \(\mathfrak l\). This completes the induction.

The line \(kv\) is killed by \(\mathfrak l\). On \(V/kv\) the induced operators remain nilpotent, so repeat the common-vector assertion. We obtain a flag

\[
0=V_0\subset V_1\subset\cdots\subset V_d=V,\qquad
\dim V_i=i,\qquad \mathfrak lV_i\subseteq V_{i-1}.
\]

A basis adapted to this flag gives the claimed matrices. \(\square\)

**Corollary 2.2 (Engel, intrinsic form).** Over every field,
\(\mathfrak g\) is nilpotent if and only if each \(\operatorname{ad}x\) is nilpotent.

**Proof.** If \(C^{c+1}\mathfrak g=0\), then
\((\operatorname{ad}x)^c\mathfrak g\subseteq C^{c+1}\mathfrak g=0\).
Conversely, apply Theorem 2.1 to \(\operatorname{ad}\mathfrak g\) acting on \(\mathfrak g\). In a strictly triangular basis every product of \(d=\dim\mathfrak g\) adjoint operators is zero. Since \(C^{d+1}\mathfrak g\) is spanned by their values on vectors, it is zero. The zero algebra needs no argument. \(\square\)

**Corollary 2.3.** Every nonzero ideal of a nilpotent algebra meets its centre nontrivially. In particular a nonzero nilpotent algebra has nonzero centre.

**Proof.** For a nonzero ideal \(I\), set \(I_0=I\) and \(I_{j+1}=[\mathfrak g,I_j]\). These spaces eventually vanish, because \(I_j\subseteq C^{j+1}\mathfrak g\). The last nonzero one is killed by bracketing with \(\mathfrak g\), hence lies in \(I\cap Z(\mathfrak g)\). \(\square\)

The representation matters. A one-dimensional abelian algebra is nilpotent, but it can act by the identity on \(k\), which is not a nilpotent operator. Engel's intrinsic criterion concerns its adjoint action.

## 3. Lie's theorem: a common eigenvector

Strict triangularity required nilpotent operators. For solvable algebras the best possible conclusion is ordinary triangularity: diagonal characters may remain.

**Theorem 3.1 (Lie).** Suppose \(k\) is algebraically closed of characteristic zero. If a solvable Lie algebra \(\mathfrak g\) acts on \(V\ne0\), it has a common eigenvector:

\[
xv=\lambda(x)v\quad(x\in\mathfrak g)
\]

for some nonzero \(v\) and linear functional \(\lambda:\mathfrak g\to k\).
The action is upper-triangular in a suitable basis.

**Proof.** Induct on \(\dim\mathfrak g\), beginning with the zero algebra. For nonzero solvable \(\mathfrak g\), the ideal \([\mathfrak g,\mathfrak g]\) is proper; otherwise its derived series would never reach zero. Choose a codimension-one subspace \(\mathfrak a\) containing it. This is an ideal and is solvable. Induction yields \(v\ne0\) and \(\lambda:\mathfrak a\to k\) such that \(yv=\lambda(y)v\).

Choose \(x\notin\mathfrak a\). Let \(W\) be the cyclic space spanned by \(v,xv,x^2v,\ldots\), and choose its basis
\(v,xv,\ldots,x^{r-1}v\), stopping at the first dependence. This basis exists because \(V\) is finite-dimensional. The space \(W\) is \(x\)-invariant.

For \(y\in\mathfrak a\), induction on \(j\) gives

\[
yx^jv-\lambda(y)x^jv
\in\operatorname{span}\{v,xv,\ldots,x^{j-1}v\}.
\tag{3.1}
\]

The case \(j=0\) is the choice of \(v\). For the step, write
\(yx^jv=x(yx^{j-1}v)+[y,x]x^{j-1}v\).
The inductive assertion applies also to \([y,x]\in\mathfrak a\), so the second term lies in the indicated lower span; the first has leading term \(\lambda(y)x^jv\). Thus \(W\) is \(\mathfrak a\)-invariant and every \(y|_W\) has all diagonal entries \(\lambda(y)\).

Both \(x\) and \(y\) preserve \(W\), so the trace of their commutator is zero. Applying (3.1) to \([x,y]\) gives

\[
0=\operatorname{tr}([x,y]|_W)=r\lambda([x,y]).
\]

Characteristic zero implies \(\lambda([x,y])=0\). Now consider the entire simultaneous eigenspace
\[
E_\lambda=\{w:yw=\lambda(y)w\text{ for all }y\in\mathfrak a\}.
\]
It is nonzero and \(x\)-invariant, because for \(w\in E_\lambda\),
\(y(xw)=\lambda(y)xw+[y,x]w=\lambda(y)xw\).
An operator on a nonzero finite-dimensional space over an algebraically closed field has an eigenvector. Choose one for \(x|_{E_\lambda}\); it is a common eigenvector for \(\mathfrak a+kx=\mathfrak g\).

Its line is invariant. Repeat the theorem on the quotient and lift the resulting flag to \(V\). A flag-adapted basis makes all operators upper-triangular. \(\square\)

Any common eigenvalue functional vanishes on \([\mathfrak g,\mathfrak g]\), since scalars commute. An irreducible nonzero finite-dimensional representation of a solvable algebra under these hypotheses is therefore one-dimensional: its common eigenvector spans a nonzero invariant subspace.

**Corollary 3.2.** Over every field of characteristic zero, \(\mathfrak g\) is solvable if and only if \([\mathfrak g,\mathfrak g]\) is nilpotent.

**Proof.** First suppose the field is algebraically closed. If \(\mathfrak g\) is solvable, triangularize its adjoint representation. Commutators of upper-triangular matrices are strictly upper-triangular. Thus for every \(z\in[\mathfrak g,\mathfrak g]\), its action on that derived ideal is nilpotent. Engel's intrinsic criterion makes the ideal nilpotent. For an arbitrary characteristic-zero field, extend to an algebraic closure and apply Proposition 1.2 to the algebra and its derived ideal. Conversely a nilpotent derived ideal is solvable, and the quotient by it is abelian; Proposition 1.1 makes \(\mathfrak g\) solvable over any field. \(\square\)

## 4. The radical collects all solvable ideals

**Proposition 4.1.** There is a largest solvable ideal, denoted
\(\operatorname{rad}(\mathfrak g)\). Its quotient has zero radical.

**Proof.** If \(I,J\) are solvable ideals, \((I+J)/I\) is isomorphic to
\(J/(I\cap J)\), so it is solvable. Proposition 1.1 shows that \(I+J\) is solvable. Induction gives the same conclusion for any finite sum.

The sum \(R\) of all solvable ideals is already a finite sum: choose a basis of \(R\), write each basis vector using finitely many such ideals, and collect the resulting finite list. Thus \(R\) is a solvable ideal containing every other one. This proves existence and maximality.

If \(\bar J\) is a solvable ideal in \(\mathfrak g/R\), its inverse image \(J\) is an ideal containing \(R\). The extension with solvable ideal \(R\) and quotient \(J/R=\bar J\) is solvable, so \(J\subseteq R\). Hence \(\bar J=0\). \(\square\)

For the two-dimensional algebra above, the radical is the whole algebra even though its centre is zero. A radical is not a centre. The radical of \(\mathfrak b_n\) is likewise \(\mathfrak b_n\).

## 5. What the field conditions protect

Over \(\mathbb R\), the abelian algebra spanned by
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]
is solvable, but its action on \(\mathbb R^2\) has no real eigenvector: \(J^2=-1\), so a real eigenvalue would have square \(-1\). This is the rotation algebra \(\mathfrak{so}(I_2)\). Passing to \(\mathbb C\) supplies the missing eigenlines.

In characteristic \(p>0\), take \(A=k[t]/(t^p)\). Differentiation \(D\) is well-defined because \(D(t^p)=0\); let \(T\) be multiplication by \(t\). Then
\[
[D,T]=1,\qquad [D,1]=[T,1]=0.
\]
The span of \(D,T,1\) is a three-dimensional Heisenberg algebra, hence nilpotent and solvable. Its action on \(A\) is irreducible. From any nonzero polynomial of degree \(r<p\), differentiation \(r\) times produces a nonzero constant, since \(r!\ne0\). Multiplication then produces every \(1,t,\ldots,t^{p-1}\). In particular, no invariant line exists. This violates Lie's conclusion, but not Engel's hypothesis: the represented algebra contains the identity.

There is also a two-dimensional example. On \(B=k[t]/(t^p-1)\), put \(X=t\partial_t\) and \(Y=t\), again interpreting \(Y\) as multiplication. Both operators are well-defined, and
\[
[X,Y]=Y,\qquad Y^p=1,\qquad X(t^j)=jt^j.
\]
The eigenvalues \(0,1,\ldots,p-1\) of \(X\) are distinct in \(k\). A nonzero invariant subspace contains one basis vector: polynomial projections in \(X\) isolate a nonzero coefficient of any of its vectors. Applying \(Y\) cyclically then gives every basis vector, including the step \(t^{p-1}\mapsto1\). The action is irreducible of dimension \(p\). The two represented generators are independent and give precisely the algebra \([x,y]=y\). Here the trace step of Lie's proof fails because the integer \(r=p\) becomes zero.

Finite-dimensionality also matters. The abelian algebra \(\mathbb Cx\) acts on \(\mathbb C[t]\) by making \(x\) multiplication by \(t\). There is no eigenvector, since \((t-\lambda)f(t)=0\) implies \(f=0\).

Engel's common-zero-vector assertion also fails for an infinite-dimensional operator algebra. Take \(V=k[t_1,t_2,\ldots]/(t_i^2:i\ge1)\) and let \(\mathfrak l\) be spanned by multiplication by the \(t_i\). These operators commute. Every element of \(\mathfrak l\) involves finitely many variables and is nilpotent: in a product longer than their number some variable repeats, making that term zero. But any nonzero polynomial involves only finitely many variables; multiplication by a fresh \(t_i\) is nonzero. The square-free monomials form a basis, so no cancellation changes this conclusion. There is no common nonzero zero vector.

## 6. Exercises with complete solutions

**Exercise 6.1 (easy).** Prove nilpotence of \(\mathfrak n_n\) and solvability of \(\mathfrak b_n\), give a bound on each series, and compute both series for \(\mathfrak n_3\).

**Solution.** Multiplication gives \(F^rF^s\subseteq F^{r+s}\). Hence \(C^r\mathfrak n_n\subseteq F^r\), which vanishes for \(r\ge n\). Also \(D^1\mathfrak b_n\subseteq F^1\) and \(D^r\mathfrak b_n\subseteq F^{2^{r-1}}\) for \(r\ge1\), so this series reaches zero. In \(\mathfrak n_3\), the basis \(E_{12},E_{23},E_{13}\) has only \([E_{12},E_{23}]=E_{13}\) nonzero. Thus \(C^2=D^1=kE_{13}\) and \(C^3=D^2=0\). The same basis realizes the three-dimensional Heisenberg algebra.

**Exercise 6.2 (medium).** Show that every nonzero ideal \(I\) in a nilpotent algebra has \(I\cap Z(\mathfrak g)\ne0\). Explain why the word “nonzero” is necessary.

**Solution.** The sequence \(I,[\mathfrak g,I],[\mathfrak g,[\mathfrak g,I]],\ldots\) terminates because its terms lie in the lower central series. Its last nonzero term is contained in \(I\), and its bracket with \(\mathfrak g\) is zero, so it lies in the centre. The zero ideal has zero intersection with every subspace, so it must be excluded. Taking \(I=\mathfrak g\ne0\) gives a nonzero centre.

**Exercise 6.3 (medium).** In characteristic \(p\), verify the two-dimensional representation on \(k[t]/(t^p-1)\) from Section 5 and prove its irreducibility. Compare it with \(D,T\) on \(k[t]/(t^p)\).

**Solution.** Since \(t\partial_t(t^p-1)=pt^p=0\), \(X\) descends; multiplication always descends. The product rule gives \([X,Y]f=tf=Yf\). On the basis \(1,t,\ldots,t^{p-1}\), \(X\) has the distinct eigenvalues \(j\). The polynomials
\[
\pi_j(z)=\prod_{\substack{0\le i<p\\i\ne j}}\frac{z-i}{j-i}
\]
are defined in \(k[z]\) and make \(\pi_j(X)\) the coordinate projections. A nonzero submodule therefore contains some \(t^j\). Since \(Y\) shifts indices cyclically modulo \(p\), it contains the whole basis. For the other pair, \(DT-TD=1\), so \(D,T\) alone do not span a Lie subalgebra; adjoining \(1\) gives the solvable three-dimensional example. Repeated differentiation followed by multiplication proves its irreducibility as above.

**Exercise 6.4 (hard).** Recover Engel's common-zero-vector theorem by induction on the dimension of the operator algebra. Identify why a maximal proper subalgebra must be an ideal of codimension one.

**Solution.** For a proper \(\mathfrak k\subsetneq\mathfrak l\), its bracket action on \(\mathfrak l/\mathfrak k\) consists of nilpotent maps: each is induced by \(\operatorname{ad}K\), and the binomial calculation gives nilpotence from nilpotence of \(K\) on \(V\). Induction, applied to the image of \(\mathfrak k\), gives a nonzero annihilated class. A representative outside \(\mathfrak k\) normalizes it, so \(N_{\mathfrak l}(\mathfrak k)\supsetneq\mathfrak k\). If \(\mathfrak k\) is maximal proper, its normalizer must be \(\mathfrak l\), making it an ideal. A quotient of dimension greater than one has a proper one-dimensional subalgebra, contradicting maximality; thus the quotient has dimension one.

Induction also gives a nonzero annihilator \(W\) of \(\mathfrak k\) in \(V\). Idealness implies \(W\) is \(\mathfrak l\)-invariant by \(K(Xw)=[K,X]w+XKw=0\). A complementary generator \(Z\) acts nilpotently on \(W\) and has nonzero kernel. A vector in that kernel is killed by \(\mathfrak k+kZ\). The zero algebra begins the induction. Applying this assertion successively to quotient spaces constructs the strictly triangular flag.

## What this lesson does not prove

The linear-algebra prerequisites are basis extension [Hefferon, Chapter Two §III.2, Corollary 2.12], trace of a commutator, and the existence of an eigenvalue over an algebraically closed field. Trace-cyclicity was computed in the prerequisite. The characteristic polynomial has a root by the definition of an algebraically closed field; over \(\mathbb C\), this also follows from the fundamental theorem of algebra [Hefferon, Chapter Five §I.1, Theorem 1.11]. Engel's theorem, Lie's theorem and every assertion about the series and radical were proved here.

Corollary 3.2 also uses [existence of an algebraic closure for every field](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-theorem-existence-algebraic-closure), proved in the AI Integrated Stacks programme's *Fields* chapter ([the complete native proof](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/fields.tex#L999)). That construction uses Zorn's lemma, a form of the axiom of choice. The algebraic closure is chosen, not asserted to be canonical. Proposition 1.2 then supplies the descent of the derived and lower central series to the original field, so the corollary retains its full characteristic-zero scope.

## References

- **[Milne, Lie algebras]** J. S. Milne, *Lie Algebras, Algebraic Groups, and Lie Groups*, version 2.00, 2013, Chapter I §§2–3. [Author's notes](https://www.jmilne.org/math/CourseNotes/LAG.pdf).
- **[Hefferon]** J. Hefferon, *Linear Algebra*, fourth edition, 2020, Chapter Five §I.1. [Author's textbook](https://jheffero.w3.uvm.edu/linearalgebra/book.pdf).
