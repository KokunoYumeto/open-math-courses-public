# SH02-COURSE-CONTRACT — How to use this course draft

Local identifier: `SH02-COURSE-CONTRACT`.

This course develops sheaf operations as tools for studying directions of
propagation. Its writing order starts with conic objects and kernel operations;
the eventual learner order follows the dependency graph in the course index.
The intended audience already knows abelian and derived categories, sheaves
on topological spaces, basic manifold topology and cotangent bundles. Exact
open prerequisites are linked in the prerequisite lesson. Further prerequisites
remain explicitly named when the available open statement does not supply
the required generality or proof.

The course covers the microlocal theory of sheaves: the Fourier–Sato transformation, specialization and
microlocalization, the micro-support and its functorial properties, and microlocal categories. This is the
theory of M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf),
Astérisque 128 (1985), Chapters 1–6; see also P. Schapira,
[*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016).
The course includes the subordinate lemmas and the substantive phenomena of the classical exercises.
Categorical foundations are taught in *Categorical and derived tools for analytic sheaves*; constructible
sheaves, characteristic cycles and contact transformations in *Constructible and perverse sheaves*.

The advanced baseline coefficient ring is commutative with identity and finite
global dimension. A theorem that specifically uses a field says so locally.
There is no general assumption of constructibility, finite-rank stalks,
compactness or orientability. Manifolds have finite dimension and are countable
at infinity; submanifolds may be locally closed. Some operations are developed
on more general locally compact spaces, and each such statement specifies its
own assumptions. The finite cohomological dimension required to construct an
exceptional inverse image is an assumption on proper-support direct image of
abelian sheaves, not an unstated claim about arbitrary continuous maps.

We use cohomological grading: $H^i(K[n])=H^{i+n}(K)$. For a locally closed
subset $A$ of $X$, $k_A$ denotes the constant sheaf on $A$ extended by zero
to $X$ using its locally closed embedding. This differs from the sheaf of
sections with support in $A$. The latter construction, its derived functor
and its restriction to a point are typed in each lemma. A functor written
$Rf_!$ uses supports proper over the target. A star or an exclamation mark
cannot be changed without a theorem or a specified comparison morphism.

Orientation sheaves are retained in formulas. Choosing a local orientation
can simplify a calculation, but it does not remove the transition functions
from a global statement. The positive and negative pairing halfspaces, the
antipodal map, the order of product orientations and the degree shifts of
Fourier–Sato operations are all part of their definitions. Local calculations
must return to these conventions before being used in a composition.

Each lesson separates statements proved there, exact imports, conditional proofs whose inputs remain open, and outstanding source obligations.

Examples and exercises are newly designed. Their solutions show the algebra
and topology needed to check the formulas. Source examples that expose a
mathematical phenomenon enter the private coverage map; their protected
expression and organization do not enter this course. Detected source
misprints or false assertions receive a visible correction and an explicit
mathematical reason.

This directory is an exchange package for the existing reader. It does not
provide another website. Its stable `SH02-...` identifiers are local course
identifiers and have not been registered as official Stacks tags.
