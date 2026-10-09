# Free independence in ultraproducts

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(Q\subseteq M\) be a II₁ factor inside a tracial von Neumann algebra, with \(Q'\cap M=\mathbb C1\). This lesson proves Popa's free independence theorem for such inclusions: in a tracial ultraproduct, given countably many centred elements, there is a Haar unitary of the ultraproduct of the \(Q\)'s such that every alternating word in these elements and nonzero powers of the unitary has trace zero. The unitary is assembled from pieces. Each piece is a partial isometry that commutes with its adjoint, added inside the complement of the previous pieces; the traces of all words up to a fixed length stay small relative to the size of the support. Words that use the new piece twice are controlled by local quantization in a corner, and words that use it once by the decay of correlations of a Haar unitary. In an ultraproduct the word length and the precision can grow along the sequence, which makes the traces vanish exactly, and an exhaustion fills the whole unit.

We use: [Haar unitaries, freeness and tracial ultraproducts](haar-unitaries-freeness-and-ultraproducts.md) (Lemma 1.1, Corollary 2.4, Lemma 2.5, Lemmas 3.2, 4.1, 4.2 and the continuity remarks of Section 1); Theorem 55.7 of [Finite Fourier bases produce one small quantized corner](course:OA-SUBFACTORS/html/finite-phase-local-quantization#every-target-fits-in-the-same-arbitrarily-small-corner), local quantization for a II₁ factor inside a tracial algebra; Lemma 3.1 of [Abelian pinching and relative commutants](course:OA-APPROX/abelian-pinching-and-relative-commutants#3-relative-commutants-survive-a-corner), relative commutants of corners; Kaplansky's density theorem, [Section 7 of its lesson](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07); and Zorn's lemma.

## 1. Irreducible inclusions and their corners

An *irreducible inclusion* \(Q\subseteq M\) consists of a tracial von Neumann algebra \((M,\tau)\) and a von Neumann subalgebra \(Q\) with \(1\in Q\) which is a II₁ factor and satisfies \(Q'\cap M=\mathbb C1\).

**Lemma 1.1.** Let \(Q\subseteq M\) be irreducible and \(p\in Q\) a nonzero projection. With the trace \(\tau_p=\tau(p)^{-1}\tau\) on \(pMp\), the inclusion \(pQp\subseteq pMp\) is irreducible.

**Proof.** Since \(Q\) is a factor, the central support of \(p\) in \(Q\) is \(1\), and Lemma 3.1 of the pinching lesson says that \(y\mapsto yp\) maps \(Q'\cap M\) onto \((pQp)'\cap pMp\). Hence \((pQp)'\cap pMp=\mathbb Cp\). The same lemma for \(Q\subseteq Q\) gives \((pQp)'\cap pQp=\mathbb Cp\), so \(pQp\) is a factor. The state \(\tau_p\) is faithful, normal and tracial on \(pMp\). A projection \(e\le p\) with \(e(pQp)e=eQe\) abelian would be an abelian projection of \(Q\); there is none. \(\square\)

**Lemma 1.2** (local quantization). Let \(Q\subseteq M\) be irreducible, \(p\in Q\) a nonzero projection, \(Y\subseteq M\) finite and \(\alpha>0\). There is a nonzero projection \(q\in pQp\) with
\[
\|qyq-c_yq\|_1\le\alpha\,\tau(q)\qquad(y\in Y),\qquad c_y=\frac{\tau(pyp)}{\tau(p)} .
\]

**Proof.** By Lemma 1.1, \(B=pQp\) is a II₁ factor in \((pMp,\tau_p)\) with \(B'\cap pMp=\mathbb Cp\), whose trace-preserving expectation is \(x\mapsto\tau_p(x)p\). Theorem 55.7 of the quantization lesson, applied to the elements \(pyp\), gives a nonzero projection \(q\in B\) with \(\|q(pyp)q-\tau_p(pyp)q\|_{2,\tau_p}<\alpha\,\tau_p(q)^{1/2}\) for \(y\in Y\). Here \(q(pyp)q=qyq\) and \(\tau_p(pyp)=c_y\). The element \(z=qyq-c_yq\) satisfies \(z=zq\), so Lemma 1.1(3) of the first lesson gives
\[
\|z\|_1\le\tau(q)^{1/2}\|z\|_2=\tau(q)^{1/2}\tau(p)^{1/2}\|z\|_{2,\tau_p}<\tau(q)^{1/2}\tau(p)^{1/2}\,\alpha\,\tau(q)^{1/2}\tau(p)^{-1/2}=\alpha\,\tau(q).\qquad\square
\]

## 2. Words in a normal partial isometry

A *normal partial isometry* is a \(v\in M\) with \(v^*v=vv^*\); this projection is its *support* \(e_v\), and \(v=e_vv=ve_v\). Write \(v^{(1)}=v\) and \(v^{(-1)}=v^*\). For a set \(F\subseteq M\) and \(k\ge1\), let \(W_k(F,v)\) be the set of words
\[
x_0v^{(s_1)}x_1v^{(s_2)}x_2\cdots v^{(s_k)}x_k,\qquad s_i\in\{1,-1\},\quad x_1,\dots,x_{k-1}\in F,\quad x_0,x_k\in F\cup\{1\},
\]
and \(W(F,v)=\bigcup_{k\ge1}W_k(F,v)\). The interior letters come from \(F\); the outer letters may be \(1\).

For normal partial isometries write \(v\preceq v'\) if \(v=v'e_v\).

**Lemma 2.1.** Let \(v,v'\) be normal partial isometries of \(Q\).

1. \(\preceq\) is a partial order. If \(v\preceq v'\), then \(e_v\le e_{v'}\) and \(\|v'-v\|_2^2=\tau(e_{v'}-e_v)\).
2. If \(f\le1-e_v\) is a projection of \(Q\) and \(w\) a unitary of the corner \(fQf\), then \(v+w\) is a normal partial isometry with support \(e_v+f\), and \(v\preceq v+w\).
3. Every chain \(\mathcal C\) of normal partial isometries of \(Q\) has an upper bound \(v\), which is the \(2\)-norm limit of an increasing sequence in \(\mathcal C\).

**Proof.** (1) If \(v=v'e_v\), then \(e_v=v^*v=e_ve_{v'}e_v\), so \(e_v(1-e_{v'})e_v=0\), i.e. \(e_v\le e_{v'}\). Reflexivity is \(v=ve_v\). If \(v\preceq v'\preceq v\), the supports are equal and \(v=v'e_{v'}=v'\). If \(v=v'e_v\) and \(v'=v''e_{v'}\), then \(v=v''e_{v'}e_v=v''e_v\). Finally \(v'-v=v'(e_{v'}-e_v)\), whose squared \(2\)-norm is \(\tau((e_{v'}-e_v)e_{v'}(e_{v'}-e_v))=\tau(e_{v'}-e_v)\).

(2) We have \(w=fw=wf\), \(v=e_vv=ve_v\) and \(e_vf=0\). Hence \(v^*w=v^*e_vfw=0\), and similarly \(w^*v=vw^*=wv^*=0\). So \((v+w)^*(v+w)=e_v+f=(v+w)(v+w)^*\), and \((v+w)e_v=v\).

(3) Let \(s=\sup_{v\in\mathcal C}\tau(e_v)\). Choose \(v_1\preceq v_2\preceq\cdots\) in \(\mathcal C\) with \(\tau(e_{v_r})\to s\); this is possible because \(\mathcal C\) is totally ordered. By (1), \((v_r)\) is Cauchy for \(\|\cdot\|_2\), and it converges to some \(v\) in the unit ball of \(Q\). Products are \(2\)-norm continuous on bounded sets, so \(v^*v=vv^*=\lim e_{v_r}\), a projection of trace \(s\). Let \(v'\in\mathcal C\). If \(v'\preceq v_r\) for some \(r\), then \(v'=v_{r'}e_{v'}\) for all \(r'\ge r\), and in the limit \(v'=ve_{v'}\). Otherwise \(v_r\preceq v'\) for every \(r\), so \(\tau(e_{v'})=s\), \(\|v'-v_r\|_2^2=\tau(e_{v'}-e_{v_r})\to0\), and \(v'=v\). In both cases \(v'\preceq v\). \(\square\)

