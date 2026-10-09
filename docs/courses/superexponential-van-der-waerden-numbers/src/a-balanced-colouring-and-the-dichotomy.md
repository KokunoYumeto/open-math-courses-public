# A balanced colouring and the dichotomy

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson colours the labels of [Coordinates, meshes and label counts](coordinates-meshes-and-label-counts.md) with two colours so that every progression of the group \(G\) either sees both colours often or is very rigid: its centred second coordinates are affine in the index (Theorem 4.1). The colouring is chosen by the local lemma (Proposition 1.1). The rigidity comes from repeated labels: a label that occurs many times along a progression forces a short rational period with a small drift (Section 3). Short periods are removed by the dilation \(\lambda\), and long periods produce eligible patterns, which the colouring balances. Notation is that of [Coordinates, meshes and label counts](coordinates-meshes-and-label-counts.md).

## 1. A balanced outer colouring

Fix a progression \(n_j=n_0+jd\) of \(G\). A label is *light* if it occurs at most \(k/M\) times among \(L(n_0),\dots,L(n_{k-1})\), and *heavy* otherwise; a position has the type of its label. These types always refer to the whole progression.

**Proposition 1.1** (Balanced outer colouring). For all large \(k\) there is a map \(c_*:\mathcal L\to\{0,1\}\) such that:

1. in every progression with at least \(\delta k\) light positions, each colour occurs on at least a quarter of the light positions;
2. in every eligible pattern (Definition 4.2 of the previous lesson), each colour occurs on at least a quarter of the regular positions.

*Proof.* Give every \(\beta\in\mathcal L\) an independent uniform bit \(\xi_\beta\). Two families of bad events are formed.

*First family.* For each word of labels of a progression with \(L_0\ge\delta k\) light positions, let \(w\le k/M\) be the largest multiplicity of a light label. List the light positions with equal labels grouped together (in a fixed way depending only on the word) and deal them cyclically into \(w\) rows. A group has at most \(w\) positions, so each row contains every label at most once, and each row has at least \(\lfloor L_0/w\rfloor\ge\delta M-1\) positions. For each row, the bad event is that some colour occurs on fewer than a quarter of its positions. There are at most \(kT_{\mathrm{glob}}\) such events (Lemma 4.1 of the previous lesson).

*Second family.* For each \(h_0<h\le2M\), each \(t\) and each eligible pattern for \(h,t\), the bad event is that some colour occurs on fewer than a quarter of its regular positions. These positions carry at least \(h/2\) distinct labels.

Each bad event \(E\) concerns \(l(E)\) distinct label bits, and by Lemma 2.1 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md), \(\Pr(E)\le2e^{-l(E)/8}\). Put \(z_E=e^{-l(E)/32}\). The first family has total weight at most \(kT_{\mathrm{glob}}e^{-(\delta M-1)/32}=o(1)\), because \(\log T_{\mathrm{glob}}=o(M)\). For a fixed label \(\beta\), Lemma 4.3 of the previous lesson bounds the weight of the second-family events using \(\xi_\beta\) by
\[
\sum_{h>D^2}(CDh)^{6D}e^{-h/64}=o(1):
\]
taking \(C\ge1\), \(\log(CDh)/h\) decreases for \(h\ge D^2\) once \(D\) is large, so \(6D\log(CDh)/h\le6\log(CD^3)/D=o(1)\), and each term is at most \(e^{-h/128}\) for large \(k\). Hence, for large \(k\), the events using any one bit have total weight at most \(1/500\).

Join two events when they share a label bit; independence of the bits makes this a family of neighbours as in Lemma 3.1 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md). Summing over the \(l(E)\) bits of \(E\), \(\sum_{F\in\Gamma(E)}z_F\le l(E)/500\). Every event has \(l(E)\ge100\) for large \(k\) (as \(l\ge\delta M-1\) or \(l\ge h/2>D^2/2\)), so \(z_E<1/2\), and \(\log(1-z)\ge-2z\) for \(0\le z\le1/2\) gives
\[
z_E\prod_{F\in\Gamma(E)}(1-z_F)\ge\exp\Bigl[-\Bigl(\frac1{32}+\frac2{500}\Bigr)l(E)\Bigr]\ge2e^{-l(E)/8}\ge\Pr(E),
\]
since \(100(\frac18-\frac1{32}-\frac2{500})>\log2\). The local lemma gives bits avoiding all bad events; let \(c_*\) be such a choice. Summing over the rows gives part 1, and the second family gives part 2. \(\square\)

