"""Original finite double-duality sign/mechanism illustration. CC0-1.0."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch

ap=argparse.ArgumentParser();ap.add_argument('--out',default=str(Path(__file__).parent/'assets'));args=ap.parse_args()
out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.hashsalt':'OA-FLOW-normal-LCA-duality-20261005','axes.unicode_minus':False})
n=3;x=np.array([2,5,9]);w=np.exp(2j*np.pi/3)
def idx(a,b,k):return (a*n+b)*n+k
Jx=np.zeros((27,27),complex);Jl=np.zeros_like(Jx);Je=np.zeros_like(Jx)
F=np.zeros_like(Jx);S=np.zeros_like(Jx)
for r in range(n):
 for c in range(n):
  for k in range(n):
   Jx[idx(r,c,k),idx(r,c,k)]=x[(k+r)%n]
   Jl[idx(r,c,k),idx((r-1)%n,c,k)]=w**c
   Je[idx(r,c,k),idx(r,(c-1)%n,k)]=1
   for t in range(n):F[idx(r,t,k),idx(r,c,k)]=w**(-c*t)/np.sqrt(n)
for q in range(n):
 for t in range(n):
  for k in range(n):S[idx(q,t,k),idx((q+t)%n,t,k)]=1
U=S@F
Bx=np.diag([x[(k+q+t)%n] for q in range(n) for t in range(n) for k in range(n)])
Bl=np.zeros_like(Jl);Be=np.zeros_like(Je)
for q in range(n):
 for t in range(n):
  for k in range(n):
   Bl[idx(q,t,k),idx(q,(t-1)%n,k)]=1
   Be[idx(q,t,k),idx(q,t,k)]=w**(-t)
errs={name:float(np.max(np.abs(a-b))) for name,a,b in [('unitarity',U@U.conj().T,np.eye(27)),('coefficient',U@Jx@U.conj().T,Bx),('first_group',U@Jl@U.conj().T,Bl),('second_group',U@Je@U.conj().T,Be)]}
assert max(errs.values())<1e-13
before=np.array([[int(x[r]) for t in range(n)] for r in range(n)])
after=np.array([[int(x[(q+t)%n]) for t in range(n)] for q in range(n)])
orbit=np.array([[int(x[(k+t)%n]) for t in range(n)] for k in range(n)])
shift=np.roll(orbit,-1,axis=1);restored=np.roll(shift,1,axis=0)
assert np.array_equal(orbit,restored)
data={'group':'Z/3Z','all_coordinates_modulo':3,'M':'C^3','alpha_1':'(x_2,x_0,x_1)','x':x.tolist(),'displayed_coefficient_component':0,'before_rows_r_columns_t':before.tolist(),'after_rows_q_columns_t':after.tolist(),'shear_input_r_equals':[[int((q+t)%n) for t in range(n)] for q in range(n)],'orbit_rows_coefficient_k_columns_t':orbit.tolist(),'right_shift_a1':shift.tolist(),'coefficient_action_a1_restored':restored.tolist(),'root_of_unity_exponents_Q1':[-t for t in range(n)],'orthonormal_fourier_entries':'3^(-1/2) exp(-2 pi i n t /3)','haar_G':'counting','haar_dual':'singleton mass 1/3','operator_max_entry_residuals':errs,'residual_interpretation':'Floating-point checks for this exact finite example; arbitrary-group theorem is the written proof.'}
(out/'duality-coordinate-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(16,11.5),dpi=180,facecolor='#f7f9fc')
fig.text(.045,.955,'Two crossings: one moving coordinate, the full matrix algebra',fontsize=24,weight='bold',color='#152a40')
fig.text(.045,.922,r'Exact example: $G=\mathbb{Z}/3\mathbb{Z}$, $M=\mathbb{C}^3$, $x=(2,5,9)$, $\alpha_1(x)=(x_2,x_0,x_1)$',fontsize=16,color='#334e66')
colors=['#b7d9f5','#d5edcb','#ffe0b5']
def grid(ax,values,rowname,title,qcolors=False):
 ax.set_xlim(-.75,3.05);ax.set_ylim(3.05,-.95);ax.axis('off');ax.set_title(title,loc='left',fontsize=18,weight='bold',pad=12,color='#152a40')
 for row in range(3):
  ax.text(-.15,row+.5,f'{rowname}={row}',ha='right',va='center',fontsize=14)
  for t in range(3):
   q=(row-t)%3 if qcolors else row
   ax.add_patch(Rectangle((t,row),1,1,fc=colors[q],ec='white',lw=2))
   ax.text(t+.5,row+.39,str(values[row,t]),ha='center',va='center',fontsize=25,weight='bold',color='#16354d')
   if qcolors:ax.text(t+.5,row+.76,f'q={q}',ha='center',va='center',fontsize=12,color='#284a60')
  ax.text(row+.5,-.19,f't={row}',ha='center',va='bottom',fontsize=14)
a=fig.add_axes([.055,.54,.26,.31]);grid(a,before,'r','1. After Fourier transform',True)
a.text(-.7,3.48,r'$j(\lambda_1):\ \xi(r,t)\mapsto\xi(r-1,t-1)$',fontsize=14)
a.text(-.7,3.87,r'Colour records $q=r-t$; this label is fixed.',fontsize=13,color='#334e66')
b=fig.add_axes([.39,.54,.26,.31]);grid(b,after,'q','2. After the Haar shear')
b.text(-.7,3.48,r'$S\xi(q,t)=\xi(q+t,t)$',fontsize=15)
b.text(-.7,3.88,r'$j(\lambda_1):\ \zeta(q,t)\mapsto\zeta(q,t-1)$',fontsize=14)
fig.add_artist(FancyArrowPatch((.327,.69),(.378,.69),transform=fig.transFigure,arrowstyle='-|>',mutation_scale=25,lw=2,color='#426c91'))
fig.text(.332,.745,r'$r=q+t$',fontsize=14,color='#426c91')
c=fig.add_axes([.73,.54,.245,.31]);E=np.zeros((3,3),int);E[2,1]=1
c.set_xlim(-.6,3.05);c.set_ylim(3.05,-.95);c.axis('off');c.set_title('3. Every matrix entry\n    from both families',loc='left',fontsize=16,weight='bold',pad=12,color='#152a40')
for row in range(3):
 c.text(-.15,row+.5,f'a={row}',ha='right',va='center',fontsize=13)
 for col in range(3):
  c.add_patch(Rectangle((col,row),1,1,fc='#e67738' if E[row,col] else '#e6edf4',ec='white',lw=2))
  c.text(col+.5,row+.5,str(E[row,col]),ha='center',va='center',fontsize=25,color='white' if E[row,col] else '#627486')
 c.text(row+.5,-.19,f'b={row}',ha='center',va='bottom',fontsize=13)
c.text(-.55,3.48,r'$p_aL_{a-b}p_b=E_{ab}$; shown: $E_{21}$.',fontsize=14)
c.text(-.55,3.88,r'$p_t=\frac{1}{3}\sum_{n=0}^{2}e^{2\pi int/3}Q_n$',fontsize=14)
fig.text(.055,.395,'4. Why the coefficient action survives in the bidual action',fontsize=19,weight='bold',color='#152a40')
def small(rect,vals,title):
 ax=fig.add_axes(rect);ax.axis('off');ax.set_xlim(-.6,3);ax.set_ylim(3,-.7)
 ax.text(-.6,-.47,title,fontsize=14,weight='bold',color='#25465f')
 for k in range(3):
  ax.text(-.12,k+.5,f'k={k}',ha='right',va='center',fontsize=12)
  for t in range(3):
   ax.add_patch(Rectangle((t,k),1,1,fc=colors[x.tolist().index(int(vals[k,t]))],ec='white',lw=1))
   ax.text(t+.5,k+.5,str(vals[k,t]),ha='center',va='center',fontsize=21,weight='bold',color='#16354d')
  ax.text(k+.5,-.12,f't={k}',ha='center',va='bottom',fontsize=12)
small([.055,.13,.23,.22],orbit,r'$A_x(t)_k=x_{k+t}$')
small([.38,.13,.23,.22],shift,r'$R_1A_xR_1^*(t)_k=x_{k+t+1}$')
small([.715,.13,.23,.22],restored,r'$\alpha_1(A_x(t+1))_k=x_{k+t}$')
for a,b in [(.30,.365),(.63,.695)]:
 fig.add_artist(FancyArrowPatch((a,.235),(b,.235),transform=fig.transFigure,arrowstyle='-|>',mutation_scale=23,lw=2,color='#426c91'))
fig.text(.3,.278,r'$\operatorname{Ad}R_1$',fontsize=13,color='#426c91');fig.text(.636,.278,r'$\alpha_1$',fontsize=14,color='#426c91')
fig.text(.055,.073,r'General theorem: $K=L^2(G,H)$ remains as the coefficient representation; the target is $M\,\bar{\otimes}\,B(L^2(G))$.',fontsize=15,color='#25465f')
fig.text(.055,.038,r'$\beta_a=\alpha_a\bar{\otimes}\operatorname{Ad}R_a$ fixes the orbit field and $L_s$, while $Q_\chi\mapsto\overline{\chi(a)}Q_\chi$.',fontsize=15,color='#25465f')
fig.savefig(out/'duality-coordinate-mechanism.png',dpi=180)
fig.savefig(out/'duality-coordinate-mechanism.svg',metadata={'Date':None,'Creator':'Original OA-FLOW double-duality figure; CC0-1.0'})
plt.close(fig);print(json.dumps({'pixels':[2880,2070],'max_residual':max(errs.values()),'output':str(out)}))
