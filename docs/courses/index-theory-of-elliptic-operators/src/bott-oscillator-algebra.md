# Exterior algebra and the Bott-oscillator identity

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions (finite trivializing covers over manifolds that are not compact; providers and proofs for the background facts) are self-checked by the writing AI. Public domain (CC0).*

Supporting excerpts from *The Bott operator, suspension and reduction of the index to Euclidean space*, Sections 3–4. These supply the exterior-algebra conventions and Lemma 4.1 used in Section 6 of the Hermite lesson. This is not the complete Bott/index lesson.

The parent lesson credits Atiyah's proof of Bott periodicity by elliptic operators for the harmonic-oscillator construction. The index-one argument itself is outside this excerpt.

## Exterior algebra: definitions and Lemma 3.1

Let \(\Lambda=\Lambda(\mathbb C^n)=\bigoplus_{q=0}^n\Lambda^q\) be the exterior algebra of \(\mathbb C^n\). We give \(\mathbb C^n\) the inner product \(\langle z,w\rangle=\sum_jz_j\overline{w_j}\), and \(\Lambda^q\) the inner product
\[
\langle u_1\wedge\dots\wedge u_q,\ v_1\wedge\dots\wedge v_q\rangle=\det\bigl(\langle u_i,v_k\rangle\bigr)_{i,k=1}^q,
\]
with different degrees orthogonal. For \(J=\{j_1<\dots<j_q\}\) put \(e_J=e_{j_1}\wedge\dots\wedge e_{j_q}\). These vectors form an orthonormal basis. Write \(\Lambda^e=\bigoplus_q\Lambda^{2q}\) and \(\Lambda^o=\bigoplus_q\Lambda^{2q+1}\). For \(w\in\mathbb C^n\) let \(\Lambda(w)v=w\wedge v\) and let \(\Lambda(w)^*\) be its adjoint. Put \(\varepsilon_j=\Lambda(e_j)\), \(\iota_j=\varepsilon_j^*\), and \(\mathcal N=\sum_j\varepsilon_j\iota_j\).

