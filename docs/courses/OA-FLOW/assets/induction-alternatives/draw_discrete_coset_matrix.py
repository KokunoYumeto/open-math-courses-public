"""Original exact coset-matrix illustration, CC0-1.0. Requires matplotlib."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

out=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,7))
fig.patch.set_facecolor('white')
ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
ink,blue,orange='#193247','#176b91','#ae5b12'
ax.text(.4,6.57,'The subgroup unitary appears when translation wraps around',
        fontsize=17,weight='bold',color=ink)
ax.text(.4,6.04,r'$G=\mathbb{Z},\quad H=3\mathbb{Z},\quad N=\mathbb{C},\quad Q=L(3\mathbb{Z})$',
        fontsize=16,color=ink)
centers=[(1.5,3.9),(3.7,3.9),(5.9,3.9)]
for j,(x,y) in enumerate(centers):
    ax.add_patch(Circle((x,y),.47,ec=blue,fc='#ecf5fa',lw=2))
    ax.text(x,y,str(j),ha='center',va='center',fontsize=20,color=ink)
    ax.text(x,y-.86,r'$p_'+str(j)+'$',ha='center',fontsize=15,color=ink)
for i in [0,1]:
    x,y=centers[i]; z,_=centers[i+1]
    ax.add_patch(FancyArrowPatch((x+.49,y),(z-.49,y),arrowstyle='-|>',mutation_scale=17,lw=2,color=blue))
    ax.text((x+z)/2,y+.24,r'$1_Q$',ha='center',fontsize=15,color=blue)
ax.add_patch(FancyArrowPatch((5.77,3.43),(1.63,3.43),connectionstyle='arc3,rad=-.48',
                            arrowstyle='-|>',mutation_scale=17,lw=2,color=orange))
ax.text(3.7,2.13,r'$v_3$',ha='center',fontsize=17,color=orange)
ax.text(3.7,1.77,'coset motion with subgroup coefficients',ha='center',fontsize=12,color=ink)
ax.add_patch(FancyBboxPatch((7.06,2.47),4.3,2.9,boxstyle='round,pad=.15',fc='#f6f8fa',ec='#adb9c2'))
ax.text(9.21,5.03,r'$u_1\ \longmapsto\ U$',ha='center',fontsize=17,color=ink)
entries=[['0','0','v_3'],['1_Q','0','0'],['0','1_Q','0']]
for i,row in enumerate(entries):
    for j,value in enumerate(row):
        ax.text(8.15+j*1.0,4.35-i*.64,'$'+value+'$',ha='center',va='center',
                fontsize=19,color=orange if value=='v_3' else ink)
ax.plot([7.56,7.40,7.40,7.56],[4.73,4.73,2.73,2.73],color=ink,lw=2)
ax.plot([10.83,10.99,10.99,10.83],[4.73,4.73,2.73,2.73],color=ink,lw=2)
ax.text(9.21,1.84,r'$U^3=v_3 I_3$',ha='center',fontsize=21,color=ink)
ax.text(.5,.94,r'$\ell^\infty(\mathbb{Z}/3\mathbb{Z})\rtimes\mathbb{Z}\ \cong\ M_3(L(3\mathbb{Z}))$',
        fontsize=19,color=ink)
ax.text(.5,.37,'Rows are destination cosets; columns are starting cosets. Every displayed entry is exact.',
        fontsize=12,color=ink)
fig.subplots_adjust(0,0,1,1)
fig.savefig(out/'discrete-coset-matrix.svg',facecolor='white')
fig.savefig(out/'discrete-coset-matrix.png',dpi=220,facecolor='white')
plt.close(fig)
# The exponents refer to powers of v_3. Exact monomial-matrix multiplication.
U={(1,0):0,(2,1):0,(0,2):1}
def multiply(A,B):
    ans={}
    for (i,k),a in A.items():
        for (l,j),b in B.items():
            if k==l:
                assert (i,j) not in ans
                ans[i,j]=a+b
    return ans
cube=multiply(multiply(U,U),U)
assert cube=={(i,i):1 for i in range(3)}
report={'group':'Z','subgroup':'3Z','representatives':[0,1,2],
        'generator_entries':[{'row':i,'column':j,'v3_exponent':e} for (i,j),e in U.items()],
        'cube_entries':[{'row':i,'column':j,'v3_exponent':e} for (i,j),e in cube.items()],
        'check':'U^3=v3 I3 exactly'}
(out/'discrete-coset-matrix-data.json').write_text(json.dumps(report,indent=2)+'\n')
print(out/'discrete-coset-matrix.png')
