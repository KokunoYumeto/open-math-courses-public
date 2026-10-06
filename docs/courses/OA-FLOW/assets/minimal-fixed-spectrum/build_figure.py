"""Exact finite model checks and reproducible original two-M2 diagram (CC0-1.0)."""
from pathlib import Path
import json, hashlib
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np

E=Path(__file__).resolve().parent
I=s.I
D=s.diag(1,-1);W=s.diag(1,I);e=s.diag(1,0)
basis=[]
for block in range(2):
 for row in range(2):
  for col in range(2):
   a=s.zeros(2);b=s.zeros(2);(a if block==0 else b)[row,col]=1;basis.append((a,b))
def vector(ab):return s.Matrix(list(ab[0])+list(ab[1]))
def alpha(ab):a,b=ab;return D*b*D,a
def beta(ab):a,b=ab;return W*b*W.conjugate().T,W.conjugate().T*a*W
A=s.Matrix.hstack(*[vector(alpha(v)) for v in basis]);B=s.Matrix.hstack(*[vector(beta(v)) for v in basis])
identity=s.eye(8)
assert W**2==D and W.conjugate().T*D==W and D*W==W.conjugate().T
assert W==(1+I)*s.eye(2)/2+(1-I)*D/2
assert A**4==identity and A**2!=identity
assert B**2==identity and B!=identity
assert (A-identity).nullspace()==[vector((e,e)),vector((s.eye(2)-e,s.eye(2)-e))]
assert A.eigenvals()=={1:2,-1:2,I:2,-I:2}
assert B.eigenvals()=={1:4,-1:4}
for pair in basis:
 assert beta(pair)==tuple(s.simplify(W.conjugate().T*x*W) for x in alpha(pair))
assert alpha((e,e))==(e,e)
for n in range(4):
 assert W**(2*n)==D**n
 assert alpha((W**n,W**n))==(W**n,W**n)
data={'description':'Exact symbolic verification, not numerical sampling of arbitrary-group spectra.',
 'basis':'(E11,0),(E12,0),(E21,0),(E22,0),(0,E11),(0,E12),(0,E21),(0,E22)',
 'D':str(D),'W':str(W),'e_in_each_summand':str(e),'alpha_generator':str(A),'beta_generator':str(B),
 'alpha_characteristic_polynomial':str(s.factor(A.charpoly().as_expr())),
 'beta_characteristic_polynomial':str(s.factor(B.charpoly().as_expr())),
 'alpha_eigenvalues_with_multiplicity':{str(k):v for k,v in A.eigenvals().items()},
 'beta_eigenvalues_with_multiplicity':{str(k):v for k,v in B.eigenvals().items()},
 'fixed_algebra_basis':['(E11,E11)','(E22,E22)'],'fixed_projection_corners':['e','1-e','1'],
 'full_exact_checks':['W^2=D','W*D=W and DW=W*','W=(1+i)I/2+(1-i)D/2',
 'alpha^4=id, alpha^2 is not id','beta=Ad(W*,W*) alpha','beta^2=id, beta is not id',
 'fixed space exactly span{(E11,E11),(E22,E22)}','alpha eigenvalues 1,-1,i,-i','beta eigenvalues 1,-1',
 'w extends v and is fixed (powers reduced using W^4=I)'],
 'proof_of_action_spectrum_not_computation':'MF.MODEL uses M9 and the topological identification of the dual of Z with T. The full fixed-projection intersection gives Gamma={1,-1}.',
 'proof_of_kernel':'Integer powers of the exact nonidentity involution beta have kernel 2Z; all odd powers retain the central swap.',
 'passed':True}
(E/'EXACT_MODEL_CHECK.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8',newline='\n')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'L119-original-exact-two-M2-v1'})
fig=plt.figure(figsize=(16,13),facecolor='#f5f7fb')
fig.text(.055,.957,'Cancel the inner even subgroup; keep the central swap',fontsize=25,weight='bold',color='#142b48')
fig.text(.055,.925,r'Exact finite model: $G=\mathbb{Z}$,  $M=M_2(\mathbb{C})\oplus M_2(\mathbb{C})$',fontsize=17,color='#374151')
fig.text(.055,.886,r'$D=\mathrm{diag}(1,-1),\quad W=\mathrm{diag}(1,i),\quad W^2=D,\quad e=(E_{11},E_{11})$',fontsize=18,color='#142b48')

def panel(pos):
 ax=fig.add_axes(pos);ax.set_facecolor('white');ax.set_xticks([]);ax.set_yticks([])
 for sp in ax.spines.values():sp.set_visible(False)
 return ax

