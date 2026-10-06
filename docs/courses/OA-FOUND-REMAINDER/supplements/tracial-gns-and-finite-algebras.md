# Tracial GNS representations and finite von Neumann algebras

*Self-checked by the writing AI. Original text: CC0 1.0.*

Definition 11.1 and Proposition 11.2(1)–(2) develop tracial GNS representations, with complete proofs. The auxiliary conjugate-linear isometry is used only to establish separation. The equality \(JMJ=M'\) and vector-state/spatial-automorphism theorems are separate assertions. Selection and route notes: GPT-6.1 Sol (OpenAI), Ultra, October 2026; new notes CC0.

## Prerequisites and notation

Inner products are linear in the first variable. Normal vector functionals, bounded separate continuity of multiplication, and ultraweak density in the bicommutant are proved in [The double commutant theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). The full GNS construction, including a nonunital algebra and positive contractive approximate units, is in [Representations and positive functionals](../../foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.html). The equivalence of order normality and ultraweak continuity is in [The universal enveloping algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). The references to Fact 2.4(4)-(5) below mean these precise density and GNS inputs. Fact 2.5(1) means the finite-trace extension and trace identity proved in Proposition 2.2 of [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html).

**Definition 11.1.** A positive linear functional \(\varphi\) on a \(C^*\)-algebra \(A\) is *tracial*, or *central*, if \(\varphi(x^*x)=\varphi(xx^*)\) for all \(x\in A\).

Then \(\varphi(xy)=\varphi(yx)\) for all \(x,y\in A\). Indeed, in any \(*\)-algebra \(4y^*x=\sum_{k=0}^3i^k(x+i^ky)^*(x+i^ky)\) and \(4xy^*=\sum_{k=0}^3i^k(x+i^ky)(x+i^ky)^*\); applying \(\varphi\) gives \(\varphi(y^*x)=\varphi(xy^*)\), and we replace \(y\) by \(y^*\).

**Proposition 11.2.** Let \(A\) be a \(C^*\)-algebra, with or without a unit, let \(\varphi\) be a positive linear functional on \(A\) that is tracial, and let \((\pi,K,\xi)\) be a cyclic representation with \(\varphi(a)=\langle\pi(a)\xi,\xi\rangle\) (Fact 2.4(5)). Let \(M=\pi(A)''\).

1. \(\tilde\varphi(x)=\langle x\xi,\xi\rangle\) is a faithful normal finite trace on \(M\).
2. \(\xi\) is cyclic and separating for \(M\).


**Proof.** *The trace property.* For \(a,b\in A\), \(\tilde\varphi(\pi(a)\pi(b))=\varphi(ab)=\varphi(ba)=\tilde\varphi(\pi(b)\pi(a))\). Fix \(y\in\pi(A)\). The functional \(x\mapsto\tilde\varphi(xy)-\tilde\varphi(yx)\) is \(\sigma\)-weakly continuous and vanishes on \(\pi(A)\), which is \(\sigma\)-weakly dense in \(M\) because \(\pi\) is nondegenerate (Fact 2.4(4)); so it vanishes on \(M\). Now fix \(x\in M\): the functional \(y\mapsto\tilde\varphi(xy)-\tilde\varphi(yx)\) vanishes on \(\pi(A)\), hence on \(M\). So \(\tilde\varphi(xy)=\tilde\varphi(yx)\) on \(M\), and \(\tilde\varphi\), a positive normal functional, is a finite normal trace (Fact 2.5(1)).

*The involution.* For \(a\in A\), \(\|\pi(a^*)\xi\|^2=\varphi(aa^*)=\varphi(a^*a)=\|\pi(a)\xi\|^2\). So \(J_0(\pi(a)\xi)=\pi(a^*)\xi\) is a well-defined conjugate-linear isometry of the dense subspace \(\pi(A)\xi\) onto itself, with \(J_0^2=1\). It extends to a conjugate-linear isometry \(J\) of \(K\) with \(J^2=1\); so \(J\) is onto. Polarization gives \(\langle J\eta,J\zeta\rangle=\langle\zeta,\eta\rangle\): the real parts agree because \(\|J(\eta+\zeta)\|=\|\eta+\zeta\|\), and replacing \(\zeta\) by \(i\zeta\) handles the imaginary parts. If \(A\) has a unit, \(J\xi=J\pi(1)\xi=\xi\). In general, let \((u_i)\) be an approximate unit of positive contractions (Fact 2.4(5)). Then \(\pi(u_i)\pi(a)\xi=\pi(u_ia)\xi\to\pi(a)\xi\), so the bounded net \(\pi(u_i)\) tends to \(1\) strongly on the dense subspace \(\pi(A)\xi\), hence on \(K\), and \(\xi=\lim_i\pi(u_i)\xi\). As \(J\pi(u_i)\xi=\pi(u_i)\xi\), \(J\xi=\xi\).

For \(a,b,x\in A\), \(J\pi(a)J\pi(x)\xi=J\pi(a)\pi(x^*)\xi=J\pi(ax^*)\xi=\pi(xa^*)\xi\). Hence
\[
J\pi(a)J\,\pi(b)\pi(x)\xi=\pi(bxa^*)\xi=\pi(b)\,J\pi(a)J\,\pi(x)\xi .
\]
So \(J\pi(a)J\) commutes with \(\pi(b)\) on a dense subspace, hence everywhere, and \(J\pi(A)J\subseteq\pi(A)'=M'\). The map \(x\mapsto JxJ\) is continuous for the weak operator topology, since \(\langle JxJ\eta,\zeta\rangle=\langle J\zeta,xJ\eta\rangle\), and \(M\) is the weak closure of \(\pi(A)\); so \(JMJ\subseteq M'\).

For \(x\in M\) and \(a\in A\), using \(\langle J\alpha,\beta\rangle=\langle J\beta,\alpha\rangle\) and the trace property,
\[
\langle J(x\xi),\pi(a)\xi\rangle=\langle\pi(a^*)\xi,x\xi\rangle=\tilde\varphi\bigl(x^*\pi(a^*)\bigr)=\tilde\varphi\bigl(\pi(a^*)x^*\bigr)=\langle x^*\xi,\pi(a)\xi\rangle .
\]
So \(J(x\xi)=x^*\xi\).

*Cyclic and separating.* \(\xi\) is cyclic for \(M\supseteq\pi(A)\). And \(M'\xi\supseteq JMJ\xi=JM\xi=M^*\xi=M\xi\), which is dense; so \(\xi\) is cyclic for \(M'\), that is, separating for \(M\). Hence \(\tilde\varphi(x^*x)=\|x\xi\|^2=0\) forces \(x=0\): \(\tilde\varphi\) is faithful. \(\square\)

**Corollary.** The algebra \(M\) of Proposition 11.2 is finite.

**Proof.** If \(v^*v=1\), traciality gives \(\tilde\varphi(1-vv^*)=0\). Faithfulness gives \(vv^*=1\). Thus the identity is a finite projection. \(\square\)
