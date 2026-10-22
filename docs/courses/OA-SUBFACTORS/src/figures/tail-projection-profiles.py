"""Exact tail-profile maps and the sharp finite-algebra example. CC0-1.0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path'})
fig=plt.figure(figsize=(6.4,13),dpi=150,facecolor='#f6f8fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def panel(y,h,title,lines,color):
 ax.add_patch(FancyBboxPatch((.055,y),.89,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#8295af'))
 ax.text(.08,y+h-.018,title,fontsize=17,weight='bold',va='top',color='#183956')
 for k,line in enumerate(lines):
  ax.text(.08,y+h-.061-.039*k,line,fontsize=16,va='top',color='#23384d')
ax.text(.055,.978,'Tail projection profiles',fontsize=25,weight='bold',va='top',color='#183956')
ax.text(.055,.942,'One fixed stage; inherited physical trace',fontsize=14,color='#52667c')
panel(.692,.210,'Exact range — TP.1',[
 r'$p\in C,\quad t_p=T_C(p)$',
 r'$0\leq t\leq t_p\quad\Longleftrightarrow$',
 r'$\exists\ q\leq p:\ T_C(q)=t$',
 r'$T_S(qf)=E_Z(ft)$'],'#e7effa')
ax.annotate('',xy=(.5,.658),xytext=(.5,.683),arrowprops=dict(arrowstyle='->',lw=2,color='#285b86'))
panel(.399,.246,'Full finite partition — TP.2',[
 r'$t_0+t_1+t_2=t_p,\quad t_i\geq0$',
 r'$q_0+q_1+q_2=p$',
 r'$q_0f+q_1f+q_2f=pf$',
 r'$\tau(q_if)=\tau(f)\tau(t_i)$',
 'The residual q₀ belongs to the same C.'],'#e6f3eb')
panel(.076,.284,'Sharp loss — TP.3–TP.4',[
 r'$a=1/8,\quad \tau(z)=\tau(1-z)=1/2$'],'#fff0e0')
for i,(label,left,right) in enumerate([
 ('Central values',r'$z$',r'$1-z$'),
 (r'$T_S(q)$',r'$a$',r'$a$'),
 (r'$T_S(qf)$',r'$0$',r'$a$'),
 (r'$az$',r'$a$',r'$0$')]):
 y=.260-.039*i
 ax.text(.08,y,label,fontsize=16,va='top',color='#23384d')
 ax.text(.55,y,left,fontsize=16,va='top',ha='center',color='#23384d')
 ax.text(.77,y,right,fontsize=16,va='top',ha='center',color='#23384d')
ax.text(.08,.104,'Support error squared × χ = ¼ × 8 = 2',fontsize=14,va='top',color='#23384d')
ax.text(.055,.041,'Values are central trace values; areas are schematic.',fontsize=10.5,color='#52667c')
ax.text(.055,.022,'Proofs: TP.1–TP.4; TE16; 56.1. Popa (1994), pp. 213–215.',fontsize=9.5,color='#52667c')
stem='tail-projection-profiles'
fig.savefig(out/(stem+'.png'),dpi=150);fig.savefig(out/(stem+'.svg'))
p=out/(stem+'.svg');p.write_text(re.sub(r'[ \t]+(?=\r?$)','',p.read_text(),flags=re.M),encoding='utf-8')
