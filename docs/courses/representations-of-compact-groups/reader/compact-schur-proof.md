# Schur's lemma through compact averaging

*Written and self-checked by GPT-6.1 Sol (OpenAI), Ultra effort, 3 October 2026. Original exposition: CC0 1.0.*

The first course lesson gives a general spectral proof of Schur's lemma. For compact groups there is also a shorter proof whose analytic input is only the compact self-adjoint spectral theorem. This route uses the already complete averaging proofs in that lesson and the included Hilbert-space chapter, and supplies the compact argument without needing the wider C*-algebra curriculum.

Let \(G\) be compact Hausdorff and let \(\pi\) be a nonzero strongly continuous irreducible unitary representation. Lemma 2.2 of the first lesson constructs a nonzero positive compact operator \(T_u\) by averaging a rank-one projection. That proof uses Haar integration, positivity on nonempty open sets, norm approximation by finite-rank operators and strong continuity; it does not use Schur's lemma. The compact spectral theorem supplies a positive eigenvalue. Its eigenspace is invariant and finite dimensional by Proposition 2.5, whose proof likewise does not use Schur's lemma. Irreducibility forces that eigenspace to be the whole representation, exactly as in Theorem 2.7.

Now let \(A\) commute with \(\pi(G)\). Since the space is a nonzero finite-dimensional complex vector space, \(A\) has an eigenvalue \(a\). The nonzero kernel of \(A-aI\) is invariant, because \(A\) commutes with every \(\pi(g)\). Irreducibility makes the kernel the whole space, so \(A=aI\). Conversely a proper nonzero closed invariant subspace has a commuting orthogonal projection by Lemma 1.1, contradicting a scalar commutant.

If \(T:V\to W\) is a nonzero bounded intertwiner between irreducibles, its kernel and image are invariant. Finite dimension makes the image closed, so \(T\) is bijective. Alternatively the scalar commutant gives \(T^*T=cI\) and \(TT^*=dI\), with \(c,d>0\). The identity \((TT^*)T=T(T^*T)\) gives \(c=d\), so \(T/\sqrt c\) is unitary. Fixing one such unitary \(U\) makes every other intertwiner a scalar multiple of \(U\), since \(U^*T\) belongs to the commutant. Thus the full compact Schur statement, including arbitrary initial Hilbert spaces, follows.

There is no circular dependency: finite dimension here comes from averaging and compact spectral theory, rather than from the earlier Schur statement. The proofs of Lemma 2.2, Proposition 2.5 and Theorem 2.7 have been checked for this independence. The original spectral proof remains available as a broader alternative, and all original course lesson bytes are retained.
