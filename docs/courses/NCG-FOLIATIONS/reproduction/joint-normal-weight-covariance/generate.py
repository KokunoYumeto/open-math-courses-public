import base64, io, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams['svg.fonttype']='none'
plt.rcParams['svg.hashsalt']='ncg-actual-domain-normal-20261010'
from matplotlib.patches import FancyArrowPatch

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12.5, 5.1))
fig.patch.set_facecolor('white')
ax0.set_xlim(-0.04, .60); ax0.set_ylim(0.75, 1.34)
ax0.axhline(1, color='#6b7280', linewidth=1.5)
ax0.fill_between([-.04,.60], .75, 1, color='#edf0f3')
ax0.text(.01,.82,'rank 3: original closed bump region',fontsize=9)
ax0.text(.01,1.28,'rank 6: original upper flat end',fontsize=9)
for x,lab in [(0,'x = 0'),(.5,'x = 1/2')]:
    ax0.scatter([x],[1.11],s=50,color='#126782')
    ax0.text(x,1.05,lab,ha='center',fontsize=11)
ax0.add_patch(FancyArrowPatch((.025,1.11),(.475,1.11),
                            arrowstyle='->',mutation_scale=15,color='#126782'))
ax0.text(.25,1.16,'suspension tau: x -> x + 1/2',ha='center',fontsize=9)
ax0.text(.585,1.007,'t = 1 seam',ha='right',fontsize=9)
ax0.set_xlabel('original period-one torus coordinate x')
ax0.set_ylabel('original t coordinate')
ax0.set_title('Actual arrows preserve the rank seam')
ax0.set_xticks([0,.5],['0','1/2']); ax0.set_yticks([1,1.11],['1','1 + s_n'])

u=(1/math.sqrt(2),1/math.sqrt(2)); v=(27/math.sqrt(730),1/math.sqrt(730))
ax1.set_aspect('equal'); ax1.set_xlim(-.08,1.12); ax1.set_ylim(-.08,1.02)
ax1.axhline(0,color='#9ca3af',lw=1); ax1.axvline(0,color='#9ca3af',lw=1)
for z,col in [(u,'#b45309'),(v,'#126782')]:
    ax1.add_patch(FancyArrowPatch((0,0),z,arrowstyle='->',mutation_scale=16,
                                linewidth=2,color=col))
ax1.plot([u[0],v[0]],[u[1],v[1]],'--',color='#7c3aed',lw=1.6)
ax1.text(.33,.78,'source: (1, 1)/sqrt(2)',color='#b45309',fontsize=9)
ax1.text(.23,.13,'range: (27, 1)/sqrt(730)',color='#126782',fontsize=9)
gap=math.sqrt(2-56/math.sqrt(1460))
ax1.text(.05,.55,'Delta = %.6f' % gap,color='#7c3aed',fontsize=9)
ax1.set_xlabel('auxiliary mass coefficient of sigma_1')
ax1.set_ylabel('normal coefficient of sigma_3 B')
ax1.set_title('Different joint phase directions')
fig.suptitle('k_n = b_n^(-3): same original normal oscillation, nonzero compact-arrow defect',
             fontsize=12)
fig.tight_layout()
fig.savefig(Path(__file__).resolve().parents[2]/'figures'/'joint-normal-weight-covariance.svg',format='svg',metadata={'Date':None})
buf=io.BytesIO(); fig.savefig(buf,format='png',dpi=150)
(Path(__file__).resolve().parents[2]/'figures'/'joint-normal-weight-covariance.png').write_bytes(buf.getvalue())
