"""Build the lesson sequence and matching offline download with native MathML.
The explicit release list excludes private records. No remote writes.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8', newline='\n')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wrap_math(match):
    math = match.group(1)
    tag = re.search(r'\\tag\{([0-9]+[a-z]?)\}', math)
    if tag:
        # Pandoc keeps tags in annotations but omits their visible numbers.
        return ('<span class="math display numbered"><span class="equation-content">'
                +math+'<span class="equation-number">('+tag.group(1)+')</span></span></span>')
    return '<span class="math display">'+math+'</span>'


def shell(body, title, nav):
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>'+html.escape(title)+'</title><link rel="stylesheet" href="reader.css">'
            '</head><body><a class="skip" href="#main">Skip to the lesson</a>'
            '<header>'+nav+'</header><main id="main">'+body+'</main>'
            '<footer>Original mathematical exposition and illustrations: '
            '<a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>. '
            'References retain their own authorship and terms.</footer></body></html>\n')


def main():
    course = json.loads((ROOT/'COURSE.json').read_text(encoding='utf-8'))
    files = ['index.html', 'reader.css', 'COURSE.json', 'PROVENANCE.json',
             'figures/three-clocks.svg', 'figures/quotient-mixing.svg', 'figures/lattice-frequencies.svg',
             'figures/renewal-crossing.svg', 'figures/phase-triangle.svg', 'figures/encounter-packing.svg', 'build/build_reader.py',
             'build/check_examples.py', 'build/check_pathway.py', 'build/check_fourier.py', 'build/check_concentration.py',
             'build/check_lattice.py', 'build/draw_lattice.py', 'build/check_renewal.py', 'build/draw_renewal.py',
             'build/check_phase.py', 'build/draw_phase.py', 'build/check_encounters.py', 'build/draw_encounters.py', 'build/check_weighted.py', 'build/check_mixing.py', 'build/check_first_passage.py', 'build/check_entrance_limits.py',
             'build/check_retained_total.py', 'checks/retained_total.json',
             'build/check_joint_mixing.py', 'build/draw_joint_mixing.py', 'checks/joint_mixing.json', 'figures/joint-total-mixing.svg',
             'build/check_coarse_conditioning.py', 'build/draw_coarse_conditioning.py', 'checks/coarse_conditioning.json', 'figures/conditioned-prefix.svg',
             'build/check_integer_boundaries.py', 'build/draw_integer_boundaries.py', 'checks/integer_boundaries.json', 'figures/integer-boundaries.svg',
             'build/check_counting_kernel.py', 'build/draw_counting_kernel.py', 'checks/counting_kernel.json', 'figures/counting-kernel.svg',
             'build/check_rotation_averages.py', 'build/draw_rotation_averages.py', 'checks/rotation_averages.json', 'figures/rotation-grid.svg',
             'build/check_profile_kernel.py', 'build/draw_profile_kernel.py', 'checks/profile_kernel.json', 'figures/profile-levels.svg',
             'build/check_logarithmic_separation.py', 'build/draw_logarithmic_separation.py', 'checks/logarithmic_separation.json', 'figures/logarithmic-minors.svg',
             'build/check_entrance_counting.py', 'build/draw_entrance_counting.py', 'checks/entrance_counting.json', 'figures/entrance-counting.svg',
             'build/check_timed_scales.py', 'build/draw_timed_scales.py', 'checks/timed_scales.json', 'figures/timed-scales.svg',
             'build/check_clock_costs.py', 'build/draw_clock_costs.py', 'checks/clock_costs.json', 'figures/first-entrance-cost.svg',
             'build/check_affine_support.py', 'build/draw_affine_support.py', 'checks/affine_support.json', 'figures/affine-support.svg',
             'build/check_strict_profiles.py', 'build/draw_strict_profiles.py', 'checks/strict_profiles.json', 'figures/strict-phase.svg',
             'build/check_lattice_profiles.py', 'build/draw_lattice_profiles.py', 'checks/lattice_profiles.json', 'figures/lattice-multiplicity.svg',
             'build/check_endpoint_weights.py', 'build/draw_endpoint_weights.py', 'checks/endpoint_weights.json', 'figures/endpoint-fibres.svg',
             'build/check_physical_windows.py', 'build/draw_physical_windows.py', 'checks/physical_windows.json', 'figures/physical-windows.svg',
             'build/check_prefix_passage.py', 'build/draw_prefix_passage.py', 'checks/prefix_passage.json', 'figures/prefix-passage.svg',
             'build/check_weighted_assembly.py', 'build/draw_weighted_assembly.py', 'checks/weighted_assembly.json', 'figures/mass-weighted-assembly.svg',
             'build/check_scheduled_transport.py', 'build/draw_scheduled_transport.py', 'checks/scheduled_transport.json', 'figures/scheduled-transport.svg',
             'build/check_reverse_transport.py', 'build/draw_reverse_transport.py', 'checks/reverse_transport.json', 'figures/reverse-fibre.svg',
             'build/check_parity_envelopes.py', 'build/draw_parity_envelopes.py', 'checks/parity_envelopes.json', 'figures/parity-reflection.svg', 'build/draw_affine_envelope.py', 'figures/affine-envelope.svg',
             'build/check_stopped_chains.py', 'build/draw_stopped_chains.py', 'checks/stopped_chains.json', 'figures/stopped-chain.svg',
             'build/check_iterated_pullbacks.py', 'build/draw_iterated_pullbacks.py', 'checks/iterated_pullbacks.json', 'figures/time-fibres.svg',
             'build/check_finite_survival.py', 'build/draw_finite_survival.py', 'checks/finite_survival.json', 'figures/three-block-survival.svg',
             'build/check_timeout_coding.py', 'build/draw_timeout_coding.py', 'checks/timeout_coding.json', 'figures/timeout-word-map.svg',
             'build/check_critical_shell.py', 'build/draw_critical_shell.py', 'checks/critical_shell.json', 'figures/critical-shell.svg',
             'build/check_uniform_paths.py', 'build/draw_uniform_paths.py', 'checks/uniform_paths.json', 'figures/uniform-paths.svg',
             'build/check_same_orbit.py', 'build/draw_same_orbit.py', 'checks/same_orbit.json', 'figures/same-orbit-joining.svg',
             'checks/examples.json', 'checks/pathway.json', 'checks/fourier.json', 'checks/concentration.json', 'checks/lattice.json', 'checks/renewal.json', 'checks/phase.json', 'checks/encounters.json', 'checks/weighted.json', 'checks/mixing.json', 'checks/first_passage.json', 'checks/entrance_limits.json']
    readers = []
    for i, lesson in enumerate(course['lessons']):
        source = (ROOT/lesson['source']).read_text(encoding='utf-8')
        built = subprocess.run(
            ['pandoc', '-f', 'markdown+tex_math_single_backslash-implicit_figures',
             '-t', 'html5', '--mathml'], input=source, text=True,
            encoding='utf-8', capture_output=True, check=True)
        if built.stderr.strip():
            raise RuntimeError(built.stderr)
        body = built.stdout.replace('src="../figures/', 'src="figures/')
        body = body.replace('href="../build/', 'href="build/')
        for other in course['lessons']:
            body = body.replace('href="'+other['id']+'.md', 'href="'+other['reader'])
        body = re.sub(r'(<math display="block"[\s\S]*?</math>)', wrap_math, body)
        assert len(re.findall(r'\\tag\{[0-9]+[a-z]?\}', source)) == body.count('class="equation-number"')
        body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
        body = re.sub(r'(<p><img\b[^>]+></p>)', r'<div class="figure-scroll">\1</div>', body)
        if '<merror' in body or '<math' not in body:
            raise ValueError('Mathematical typesetting failed: '+lesson['id'])
        nav = '<a href="index.html">'+html.escape(course['title'])+'</a> · '
        nav += '<a href="'+lesson['source']+'">Lesson source</a>'
        nextlinks = []
        if i:
            p = course['lessons'][i-1]
            nextlinks.append('<a href="'+p['reader']+'">Previous: '+html.escape(p['title'])+'</a>')
        if i+1 < len(course['lessons']):
            n = course['lessons'][i+1]
            nextlinks.append('<a href="'+n['reader']+'">Next: '+html.escape(n['title'])+'</a>')
        body += '<nav aria-label="Lesson sequence"><p>'+'<br>'.join(nextlinks)+'</p></nav>'
        write(lesson['reader'], shell(body, lesson['title'], nav))
        files.extend([lesson['reader'], lesson['source']])
        readers.append({'id':lesson['id'], 'math_expressions':body.count('<math'),
                        'source_words':len(source.split())})
    overview = '''<h1>Discrete dynamics, coding and probability</h1>
<p>A dynamical system can be described by its successive states, by the branches it follows, or by the distributions obtained from many starting points. These descriptions retain different information. This sequence develops the maps between them and proves exactly what each preserves.</p>
<p>The Collatz iteration is a sustained case study, not the endpoint of the course. Its elementary definition makes it possible to see return maps, symbolic coding, congruence counting and probability transport working together. Other examples separate the general mechanisms from the unresolved conjecture.</p>
<h2>Thirty-nine lessons</h2>
<ol>
<li><a href="NT-COLLATZ-01.html">Return maps and exact changes of clock</a> proves a general return-clock theorem, then reconstructs ordinary, shortcut and odd-return Collatz trajectories. It identifies when deleting states does and does not preserve an orbit minimum.</li>
<li><a href="NT-COLLATZ-02.html">Symbolic itineraries and affine composition</a> derives exact branch coordinates, proves that finite parity words correspond to residue classes, and obtains a finite probability law by counting these classes.</li>
<li><a href="NT-COLLATZ-03.html">Pushforward measures and logarithmic sampling</a> proves composition and contraction of transported measures, then calculates the effect of the odd-part projection on uniform and logarithmic sampling. The density conclusions do not require density limits to exist.</li>
<li><a href="NT-COLLATZ-04.html">First passage and transport across scales</a> constructs entrance maps, identifies their kernels and images, and proves finite-chain and summable-scale bounds for orbit minima.</li>
<li><a href="NT-COLLATZ-05.html">Quotient distributions and Fourier mixing</a> distinguishes mixing within observation classes from uniformity on an entire group. It proves an estimate combining Fourier decay and collision probability, gives an exact affine prefix–tail decomposition, and works out a complete random-walk mixing example.</li>
<li><a href="NT-COLLATZ-06.html">Geometric waiting times and controlled conditioning</a> proves explicit concentration bounds, an exact finite-residue comparison for valuation words, and the conditions under which stopping or conditioning leaves an independent unused tail.</li>
<li><a href="NT-COLLATZ-07.html">Local probabilities for lattice sums</a> proves the dimension-dependent point-probability bound using a finite support certificate and exponential weights. It constructs the two-coordinate holding time used in the renewal application and verifies its mean, support and exponential moment.</li>
<li><a href="NT-COLLATZ-08.html">Renewal paths and first-crossing locations</a> sums the local estimates into a renewal measure, proves an exit-location bound with exponential overshoot tails, and derives exact restart and stopped-mean formulas. The marked geometric blocks give the worked Collatz application.</li>
<li><a href="NT-COLLATZ-09.html">Conditional cancellation and arithmetic phase geometry</a> calculates the cancellation left after conditioning on paired waiting times, proves that low-phase positions form separated lattice triangles, and identifies the remaining expectation with an exact renewal occupation count.</li>
<li><a href="NT-COLLATZ-10.html">Renewal encounters with separated regions</a> proves a uniform chance of cancellation at a triangle exit and a local-probability bound for hitting another large triangle. These give a finite horizon with many cancelling visits, with stopping, rounding and strip-departure errors kept explicit.</li>
<li><a href="NT-COLLATZ-11.html">Weighted renewal estimates and Fourier decay</a> balances multiplicative cancellation against the distance consumed by a crossing. It proves a remaining-width estimate and Tao's arbitrary-power Fourier bound for full-order characters, then calculates why a lower-order coefficient can persist.</li>
<li><a href="NT-COLLATZ-12.html">Arithmetic separation and fine-scale mixing</a> recovers a word from its rational offset and proves modular injectivity under an integer-height bound. Exact stopped-prefix masses and an independent tail then give Tao's fine-scale mixing theorem, first between nearby scales and then between arbitrary scales.</li>
<li><a href="NT-COLLATZ-13.html">Logarithmic sampling and first-passage distributions</a> connects the independent-word model to integer trajectories. It proves the sampling comparison, the exact word-and-endpoint inverse, the uniform harmonic bound and Tao’s entrance-law stabilization, with failure kept as a separate state.</li>
<li><a href="NT-COLLATZ-14.html">Compatible entrance laws and weighted orbit minima</a> constructs exactly compatible limiting laws and simultaneous entrance observations. It proves the general weighted tightness criterion and derives Tao’s fixed-threshold and arbitrary-diverging-threshold orbit-minimum conclusions with exact harmonic weights.</li>
<li><a href="NT-COLLATZ-15.html">Retaining information through Fourier cancellation</a> proves a retained-statistic estimate, Allikvere's sum-conditioned Fourier theorem and the exact convolution formula for shorter character orders. It explains why a joint offset and total is needed when changing the arithmetic sampling law.</li>
<li><a href="NT-COLLATZ-16.html">Joint distributions and mixing under conditioning</a> retains the total through arithmetic prefix separation, tail cancellation and comparisons across scales. It proves joint offset-total mixing and derives conditioned mixing at every residue scale whose exponent is at least a fixed positive power of the word length.</li>
<li><a href="NT-COLLATZ-17.html">Fixed totals and the law of a short prefix</a> gives exact clock covariances and a martingale for uniform compositions, proves the factorial and local-probability estimates, and compares a conditioned prefix with independent waiting times. A paired likelihood estimate covers every positive prefix below any fixed sublinear power; combining it with joint mixing yields the offset product approximation.</li>
<li><a href="NT-COLLATZ-18.html">Integer fibres and the cost of moving a boundary</a> retains the exact arithmetic inverse, counts first-passage cylinders modulo odd integers and proves an explicit boundary error. Integer separation limits each endpoint to one encounter; the full return-band error is of order (log x)<sup>−1/2</sup>.</li>
<li><a href="NT-COLLATZ-19.html">Counting kernels and weighted probability errors</a> sums the sharp integer cutoffs exactly, proves a uniform binomial kernel bound and transfers probability errors through actual residue populations. The arithmetic fibre formula holds at every fixed coarse exponent between zero and one, with an explicit exponent-dependent absolute remainder.</li>
<li><a href="NT-COLLATZ-20.html">Rational grids and weighted rotation averages</a> divides a rotation orbit into blocks close to complete rational grids. A lower bound on rational approximation gives an explicit discrepancy estimate; full Koksma and summation-by-parts proofs then control unequal weights. The square-root-of-two example supplies every arithmetic input directly.</li>
<li><a href="NT-COLLATZ-21.html">Unimodal weights and sharp counting kernels</a> bounds a weighted phase average by the profile's mass and maximum, removing a support-width logarithm. It evaluates the exact asymmetric envelope integral and derives a sharp binomial kernel's leading constant, with all floor, tail and lower-boundary errors retained.</li>
<li><a href="NT-COLLATZ-22.html">Integer polynomials and separation of logarithms</a> constructs simultaneous logarithmic approximations with integer coefficients. Weighted divisibility, positive integral minors and prime counting give a uniform separation theorem, which supplies the arithmetic input for the actual logarithmic-slope counting kernel. The argument includes exact rational bounds for Rhin's six polynomial factors.</li>
<li><a href="NT-COLLATZ-23.html">Counting trajectories and comparing entrance distributions</a> explains when a weighted path count represents an actual probability law. A complete concentration and first-entrance argument keeps the exceptional multiplicity and failure state explicit. Combining the earlier kernel and arithmetic estimates gives a common entrance profile for two uniformly sampled input ranges, with a quantitative summed error.</li>
<li><a href="NT-COLLATZ-24.html">Summable scale comparisons and timed orbit bounds</a> carries a time-bounded continuation through a target set. Explicit concentration gives a square-root logarithmic time allowance; summable errors and a disjoint interval cover then yield a uniform fixed-target count and natural density for arbitrary diverging targets on odd-return trajectories.</li>
<li><a href="NT-COLLATZ-25.html">First entrances and quantitative changes of clock</a> bounds an accumulated correction by sorting the distinct states before first entrance. Exact telescoping gives the leading shortcut and ordinary drift coefficients. Disjoint input fibres retain the natural-density rate and a common endpoint on all positive integers. Exact truncation and continuation of two marked odd visits give finite tail lengths and heights.</li>
<li><a href="NT-COLLATZ-26.html">Exact preimages and mass-weighted error bounds</a> constructs genuine positive inverse branches from a congruence alone. Disjoint terminal events let relative errors be charged to their actual mass; moving the support instead costs boundary mass. The exact maximal affine offset yields a sharper local correction estimate, with all sampling endpoints and finite sums retained.</li>
<li><a href="NT-COLLATZ-27.html">Integer thresholds and weighted phase averages</a> enumerates the exact levels in a strict logarithmic band. An explicit probability ratio and a count of boundary terms compare neighboring profiles. Separate-mass averaging, weighted interval discrepancy and sharp proportional-error absorption explain how the finite comparisons combine without losing their actual weights.</li>
<li><a href="NT-COLLATZ-28.html">Local probabilities and moving lattice cutoffs</a> calculates exact level multiplicities and sums their Gaussian weights with explicit finite errors. A common-center local estimate gives the original profile's mass. Combining it with mass-height averaging removes the support-width logarithm from both geometric band profiles, while exact recurrences and clipping bounds preserve their actual weights.</li>
<li><a href="NT-COLLATZ-29.html">Arithmetic fibres and weighted exponential tails</a> identifies actual first-passage integers in exact residue classes and bounds their reciprocal mass. Retaining the first point and exact interval ratio gives coefficient 1/2 + (1/2) log(8/3) with a decaying error. Exact terminal exponential moments control the exterior endpoints, and a mass-weighted assembly theorem connects these arithmetic bounds to analytic profiles.</li>
<li><a href="NT-COLLATZ-30.html">Logarithmic bands and exact time windows</a> proves an invertible time translation that retains both strict level supports in the actual trajectory window. Rational scale bounds preserve positivity and integer rounding. Exact odd-integer sampling denominators and weighted exterior tails then give the full reference-profile comparison with its original arithmetic mass.</li>
<li><a href="NT-COLLATZ-31.html">Maximal deviations and exact first passage</a> proves a stopped-exponential bound for all prefixes at once, then transfers it to actual arithmetic sampling by exact residue maps. Finite affine bounds locate the first crossing and its shifted endpoint. Both directions of the word-and-endpoint correspondence are proved, so the event comparison costs one exceptional probability.</li>
<li><a href="NT-COLLATZ-32.html">Combining weighted estimates into a first-passage law</a> preserves every endpoint through exact fibre averages and conditional laws. Relative errors sum against actual probability mass, while absolute errors sum with their total probabilities. The preceding analytic and arithmetic arguments then give one common first-passage reference for both sampling laws, completed probability comparisons and the original reference mass.</li>
<li><a href="NT-COLLATZ-33.html">Coarsening laws and preserving travel times</a> measures exactly what merging outcomes loses, calculates weighted source overlap, and proves a deterministic recurrence carrying integer time budgets. Uniform source comparisons remove a final change of sampling law. The resulting scheduled clock is compared with the sharper drift clock, showing which trajectory information accounts for the difference.</li>
<li><a href="NT-COLLATZ-34.html">Reverse maps and first passage fibres</a> turns an exact reverse product into an integer preimage bound. Shell clipping and odd-step denominators sharpen its finite constants. Geometric rescaling controls loss across decreasing thresholds, and explicit inverse clock maps identify the same first passage in the shortcut, odd-return and ordinary dynamics. A finite logarithmic path bound transfers to the parity count, the ordinary trajectory and every intermediate first crossing.</li>
<li><a href="NT-COLLATZ-35.html">Maximal parity deviations and orbit envelopes</a> turns exact parity sampling into maximal entropy bounds. An invertible reflection retains the binomial prefactor. Bounding the affine correction then gives a full-entropy orbit envelope with explicit startup, including a uniform estimate for shrinking tolerances.</li>
<li><a href="NT-COLLATZ-36.html">Exceptional sets and stopped orbit chains</a> proves finite preimage counting, an exact endpoint exchange and first-failure transport. A rank telescope and final-shell summation retain the same path, its time and height, and the full exceptional-set exponent and prefactor.</li>
<li><a href="NT-COLLATZ-37.html">Iterated pullbacks and the cost of descent</a> sums individual time fibres, retains the endpoint density exponent and tracks its logarithmic cost through a fixed number of pullbacks. An absorbing startup region and earlier guaranteed horizons give a closed power target with simultaneous shortcut, odd-return and ordinary clocks.</li>
<li><a href="NT-COLLATZ-38.html">Finite survival and changes of probability weights</a> proves finite stopped moments, a variance-dependent barrier estimate and an explicit binomial atom bound. Two disjoint outer survival constraints and a conditional middle-block estimate give the three square-root factors in a tilted word bound. A second exact weighting gives reciprocal maximum bounds.</li>
<li><a href="NT-COLLATZ-39.html">From word survival to integer exceptions</a> combines exact timeout coding, one decreasing high-rank sequence and bounded first-passage fibres. The full critical theorem gives a common small endpoint, both centered clocks and both relative-height bounds. Independent divergent allowances give natural density one; uniform path and intermediate-passage bounds use the same inputs. Moving exponents and iterated-logarithmic targets retain their quantitative rates, while a height obstruction proves the matching joint lower counts. Intersecting with the timed fixed-target event on original inputs retains the sharper three clocks, relative heights and uniform paths down to arbitrary diverging targets.</li>
</ol>
<p>Each lesson contains complete written arguments, worked examples, and four exercises with solutions. The specialised results used later are proved here or linked to a preceding lesson.</p>
<h2>Two ways to read</h2>
<p>For the connected Collatz case study, read the lessons in order. For the general subjects, begin with return maps; continue to the second lesson for coding and arithmetic, or to the third and fourth for probability transport. The third and fifth give a route into probability on finite groups and harmonic analysis; the sixth adds concentration and conditional independence, the seventh continues to lattice Fourier analysis and point probabilities, and the eighth develops renewal measures, exit laws and random stopping. The ninth joins conditional Fourier cancellation to arithmetic geometry; the tenth estimates repeated renewal encounters and occupation counts; the eleventh turns these into a weighted renewal bound and Fourier decay. The twelfth combines that decay with arithmetic separation to control a full probability law. The thirteenth converts that control into a comparison of first-passage distributions for sampled integer trajectories. The fourteenth returns to general probability transport and weighted tightness, using the proved arithmetic estimates for the Collatz application. The sixth lesson's arithmetic application returns to the parity coding of the second lesson. These are routes through the same lessons, not separate courses.</p>
<p>The first two lessons assume positive-integer arithmetic, induction, well-ordering and division with remainder. The probability-transport lessons also use elementary limits, completeness of the real numbers, logarithms and integration of elementary functions. The Fourier lesson assumes complex conjugation, complex exponentials and geometric sums; it proves its finite transform identities explicitly. Concentration adds elementary differentiation and binomial coefficients. The lattice lesson uses Euclidean vectors and repeated one-variable integrals, with all exchanges of sums and integrals justified.</p>
<h2>Placement in the wider subjects</h2>
<p>The <a href="NT-COLLATZ-14.html#tightness-under-weighted-counting">weighted tightness criterion</a> can be read after the sampling lesson, independently of the renewal proof. The <a href="NT-COLLATZ-04.html#nested-targets-compose-exactly">nested-passage operators</a> belong to induced dynamics and probability transport. The <a href="NT-COLLATZ-05.html#what-a-quotient-observation-forgets">quotient projection</a> belongs to finite-group harmonic analysis. The <a href="NT-COLLATZ-07.html">lattice probability estimates</a> and <a href="NT-COLLATZ-08.html">renewal crossing bounds</a> provide a route into random walks and stopping times. These subject routes reuse the same proofs; the Collatz example shows how they interact.</p>
<h2>What the sequence establishes</h2>
<p>Induced dynamics, symbolic dynamics, arithmetic density, probability and harmonic analysis provide the broader mathematical homes for these lessons. First passage explains how distributional estimates can feed into an orbit-minimum theorem. The renewal, phase and arithmetic arguments give complete proofs of Tao's arbitrary-power Fourier decay and fine-scale mixing for random affine offsets. The thirteenth completes the transition to first-passage distributions of sampled integer trajectories. The fourteenth constructs compatible entrance laws and derives Tao’s orbit-minimum theorem through summable probability transport. It also proves a general weighted tightness criterion. These are logarithmic distributional conclusions, not a solution of the Collatz conjecture or a universal bound on stopping time.</p>
<h2>Read, study and reproduce</h2>
<p>The fifteenth through thirty-ninth lessons continue beyond logarithmic sampling. They retain the total through Fourier cancellation and mixing, prove coarse conditioning and the product approximation, and then return to exact integer fibres, boundary errors and weighted counting kernels. Rotation averages and polynomial approximation supply the logarithmic kernel constant. The entrance-counting lesson combines these estimates with actual-input concentration and deterministic first-entrance identification. The timed-scale lesson proves the full natural-density iteration on odd starting integers, with a target-independent odd-return clock and no discarded-interval error. Its smaller time allowance follows from the explicit concentration estimate. The next lesson uses distinct first-entrance states and exact input fibres to retain the drift clock coefficients on all integers, without another exceptional estimate. Further lessons develop Mazur's terminal comparison through inverse maps, boundary strips, strict phases, neighboring probabilities and mass-weighted absorption. Exact multiplicities and local probabilities determine the geometric profiles' masses and quantitative phase limits. Arithmetic fibres and terminal exponential moments then control the actual reciprocal endpoint weights and their tails. Exact time-window inclusion and sampling denominators now complete the weighted reference profile. A maximal inequality now controls all prefixes under the actual band laws. Exact forward and reverse path arguments identify the terminal records with first passages on that common good set. Conditional fine mixing and paired relative likelihoods now combine against actual total mass to complete a common genuine first-passage law for both uniform and harmonic inputs. The proof retains exact closed-block endpoints, a separate nonpassage state and the original reference measure. Exact source overlap and a separate scheduled-failure event now carry the second construction through timed scale iteration. Its complete family of comparisons permits uniform sampling throughout, removing an extra final passage. The exact geometric clock is kept distinct from the sharper earlier drift clock. The reverse-map lesson now develops Shaik's finite deterministic route: exact product defects, integer fibres, geometric suppression of earlier loss, and invertible changes of first-passage clock. The next lesson now develops exact parity sampling, maximal entropy bounds, reflection and the full affine correction. The exact affine correction requires an allowance of only log₂(7/6), retaining the full entropy exponent with smaller explicit constants and startup ranks. The uniform quadratic bound has prefactor two. The stopped-chain lesson combines these inputs without assuming uniform landings. It proves the same path's time and height estimates and sums exact finite counts into global stretched and power-law descent conclusions. The next lesson retains logarithmic costs through repeated pullbacks and proves a graded time bound for the exact target exponent, including an absorbing startup region. Finite centered survival and exact changes of word weights now supply the three-block estimate from Shaik's version4.0.2. Exact affine bounds now turn survival into a literal integer timeout estimate. A common interval of passage times and the original-source fibre bounds retain the critical first-timeout saving. The complete critical shell theorem now combines a small common endpoint, both centered clocks and both relative-height bounds. Independent arbitrarily slow target and height allowances give natural density one; fixed logarithmic powers give a matching upper and lower count for the joint requirement. Uniform trajectory tubes now control actual first passages at every intermediate level, without another exceptional event. Moving critical exponents and slower iterated-logarithmic factors retain their exact joint exceptional orders. A fixed relative-height obstruction explains why a diverging allowance matters. The same-orbit synthesis now joins the timed fixed-target event to the critical controlled prefix. Subtracting its lower odd-return clock from the upper total clock controls the actual remaining path; arbitrary independent divergent target and height functions retain all three existing clocks, uniform trajectories and intermediate first passages. Inselmann's full-horizon envelopes and further survey-routed literature remain the subject of the continuing sequence. The aim is a proof-complete pedagogical synthesis; resolving Collatz is not a requirement for completing the course.</p>
<p>The <a href="../../downloads/NT-COLLATZ.zip">offline download</a> contains all thirty-nine readers, editable lesson sources, diagrams and reproducible checks. Exact finite checks and high-precision numerical diagnostics are distinguished. After extracting it, open the included index.html. The general results are established by the written proofs, not by a finite computation. The logarithmic-separation lesson links to the existing prime-counting course for its proved prime number theorem prerequisite; that separate course is not duplicated in this download. The writing AI has self-checked the lessons; no independent review or Lean certification is claimed.</p>
<p><a href="PROVENANCE.json">Authorship and mathematical references</a>.</p>'''
    write('index.html', shell(overview, course['title'], 'Open Mathematics Courses'))
    checks = {}
    for stem in ['examples', 'pathway', 'fourier', 'concentration', 'lattice', 'renewal', 'phase', 'encounters', 'weighted', 'mixing', 'first_passage', 'entrance_limits', 'retained_total', 'joint_mixing', 'coarse_conditioning', 'integer_boundaries', 'counting_kernel', 'rotation_averages', 'profile_kernel', 'logarithmic_separation', 'entrance_counting', 'timed_scales', 'clock_costs', 'affine_support', 'strict_profiles', 'lattice_profiles', 'endpoint_weights', 'physical_windows', 'prefix_passage', 'weighted_assembly', 'scheduled_transport', 'reverse_transport', 'parity_envelopes', 'stopped_chains', 'iterated_pullbacks', 'finite_survival', 'timeout_coding', 'critical_shell', 'uniform_paths', 'same_orbit']:
        checked = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT/'build'/('check_'+stem+'.py'))],
                                 capture_output=True, text=True, encoding='utf-8', check=True)
        checks[stem] = json.loads(checked.stdout)
        assert checks[stem]['passed']
        write('checks/'+stem+'.json', json.dumps(checks[stem], ensure_ascii=False, indent=2)+'\n')
    for name in ['index.html']+[x['reader'] for x in course['lessons']]:
        text = (ROOT/name).read_text(encoding='utf-8')
        for link in re.findall(r'(?:href|src)="([^"]+)"', text):
            if ':' in link or link.startswith('#') or link == course['download']:
                continue
            path = html.unescape(link.split('#')[0])
            assert (ROOT/path).is_file(), (name, path)
    manifest = {'files':[{'path':p,'sha256':digest(ROOT/p)} for p in files],
                'readers':readers, 'reader_engine':'Pandoc native MathML',
                'local_links_checked':True}
    write('checks/artifacts.json', json.dumps(manifest, indent=2)+'\n')
    archive = ROOT/'dist/NT-COLLATZ.zip'
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name in files+['checks/artifacts.json']:
            info = zipfile.ZipInfo('NT-COLLATZ/'+name, date_time=(2026,10,9,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, (ROOT/name).read_bytes())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name in files+['checks/artifacts.json']:
            assert z.read('NT-COLLATZ/'+name) == (ROOT/name).read_bytes()
    print(json.dumps({'readers':readers, 'finite_checks':checks,
                      'zip_sha256':digest(archive)}, indent=2))


if __name__ == '__main__':
    main()
