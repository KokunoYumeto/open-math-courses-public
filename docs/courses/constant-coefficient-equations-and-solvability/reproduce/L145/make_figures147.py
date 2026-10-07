"""Original normal-coordinate and codimension figures;CC0;no TeX process."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':12,'svg.fonttype':'none','svg.hashsalt':'AN02-L145','text.usetex':False,'savefig.dpi':170})
BLUE='#2364a5';ORANGE='#bd5700';GREEN='#197450';GREY='#5c6670'
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),facecolor='white',metadata={'Software':'Original AN-02 L145 figure script'})
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Creator':'Original AN-02 L145 figure script','Date':None})
    plt.close(fig)
fig,axes=plt.subplots(1,3,figsize=(13.4,5.4));fig.subplots_adjust(left=.065,right=.98,top=.79,bottom=.25,wspace=.38)
fig.suptitle('A normal cutoff creates an annular error; a normal pole cannot survive the trace',fontsize=15,y=.965)
ax=axes[0]
ax.add_patch(Circle((0,0),1,facecolor=ORANGE,alpha=.18,edgecolor='none'))
ax.add_patch(Circle((0,0),.5,facecolor='white',edgecolor=BLUE,lw=1.7))
ax.add_patch(Circle((0,0),1,fill=False,edgecolor=ORANGE,lw=1.7))
ax.plot([0,1],[0,0],color=GREY,lw=.9)
ax.scatter([0],[0],color=BLUE,s=25);ax.text(-.02,.12,r'$w=0$; $\eta=1$',ha='center',color=BLUE)
ax.text(0,.73,r'$f_d/u=-1/r$',color=ORANGE,fontsize=11,ha='center')
ax.text(.25,-.16,r'$1/2$',ha='center');ax.text(.78,-.16,'1',ha='center')
ax.set(xlabel=r'Normal real coordinate $\mathrm{Re}\,w$',ylabel=r'Normal imaginary coordinate $\mathrm{Im}\,w$',title=r'Error support: $1/2<|w|<1$')
ax.set_xlim(-1.2,1.2);ax.set_ylim(-1.2,1.2);ax.set_aspect('equal');ax.grid(alpha=.15)
ax=axes[1]
r=np.linspace(0,1.25,1201);eta=np.where(r<=.5,1,np.where(r<1,2*(1-r),0))
ax.plot(r,eta,color=BLUE,lw=2.4,label=r'Cutoff $\eta$')
ax.plot([0,.5],[0,0],color=ORANGE,lw=2.2)
middle=np.linspace(.5,1,501);ax.plot(middle,1/middle,color=ORANGE,lw=2.2,label=r'Error $|f_d/u|=1/r$ a.e.')
ax.plot([1,1.25],[0,0],color=ORANGE,lw=2.2)
ax.plot([.5,.5],[0,2],color=ORANGE,ls=':',lw=1);ax.plot([1,1],[0,1],color=ORANGE,ls=':',lw=1)
ax.set(xlabel=r'Normal radius $r=|w|$',ylabel='Cutoff or coefficient modulus',title='The actual error stays away from 0')
ax.set_xlim(0,1.25);ax.set_ylim(-.04,2.15);ax.grid(alpha=.2);ax.legend(fontsize=9,loc='upper right')
ax=axes[2];epsilon=np.geomspace(1e-4,1,501)
ax.semilogx(epsilon,2*np.pi*np.log(1/epsilon),color=GREEN,lw=2.4)
ax.set(xlabel=r'Relative inner radius $\varepsilon$',ylabel=r'Truncated square integral $2\pi\log(1/\varepsilon)$',title='Hypothetical pole; rescaled outer radius 1')
ax.set_xlim(1e-4,1);ax.grid(alpha=.2)
ax.text(.04,.25,r'$\varepsilon\downarrow0$'+ '\n'+r'$\Rightarrow$ integral $\uparrow\infty$',transform=ax.transAxes,color=GREEN)
fig.text(.065,.065,r'Actual annular quotient norm: $2\pi\log2$. A nonzero trace difference would force a pole to radius 0.'+'\nThe right panel depicts that obstruction, not a returned solution. Formal E4, EX11–EX18; Hörmander II, Theorem 15.1.3.',fontsize=10,color=GREY)
save(fig,'normal-cutoff-and-trace')

fig,axes=plt.subplots(1,2,figsize=(11.8,5.6),gridspec_kw={'width_ratios':[1,1.2]});fig.subplots_adjust(left=.07,right=.98,top=.81,bottom=.24,wspace=.25)
fig.suptitle('Codimension changes the dimension, norm budget and weight exponent together',fontsize=15,y=.965)
ax=axes[0];ax.set_axis_off()
rows=[[str(j),f'm + {j}' if j else 'm',f'$R^{{-{3*j}}}$' if j else '1','C = 1'] for j in range(5)]
table=ax.table(cellText=rows,colLabels=['Step j','Complex dim.','Weight loss','Same C'],loc='center',cellLoc='center',colWidths=[.16,.29,.29,.25])
table.auto_set_font_size(False);table.set_fontsize(11);table.scale(1,2.0)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#c4ccd4')
    if row==0:cell.set_facecolor('#e5edf5');cell.set_text_props(weight='bold')
ax.set_title(r'Flag $W=E_0\subset E_1\subset\cdots\subset E_4$',pad=14)
ax.text(.5,.02,'Each step adds one complex normal coordinate.\nThe extra logarithm is nonnegative normally.',ha='center',transform=ax.transAxes,color=GREY,fontsize=10)
j=np.arange(5);q=6*np.pi*np.e
universal=q**j
comparison=np.array([1]+[np.pi**int(k)*math.factorial(2*int(k)-1)/math.factorial(3*int(k)-1) for k in j[1:]])
ax=axes[1];ax.semilogy(j,universal,'o-',color=BLUE,lw=2.2,label=r'Universal upper bound $(6\pi e)^j$')
ax.semilogy(j,comparison,'s-',color=ORANGE,lw=2.2,label=r'Normal-monotone direct bound $B_j$')
ax.set(xlabel='Number j of added complex coordinates',ylabel=r'Proved upper norm bound divided by $J_0$',title='Two upper bounds with different hypotheses')
ax.set_xticks(j);ax.set_xlim(-.12,4.12);ax.grid(alpha=.2,which='both');ax.legend(loc='upper left',fontsize=9)
fig.text(.07,.066,r'Upper bounds, not actual solution norms. $B_0=1$; $B_j=\pi^j(2j-1)!/(3j-1)!$ for $j\geq1$.'+'\nThe direct bound additionally assumes global normal monotonicity. Formal E6/E9; Hörmander II, Theorem 15.1.3.',fontsize=10,color=GREY)
save(fig,'codimension-and-norm-budgets')
geometry={
    'schema':'AN02-L145-exact-figure-geometry/v1',
    'normal_cutoff':{'normal_dimension':'One complex coordinate w','inner_radius':'1/2','outer_radius':'1','cutoff':'1 for r<=1/2;2(1-r) for1/2<r<1;0 forr>=1','error_coefficient_over_datum':'-1/r on1/2<r<1;0 elsewhere,a.e.','actual_unweighted_square_area_integral':'2*pi*log(2)','coarse_bound_used':'4*pi','obstruction':'Nonzero entire trace difference would force local |v|>=c/|w|','obstruction_plot':'Rescaled outer radius1,relative inner radius epsilon;integral2*pi*log(1/epsilon)','obstruction_is_actual_returned_solution':False,'proof':'Formal E4,EX11-EX18'},
    'codimension_iteration':{'steps':[0,1,2,3,4],'complex_dimensions':['m','m+1','m+2','m+3','m+4'],'weight_loss_exponents':[0,3,6,9,12],'fixed_C':1,'universal_bounds_divided_by_initial_norm':universal.tolist(),'normal_monotone_bounds_divided_by_initial_norm':comparison.tolist(),'normal_monotone_bound_formula':'pi^j*(2j-1)!/(3j-1)! forj>=1;1 forj=0','plotted_points_are_upper_bounds_not_actual_norms':True,'different_hypotheses_explicit':True,'proof':'Formal E6,EX20-EX23;E9,EX32-EX33'},
    'human_source':'Lars Hörmander,Analysis of Linear PDE II,Theorem15.1.3,printed274-275;1983/1990/2005',
    'original_material_license':'CC0-1.0','font':'DejaVu Sans,separate license retained','protected_source_media_used':False,
}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Two original PNG/SVG pairs and exact figure geometry written.')