Fix \(c_*\) and define the *outer colouring* \(c_0(n)=c_*(L(n))\) of \(G\).

## 2. Affinity in a small box

**Lemma 2.1.** Let \(z_j=a+jb\) in \(\mathbb T^e\) (\(0\le j<k\)) and \(J\subseteq\{0,\dots,k-1\}\). If real representatives \(Z_j\in\mathbb R^e\) (\(j\in J\)) lie in a box whose sides have length at most \(2H\), and \(2kH<1\), then \(Z_j=A+jB\) for some \(A,B\in\mathbb R^e\) and all \(j\in J\).

*Proof.* For \(j_1<j_2<j_3\) in \(J\), the vector \((j_3-j_2)(Z_{j_2}-Z_{j_1})-(j_2-j_1)(Z_{j_3}-Z_{j_2})\) is integral, being \(0\) modulo \(\mathbb Z^e\), and its coordinates have absolute value at most \(2H(j_3-j_1)<1\); so it vanishes. Interpolating between the smallest and largest indices of \(J\) gives \(A,B\). \(\square\)

## 3. Repeated labels

Fix a progression with a heavy label. Throughout this section *light* and *heavy* refer to it.

**Lemma 3.1** (Closest return). Let \(J\) be the set of positions of a heavy label, \(m_*=|J|>k/M\), and let \(h\) be the smallest positive difference of two elements of \(J\), attained at \(j'\) and \(j'+h\). Put \(u=\hat x(n_{j'+h})-\hat x(n_{j'})\) and \(v=\tilde y(n_{j'+h})-\tilde y(n_{j'})\). For large \(k\),
\[
1\le h\le2M,\qquad|u_i|\le\frac{H_x}{m_*-1}\le\frac{2MH_x}k,\qquad|v_i|\le\frac{2H}{m_*-1}\le\frac{4MH}k,
\]
and \(v=\lambda u\) as real vectors.

*Proof.* For large \(k\), \(m_*-1\ge k/(2M)\). The smallest of the \(m_*-1\) gaps of \(J\) is at most \((k-1)/(m_*-1)\le2M\). All points \((\hat x(n_j),\tilde y(n_j))\), \(j\in J\), lie in one box of the label, with sides at most \(2H\) (Lemma 3.1 of the previous lesson), so by Lemma 2.1 they are affine in \(j\). The difference at the gap \(h\) is therefore \(h/(j_+-j_-)\le1/(m_*-1)\) times the difference between the extreme positions \(j_\pm\) of \(J\), which is at most \(H_x\) in the first and \(2H\) in the second coordinates. Finally \(y=\lambda x\) on the torus gives \(v-\lambda u\in\mathbb Z^D\), and \(|v_i-\lambda u_i|\le6MH/k<1\) since \(\lambda H_x=H\); so \(v=\lambda u\). \(\square\)

**Lemma 3.2** (Rational path). With \(h,u,v\) as in Lemma 3.1, there is \(t\in\{0,\dots,h-1\}^D\) such that for all \(0\le j<k\)
\[
x(n_j)=x(n_0)+\frac jh(t+u),\qquad y(n_j)=y(n_0)+\frac jh(\lambda t+v)\qquad\text{in }\mathbb T^D .
\]
Moreover \(\gcd(t_1,\dots,t_D,h)=1\), positions incongruent modulo \(h\) have different labels, and all positions of one label lie in one residue class modulo \(h\).

