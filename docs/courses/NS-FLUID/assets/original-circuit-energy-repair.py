"""The full original rotor product and correctly signed modified energy."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(17,10),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
teal='#126471';orange='#b85b19'
def txt(x,y,t,size=18,**kw):ax.text(x,y,t,ha='center',va='center',fontsize=size,**kw)
txt(.5,.951,'The actual rotor product fixes the modified-energy sign',25)
txt(.5,.886,r'$a^\prime=-\epsilon^{-2}cd-\epsilon ab-\epsilon^2e^{-K^{10}}ac,\quad d^\prime=\epsilon^{-2}ca-KdZ,\quad Z^\prime=Kd^2$',20)
txt(.5,.825,r'$Z=\widetilde a,\quad c(t)>0\ (t>0),\quad M=ad\,\epsilon^2/c,\quad E=(a^2+b^2+c^2+d^2)/2$',21)
for x in [.055,.53]:
 ax.add_patch(FancyBboxPatch((x,.625),.415,.135,boxstyle='round,pad=0.012',facecolor='#f0f6f7',edgecolor=teal,lw=2))
txt(.2625,.710,r"$M^\prime=a^2-d^2$",24,color=teal)
txt(.2625,.655,r'$-\left(\epsilon b+\epsilon^2e^{-K^{10}}c+KZ+c^\prime/c\right)M$',18)
txt(.7375,.690,r"$E^\prime=-Kd^2Z$",26,color=teal)
ax.annotate('',xy=(.5,.546),xytext=(.5,.612),arrowprops=dict(arrowstyle='-|>',lw=2,color=orange))
txt(.5,.522,r'$E_{\mathrm{corr}}=E-\dfrac{K}{2} MZ$',28,color=orange)
txt(.5,.440,r"$E_{\mathrm{corr}}^\prime=-KZE_{\mathrm{corr}}+\mathcal{R}$",27)
txt(.5,.359,r'$\mathcal{R}=\dfrac{K}{2}Z(b^2+c^2)+\dfrac{K}{2}M\left[\left(\epsilon b+\epsilon^2e^{-K^{10}}c+\dfrac{c^\prime}{c}\right)Z-Kd^2\right]$',23)
txt(.5,.267,r'$E_{\mathrm{corr}}(t)=e^{-K\int_{t_1}^t Z}E_{\mathrm{corr}}(t_1)+\int_{t_1}^t e^{-K\int_s^t Z}\mathcal{R}(s)\,ds,\quad 0<t_1\leq t$',21)
txt(.5,.185,'The leading product sign is positive. The correction to the original energy therefore has a minus sign.',17)
txt(.5,.133,'CR1–CR11 prove every identity and explicit finite-interval bounds from the actual globally constructed five-mode flow.',14)
txt(.5,.089,'Human source: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex, equations a-eq–ta-eq and douse.',12)
txt(.5,.051,'All small-mode, weak-pump, varying-frequency and output-pump contributions remain in the exact remainder.',13)
txt(.5,.02,'This diagram records proved identities. The later delayed-transfer and infinite-cascade estimates remain separate calculations.',12)
for ext in ['png','svg']:fig.savefig(OUT/f'original-circuit-energy-repair.{ext}',dpi=150)
plt.close(fig)
