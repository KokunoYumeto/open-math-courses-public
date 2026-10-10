from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
fig = plt.figure(figsize=(15, 8.5), facecolor='#f8fafc')
fig.text(.045, .947, 'Original WM.22: what the finite argument proves', fontsize=23,
         weight='bold', color='#10243a')
fig.text(.045, .902, r'$\lambda=1+2^{-31}25^{-198153}$; full lamp, spatial, central and parity data retained',
         fontsize=15, color='#334155')

left = fig.add_axes([.055, .435, .405, .38])
left.set_xlim(-3, 2); left.set_ylim(-1.1, 1.45); left.axis('off')
left.set_title('An actual finite cylinder prefix', loc='left', fontsize=18, weight='bold', pad=16)
left.plot([-2.7, 1.7], [0, 0], color='#64748b', lw=2)
for x in range(-2, 2):
    left.plot([x, x], [-.06, .06], color='#64748b')
    left.text(x, -.2, str(x), ha='center', fontsize=13)
left.scatter([0, 1], [0, 0], s=140, color='#e58b30', zorder=4)
left.scatter([-2], [0], s=145, color='#1a7f8e', zorder=4)
left.text(.5, .22, r'$E=\{0,e_1\}$: both bits set to 1', ha='center', fontsize=14)
left.text(-2, -.48, r'$x=(-2,0,0)$', ha='center', fontsize=14, color='#086b79')
left.annotate('', xy=(1, .55), xytext=(0, .55), arrowprops={'arrowstyle':'->', 'color':'#e58b30', 'lw':2})
left.annotate('', xy=(-2, .95), xytext=(1, .95), arrowprops={'arrowstyle':'->', 'color':'#1a7f8e', 'lw':2})
left.text(-.5, 1.12, 'Route projected onto the actual e₁ axis', ha='center', fontsize=12, color='#475569')
left.text(-2.7, -.88, r'Full endpoint: $(\delta_0+\delta_{e_1},(-2,0,0),2)$', fontsize=14)

right = fig.add_axes([.535, .44, .405, .37]); right.axis('off')
right.set_title('The weighted pair is not an adjoint pair', loc='left', fontsize=18, weight='bold', pad=20)
rows = [r'$U_g\Omega=\Omega$ in the original invariant-state GNS space',
        r'$S=\sum_iU_{s_i}$: $\|S\|=5$',
        r'$A_\nu=\sum_i\nu_iU_{s_i}$: $\|A_\nu\|=S_+$',
        r'$B_\nu=\sum_i\nu_i^{-1}U_{s_i}^*$: $\|B_\nu\|=S_-$',
        r'$B_\nu-A_\nu^*=(\lambda^{-1}-\lambda)U_{s_1}^*\ne0$',
        r'$\|A_\nu B_\nu\|=d>25$, while $\|S/\sqrt{d}\|<1$']
for i, text in enumerate(rows):
    right.text(0, .98-i*.155, text, fontsize=14.5, va='top', color='#10243a')

boxes = [(.045, .24, .435, .13, '#e7f3f4'), (.52, .24, .435, .13, '#edf1f7')]
for x, y, w, h, color in boxes:
    box = FancyBboxPatch((x,y),w,h,transform=fig.transFigure,
                         boxstyle='round,pad=0.01,rounding_size=0.012',
                         facecolor=color,edgecolor='#bccbd6')
    fig.add_artist(box)
fig.text(.058,.327,'Both original cylinder masses have an explicit bound:',fontsize=14,weight='bold')
fig.text(.058,.285,r'$\mu_\sigma(\eta|_E=b)\geq\lambda^s d^{-(\ell+s+1)}(1-\lambda^{-r})>0$',fontsize=15)
fig.text(.533,.327,'The domains and trace characters stay separate:',fontsize=14,weight='bold')
fig.text(.533,.282,r'$U_{z^2}=I$ on the center; physical $\chi(z^2)=\lambda^2$',fontsize=15)
fig.text(.045,.163,'No RN-tube positivity or finite RN exclusion follows from these facts.',fontsize=18,
         weight='bold',color='#8b3f25')
fig.text(.045,.113,'CY29.1–CY29.2 prove the prefix and height-escape bound. SB29.1–SB29.2 prove the operator correction.',fontsize=12.5,color='#475569')
fig.text(.045,.077,'Count-depth control: CD29.3–CD29.11. Original inputs: WM.20, FWT.26–28, OM.15–21 and C13.12–24.',fontsize=12.5,color='#475569')
fig.text(.045,.042,'Coordinates and formulas are exact; box sizes encode no probabilities or physical trace masses.',fontsize=12,color='#64748b')
fig.savefig(OUT/'original-support-correction.png',dpi=160,facecolor=fig.get_facecolor())
fig.savefig(OUT/'original-support-correction.svg',facecolor=fig.get_facecolor())
print('Rendered exact original-prefix and weighted-adjoint proof diagram.')