**Lemma 3.1.** (1) Let \(\sigma(j,J)=(-1)^{\#\{k\in J:\,k<j\}}\). Then \(\varepsilon_je_J=\sigma(j,J)e_{J\cup\{j\}}\) if \(j\notin J\) and \(0\) otherwise; \(\iota_je_J=\sigma(j,J)e_{J\setminus\{j\}}\) if \(j\in J\) and \(0\) otherwise.

(2) For all \(j,l\):
\[
\varepsilon_j\varepsilon_l+\varepsilon_l\varepsilon_j=0,\qquad
\iota_j\iota_l+\iota_l\iota_j=0,\qquad
\varepsilon_j\iota_l+\iota_l\varepsilon_j=\delta_{jl}I .
\tag{3.1}
\]
(3) \(\Lambda(w)=\sum_jw_j\varepsilon_j\), \(\Lambda(w)^*=\sum_j\overline{w_j}\iota_j\), \(\Lambda(w)^2=0\), and
\[
\Lambda(w)\Lambda(w)^*+\Lambda(w)^*\Lambda(w)=|w|^2I .
\tag{3.2}
\]
Also \(\mathcal Ne_J=|J|\,e_J\): the operator \(\mathcal N\) multiplies a form of degree \(q\) by \(q\).

**Proof.** (1) To write \(e_j\wedge e_J\) in increasing order, move \(e_j\) past the elements of \(J\) that are smaller than \(j\); each move gives a factor \(-1\). If \(J=K\cup\{j\}\) with \(j\notin K\), then \((\varepsilon_je_K,e_J)=\sigma(j,K)=\sigma(j,J)\), and all other inner products vanish; this gives \(\iota_j\).

(2) The first relation is \(e_j\wedge e_l=-e_l\wedge e_j\); the second is its adjoint. For the third, take \(j=l\) first. If \(j\in J\) then \(\varepsilon_j\iota_je_J=e_J\) (the two signs are equal) and \(\iota_j\varepsilon_je_J=0\); if \(j\notin J\) the roles swap. Now let \(j\ne l\). Both \(\varepsilon_j\iota_le_J\) and \(\iota_l\varepsilon_je_J\) vanish unless \(l\in J\) and \(j\notin J\). Then both are multiples of \(e_K\), \(K=(J\setminus\{l\})\cup\{j\}\):
\[
\varepsilon_j\iota_le_J=\sigma(l,J)\sigma(j,J\setminus\{l\})e_K,\qquad
\iota_l\varepsilon_je_J=\sigma(j,J)\sigma(l,J\cup\{j\})e_K .
\]
If \(j<l\), then \(\sigma(j,J\setminus\{l\})=\sigma(j,J)\) and \(\sigma(l,J\cup\{j\})=-\sigma(l,J)\). If \(j>l\), then \(\sigma(j,J\setminus\{l\})=-\sigma(j,J)\) and \(\sigma(l,J\cup\{j\})=\sigma(l,J)\). In both cases the two terms cancel.

(3) The first two formulas follow from linearity of \(w\mapsto w\wedge v\) and conjugate-linearity of the adjoint. \(\Lambda(w)^2v=w\wedge w\wedge v=0\). By (3.1), \(\Lambda(w)\Lambda(w)^*+\Lambda(w)^*\Lambda(w)=\sum_{j,l}w_j\overline{w_l}(\varepsilon_j\iota_l+\iota_l\varepsilon_j)=\sum_j|w_j|^2I\). Finally \(\varepsilon_j\iota_je_J=e_J\) for \(j\in J\) and \(0\) otherwise. \(\square\)

## Oscillator operators: definitions and Lemma 4.1

A *form* on \(\mathbb R^n\) is a function \(u=\sum_Ju_Je_J\) with values in \(\Lambda\); operators on functions act on each coefficient \(u_J\). Put
\[
a_j=x_j+\partial_j=x_j+iD_j,\qquad a_j^\dagger=x_j-\partial_j,\qquad
d_x=\sum_ja_j\varepsilon_j,\quad \delta_x=\sum_ja_j^\dagger\iota_j,\quad \mathcal D=d_x+\delta_x .
\]

**Lemma 4.1** (Algebra). On smooth forms, and on distributions:
1. \([a_j,a_l]=0\), \([a_j^\dagger,a_l^\dagger]=0\), \([a_j,a_l^\dagger]=2\delta_{jl}\).
2. \(d_x=e^{-|x|^2/2}\circ d\circ e^{|x|^2/2}\), where \(d=\sum_j\partial_j\varepsilon_j\) is the exterior derivative. Also \(d_x^2=0\) and \(\delta_x^2=0\).
3. With \(\mathcal N\) the degree operator of Lemma 3.1,
\[
\mathcal D^2=d_x\delta_x+\delta_xd_x=\sum_ja_j^\dagger a_j+2\mathcal N .
\tag{4.1}
\]
4. \(\sum_ja_j^\dagger a_j=-\Delta+|x|^2-n\) on each coefficient.

**Proof.** (1) Using \([\partial_j,x_l]=\delta_{jl}\): \([x_j+\partial_j,x_l-\partial_l]=[\partial_j,x_l]-[x_j,\partial_l]=2\delta_{jl}\), while \([x_j+\partial_j,x_l+\partial_l]=\delta_{jl}-\delta_{jl}=0\), and similarly for \(a^\dagger\). (2) \(e^{-|x|^2/2}\partial_j(e^{|x|^2/2}f)=\partial_jf+x_jf\). In \(d_x^2=\sum_{j,l}a_ja_l\varepsilon_j\varepsilon_l\) the factor \(a_ja_l\) is symmetric in \((j,l)\) and \(\varepsilon_j\varepsilon_l\) is antisymmetric by (3.1), so the sum vanishes; the same argument works for \(\delta_x\). (3) The scalar operators \(a_j,a_l^\dagger\) commute with the constant matrices \(\varepsilon_j,\iota_l\). Writing \(a_ja_l^\dagger=a_l^\dagger a_j+2\delta_{jl}\),
\[
d_x\delta_x+\delta_xd_x=\sum_{j,l}a_l^\dagger a_j(\varepsilon_j\iota_l+\iota_l\varepsilon_j)+2\sum_j\varepsilon_j\iota_j=\sum_ja_j^\dagger a_j+2\mathcal N
\]
by (3.1). (4) \((x_j-\partial_j)(x_j+\partial_j)=x_j^2-\partial_j^2+x_j\partial_j-\partial_jx_j=x_j^2-\partial_j^2-1\). \(\square\)
