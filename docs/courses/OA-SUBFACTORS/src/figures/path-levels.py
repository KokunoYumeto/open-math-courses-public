"""Original, reproducible diagram of the A4 path model; standard library only."""
from pathlib import Path
from html import escape

OUT=Path(__file__).with_suffix('.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="640" viewBox="0 0 500 640" role="img" aria-labelledby="title desc">',
       '<title id="title">A4 vertex weights and the first six path levels</title>',
       '<desc id="desc">A four-vertex line rooted at zero, with weights one, phi, phi, one. Below it, a Bratteli diagram displays path counts at levels zero through five. Each node is a matrix block whose size is the displayed count.</desc>',
       '<rect width="500" height="640" fill="white"/>']
def text(x,y,s,size=16,anchor='middle',fill='#16324f'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" text-anchor="{anchor}" fill="{fill}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#a6b5c5',width=2):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
def circle(x,y,s,fill='#e9f2fa'):
    parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{fill}" stroke="#315c83" stroke-width="1.5"/>')
    text(x,y+6,s,18)

xs=[85,195,305,415]
text(250,28,'A₄ path model: δ = φ, λ = φ⁻²',20)
text(250,53,'φ = (1 + √5)/2',16)
for j in range(3):line(xs[j],89,xs[j+1],89,'#315c83',2)
for j,weight in enumerate(['1','φ','φ','1']):
    circle(xs[j],89,str(j))
    text(xs[j],125,'μ = '+weight)
text(250,155,'Each node below represents Mₖ; its label is k.',15)
text(250,176,'Edges record extension by one graph edge.',15)
counts=[[1,0,0,0],[0,1,0,0],[1,0,1,0],[0,2,0,1],[2,0,3,0],[0,5,0,3]]
ys=[222+58*n for n in range(6)]
for n in range(5):
    for j,a in enumerate(counts[n]):
        if a:
            for k,b in enumerate(counts[n+1]):
                if b and abs(j-k)==1:line(xs[j],ys[n],xs[k],ys[n+1])
for n,row in enumerate(counts):
    text(18,ys[n]+5,str(n),16)
    for j,a in enumerate(row):
        if a:circle(xs[j],ys[n],str(a))
text(20,202,'n',15)
text(250,564,'Minimal-projection trace at vertex j, level n:',15)
text(250,588,'τ([p,p]) = φ⁻ⁿ μ(j)',19)
text(250,615,'Propositions 9.1–9.2 and Theorem 9.4.',15)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT.name)
