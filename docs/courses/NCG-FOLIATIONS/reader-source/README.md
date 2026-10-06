# NCG lesson readers

The lesson sources and static readers are kept together in this course folder.
The companion readings provide the algebra, topology, analysis and measure
theory used by the foliation lessons. The finite-kernel reading proves finite
upward convergence, measurable bounded-kernel densities and positive s-finite
integration, with its ordinary measure-theory assumptions stated explicitly.

Use Python 3.10 or newer to refresh the readers in a checkout of the programme:

```text
python reader-source/sync_lessons.py --companions --kernel --lessons k-theory-of-the-leaf-space transverse-measures-of-foliations
```

Run that command from this course folder, or supply `--course` with its path.
`--lessons` selects the core lessons to render. Sources and pages keep their
existing section aliases so links to earlier results remain usable. The
renderer preserves the TeX expression in each formula's `data-tex` attribute.
MathJax restores the requested section after formula layout finishes.

Serve the repository's `docs` directory with an HTTP server. Links to other
programme lessons use their current paths in that same checkout. The CSS,
MathJax and CommonMark dependencies are already included; no CDN is needed.

Original lesson text and renderer code retain their CC0 terms. The existing
spectral-calculus reading retains GFDL 1.2 with its complete title, history,
rights and licence notices. The Local tools reading gives a complete CC0 partition-of-unity proof
in Section 3, with Brenner and Wikiversity credited as further reading.
The K-theory Lemma 7.7 adaptation retains CC BY 4.0. Consult the
source files and component notices for their attribution. New original text
does not change any inherited licence.

Figure generators, editable SVGs, fonts and complete software/font notices
accompany the figures in `reproduction` and `finite-kernel-prerequisite`.
Their README files give the reproduction commands. Fonts and software retain
their own terms.

Original reader adapter: GPT-6.1 Sol (OpenAI), CC0 1.0. MathJax: Apache License
2.0; markdown-it-py and mdurl: MIT. Full dependency notices accompany the code.
