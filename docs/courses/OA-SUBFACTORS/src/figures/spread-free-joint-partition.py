"""Reproduce Figure71.2 with exact masses and constants; positions are schematic.

Proof: Lesson71.5–71.6 and Example71.3, equations71.16–71.26.
Problem source: Sorin Popa, Classification of amenable subfactors of type II,
Theorem4.2.2, printed213–214. The capped-log estimate is proved in the lesson.
Original exposition by GPT-6.1 Sol (OpenAI), Ultra, CC0 1.0.
"""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="980" height="1050" viewBox="0 0 980 1050" role="img" aria-labelledby="title desc">
<title id="title">Joint distance controls logarithmic partitions independently of spread</title>
<desc id="desc">The actual pair weights are w alpha times v gamma. Capped logarithms yield the bound C w times one plus norm kappa times J joint divided by c. A three-atom diagnostic has conditional rare-branch weights one half, arbitrarily large ratio R, and normalized joint error one over10000001.</desc>
<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#182d47}.title{font-size:29px;font-weight:700}.head{font-size:24px;font-weight:700}.body{font-size:21px}.small{font-size:19px}.formula{font-size:23px}.label{font-size:20px;font-weight:600}.box{fill:#edf4ff;stroke:#506b8c;stroke-width:2}.green{fill:#edf8f1;stroke:#527966;stroke-width:2}.orange{fill:#fff5e8;stroke:#956d38;stroke-width:2}.edge{stroke:#416990;stroke-width:3;fill:none}</style>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#416990"/></marker></defs>
<rect width="980" height="1050" fill="#fbfcff"/>
''']
def text(x,y,s,cls='body',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def box(x,y,w,h,cls='box'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" class="{cls}"/>')
text(35,46,'From actual joint distance to a logarithmic partition','title')
box(30,72,920,235)
text(52,107,'Actual centers and asymmetric pair weights','head')
text(52,145,'C = Z(S),  F = Z(R),  D₀ = C ∨ F;   β = P₀ζ')
text(52,181,'wα = P₀(qα),  vγ = Pκ(qγ);   pair weight = wα vγ')
text(52,218,'Σ wα = Σ vγ = 1;   vγ ≤ ‖κ‖ wγ   [71.18]')
text(52,263,'Jjoint = ‖ζ − β‖₁,τ;   c = τ(ζ) > 0   [71.16]','formula')
box(30,331,920,194,'green')
text(52,367,'Cap the log separation before taking its mean','head')
text(52,410,'a πw(a,b) ≤ Cw |a − b|;   Cw = 1 / (1 − e⁻ʷ)   [71.19]','formula')
text(52,449,'πw = min(1, |log a − log b| / w) for a,b > 0')
text(52,487,'One-zero pair: πw = 1.   Both-zero pair: πw = 0.')
box(30,549,920,306)
text(52,585,'Finite diagnostic: a rare fiber, with branch weights ½ and ½','head')
text(52,621,'η = 10⁻⁷,  R ≥ 2,  μ = 2η / (R − 1),  K = 256   [71.23]')
box(65,644,255,90,'green')
text(192,681,'Background: mass 1 − μ','label','middle')
text(192,715,'ζ = K;   P₀ζ = K','body','middle')
box(425,644,200,90);box(685,644,200,90)
text(525,680,'Mass μ/2;  ζ = K','label','middle')
text(785,680,'Mass μ/2;  ζ = KR','label','middle')
text(525,713,'Branch weight ½','small','middle')
text(785,713,'Branch weight ½','small','middle')
parts.append('<path d="M635,660 L674,660" class="edge" marker-end="url(#arrow)"/><path d="M675,704 L635,704" class="edge" marker-end="url(#arrow)"/>')
text(655,761,'Rare fiber: P₀ζ = K(1 + R)/2; each pair weight = ¼','small','middle')
text(52,807,'c = K(1 + η),  Jjoint = Kη,  Jjoint/c = 1/10000001   [71.24]')
text(52,836,'Small μ is a fiber mass; no conditional weight tends to zero.','small')
box(30,879,920,143,'orange')
text(52,915,'A bound that does not contain W = log R','head')
text(52,956,'w = log(257/256):  Cw = 257;   B ≤ 514/10000001 < 1/1024','formula')
text(52,991,'Finite diagnostic only. Actual projection and coefficient inputs stay separate.','small')
parts.append('</svg>\n')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts),encoding='utf-8')
