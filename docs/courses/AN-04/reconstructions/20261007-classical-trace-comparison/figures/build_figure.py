"""Sample the exact functions in VP33 and Example 4; no schematic data."""
from pathlib import Path
import math
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="610" viewBox="0 0 1120 610">','<rect width="1120" height="610" fill="white"/>']
def text(x,y,s,size=14,color='#17324d',anchor='start',weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>')
def line(x1,y1,x2,y2,color='#d7e0e7',width=1,extra=''):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>')
def curve(fun,lo,hi,xx,yy,color):
    pts=[(xx(lo+(hi-lo)*k/400),yy(fun(lo+(hi-lo)*k/400))) for k in range(401)]
    d='M'+' L'.join(f'{x:.3f},{y:.3f}' for x,y in pts)
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"/>')
text(60,36,'A lower-order correction can have a nonzero limit',20,weight='bold')
text(635,36,'A smooth trace does not remove the normal cusp',19,weight='bold')
text(60,68,'η > 0; imaginary part of the lower left jet entry')
text(635,68,'Exact normal Fourier factor; t = output − input normal')
xx=lambda t:90+(t-1)*45
yy=lambda t:420-750*t
for t in [1,2,4,6,8,10]:
    line(xx(t),100,xx(t),420);text(xx(t),443,str(t),anchor='middle')
for t in [0,.1,.2,.3,.4]:
    line(90,yy(t),495,yy(t));text(78,yy(t)+5,str(t),anchor='end')
line(90,yy(.25),495,yy(.25),'#718096',1.5,'stroke-dasharray="6 5"')
delta=lambda t:(math.sqrt(t*t+t+1)-t)/2
curve(delta,1,10,xx,yy,'#196eaa')
curve(lambda t:delta(t)/t,1,10,xx,yy,'#bc5700')
text(302,473,'tangential frequency η',anchor='middle')
text(60,512,'Blue: Δ(η) = (√(η² + η + 1) − η)/2 → 1/4.',13,color='#196eaa')
text(60,539,'Orange: Δ(η)/η → 0 after the jet weight is removed.',13,color='#bc5700')
xx=lambda t:850+66*t
yy=lambda t:420-580*t
for t in [-3,-2,-1,0,1,2,3]:
    line(xx(t),102,xx(t),420);text(xx(t),443,str(t),anchor='middle')
for t in [0,.25,.5]:
    line(652,yy(t),1048,yy(t));text(640,yy(t)+5,str(t),anchor='end')
curve(lambda t:math.exp(-abs(t))/2,-3,3,xx,yy,'#196eaa')
parts.append(f'<circle cx="850" cy="{yy(.5)}" r="4" fill="#196eaa"/>')
text(720,107,'left slope +1/2',13)
text(898,107,'right slope −1/2',13)
text(850,473,'normal difference t',anchor='middle')
text(635,512,'Kernel factor: exp(−|t|)/2; positive trace value: 1/2.',13)
text(635,539,'A compact tangential multiplier makes that trace smoothing.',13)
text(560,581,'VP33 and Examples 1, 4. Curves sample exact formulas; the proofs establish the limits and derivative jump.',13,anchor='middle')
parts.append('</svg>')
Path(__file__).with_name('classical-trace-comparison.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