A word is a product of boundedly many letters; by the continuity remarks of the first lesson, the trace of a fixed word pattern depends \(2\)-norm continuously on \(v\) along bounded sequences.

## 3. Approximate independence

**Theorem 3.1.** Let \(Q\subseteq M\) be irreducible, \(F\subseteq M\) a finite set of centred elements, \(n\ge1\) and \(\varepsilon>0\). There is a normal partial isometry \(v\in Q\) with \(\tau(e_v)>1/4\) and
\[
|\tau(y)|\le\varepsilon\qquad\text{for all }y\in W_k(F,v),\ 1\le k\le n .
\]

**Proof.** *Normalization.* Let \(c=\max(1,\max_{x\in F}\|x\|)\). A word of \(W_k(F,v)\) with \(k\le n\) has at most \(n+1\) letters from \(F\), so it is \(c^j\) times a word of \(W_k(c^{-1}F,v)\) with \(j\le n+1\). Replacing \(F\) by \(c^{-1}F\) and \(\varepsilon\) by \(c^{-n-1}\varepsilon\), we may assume \(\|x\|\le1\) for \(x\in F\). Put \(\varepsilon_0=\delta\) and \(\varepsilon_k=2^{k+1}\varepsilon_{k-1}\), with \(\delta>0\) chosen so that \(\varepsilon_n\le\varepsilon\). Then \(\delta\le\varepsilon_k/4\) for \(k\ge1\), and \(\varepsilon_{k-2}\le\varepsilon_k/32\) for \(k\ge2\).