*Proof.* Since \(hx(d)\equiv u\), the vector \(t'=h\hat x(d)-u\) is integral; reduce it modulo \(h\) to get \(t\). Then \(x(n_j)=x(n_0)+jx(d)=x(n_0)+\frac jh(t+u)\) modulo \(\mathbb Z^D\), and multiplying by \(\lambda\), with \(v=\lambda u\), gives the second identity.

If an integer \(e>1\) divided \(h\) and all \(t_i\), the displacement from position \(j'\) to \(j'+h/e\) would be \((u,v)/e\) modulo \(1\). The point \((\hat x(n_{j'}),\tilde y(n_{j'}))+(u,v)/e\) lies on the segment between the representatives at \(j'\) and \(j'+h\), hence in their common box, which is convex; so it is the representative of position \(j'+h/e\), which would carry the same label at the smaller gap \(h/e\). This contradiction proves the gcd assertion.

Consequently \(t/h\) has order exactly \(h\) in \(\mathbb T^D\). For \(j_1\not\equiv j_2\pmod h\), some coordinate has \((j_1-j_2)t_i/h\) at circle distance at least \(1/h\) from \(0\), while the drift contributes at most \(k|u_i|/h\le2MH/h\). So the two first-system values are at circle distance at least \((1-2MH)/h\ge(1-2MH)/(2M)>H\ge H_x\), and lie in different intervals of \(U\). \(\square\)

**Lemma 3.3** (Drift relative to heavy intervals). For every heavy position \(j_*\) and every \(i\),
\[
|v_i|\le\frac{2M}k\,|V(y_i(n_{j_*}))| .
\]

*Proof.* Let the label at \(j_*\) occur \(m'>k/M\) times, at extreme positions \(j_-<j_+\). By Lemma 3.2, \(j_+-j_-=ah\) with \(m'-1\le a<k/h\). With \(L_i=|V(y_i(n_{j_*}))|\), the difference \(\Delta_i=\tilde y_i(n_{j_+})-\tilde y_i(n_{j_-})\) satisfies \(|\Delta_i|\le L_i\le2H\) and \(\Delta_i\equiv av_i\pmod1\). As \(|av_i|\le4MH/h\) and \(|\Delta_i-av_i|<1\), \(\Delta_i=av_i\), so \(|v_i|\le L_i/a\le L_i/(m'-1)\le2ML_i/k\). \(\square\)

## 4. The dichotomy

**Theorem 4.1** (Outer-colour dichotomy). For all large \(k\), every progression \(n_j=n_0+jd\) (\(0\le j<k\), \(d\ne0\)) of \(G\) satisfies at least one of:

1. each colour occurs at least \(\gamma k\) times among \(c_0(n_0),\dots,c_0(n_{k-1})\);
2. there are \(A,B\in\mathbb R^D\) with \(\tilde y(n_j)=A+jB\) for all \(0\le j<k\).

*Proof.* If at least \(\delta k\) positions are light, Proposition 1.1(1) gives each colour at least \(\delta k/4\ge\gamma k\) times. Otherwise there is a heavy label; let \(h,t,u,v\) be as in Lemmas 3.1–3.3.

*Short periods: \(h\le h_0\).* Then \(h\mid\lambda\) (Lemma 1.1 of the previous lesson), so \(\lambda t/h\) is integral and \(y(n_j)=y(n_0)+jw\) with \(w=v/h\); also \(k|w_i|\le4MH/h<1/2\). Since \(w_i\equiv y_i(d)=\lambda d/q^i\pmod1\), \(w_i\in q^{-i}\mathbb Z\), so \(w_i\ne0\) implies \(|w_i|\ge q^{-D}\ge\alpha\). Suppose the representatives were not \(\tilde y(n_0)+jw\). Then some coordinate has \(w_i\ne0\) and the closed real segment \(\tilde y_i(n_0)+\tau w_i\), \(0\le\tau\le k-1\), meets a cut point \(\frac12+\mathbb Z\) (otherwise all its points are their own representatives). Each sampled value is then within \(k|w_i|\) of the cut, and by Lemma 3.1 of the previous lesson
\[
|V(y_i(n_j))|\le2H(k|w_i|+\alpha)\le2H(k+1)|w_i|<|w_i| .
\]
But distinct samples in this coordinate are at circle distance \(|j-j'||w_i|\ge|w_i|\) (the total motion is below \(1/2\)), so no two share an interval of \(V\), and all labels would be distinct, contradicting the heavy label. Hence alternative 2 holds.

*Long periods: \(h_0<h\le2M\).* Cut the first \(h\lfloor k/h\rfloor\) positions into consecutive blocks of length \(h\). A block starting at \(j_0\) is a path as in Definition 4.2 of the previous lesson, with \(x=x(n_{j_0})\), \(y=y(n_{j_0})\) and the same \(h,t,u,v\).

*Regular positions.* In a rotating coordinate, \(s_i=h/\gcd(h,\lambda t_i)>h_0\); without drift the values \(y_i(n_{j_0})+z\lambda t_i/h\) run through \(s_i\) equally spaced points, each \(h/s_i\) times, and the drift moves them by at most \(|v_i|\le4MH/k<\eta\). A position that is not regular in coordinate \(i\) has its grid point within \(2\eta\) of the cut, and an arc of length \(4\eta\) contains at most \(4\eta s_i+1\) grid points; so at most a fraction \(4\eta+1/s_i\) of the positions is lost in this coordinate. Over the at most \(D\) rotating coordinates, at most a fraction \(D(4\eta+1/h_0)=\frac4{1000}+\frac1D<\frac12\) is not regular. The labels within a block are distinct (Lemma 3.2), and \(|u_i|\le H_x\), \(|v_i|\le H\) (Lemma 3.1).

*Stationary coordinates.* Let a block contain a heavy position \(j_*\), let \(i\) be stationary, and \(I_*=V(y_i(n_{j_*}))\), \(L_*=|I_*|\). Since \(\lambda t_i/h\) is an integer, every position \(j\) of the block has \(y_i(n_j)\) within \(|v_i|\le\frac{2M}kL_*\le L_*\) of \(y_i(n_{j_*})\) (Lemma 3.3), hence in \(\mathcal N(I_*)\); Lemma 3.2 of the previous lesson gives \(|V(y_i(n_j))|\ge L_*/16\ge|v_i|\), using \(2M/k\le1/16\).

So every block containing a heavy position is eligible, and by Proposition 1.1(2) it contributes at least \(\frac14\cdot\frac h2=\frac h8\) occurrences of each colour. The other blocks consist of light positions, of which there are fewer than \(\delta k\), and fewer than \(h\) positions lie outside the blocks. So the blocks with a heavy position cover at least \(k-h-\delta k\ge\frac45k\) positions, and each colour occurs at least \(k/10\ge\gamma k\) times. \(\square\)

## 5. Exercises

**5.1.** Show that Lemma 2.1 fails without the size condition: give three points \(z_j=a+jb\) on \(\mathbb T\) whose representatives in \([0,1)\) are not affine in \(j\).

**5.2.** In Proposition 1.1, explain why the first family deals the light positions into rows rather than treating all light positions of a progression as one event.

**5.3.** Explain why the short-period case of Theorem 4.1 needs the closed segment, and why a cut met at the first or last sample causes no difficulty.

**5.4.** In the long-period case, why may a heavy position \(j_*\) be irregular, and why does that not matter?

## 6. Solutions

**5.1.** Take \(a=0.9\), \(b=0.2\): the points \(0.9,0.1,0.3\) have representatives \(0.9,0.1,0.3\), which are not affine in \(j=0,1,2\) (the differences are \(-0.8\) and \(0.2\)). They do not lie in a box of side \(2H\).

**5.2.** A light label may occur up to \(k/M\) times, so the colour of one bit would be repeated many times in a single event, and the events would not involve distinct bits; the tail bound of Lemma 2.1 of [Arrangements, tails and the local lemma](arrangements-tails-and-the-local-lemma.md) needs distinct independent bits. Within a row each label occurs at most once.

**5.3.** If the segment met the cut only at an endpoint, the representatives could still jump there (a value equal to \(-1/2\) is its own representative, but a value equal to \(1/2\) is represented by \(-1/2\)). Including the endpoints makes the argument cover every case in which the sampled representatives fail to be \(\tilde y(n_0)+jw\); in all such cases every sample is within \(k|w_i|\) of a cut point.

**5.4.** Regularity concerns rotating coordinates, and \(j_*\) may lie near the cut in one of them. The heavy position is only used to supply the interval \(I_*\) and the bound of Lemma 3.3 for stationary coordinates, which hold for every heavy position.

## References

- [OpenAI-vdW] OpenAI, *Quantitative superexponential bounds for van der Waerden numbers*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/Quantitative-Superexponential-Bounds-for-van-der-Waerden-Numbers-September-23-2026/paper.pdf
