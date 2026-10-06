"""Original exact L127 diagram; mathematical integer data is separate from display coordinates."""
from pathlib import Path
import argparse,json,math,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'L127-CN18-20261005','font.size':13})
E=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--output',default='figure');args=parser.parse_args()
out=(E/args.output).resolve();assert out.is_relative_to(E.resolve()),'Output must remain inside this owned writer directory'
out.mkdir(parents=True,exist_ok=True)
rows=[]
for n in range(5):
 raw=[n*n%8,(n*n+4*n)%8];character=n*n%8;correction=(-n*n)%8;normalized=[(p+correction)%8 for p in raw]
 assert normalized==[0,(4*n)%8]
 rows.append({'n':n,'raw_diagonal_exponents_mod8':raw,'character_exponent_mod8':character,
  'scalar_correction_exponent_mod8':correction,'normalized_diagonal_exponents_mod8':normalized})
for m in range(-6,7):
 for n in range(-6,7):
  assert (m*m+n*n-(m+n)**2)%8==(-2*m*n)%8
  assert (4*m+4*n)%8==(4*(m+n))%8
assert (-2*1*1)%8==6
data={'model':'M2(C), G=Z, alpha_n=Ad diag(1,(-1)^n)','zeta':'exp(i*pi/4)',
 'phase_coordinates':'Integer exponents modulo8; angles are exponent*pi/4',
 'character':'chi(diag(a,b))=a','rows':rows,
 'lambda_1_1_exponent_mod8':6,'lambda_1_1_exact':'-i','v1_squared':'i*I2','v2':'-I2',
 'all169_integer_multiplier_checks':True,'all169_corrected_representation_checks':True,
 'proof_locators':['CN1','CN3','CN4','CN5','CN18'],'numeric_coordinates_only_for_display':True}
(out/'character-normalization-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
fig=plt.figure(figsize=(15,11),dpi=200,facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,15),ylim=(0,11));ax.axis('off')
ax.text(.55,10.6,'A character removes the exact scalar phase',fontsize=24,fontweight='bold',color='#142b45')
ax.text(.55,10.15,r'$\zeta=e^{i\pi/4}$     $v_n=\zeta^{n^2}\mathrm{diag}(1,(-1)^n)$     $\chi(\mathrm{diag}(a,b))=a$',fontsize=17)
ax.text(.65,9.45,'n',fontsize=17,fontweight='bold')
ax.text(2.3,9.45,r'Raw $v_n$',fontsize=17,fontweight='bold')
ax.text(5.2,9.45,r'$\chi(v_n)$ and scalar correction',fontsize=16,fontweight='bold')
ax.text(10.4,9.45,r'Normalized $w_n$',fontsize=17,fontweight='bold')
ax.plot([.55,14.45],[9.2,9.2],color='#ccd6e2')
def draw_phase(cx,cy,phases):
 ax.add_patch(Circle((cx,cy),.34,fill=False,color='#a9b8c9',lw=1.3))
 ax.plot([cx-.39,cx+.39],[cy,cy],color='#d7e0e9',lw=.8)
 for j,p in enumerate(phases):
  length=.26 if j==0 else .34
  theta=p*math.pi/4
  ax.plot([cx,cx+length*math.cos(theta)],[cy,cy+length*math.sin(theta)],color=['#2165a8','#bd5e21'][j],lw=2.7,linestyle=['-','--'][j])
  ax.plot(cx+length*math.cos(theta),cy+length*math.sin(theta),'o',color=['#2165a8','#bd5e21'][j],ms=4)
phase_text={0:'1',1:r'\zeta',4:'-1',5:r'-\zeta',6:'-i',7:r'\zeta^{-1}'}
for row in rows:
 n=row['n'];y=8.55-1.24*n
 if n%2==0:ax.add_patch(plt.Rectangle((.55,y-.5),13.9,1.06,color='#edf2f8',zorder=-1))
 ax.text(.7,y,str(n),fontsize=20,va='center',fontweight='bold',color='#142b45')
 draw_phase(1.75,y,row['raw_diagonal_exponents_mod8'])
 p,q=row['raw_diagonal_exponents_mod8']
 ax.text(2.35,y,'$\\mathrm{diag}('+phase_text[p]+','+phase_text[q]+')$',fontsize=17,va='center')
 ax.text(5.25,y+.15,'$\\chi(v_n)='+phase_text[row['character_exponent_mod8']]+'$',fontsize=17,va='center')
 ax.text(5.25,y-.23,'$\\overline{\\chi(v_n)}='+phase_text[row['scalar_correction_exponent_mod8']]+'$',fontsize=16,va='center',color='#3a526d')
 ax.add_patch(FancyArrowPatch((8.5,y),(9.8,y),arrowstyle='-|>',mutation_scale=18,lw=1.8,color='#536e8b'))
 draw_phase(10.3,y,row['normalized_diagonal_exponents_mod8'])
 p,q=row['normalized_diagonal_exponents_mod8']
 ax.text(10.95,y,'$\\mathrm{diag}('+phase_text[p]+','+phase_text[q]+')$',fontsize=17,va='center')
ax.text(.7,2.13,'Solid blue = first diagonal entry; dashed orange = second. Coincident phases are shown by two ray lengths.',fontsize=12,color='#3a526d')
ax.text(.7,1.68,r'Exact defect:  $v_1^2=iI_2$,  $v_2=-I_2$,  $v_1^2=(-i)v_2$; hence $\lambda(1,1)=-i$.',fontsize=17,color='#142b45')
ax.text(.7,1.13,r'$w_mw_n=w_{m+n}$;  $u_n=w_n^*$ cancels $\alpha_n$ on all four matrix units, so $\beta_n=\mathrm{id}$.',fontsize=16,color='#142b45')
ax.text(.7,.58,'CN18: exact sample n=0,...,4 of the Z model. CN1–CN5 treat the stated implementing family in D.',fontsize=12,color='#3a526d')
ax.text(.7,.25,'Circle coordinates show exact phase directions; sampled matrices do not replace the general extension and kernel proofs.',fontsize=11,color='#3a526d')
fig.savefig(out/'character-normalization.png',dpi=200)
fig.savefig(out/'character-normalization.svg',metadata={'Date':None})
plt.close(fig);shutil.copyfile(E/'FONT-LICENSE.txt',out/'FONT-LICENSE.txt')
print(json.dumps({'output':str(out),'pixels':[3000,2200],'exact_rows':5,'integer_checks':338}))