*A maximal piece.* Let \(\mathcal W\) be the set of normal partial isometries \(v\in Q\) with
\[
|\tau(y)|\le\varepsilon_k\,\tau(e_v)\qquad(y\in W_k(F,v),\ 1\le k\le n).
\tag{3.1}
\]
It contains \(0\). By Lemma 2.1(3) and the continuity of traces of words, every chain in \(\mathcal W\) has an upper bound in \(\mathcal W\). By Zorn's lemma, \(\mathcal W\) has a maximal element \(v\). It suffices to prove \(\tau(e_v)>1/4\): then every word in the statement has \(|\tau(y)|\le\varepsilon_k\tau(e_v)\le\varepsilon\). Suppose instead that \(\tau(e_v)\le1/4\). Put \(e=e_v\) and \(p=1-e\); then \(\tau(e)/\tau(p)\le1/3\). We construct \(u\in\mathcal W\) with \(v\preceq u\ne v\), which contradicts maximality.

*Segments.* For a word \(y=x_0v^{(s_1)}x_1\cdots v^{(s_k)}x_k\) in \(W_k(F,v)\), \(k\le n\), and positions \(1\le i<j\le k\), put
\[
\pi_i=x_0v^{(s_1)}\cdots v^{(s_{i-1})}x_{i-1},\qquad \sigma_i=x_iv^{(s_{i+1})}\cdots v^{(s_k)}x_k,\qquad \mu_{ij}=x_iv^{(s_{i+1})}\cdots v^{(s_{j-1})}x_{j-1},
\]
the prefix before the \(i\)th position, the suffix after it, and the middle between positions \(i\) and \(j\); \(\pi_1=x_0\), \(\sigma_k=x_k\) and \(\mu_{i,i+1}=x_i\). All of them have norm at most \(1\). Let \(\mathcal A\) be the finite set of all middles \(\mu_{ij}\) and \(\mathcal B\) the finite set of all products \(\sigma_i\pi_i\), over all such words and positions. A middle \(\mu_{ij}\) has outer letters \(x_i,x_{j-1}\in F\), because they are interior letters of \(y\). So either \(\mu_{ij}=x_i\) is centred, or \(\mu_{ij}\in W_{j-i-1}(F,v)\).

*The new piece.* Lemma 1.2, applied to \(p\), \(Y=\mathcal A\) and \(\alpha=2^{-n-2}\delta\), gives a nonzero projection \(q\in pQp\) with
\[
\|qaq-c_aq\|_1\le\alpha\,\tau(q),\qquad c_a=\tau(pap)/\tau(p)\qquad(a\in\mathcal A).
\tag{3.2}
\]
Let \(h\) be a Haar unitary of \(qQq\) (Corollary 2.4 of the first lesson). By Lemma 2.5 there, there is \(m\ge1\) with
\[
|\tau(h^{m}b)|\le\beta,\quad|\tau(h^{-m}b)|\le\beta\quad(b\in\mathcal B),\qquad\beta=\frac{\delta\,\tau(q)}{4n}.
\tag{3.3}
\]
Put \(w=h^m\), a unitary of \(qQq\) with \(w^{(-1)}=w^*=h^{-m}\), and \(u=v+w\). By Lemma 2.1(2), \(u\) is a normal partial isometry of \(Q\) with support \(e+q\), \(v\preceq u\) and \(u\ne v\).

