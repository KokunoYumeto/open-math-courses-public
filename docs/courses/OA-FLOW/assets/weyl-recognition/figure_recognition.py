"""Original exact Z5 multiplicity illustration; CC0 expression."""
from pathlib import Path
import argparse,json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'weyl-recognition-Z5-multiplicity-20261005'})
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'assets');args=ap.parse_args();args.output.mkdir(exist_ok=True)
n=5;k=2;omega=np.exp(2j*np.pi/n)
E=np.eye(n);I=np.eye(k);U=np.kron(np.roll(E,1,axis=0),I)
V=[np.kron(np.diag([omega**(-q*r) for r in range(n)]),I) for q in range(n)]
P=[sum(omega**(q*r)*V[q] for q in range(n))/n for r in range(n)]
T={(r,v):np.kron(np.outer(E[:,r],E[:,v]),I) for r in range(n) for v in range(n)}
Q=np.kron(E,np.diag([1,0]))
res={}
res['Weyl_U1_Vk']=max(np.max(np.abs(U@V[q]@U.conj().T-omega**q*V[q])) for q in range(n))
res['selectors']=max(np.max(np.abs(P[r]-T[r,r])) for r in range(n))
res['matrix_units']=max(np.max(np.abs(T[r,v]@T[z,w]-(T[r,w] if v==z else np.zeros((10,10))))) for r in range(n) for v in range(n) for z in range(n) for w in range(n))
res['R22']=max(np.max(np.abs(P[r]@np.linalg.matrix_power(U,(r-v)%n)-T[r,v])) for r in range(n) for v in range(n))
assert max(res.values())<1e-12
fig=plt.figure(figsize=(14,8.2),dpi=200,facecolor='#fbfcfe')
fig.text(.035,.947,'Which projection recovers the multiplicity?',fontsize=24,weight='bold',color='#14263d')
fig.text(.035,.900,'Exact model: G = Z/5Z, H = C⁵ ⊗ C²; counting Haar measure',fontsize=15,color='#36465b')
ax1=fig.add_axes([.045,.36,.41,.48]);ax2=fig.add_axes([.525,.36,.41,.48])
blue='#136aab';orange='#cf6b21'
for ax,kind in [(ax1,'generated'),(ax2,'commutant')]:
 ax.set_xlim(-.95,2.0);ax.set_ylim(-.8,5.35);ax.axis('off')
 ax.text(-.82,5.05,'A. Generated-algebra projection' if kind=='generated' else 'B. Commutant projection',fontsize=16,weight='bold',color='#14263d')
 for a in range(2):ax.text(a,4.52,f'a = {a}',ha='center',fontsize=13)
 for r in range(5):
  y=4-r
  ax.text(-.55,y,f'r = {r}',ha='right',va='center',fontsize=13)
  for a in range(2):
   chosen=(r==0 if kind=='generated' else a==0)
   c=(blue if kind=='generated' else orange) if chosen else '#dee5ee'
   ax.add_patch(Rectangle((a-.25,y-.20),.50,.40,facecolor=c,edgecolor='white',lw=1.5))
   ax.text(a,y,f'δ{r} ⊗ f{a}',ha='center',va='center',fontsize=10,color='white' if chosen else '#394a60')
 if kind=='generated':
  ax.text(.2,-.48,'P₀ = E₀₀ ⊗ I₂: range dimension 2',ha='center',fontsize=14,color=blue)
 else:
  ax.text(.25,-.48,'Q = I₅ ⊗ q: range dimension 5',ha='center',fontsize=14,color=orange)
fig.text(.058,.316,'P₀ A P₀ = C P₀;     A = M₅(C) ⊗ I₂',fontsize=15,color=blue)
fig.text(.538,.316,'Q A′ Q = C Q;     A′ = I₅ ⊗ M₂(C)',fontsize=15,color=orange)
fig.text(.045,.253,'C. Matrix units carry the two-dimensional range through all five rows',fontsize=16,weight='bold',color='#14263d')
fig.text(.060,.191,'Tᵣ₀(δ₀ ⊗ fₐ) = δᵣ ⊗ fₐ',fontsize=17,color=blue)
fig.text(.535,.191,'W: C⁵ ⊗ (P₀H) → H is onto and isometric',fontsize=15,color='#14263d')
fig.text(.060,.135,'U₁ δᵣ = δᵣ₊₁;     Vₖ δᵣ = exp(−2πikr/5) δᵣ',fontsize=15,color='#14263d')
fig.text(.060,.075,'U₁VₖU₁* = exp(2πik/5)Vₖ. Indices are modulo five; neither projection is rank one on H.',fontsize=13,color='#36465b')
fig.savefig(args.output/'weyl-recognition.png',dpi=200,metadata={'Software':'Original reproducible OA-FLOW figure'})
fig.savefig(args.output/'weyl-recognition.svg',metadata={'Date':None})
plt.close(fig)
data={'group':'Z/5Z','H_dimension':10,'multiplicity_dimension':2,'generated_minimal_projection_range_dimension':2,'commutant_minimal_projection_range_dimension':5,'counting_Haar':1,'dual_Haar_per_point':.2,'U1_basis_shift':'+1','Vk_phase':'exp(-2*pi*i*k*r/5)','basis_order':[[r,a] for r in range(5) for a in range(2)],'matrix_unit_products_checked':625,'exact_proof':'Finite geometric sum and rank-one tensor formulas in R22 and caption; floating residuals are supplementary checks.','max_entry_residuals':res}
(args.output/'weyl-recognition-data.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'pixels':[2800,1640],'checks':res}))
