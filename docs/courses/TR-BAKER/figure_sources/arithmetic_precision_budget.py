"""CC0. Reproduce Figure10.6, the finite-valuation zero-forcing mechanism.

Proof locator: TR-BAKER-10, Theorems10.41 and10.43, equations10.116,
10.119–10.120. A=3 and G=5 illustrate interval separation only;
they are not asserted to come from a particular auxiliary function.
Human-source context: Kunrui Yu's freely accessible2013 article,
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6782-11511_2013_Article_106.pdf
The interval diagram and the complete course proof are original CC0 work.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

source_dir=Path(__file__).resolve().parent
out_dir=source_dir.parent/'figures' if source_dir.name=='figure_sources' else source_dir
out_dir.mkdir(exist_ok=True)
out=out_dir/'arithmetic-precision-budget.png'
fig,ax=plt.subplots(figsize=(12,6.3),dpi=200)
fig.patch.set_facecolor('white')
ax.set_xlim(-.2,8.3);ax.set_ylim(-.7,2.6)
ax.set_yticks([]);ax.set_xticks(range(9))
fig.text(.5,.25,r'Finite valuation excess $\nu=v_p(\Phi(x;\mathbf{t}))-\delta$',ha='center',fontsize=17)
ax.tick_params(axis='x',labelsize=15)
for side in ['left','right','top']:ax.spines[side].set_visible(False)
ax.spines['bottom'].set_position(('data',-.5))
ax.hlines(1.3,0,3,color='#236da4',lw=14,alpha=.7)
ax.plot([0,3],[1.3,1.3],'o',color='#236da4',ms=11)
ax.hlines(.45,5,8,color='#b95420',lw=14,alpha=.7)
ax.plot(5,.45,'o',color='#b95420',ms=11)
ax.annotate('',xy=(8.25,.45),xytext=(7.8,.45),arrowprops={'arrowstyle':'->','color':'#b95420','lw':3})
ax.vlines([3,5],-.45,1.65,linestyles='dashed',colors=['#236da4','#b95420'],lw=1.5)
ax.text(0,1.85,r'Arithmetic, if $\Phi\ne0$: $0\leq\nu\leq\mathcal{A}$',fontsize=18,color='#174d75')
ax.text(3.35,.88,r'Analytic: $\nu\geq G$',fontsize=18,color='#883811')
ax.text(3,-.25,r'$\mathcal{A}=3$',ha='center',fontsize=17,color='#174d75')
ax.text(5,-.25,r'$G=5$',ha='center',fontsize=17,color='#883811')
ax.text(4.1,2.35,'No finite valuation satisfies both bounds',ha='center',fontsize=20,weight='bold')
fig.text(.5,.145,r'$G=(n\mu-D)\theta-Lv_p(k!),\quad D=kL,\quad \mathcal{A}=\mathcal{A}_I(X,T^{\prime})$',ha='center',fontsize=17)
fig.text(.5,.065,r'$G>\mathcal{A}\quad\Longrightarrow\quad\Phi(x;\mathbf{t})=0$  (Theorem 10.43)',ha='center',fontsize=18,weight='bold')
fig.subplots_adjust(left=.07,right=.97,top=.96,bottom=.36)
fig.savefig(out,dpi=200,facecolor='white')
plt.close(fig)
print(out)