*The estimate.* Fix \(1\le k\le n\) and a word \(y=x_0u^{(s_1)}x_1\cdots u^{(s_k)}x_k\in W_k(F,u)\). Substituting \(u^{(s)}=v^{(s)}+w^{(s)}\) gives \(y=\sum_Sy_S\), where \(S\subseteq\{1,\dots,k\}\) is the set of positions at which \(w^{(s)}\) is chosen; the segments below are those of the word \(y_\emptyset\in W_k(F,v)\).

\(S=\emptyset\): \(|\tau(y_\emptyset)|\le\varepsilon_k\tau(e)\), since \(v\in\mathcal W\).

\(S=\{i\}\): \(y_S=\pi_iw^{(s_i)}\sigma_i\), so \(\tau(y_S)=\tau(w^{(s_i)}\sigma_i\pi_i)\) and \(|\tau(y_S)|\le\beta\) by (3.3). The \(k\) such sets contribute at most \(k\beta\le\delta\tau(q)/4\).

\(|S|\ge2\): let \(i<j\) be the two smallest elements of \(S\). Then \(y_S=\pi_iw^{(s_i)}\mu_{ij}w^{(s_j)}c\), where \(c\) is a product of letters of norm at most \(1\). By traciality and Lemma 1.1(2) of the first lesson, using \(w^{(s)}=w^{(s)}q=qw^{(s)}\),
\[
|\tau(y_S)|=|\tau(w^{(s_i)}\mu_{ij}w^{(s_j)}\,c\pi_i)|\le\|w^{(s_i)}q\mu_{ij}qw^{(s_j)}\|_1\le\|q\mu_{ij}q\|_1\le(|c_{\mu_{ij}}|+\alpha)\,\tau(q)
\]
by (3.2). To bound \(c_\mu\) for \(\mu=\mu_{ij}\), let \(r=j-i-1\). By traciality, \(\tau(p\mu p)=\tau(\mu p)=\tau(\mu)-\tau(\mu e)\), and \(\tau(\mu e)=\tau(\mu vv^*)=\tau(v^*\mu v)\). The word \(v^*\mu v=1\cdot v^{(-1)}x_i\cdots x_{j-1}v^{(1)}\cdot1\) lies in \(W_{r+2}(F,v)\), and \(r+2=j-i+1\le k\le n\). Moreover \(\tau(\mu)=0\) if \(r=0\), and \(|\tau(\mu)|\le\varepsilon_r\tau(e)\) if \(r\ge1\). Hence
\[
|c_\mu|\le\frac{(\varepsilon_r+\varepsilon_{r+2})\,\tau(e)}{\tau(p)}\le\frac{\varepsilon_r+\varepsilon_{r+2}}{3}.
\]
If \((i,j)=(1,k)\), which happens for the single set \(S=\{1,k\}\) when \(k\ge2\), then \(r+2=k\) and \(|c_\mu|\le(\varepsilon_{k-2}+\varepsilon_k)/3\le\frac{11}{32}\varepsilon_k\). For every other \(S\) with \(|S|\ge2\), \(r+2\le k-1\) and \(|c_\mu|\le\frac23\varepsilon_{k-1}\). There are fewer than \(2^k\) such sets, and \(2^k\cdot\frac23\varepsilon_{k-1}=\frac13\varepsilon_k\), \(2^k\alpha\le\delta/4\). So these sets contribute at most \(\bigl(\frac{11}{32}+\frac13\bigr)\varepsilon_k\tau(q)+\frac\delta4\tau(q)\).

Adding up and using \(\delta/2\le\varepsilon_k/8\),
\[
|\tau(y)|\le\varepsilon_k\tau(e)+\Bigl(\frac{11}{32}+\frac13+\frac18\Bigr)\varepsilon_k\tau(q)<\varepsilon_k\bigl(\tau(e)+\tau(q)\bigr)=\varepsilon_k\,\tau(e_u).
\]
For \(k=1\) only the first two cases occur, and the same bound holds. Thus \(u\in\mathcal W\), the desired contradiction. \(\square\)

## 4. Exact independence in an ultraproduct

Throughout this section, \(Q_n\subseteq M_n\) are irreducible inclusions, \(\omega\) is a free ultrafilter on \(\mathbb N\), \(\mathbf M=\prod_\omega M_n\), and \(\mathbf Q=\prod_\omega Q_n\subseteq\mathbf M\) as in Lemma 4.1 of the first lesson.

