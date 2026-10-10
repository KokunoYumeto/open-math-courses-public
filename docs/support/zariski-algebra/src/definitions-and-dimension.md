# Finite presentations and dimension under a quotient

*Independent programme text by GPT-6 Astra (OpenAI), Codex, Ultra, October 2026. CC0-1.0.*

These definitions and the quotient comparison complete the prerequisite routes for the conductor and field-extension arguments. All rings are commutative with identity, and their homomorphisms preserve the identity.

## Finite modules and their presentations

An \(R\)-module \(M\) is **finite**, or **finitely generated**, when some finite list \(m_1,\ldots,m_n\) spans it with coefficients in \(R\). Equivalently, the \(R\)-linear map \(R^n\to M\) sending the standard basis to that list is surjective.

The module is **finitely presented** when there are finite nonnegative integers \(a,b\) and an exact sequence of \(R\)-linear maps

\[
R^a\xrightarrow{C}R^b\xrightarrow{\pi}M\longrightarrow0.
\]

Thus \(\pi\) is onto and \(\ker\pi=\operatorname{im}C\): finitely many chosen generators admit a finite list of module relations. Nothing requires \(C\) to be injective. Zero generators and zero relations are permitted. The distinction between finiteness and finite presentation matters over non-Noetherian rings.

## Finite-type and finitely presented algebras

For a specified homomorphism \(R\to S\), the algebra \(S\) is **of finite type** over \(R\) if a homomorphism of \(R\)-algebras \(R[T_1,\ldots,T_n]\to S\) is surjective for some finite \(n\). It is **of finite presentation** over \(R\) if such a surjection can be chosen with a finitely generated kernel. Explicitly, there are finite lists of variables and polynomials with

\[
S\cong R[T_1,\ldots,T_n]/(f_1,\ldots,f_m)
\]

as \(R\)-algebras. Empty lists are allowed. The polynomials generate an ideal, whereas the relations in a module presentation generate a submodule; these are different notions of finite presentation.

## Finite ring maps

A ring homomorphism \(R\to S\) is **finite** if the \(R\)-module underlying \(S\), with scalar action induced by this homomorphism, is finite. This condition is stronger than finite type: a finite module generating list also generates the algebra, but \(R[T]\) over a nonzero \(R\) is of finite type and is not a finite \(R\)-module. Indeed, the degrees in any finite list of polynomials are bounded, and taking \(R\)-linear combinations cannot produce a monomial of higher degree.

The finite-presentation comparison requires both a finite ring map and an algebra of finite presentation. Its proof includes the conversion to a finite module presentation and explains why neither hypothesis can simply be dropped.

## Dimension comparison for a surjective algebra map

**Proposition.** Let \(k\) be a field and let \(f\colon B\twoheadrightarrow A\) be a surjective homomorphism of finite-type \(k\)-algebras. For a prime \(p\subset A\), put \(q=f^{-1}(p)\subset B\). Let \(x\in X=\operatorname{Spec}A\) and \(y\in Y=\operatorname{Spec}B\) be the corresponding points. Then

\[
\dim_yY-\dim_xX=\operatorname{ht}_B(q)-\operatorname{ht}_A(p).
\]

Here pointwise dimension means the minimum of the dimensions of open neighborhoods. It is not generally the dimension of the local ring. No reducedness, equidimensionality or closed-point assumption is made.

**Proof.** The induced map \(B/q\to A/p\) is a \(k\)-algebra isomorphism: surjectivity follows from that of \(f\), and its kernel is zero by the definition of \(q\). Taking fraction fields gives a specified \(k\)-isomorphism \(\kappa(q)\cong\kappa(p)\). Write their common transcendence degree over \(k\) as \(e\).

AG-CA-09, Theorem 6.1 proves the pointwise-dimension formula for every finite-type algebra over a field, including rings with nilpotents and components of different dimensions. Applying it separately to the two algebras yields

\[
\dim_yY=\dim B_q+e,
\qquad
\dim_xX=\dim A_p+e.
\]

For any ring \(C\) and prime \(r\), localization identifies prime chains in \(C_r\) with prime chains in \(C\) contained in \(r\), preserving strict inclusions. Every such chain can be extended to end at \(r\). Therefore \(\dim C_r=\operatorname{ht}_C(r)\); the prime correspondence is proved in AG-CA-02, Theorem 3.1. Substitute these two height identities and subtract the displayed equations. The residue-field terms cancel because of the actual quotient-induced isomorphism, not an assumption that the points are closed. \(\square\)

**Check at nonclosed points.** For \(B=k[U,V]\), \(A=B/(U)\), and the generic point \(p=(0)\) of \(A\), the inverse-image prime is \(q=(U)\). The pointwise dimensions are \(2\) and \(1\); the heights are \(1\) and \(0\). Both differences are \(1\). In particular, replacing pointwise dimension by local-ring dimension in the premise would change the meaning of the theorem.

## Sources and proof routes

The finite-type definition and quotient comparison correspond respectively to Stacks Project tags [00F3](https://stacks.math.columbia.edu/tag/00F3) and [00P2](https://stacks.math.columbia.edu/tag/00P2). The other two definitions fix the module and algebra conventions. The proposition above is independently written from the full internal dimension formula, rather than using an external proof citation as its proof.

The complete result route map identifies all seventeen units formerly supplied by the conductor-support selection, including the intermediate lemmas now proved in AG-QC, Appendix Z. The main algebra reader supplies the finite-presentation and arbitrary-field-extension comparisons. Their full hypotheses and useful alternative arguments remain unchanged.
