# Corner and matrix invariance of the modular spectral intersection

This original CC0-1.0 proof uses the complete projection results PC-5, PC-7 and PC-8, the finite-domain GNS construction [GW-1–2](OA-FLOW-GW.md#oa-flow.gw.1) and [GW-3](OA-FLOW-GW.md#oa-flow.gw.3), the closed involution WR-3, and its polar operator [CI-3](OA-FLOW-CI.md#oa-flow.ci.3). The spectral and resolvent domains are proved in [SF, SB-4–6](OA-FLOW-SF.md#oa-flow.sf.sb4). These are earlier proofs in this collection.

<a id="normal-isomorphism-spectral-intersection"></a>

<a id="oa-flow.ct.1"></a><a id="ct-1"></a>

## Normal isomorphisms preserve the modular spectral intersection

Write $S(M)$ for the intersection of modular-operator spectra over all faithful normal semifinite weights on $M$, retaining zero when it belongs to every spectrum.

Let $\theta:N\to M$ be a normal unital star isomorphism. An order isomorphism carries each increasing supremum to the supremum of its image, so its inverse is normal as well. For every n.s.f. weight $\omega$ on $M$, its pullback $\omega\theta$ is n.s.f. on $N$. Positivity, normality and faithfulness follow immediately from the order-preserving normal isomorphism. Its finite ideal is $\theta^{-1}(\mathfrak n_\omega)$; the corresponding finite-domain density proves semifiniteness. Pullback by $\theta^{-1}$ is the inverse operation, so all n.s.f. weights are matched bijectively.

The formula

$$
 W\Lambda_{\omega\theta}(x)=\Lambda_\omega(\theta(x)),
 \qquad x\in\mathfrak n_{\omega\theta},
$$

is isometric by the GNS inner-product identity. Its range contains the dense GNS range for $\omega$, so it extends to a unitary. On the full finite-star domains,

$$
 W S_{\omega\theta,0}\Lambda_{\omega\theta}(x)
 =\Lambda_\omega(\theta(x^*))
 =S_{\omega,0}W\Lambda_{\omega\theta}(x).
$$

The same identity through $\theta^{-1}$ shows equality of both initial graphs, not just an inclusion. Taking graph closures yields $W S_{\omega\theta}W^*=S_\omega$. Taking the antilinear adjoints and their products gives

$$
 W\Delta_{\omega\theta}W^*=\Delta_\omega.
$$

The domains are transported by the graph unitary, so this is an equality of the complete positive self-adjoint operators. Unitary conjugation preserves spectra: each resolvent equation and bounded inverse is transported by $W$. Intersecting these spectra over the bijection of all n.s.f. weights proves $S(N)=S(M)$, with zero included exactly as in the definition. No state-only restriction or unsupported modular covariance theorem is used.

<a id="separable-predual-countability"></a>

<a id="oa-flow.ct.2"></a><a id="ct-2"></a>

## Countability and nonzero corners

A von Neumann algebra with separable predual is countably decomposable. Indeed, choose a unit vector in the range of each member of an orthogonal family of nonzero projections. Their vector states are normal by [CP-4](OA-FLOW-CP.md#oa-flow.cp.4). Any two states are at norm distance at least one, by evaluation on the first projection. A countable dense subset of the predual gives a cover by balls of radius one third, each containing at most one of these states. Hence the orthogonal family is countable.

Now let $M$ be a type III factor with separable predual and $0\ne p\in M$. The complete countably decomposable comparison proof PC-8 gives $v^*v=1$, $vv^*=p$. The map $x\mapsto vxv^*$ is a normal unital star isomorphism from $M$ onto $pMp$; its inverse is $y\mapsto v^*yv$. The graph calculation proves $S(pMp)=S(M)$. Thus a type III1 factor, defined by $S(M)=0,\infty)$, has the same type in every nonzero corner.

<a id="finite-matrix-amplification"></a>

<a id="oa-flow.ct.3"></a><a id="ct-3"></a>

## Finite matrix amplification

Split $1=p_1+p_2$ into two nonzero orthogonal projections. Such a split follows from the explicit halving and filling proof [PC-5. Choose $v_i^*v_i=1$, $v_iv_i^*=p_i$ using the same type III comparison theorem. Then $v_i^*v_j=\delta_{ij}1$. The maps

$$
 \Theta:M_2(M)\longrightarrow M,\qquad
 \Theta([x_{ij}])=\sum_{i,j=1}^2v_ix_{ij}v_j^*,
 \qquad
 \Theta^{-1}(x)=[v_i^*xv_j]_{i,j=1}^2
$$

are normal, mutually inverse, unital star homomorphisms. Multiplication follows by inserting $v_i^*v_j=\delta_{ij}1$; the inverse identity follows from $\sum_i v_iv_i^*=1$. The graph calculation again gives $S(M_2(M))=S(M)$. In particular, the exact matrix algebra used for the balanced homogeneity functional is type III1.

The argument proves the stated corner and matrix invariance from the earlier proofs linked above. The earlier NC/CR/MC lessons supply the natural-cone construction. The following TS lesson proves the specific type III1 spectral passage; the full homogeneity theorem and general S/Gamma intersection identity remain separate.

The free comparison provider for the projection step is [Nelson, Math 209: von Neumann Algebras, Lemma 5.2.9 and Proposition 5.2.13, printed 51](https://users.math.msu.edu/users/banelson/teaching/209/209_notes.pdf). Its role is comparison with the complete local PC proof; no external projection theorem is used in place of that proof.
