"""Original reproducible illustration for LIE-TG-10, equation (6.5).

CC0. Written by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026.
Exact parametric curves are sampled for display; no numerical plot proves a theorem.
Run with Python, NumPy and Matplotlib. Outputs are adjacent to this source.
"""
from pathlib import Path
import struct
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
navy,teal,orange='#203b60','#007d78','#b64c15'
plt.rcParams.update({'font.size':18,'axes.titlesize':21,'axes.labelsize':19,
                     'legend.fontsize':16,'xtick.labelsize':16,'ytick.labelsize':16,
                     'font.family':'DejaVu Sans'})
s=np.linspace(-1.7,1.7,1801)
fig,axes=plt.subplots(2,1,figsize=(6.5,8.6),layout='constrained')
for ax,t,title in zip(axes,[0.45,1.5],['Regular offset: t = 0.45','Cusps in the projection: t = 1.5']):
    ax.plot(s,s*s/2,color=navy,lw=2.6,label='Original parabola')
    speed=np.sqrt(1+s*s)
    ax.plot(s-t*s/speed,s*s/2+t/speed,color=teal,lw=3,label='Normal offset')
    for a in [-1.35,-0.9,-0.4,0.4,0.9,1.35]:
        normal=np.array([-a,1])/np.sqrt(1+a*a)
        base=np.array([a,a*a/2])
        ax.plot([base[0],base[0]+t*normal[0]],
                [base[1],base[1]+t*normal[1]],color='#8c98a5',lw=1.15,alpha=.65)
    if t>1:
        a=np.sqrt(t**(2/3)-1)
        for b in [-a,a]:
            speed=np.sqrt(1+b*b)
            ax.scatter([b-t*b/speed],[b*b/2+t/speed],s=75,color=orange,zorder=5)
        ax.text(.47,1.54,'Cusps',color=orange,fontsize=18)
    ax.set_title(title,pad=12)
    ax.set_xlabel('New horizontal coordinate X')
    ax.set_ylabel('Height Z')
    ax.set_xlim(-1.85,1.85);ax.set_ylim(-.12,2.45)
    ax.set_aspect('equal',adjustable='box')
    ax.grid(alpha=.16)
    ax.spines[['right','top']].set_visible(False)
    if t<1: ax.legend(loc='upper left',frameon=False)
png=out/'parallel-curves.png'
fig.savefig(png,dpi=160,metadata={})
fig.savefig(out/'parallel-curves.svg',metadata={'Creator':'Open Mathematics Courses','Date':None})
plt.close(fig)
# Publish no software, path, timestamp or EXIF metadata in the raster asset.
data=png.read_bytes();kept=[data[:8]];pos=8
while pos<len(data):
    size,kind=struct.unpack('>I4s',data[pos:pos+8]);end=pos+12+size
    if kind not in {b'tEXt',b'zTXt',b'iTXt',b'eXIf',b'tIME'}:kept.append(data[pos:end])
    pos=end
png.write_bytes(b''.join(kept))
print('Generated the exact normal-offset illustration.')