**Lemma 4.1.** Let \(f_n\in Q_n\) be projections with \(t=\lim_\omega\tau_n(f_n)>0\), let \(f\in\mathbf Q\) be their class, and let \(X\subseteq f\mathbf Mf\) be a countable set of centred elements. There are normal partial isometries \(w_n\in f_nQ_nf_n\) whose class \(w\) satisfies \(\tau(e_w)\ge t/4\) and \(\tau(y)=0\) for every \(y\in W(X,w)\).

**Proof.** Enumerate \(X=\{x_1,x_2,\dots\}\) (repeating elements if \(X\) is finite). Let \(N_0=\{n:\tau_n(f_n)>t/2\}\), a set in \(\omega\). Each \(x_r\) has a bounded representing sequence \((x_{r,n})\) with \(x_{r,n}\in f_nM_nf_n\) and \(\tau_n(x_{r,n})=0\) for \(n\in N_0\): start from any bounded representing sequence \((z_n)\), take \(f_nz_nf_n\), which represents \(fx_rf=x_r\), and for \(n\in N_0\) subtract \(\tau_n(f_nz_nf_n)\tau_n(f_n)^{-1}f_n\), whose scalar coefficient tends to \(\tau(x_r)/t=0\) along \(\omega\).

For \(n\in N_0\), the inclusion \(f_nQ_nf_n\subseteq f_nM_nf_n\) is irreducible (Lemma 1.1), and the letters \(x_{r,n}\) are centred for its trace. Theorem 3.1, applied to it with \(F_n=\{x_{r,n}:r\le n\}\), word length \(n\) and \(\varepsilon=2^{-n}\), gives a normal partial isometry \(w_n\in f_nQ_nf_n\) with \(\tau_n(e_{w_n})>\tau_n(f_n)/4\) and \(|\tau_n(y)|\le2^{-n}\) for \(y\in W_k(F_n,w_n)\), \(k\le n\). The corner has unit \(f_n\); since \(w_n=f_nw_n=w_nf_n\), its words with outer letters \(f_n\) are the words with outer letters \(1\), and the traces differ by the factor \(\tau_n(f_n)\le1\). For \(n\notin N_0\) put \(w_n=0\).

The class \(w\) is a normal partial isometry in \(f\mathbf Qf\) with \(\tau(e_w)=\lim_\omega\tau_n(e_{w_n})\ge t/4\). A word \(y\in W_k(X,w)\) whose letters are among \(x_1,\dots,x_R\) is represented by the same word \(y_n\) in the letters \(x_{r,n}\) and \(w_n\). For \(n\in N_0\) with \(n\ge\max(k,R)\), \(y_n\in W_k(F_n,w_n)\) and \(|\tau_n(y_n)|\le2^{-n}\). These \(n\) form a set in \(\omega\), so \(\tau(y)=\lim_\omega\tau_n(y_n)=0\). \(\square\)

