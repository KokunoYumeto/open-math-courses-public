"""Original CC0 lattice-tree illustration for lesson 11.
Run this script beside its outputs with Python and Matplotlib.
The drawing uses the exact ball proved in Theorem 11.3; coordinates are schematic.
"""
from pathlib import Path
import hashlib, json, re, struct
from fractions import Fraction
from collections import deque
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
matrices={'Lstar':[[1,0],[0,1]],'L0':[[1,0],[0,2]],'L1':[[1,0],[1,2]],'Linf':[[2,0],[0,1]]}
for a in range(4): matrices['A'+str(a)]=[[1,0],[a,4]]
for b in (0,2): matrices['B'+str(b)]=[[4,b],[0,1]]
edges=[('Lstar',x) for x in ('L0','L1','Linf')]+[('L0','A0'),('L0','A2'),('L1','A1'),('L1','A3'),('Linf','B0'),('Linf','B2')]
def det(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def val2(x):
    x=Fraction(x)
    if not x: return 10**6
    n,d=abs(x.numerator),x.denominator
    v=0
    while n%2==0: n//=2; v+=1
    while d%2==0: d//=2; v-=1
    return v

def relative(P,Q):
    dd=det(P)
    inv=[[Fraction(P[1][1],dd),Fraction(-P[0][1],dd)],[Fraction(-P[1][0],dd),Fraction(P[0][0],dd)]]
    return [[sum(inv[i][k]*Q[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def distance(P,Q):
    R=relative(P,Q)
    return val2(det(R))-2*min(val2(x) for row in R for x in row)
graph={x:[] for x in matrices}
for x,y in edges: graph[x].append(y); graph[y].append(x)
checked=[]
for source in matrices:
    d={source:0}; queue=deque([source])
    while queue:
        x=queue.popleft()
        for y in graph[x]:
            if y not in d: d[y]=d[x]+1; queue.append(y)
    assert len(d)==10
    for target in matrices:
        assert distance(matrices[source],matrices[target])==d[target]
        checked.append({'from':source,'to':target,'distance':d[target]})
assert len(edges)==9
for name,M in matrices.items():
    assert min(val2(x) for row in M for x in row)==0
    assert val2(det(M))==distance(matrices['Lstar'],M)
for parent,child in edges:
    R=relative(matrices[parent],matrices[child])
    assert all(val2(x)>=0 for row in R for x in row)
    assert val2(det(R))==1

positions={'Lstar':(330,335),'L0':(110,220),'L1':(330,220),'Linf':(550,220),'A0':(55,95),'A2':(165,95),'A1':(275,95),'A3':(385,95),'B0':(495,95),'B2':(605,95)}
labels={'Lstar':r'$[L_*]$','L0':r'$[L_0]$','L1':r'$[L_1]$','Linf':r'$[L_\infty]$'}
labels.update({x:r'$['+x[0]+'_'+x[1:]+r']$' for x in matrices if x.startswith(('A','B'))})
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(6.6,4.25),dpi=200)
fig.subplots_adjust(0,0,1,1)
ax.set(xlim=(0,660),ylim=(0,425)); ax.axis('off')
fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#ffffff')
for x,y in edges:
    px,py=positions[x]; qx,qy=positions[y]
    ax.plot([px,qx],[py,qy],color='#536375',lw=1.8,zorder=1)
for name,(x,y) in positions.items():
    height=distance(matrices['Lstar'],matrices[name])
    colour='#1f5f91' if height%2==0 else '#a45c14'
    ax.scatter([x],[y],s=125,color=colour,zorder=3)
    ax.text(x,y+18 if height<2 else y-20,labels[name],ha='center',va='bottom' if height<2 else 'top',fontsize=22,color='#152636',bbox={'facecolor':'white','edgecolor':'none','pad':1},zorder=4)
ax.text(330,404,'Tree over Q₂: the ball of radius 2',ha='center',va='center',fontsize=16.5,color='#152636')
for x,colour,text in [(150,'#1f5f91','even height'),(415,'#a45c14','odd height')]:
    ax.scatter([x-25],[26],s=70,color=colour)
    ax.text(x,26,text,fontsize=14.5,va='center',color='#152636')
fig.savefig(out/'tree-q2.png',dpi=200,metadata={'Software':None})
fig.savefig(out/'tree-q2.svg',metadata={'Date':None,'Creator':None,'Title':'The radius-two lattice tree over Q2'})
plt.close(fig)
svg=(out/'tree-q2.svg').read_text(encoding='utf-8')
svg=re.sub(r'<metadata>.*?</metadata>','',svg,flags=re.S)
(out/'tree-q2.svg').write_text(svg,encoding='utf-8',newline='\n')
# Strip incidental text metadata from the raster while keeping pixels unchanged.
data=(out/'tree-q2.png').read_bytes(); chunks=[data[:8]]; offset=8
while offset<len(data):
    size,kind=struct.unpack('>I4s',data[offset:offset+8]); end=offset+size+12
    if kind not in {b'tEXt',b'zTXt',b'iTXt',b'eXIf',b'tIME'}: chunks.append(data[offset:end])
    offset=end
(out/'tree-q2.png').write_bytes(b''.join(chunks))
receipt={'figure':'11.1','activity':'author exact arithmetic check, not independent review','field':'Q2','ring':'Z2','uniformizer':2,'q':2,'vertices':10,'edges':9,'radius':2,'matrix_columns':matrices,'edges_by_id':edges,'all_ordered_pair_distances':checked,'checks':{'100_pairwise_distances_match_elementary_divisors':True,'all_9_edges_are_index_2_inclusions':True,'all_representatives_normalized':True},'schematic':'Only drawing coordinates are schematic; displayed vertices and adjacency are exact. Boundary vertices have further children outside the ball.','proof_locator':'Lesson 11, Theorem 11.3, equations (3)-(5); Proposition 11.5 for parity colours','sha256':{name:hashlib.sha256((out/name).read_bytes()).hexdigest().upper() for name in ['tree-q2.png','tree-q2.svg']}}
(out/'tree-q2-check.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'vertices':10,'edges':9,'ordered_pair_distances':len(checked),'png':receipt['sha256']['tree-q2.png'],'svg':receipt['sha256']['tree-q2.svg']}))