ax1=panel([.055,.48,.40,.355]);ax2=panel([.545,.48,.40,.355])
def spectrum(ax,points,title,formula,claim):
 ax.set_xlim(-1.75,1.75);ax.set_ylim(-1.6,1.65);ax.set_aspect('equal')
 ax.add_patch(Circle((0,0),1,fill=False,lw=2,color='#b8c4d3'))
 ax.plot([-1.28,1.28],[0,0],color='#dce2e9',lw=1);ax.plot([0,0],[-1.25,1.25],color='#dce2e9',lw=1)
 ax.text(.98,1.17,'unit circle',ha='center',fontsize=11,color='#657083')
 for x,y,label,color in points:
  ax.scatter([x],[y],s=145,color=color,zorder=3)
  if x:ax.text(x*1.22,y,label,ha='center',va='center',fontsize=18,color=color,weight='bold')
  else:ax.text(x,y*1.2,label,ha='center',va='center',fontsize=18,color=color,weight='bold')
 ax.set_title(title,loc='left',pad=24,fontsize=18,weight='bold',color='#142b48')
 ax.text(.5,-.035,formula,transform=ax.transAxes,ha='center',fontsize=17,color='#142b48')
 ax.text(.5,-.14,claim,transform=ax.transAxes,ha='center',fontsize=14,color='#374151')
blue='#176482';orange='#bb481f'
spectrum(ax1,[(1,0,r'$1$',blue),(-1,0,r'$-1$',blue),(0,1,r'$i$',orange),(0,-1,r'$-i$',orange)],
 'Before cancellation',r'$\alpha_1(a,b)=(DbD^*,a)$',r'$\mathrm{Sp}(\alpha)=\{1,-1,i,-i\}$')
spectrum(ax2,[(1,0,r'$1$',blue),(-1,0,r'$-1$',blue)],
 'After cancellation',r'$\beta_1(a,b)=(WbW^*,W^*aW)$',r'$\mathrm{Sp}(\beta)=\Gamma(\alpha)=\{1,-1\}$')
fig.add_artist(FancyArrowPatch((.46,.659),(.535,.659),transform=fig.transFigure,arrowstyle='-|>',mutation_scale=25,lw=2,color='#546980'))
fig.text(.499,.692,r'$\beta=\mathrm{Ad}(u)\alpha$',ha='center',fontsize=13,color='#142b48')
fig.text(.499,.619,r'$u_n=w_n^*$',ha='center',fontsize=14,color='#142b48')

fig.text(.055,.402,r'$v_{2n}=(D^n,D^n),\qquad w_n=(W^n,W^n),\qquad u_n=(W^{-n},W^{-n})$',fontsize=19,color='#142b48')
fig.text(.055,.368,r'$W^*(v(2\mathbb{Z}))=W^*(w(\mathbb{Z}))=\{(\mathrm{diag}(a,b),\mathrm{diag}(a,b)):a,b\in\mathbb{C}\}\subseteq M^\alpha$',fontsize=16,color='#142b48')

ax3=panel([.055,.105,.42,.22]);ax4=panel([.515,.105,.43,.22])
ax3.text(.045,.85,'The fixed minimal corner',fontsize=17,weight='bold',color='#142b48',transform=ax3.transAxes)
ax3.text(.045,.62,r'$e(a,b)e\ \leftrightarrow\ (a_{11},b_{11})\in\mathbb{C}^2$',fontsize=18,transform=ax3.transAxes,color='#142b48')
ax3.text(.045,.4,r'$\alpha_1^e(z_1,z_2)=(z_2,z_1)$',fontsize=18,transform=ax3.transAxes,color='#142b48')
ax3.text(.045,.17,r'$c_M(e)=1,\qquad eM^\alpha e=\mathbb{C}e$',fontsize=17,transform=ax3.transAxes,color='#142b48')
ax4.set_xlim(-4.8,4.8);ax4.set_ylim(-1,2.5)
ax4.text(.035,.85,r'The exact remaining kernel: $2\mathbb{Z}$',fontsize=17,weight='bold',color='#142b48',transform=ax4.transAxes)
ax4.plot([-4.35,4.35],[.8,.8],color='#bdc7d6',lw=2)
for n in range(-4,5):
 ax4.scatter([n],[.8],s=90,facecolors=blue if n%2==0 else 'white',edgecolors=blue,lw=2,zorder=2)
 ax4.text(n,.37,str(n),ha='center',fontsize=12,color='#374151')
ax4.text(.035,.13,r'$\beta_{2n}=\mathrm{id}$; odd powers still swap the center.',fontsize=14,transform=ax4.transAxes,color='#142b48')

fig.text(.055,.066,'Filled integer points lie in the kernel. Spectral positions and phases are exact; the theorem covers arbitrary LCA groups.',fontsize=11.5,color='#536175')
fig.text(.055,.039,'Proof: L119, MF10–MF16 and M25. Original model and diagram; source context: Takesaki II, Lemma XI.2.14, p. 339.',fontsize=11,color='#536175')
fig.savefig(E/'minimal-fixed-spectrum.png',dpi=150,metadata={'Software':'L119 reproducible original mathematical diagram'})
fig.savefig(E/'minimal-fixed-spectrum.svg',metadata={'Date':'2026-10-05','Creator':'GPT-6 Astra (OpenAI), Ultra; original diagram, CC0-1.0'})
plt.close(fig)
print(json.dumps({'passed':True,'png_sha256':hashlib.sha256((E/'minimal-fixed-spectrum.png').read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256((E/'minimal-fixed-spectrum.svg').read_bytes()).hexdigest(),'png_pixels':[2400,1950]}))