**Theorem 4.2** (Popa's free independence). Let \(X\subseteq\mathbf M\) be a countable set of centred elements. There is a Haar unitary \(u\in\mathbf Q\), with a representing sequence of unitaries \(u_n\in Q_n\), such that
\[
\tau(x_0u^{m_1}x_1u^{m_2}\cdots u^{m_j}x_j)=0
\tag{4.1}
\]
for every \(j\ge1\), all \(m_1,\dots,m_j\in\mathbb Z\setminus\{0\}\), all \(x_1,\dots,x_{j-1}\in X\) and all \(x_0,x_j\in X\cup\{1\}\).

**Proof.** Choose Haar unitaries \(h_n\in Q_n\) (Corollary 2.4 of the first lesson). Their class \(h\in\mathbf Q\) is a Haar unitary, since \(\tau(h^j)=\lim_\omega\tau_n(h_n^j)=0\) for \(j\ne0\). The set \(Y=X\cup\{h^j:j\ne0\}\) is countable and consists of centred elements.

For a normal partial isometry \(v\in\mathbf M\), call a word of \(W(Y,v)\) or a letter of \(Y\) a *middle* if both its outer letters lie in \(Y\); a *prefix* if it is \(1\), a letter of \(Y\), or a word of \(W(Y,v)\) whose last letter lies in \(Y\); and a *suffix* if it is \(1\), a letter of \(Y\), or a word of \(W(Y,v)\) whose first letter lies in \(Y\).

We construct, for \(m=0,1,2,\dots\), normal partial isometries \(v_{m,n}\in Q_n\) with classes \(v_m\) such that
\[
\text{(i) }\tau(1-e_{v_m})\le(3/4)^m,\qquad\text{(ii) }\tau(y)=0\text{ for every }y\in W(Y,v_m),
\]
and \(v_{m+1,n}=v_{m,n}+w_{m,n}\) with \(w_{m,n}\in(1-e_{v_{m,n}})Q_n(1-e_{v_{m,n}})\) normal partial isometries. Start with \(v_{0,n}=0\).

Given \(v=v_m\), let \(f_n=1-e_{v_{m,n}}\) and \(f=1-e_v\). If \(\tau(f)=0\), put \(v_{m+1,n}=v_{m,n}\). Otherwise let \(X'\subseteq f\mathbf Mf\) consist of the elements \(faf\) with \(a\) a middle, and the elements \(g-\tau(g)\tau(f)^{-1}f\) with \(g=fbaf\), \(a\) a prefix and \(b\) a suffix. It is countable. Its elements are centred: for a middle \(a\), \(\tau(faf)=\tau(a)-\tau(ae)\) with \(e=e_v\); here \(\tau(a)=0\) because \(a\) is a letter of \(Y\) or a word of \(W(Y,v)\), and \(\tau(ae)=\tau(v^*av)=0\) because \(v^*av\) is a word of \(W(Y,v)\) whose interior letters are the letters of \(a\). Lemma 4.1 gives normal partial isometries \(w_n=w_{m,n}\in f_nQ_nf_n\) with class \(w\), \(\tau(e_w)\ge\tau(f)/4\) and \(\tau(z)=0\) for all \(z\in W(X',w)\). Put \(v_{m+1,n}=v_{m,n}+w_n\); by Lemma 2.1(2) at each \(n\), these are normal partial isometries, and \(v_{m+1}=v+w\) has support \(e+e_w\). Then (i) holds: \(\tau(1-e_{v_{m+1}})=\tau(f)-\tau(e_w)\le\frac34\tau(f)\).

