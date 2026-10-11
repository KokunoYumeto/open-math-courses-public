"""Reproduce the final lesson's exact maps and numerical heat-density figure."""
from pathlib import Path
import html,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

COURSE=Path(__file__).resolve().parents[1]
F=COURSE/'figures'

def svg(name,title,desc,body,height=780):
    doc=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc)}</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#256773"/></marker></defs>
<rect width="1200" height="{height}" fill="#f4f7f5"/><g font-family="Arial,sans-serif" fill="#193d46">
{body}</g></svg>'''
    (F/name).write_text(doc,encoding='utf8')

def build():
    F.mkdir(exist_ok=True)
    body='<text x="38" y="48" font-size="28" font-weight="bold">Physical rectangle and compatible holonomies</text>'
    body+='<text x="38" y="88" font-size="20">SU(2); κ(X,Y) = −tr(XY); L₁,L₂,g₂ &gt; 0; every boundary link is integrated.</text>'
    for x0,n,label in [(90,2,'Grid Γ₁'),(760,4,'Grid Γ₂')]:
        body+=f'<text x="{x0+85}" y="142" font-size="24">{label}</text>'
        for j in range(n+1):
            x=x0+300*j/n;y=180+200*j/n
            body+=f'<path d="M{x} 180 V380 M{x0} {y} H{x0+300}" stroke="#26776e" stroke-width="2"/>'
        body+=f'<text x="{x0+132}" y="418" font-size="22">L₁</text><text x="{x0-40}" y="288" font-size="22">L₂</text>'
        body+=f'<text x="{x0}" y="460" font-size="20">Face area = L₁L₂/{n*n}</text>'
    body+='<path d="M726 265 H432" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>'
    body+='<text x="476" y="235" font-size="22">π₁: compose edges</text>'
    body+='<text x="458" y="309" font-size="20">U = U₂U₁</text>'
    body+='<text x="422" y="349" font-size="20">(π₁)∗ μ₂ = μ₁</text>'
    body+='<rect x="40" y="500" width="1120" height="211" rx="12" fill="white" stroke="#a4bdbe"/>'
    body+='<text x="65" y="540" font-size="22">t_f = g₂²|f|/4; chord integration adds the two original face times.</text>'
    body+='<text x="65" y="582" font-size="22">Continuous connections A</text>'
    body+='<path d="M425 575 H735" stroke="#256773" stroke-width="2" marker-end="url(#arrow)"/>'
    body+='<text x="523" y="562" font-size="19">Hol(A)</text>'
    body+='<text x="766" y="582" font-size="22">Compatible space X∞</text>'
    body+='<text x="65" y="628" font-size="20">The smooth image is dense and lies in E = {W_m / a_m → 0}, with μ∞(E) = 0.</text>'
    body+='<text x="65" y="674" font-size="20">Exact loop law: E[tr(H∂R)/2] = exp(−3g₂² area(R)/8).</text>'
    body+='<text x="38" y="754" font-size="18">Schematic physical lengths; exact maps: GP.1–GP.13 and DP.16–DP.19. No arbitrary-path extension.</text>'
    svg('f18-holonomy-construction.svg','Physical rectangle and compatible holonomies',
        'Two successive dyadic rectangle grids and their edge-composition projection. The holonomy map sends continuous connections into the compatible space, whose constructed probability gives its image a Borel null set. Lengths are schematic; all constants and domains are printed.',body)

    plt.rcParams.update({'svg.hashsalt':'ym-f18-cube','font.family':'DejaVu Sans','font.size':13})
    times=np.array([1/7,2/9,3/11,4/13,5/17,6/19])
    theta=np.linspace(-np.pi,np.pi,1201)
    def heat(t,x):
        return np.sqrt(np.pi/t)*sum(np.exp(-(x+2*np.pi*k)**2/(4*t)) for k in range(-12,13))
    total=float(times.sum());z=float(heat(total,0.0));a=float(times[0])
    ind=heat(a,theta);cube=ind*heat(total-a,-theta)/z
    fig,ax=plt.subplots(figsize=(12,7.8))
    ax.plot(theta,cube,label='Cube face X₋: pₜ(θ) pₜᵣ(−θ) / pₜ₊ₜᵣ(0)',lw=2.8,color='#26776e')
    ax.plot(theta,ind,label='Independent heat face: pₜ(θ)',lw=2.5,ls='--',color='#ac632c')
    ax.set(xlabel='Angle θ (radians)',ylabel='Density relative to dθ / (2π)',xlim=(-np.pi,np.pi),ylim=(0,5.7))
    ax.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['−π','−π/2','0','π/2','π'])
    ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=12)
    fig.suptitle('A face law retains the closed-surface constraint',fontsize=20,y=.97)
    fig.text(.12,.885,'Times (X₋,X₊,Y₋,Y₊,Z₋,Z₊) = (1/7, 2/9, 3/11, 4/13, 5/17, 6/19)',fontsize=13)
    fig.text(.12,.077,'t = t(X₋); tᵣ = sum of the other five times. All six faces obey ∏ H_f = 1.',fontsize=12)
    fig.text(.12,.035,'Numerical evaluation of the exact image formula; proofs and error bounds: CF.8–CF.13, C26–C42.',fontsize=11)
    fig.subplots_adjust(top=.83,bottom=.18,left=.12,right=.97)
    fig.savefig(F/'f18-cube-marginal.svg',metadata={'Date':None})
    fig.savefig(F/'f18-cube-marginal.png',dpi=140,metadata={'Software':'YM-GAUGE reproducible figure'})
    plt.close(fig)
    (F/'f18-cube-parameters.json').write_text(json.dumps({'times_exact':['1/7','2/9','3/11','4/13','5/17','6/19'],
      'angle_samples':1201,'image_indices':[-12,12],'partition_numerical':z,
      'meaning':'Numerical image-series evaluation of C26 and C35; exact proofs and Fourier tails in CF.8–CF.13.'},indent=2)+'\n',encoding='utf8')

    body='<text x="38" y="48" font-size="28" font-weight="bold">Follow the mathematical map</text>'
    body+='<text x="38" y="88" font-size="20">Each row has its own stated model and domain; these rows are not one commuting diagram.</text>'
    rows=[
      ('Constrained Cauchy data','evolution','Classical connection','Unit 9: energy, gauge and propagation estimates'),
      ('Finite joint measure','projection / integration','Marginal probability','F18.4–F18.6: determinant, sources and full partition'),
      ('Fine graph probability','edge composition','Coarse graph probability','GP.5–GP.11: exact heat convolution and compatible limit'),
      ('Euclidean correlations','reflection quotient','Physical Hilbert space','Unit 17: proved free-field quotient and reconstruction'),
      ('Observable vector ψ','spectral measure','ρψ and its correlation','Unit 16 and F18.21: support of the actual vector')
    ]
    for j,(left,arrow,right,loc) in enumerate(rows):
        y=120+118*j
        body+=f'<rect x="38" y="{y}" width="1124" height="102" rx="9" fill="white" stroke="#a4bdbe"/>'
        body+=f'<text x="60" y="{y+36}" font-size="22">{html.escape(left)}</text>'
        body+=f'<text x="772" y="{y+36}" font-size="22">{html.escape(right)}</text>'
        body+=f'<path d="M426 {y+35} H736" stroke="#256773" stroke-width="2" marker-end="url(#arrow)"/>'
        body+=f'<text x="465" y="{y+22}" font-size="18">{html.escape(arrow)}</text>'
        body+=f'<text x="60" y="{y+78}" font-size="18">{html.escape(loc)}</text>'
    body+='<text x="38" y="753" font-size="19">A claim transfers through the displayed map with its hypotheses, observables and constants intact.</text>'
    svg('f18-method-maps.svg','The maps connecting course constructions',
        'Five rows give precise source and target objects, their mathematical maps, and proof locators: classical evolution, Gaussian projection, graph composition, reflection quotient and spectral measure.',body)

if __name__=='__main__':build()
