# Real spectral decomposition

*Theorem 3.1 and its proof from the earlier programme lesson **Fourier transforms, finite spectra and convex separation**. Programme credits and the CC0 dedication are retained in the accompanying [credits](notices/TITLE_PAGE.md) and [rights notice](notices/RIGHTS.md). Selection by GPT-6 Astra (OpenAI), October 2026.*

The [scalar foundation](metric-foundation-bridges.md), Sections 12.5–12.9 and 13.4, supplies compactness, extrema and differentiation. The [finite algebra foundation](stable-prerequisite-bridges.md), Sections 10.1–10.8, supplies bases, Gram–Schmidt and inner-product identities. This proof applies to the actual given real inner product, including repeated and zero eigenvalues.

## 3. Real spectral decomposition

**Theorem 3.1 (Real spectral decomposition).** Every self-adjoint endomorphism of a finite-dimensional real inner-product space has a real orthonormal eigenbasis, including repeated and zero eigenvalues.

**Proof.** In dimension zero the empty basis suffices. Otherwise maximize \(\langle Av,v\rangle\) over the compact unit sphere, and call a maximizer \(v\). For each \(w\perp v\), differentiate \(\langle A(v+tw),v+tw\rangle/\langle v+tw,v+tw\rangle\) at \(t=0\). Its derivative vanishes, so \(\langle Av,w\rangle=0\); hence \(Av=\lambda v\) for \(\lambda=\langle Av,v\rangle\). Self-adjointness makes \(v^\perp\) invariant, since \(\langle Aw,v\rangle=\langle w,Av\rangle=0\) for \(w\perp v\). Induction on dimension gives an orthonormal eigenbasis of \(v^\perp\). Together with \(v\) it gives the asserted basis, with no distinct-eigenvalue assumption. ∎