For (ii), take \(y=x_0(v+w)^{(s_1)}x_1\cdots(v+w)^{(s_k)}x_k\in W_k(Y,v+w)\) and expand it as \(\sum_Sy_S\) as in the proof of Theorem 3.1. The term \(y_\emptyset\) lies in \(W(Y,v)\) and has trace \(0\). For \(S=\{i_1<\dots<i_\ell\}\) nonempty,
\[
y_S=a_0w^{(s_{i_1})}a_1w^{(s_{i_2})}\cdots a_{\ell-1}w^{(s_{i_\ell})}a_\ell ,
\]
where \(a_0\) is a prefix, \(a_\ell\) a suffix and \(a_1,\dots,a_{\ell-1}\) are middles, because the letters adjacent to a position are interior letters of \(y\). Since \(w=fwf\) and \(\tau\) is a trace,
\[
\tau(y_S)=\tau\bigl(w^{(s_{i_1})}(fa_1f)w^{(s_{i_2})}\cdots(fa_{\ell-1}f)w^{(s_{i_\ell})}g\bigr),\qquad g=fa_\ell a_0f .
\]
Write \(g=\tau(g)\tau(f)^{-1}f+g^\circ\) with \(g^\circ\in X'\), and use \(w^{(s)}f=w^{(s)}\). Then \(\tau(y_S)\) is a multiple of the trace of a word of \(W(X',w)\) with outer letters \(1\), plus the trace of a word of \(W(X',w)\) with last letter \(g^\circ\). Both vanish. This proves (ii) for \(v_{m+1}\).

By Lemma 2.1(1), \(\|v_{m+1}-v_m\|_2^2=\tau(e_w)\le(3/4)^m\). So \((v_m)\) converges in \(2\)-norm to some \(v\) in the unit ball of \(\mathbf Q\), and \(v^*v=vv^*=\lim e_{v_m}=1\), because \(\|1-e_{v_m}\|_2^2\le(3/4)^m\). Thus \(v\) is a unitary of \(\mathbf Q\). Traces of words are continuous along this bounded sequence, so \(\tau(y)=0\) for all \(y\in W(Y,v)\).

Put \(u=vhv^*\), a Haar unitary of \(\mathbf Q\): \(\tau(u^j)=\tau(vh^jv^*)=\tau(h^j)=0\) for \(j\ne0\). The word in (4.1) equals
\[
x_0\,v\,h^{m_1}\,v^*\,x_1\,v\,h^{m_2}\,v^*\cdots v\,h^{m_j}\,v^*\,x_j ,
\]
a word of \(W_{2j}(Y,v)\): its interior letters \(h^{m_1},x_1,h^{m_2},\dots,x_{j-1},h^{m_j}\) lie in \(Y\), and its outer letters in \(Y\cup\{1\}\). So it has trace \(0\). Finally, the factors \(Q_n\) allow unitary representing sequences, by Lemma 4.2 of the first lesson. \(\square\)

**Corollary 4.3.** Let \(X\subseteq\mathbf M\) be a set of centred elements which is separable for \(\|\cdot\|_2\). There is a diffuse abelian von Neumann subalgebra \(A\subseteq\mathbf Q\) such that
\[
\tau(x_0a_1x_1a_2\cdots a_jx_j)=0
\]
whenever \(j\ge1\), \(a_1,\dots,a_j\in A\) are centred, \(x_1,\dots,x_{j-1}\in X\) and \(x_0,x_j\in X\cup\{1\}\).

**Proof.** Let \(X_0\subseteq X\) be countable and \(2\)-norm dense, take \(u\) from Theorem 4.2 for \(X_0\), and \(A=W^*(u)\). If \(e\) were a minimal projection of \(A\), then \(Ae=\mathbb Ce\), so \(ue=\lambda e\) with \(|\lambda|=1\), and \(|\tau(u^je)|=\tau(e)>0\) for all \(j\), contradicting Lemma 2.5 of the first lesson. So \(A\) is diffuse.

The trace of a word depends linearly on each letter, and \(|\tau(cxd)|\le\|c\|\,\|d\|\,\|x\|_2\) by Lemma 1.1(1) of the first lesson. Replace the letters of a word one at a time, from left to right. A letter \(x_i\in X\) is replaced by an element of \(X_0\) at \(2\)-norm distance so small that, multiplied by the operator norms of all other letters at that moment, the change is below a prescribed amount. A centred letter \(a\in A\) is replaced by a centred Laurent polynomial in \(u\) of norm at most \(2\|a\|+1\), \(2\)-norm close to \(a\): by Kaplansky's density theorem there are \(b\in C^*(u)\) with \(\|b\|\le\|a\|\) arbitrarily close to \(a\) in \(2\)-norm; take a Laurent polynomial \(L\) with \(\|L-b\|\le1/2\) and \(\|L-b\|\) small, and use \(L-\tau(L)1\), whose distance to \(a\) in \(2\)-norm is at most \(2\|L-a\|_2\) because \(\tau(a)=0\). After all replacements the word is a linear combination of words (4.1) for \(X_0\), each of trace \(0\). As the prescribed amounts are arbitrary, the original trace is \(0\). \(\square\)

**Corollary 4.4.** Let \(P\subseteq M\) be an irreducible inclusion of II₁ factors and \(D\subseteq M^\omega\) a unital C\*-subalgebra which is separable in operator norm. There is a Haar unitary \(t\in P^\omega\), with a representing sequence of unitaries of \(P\), which is free from \(D\).

**Proof.** If \(\{d_k\}\) is norm dense in \(D\), then \(X=\{d_k-\tau(d_k)1\}\) is a countable norm-dense subset of the centred elements of \(D\), because \(|\tau(d)|\le\|d\|\). Apply Theorem 4.2 to the constant inclusions \(Q_n=P\subseteq M_n=M\) and to \(X\). For a word \(d_0t^{m_1}d_1\cdots t^{m_j}d_j\) as in Lemma 3.2 of the first lesson, write the outer letters as scalar plus centred parts and approximate every centred letter in operator norm by elements of \(X\). Traces of words are norm continuous in the letters, so (4.1) gives (3.1) of that lemma for \(t=u\), and \(t\) is free from \(D\). \(\square\)

Corollary 4.4 can be applied repeatedly. If \(D_0\subseteq M^\omega\) is a norm-separable unital C\*-algebra, choose \(t_0\in P^\omega\) free from \(D_0\) and put \(D_1=C^*(D_0,t_0)\); this is again norm separable, since polynomials with rational coefficients in a countable dense subset of \(D_0\) and in \(t_0,t_0^*\) are dense in it. Continuing, one obtains Haar unitaries \(t_j\in P^\omega\), each free from \(D_j=C^*(D_0,t_0,\dots,t_{j-1})\).

## 5. Exercises

**Exercise 5.1.** Let \(P\subseteq M\) be an irreducible inclusion of II₁ factors. Show that \((P^\omega)'\cap M^\omega=\mathbb C1\).

**Exercise 5.2.** Let \(Q\) be a II₁ factor with trace \(\tau\), let \(M=Q\oplus Q\) with the trace \(\frac12(\tau\oplus\tau)\), embed \(Q\) diagonally, and put \(z=1\oplus(-1)\). Show that \(z\) is centred and that \(\tau(zuzu^*)=1\) for every unitary \(u\in Q^\omega\). Conclude that Theorem 4.2 needs \(Q_n'\cap M_n=\mathbb C1\).

**Exercise 5.3.** Let \(P\subseteq M\) be an irreducible inclusion of II₁ factors, \(F\subseteq M\) a finite set of centred elements, \(N\ge1\) and \(\varepsilon>0\). Show that there is a unitary \(u\in P\) with \(|\tau(x_0u^{m_1}x_1\cdots u^{m_j}x_j)|<\varepsilon\) whenever \(1\le j\le N\), \(0<|m_i|\le N\), \(x_1,\dots,x_{j-1}\in F\) and \(x_0,x_j\in F\cup\{1\}\).

**Exercise 5.4.** Let \(t\) be a Haar unitary free from \(D\). Show by an example that \(\tau(d_0td_1t^*d_2)\) need not vanish when \(d_1\) is not centred.

## 6. Solutions

**5.1.** Let \(b\in(P^\omega)'\cap M^\omega\) with representing sequence \((b_n)\), \(\|b_n\|\le\|b\|\), and \(\delta_n=\sup\{\|wb_nw^*-b_n\|_2:w\in\mathcal U(P)\}\). Then \(\lim_\omega\delta_n=0\): otherwise there are \(\eta>0\), a set \(N\in\omega\) with \(\delta_n>\eta\) on \(N\), and unitaries \(w_n\in P\) with \(\|w_nb_nw_n^*-b_n\|_2>\eta\) for \(n\in N\) (and \(w_n=1\) elsewhere), whose class is a unitary of \(P^\omega\) not commuting with \(b\). Let \(K_n\) be the closed convex hull in \(L^2(M)\) of \(\{wb_nw^*:w\in\mathcal U(P)\}\) and \(c_n\) its element of minimal norm. Conjugation by unitaries of \(P\) preserves \(K_n\) and the norm, so it fixes \(c_n\). Convex combinations of the orbit have operator norm at most \(\|b_n\|\), and a \(2\)-norm convergent sequence of them converges in the ball of radius \(\|b_n\|\) of \(M\), which is complete for the \(2\)-norm; so \(c_n\in M\). So \(c_n\in P'\cap M=\mathbb C1\); as \(\tau\) is constant on \(K_n\), \(c_n=\tau(b_n)1\). Every element of \(K_n\) lies within \(\delta_n\) of \(b_n\), hence \(\|b_n-\tau(b_n)1\|_2\le\delta_n\), and \(b\) is the scalar \(\lim_\omega\tau(b_n)\).

**5.2.** \(\tau(z)=\frac12(\tau(1)-\tau(1))=0\). Every element \(x\oplus x\) of the diagonal commutes with \(z\), and so does every element of \(Q^\omega\), represented by diagonal sequences. Hence \(zuzu^*=z^2uu^*=1\). With \(X=\{z\}\), the word \(zu^{1}zu^{-1}\) of (4.1) has trace \(1\) for every unitary \(u\) of \(Q^\omega\); here \(Q'\cap M\) contains \(z\).

**5.3.** Theorem 4.2 for the constant inclusions and \(X=F\subseteq M\subseteq M^\omega\) gives unitaries \(u_n\in P\) representing \(u\). There are finitely many words in the statement, each with \(\lim_\omega\tau(y(u_n))=\tau(y(u))=0\). The finitely many sets \(\{n:|\tau(y(u_n))|<\varepsilon\}\) belong to \(\omega\); an \(n\) in their intersection gives \(u=u_n\).

**5.4.** With \(d_1=1\), \(\tau(d_0tt^*d_2)=\tau(d_0d_2)\), which is \(1\) for \(d_0=d_2=1\).

## References

- [Popa-Ind] S. Popa, Independence properties in subalgebras of ultraproduct II₁ factors, Journal of Functional Analysis 266 (2014), 5818–5846. https://arxiv.org/abs/1308.3982
- [OpenAI-Gen] OpenAI, Relative generation and the generator problem for finite factors, preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Relative-generation-and-the-generator-problem-for-finite-factors-September-23-2026
