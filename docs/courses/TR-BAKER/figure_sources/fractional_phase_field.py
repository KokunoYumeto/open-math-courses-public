"""Original exact fractional field/valuation diagram, GPT-6.1 Sol, Ultra. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':19,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15.5,8),facecolor='white')
fig.text(.5,.965,'The support field controls the fractional valuation budget',ha='center',fontsize=24,weight='bold')
fig.text(.5,.90,r'$p=5,\ q=2,\ P=1,\ \theta_1=6,\ G_0=2,\ d_1=0,\ \Lambda=\{0,1\}$',ha='center',fontsize=23)
canvas=fig.add_axes([0,0,1,1]);canvas.set(xlim=(0,1),ylim=(0,1));canvas.axis('off')
fields=[(.045,r'$K=\mathbb{Q}$','1'),(.375,r'$E=\mathbb{Q}(\sqrt{6})$','2'),(.705,r'$F=\mathbb{Q}(i,\sqrt{6})$','4')]
for x,name,degree in fields:
    canvas.add_patch(FancyBboxPatch((x,.625),.25,.20,boxstyle='round,pad=0.007',facecolor='#eff6ff',edgecolor='#94a3b8',linewidth=1.5))
    canvas.text(x+.125,.785,name,ha='center',va='center',fontsize=23)
    canvas.text(x+.125,.735,r'Global degree $'+degree+'$',ha='center',fontsize=20)
    canvas.text(x+.125,.690,r'Chosen completion $\mathbb{Q}_5$',ha='center',fontsize=19)
    canvas.text(x+.125,.642,r'Degree factor $'+degree+'$',ha='center',fontsize=20,color='#1d4ed8')
for x in [.31,.64]:
    canvas.annotate('',xy=(x+.04,.76),xytext=(x-.005,.76),arrowprops={'arrowstyle':'->','color':'#334155','lw':2})
    canvas.text(x+.017,.81,r'$\times2$',ha='center',fontsize=19)
canvas.text(.5,.55,r'$g=2,\quad G_*=1,\quad w=0,\quad v_0=(0,0),\quad v_1=(0,1),\quad h_\Lambda=1$',ha='center',fontsize=22)
canvas.text(.5,.475,r'$V=\frac{3}{2}(1-\sqrt{6})\in E$',ha='center',fontsize=25)

canvas.add_patch(FancyBboxPatch((.055,.19),.255,.22,boxstyle='round,pad=0.012',facecolor='#fff7ed',edgecolor='#fed7aa'))
canvas.text(.1825,.36,r'$\eta^2=6,\quad\eta\equiv1\ (\mathrm{mod}\ 5)$',ha='center',fontsize=20)
canvas.text(.1825,.30,r'$(1-\eta)(1+\eta)=-5$',ha='center',fontsize=21)
canvas.text(.1825,.235,r'$v_5(1+\eta)=0$',ha='center',fontsize=20)
bars=fig.add_axes([.42,.18,.50,.24])
bars.bar([0,1],[1,0],width=.44,color=['#2563eb','#b45309'],zorder=3)
bars.scatter([1],[0],s=95,color='#b45309',zorder=4)
bars.set(ylim=(-.10,1.25),xlim=(-.55,1.55),yticks=[0,1])
bars.set_xticks([0,1],[r'$\sqrt{6}\mapsto\eta$',r'$\sqrt{6}\mapsto-\eta$'])
bars.set_ylabel(r'$v_5(V)$');bars.grid(axis='y',alpha=.22,zorder=0)
bars.text(0,1.06,'1',ha='center',fontsize=22,color='#1d4ed8')
bars.text(1,.08,'0',ha='center',fontsize=22,color='#b45309')
bars.spines[['top','right']].set_visible(False)
fig.text(.5,.085,'The same completion does not imply the same global degree or conjugate valuation.',ha='center',fontsize=20,color='#334155')
fig.text(.5,.035,'Theorems 10.56–10.57, equations (10.154)–(10.156), and Solution 29.',ha='center',fontsize=19,color='#475569')
folder=Path(__file__).resolve().parent
destination=folder.parent/'figures/fractional-phase-field.png' if folder.name=='figure_sources' else folder/'fractional-phase-field.png'
destination.parent.mkdir(exist_ok=True)
fig.savefig(destination,dpi=180,bbox_inches='tight')
print(destination)
