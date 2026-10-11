"""Original CC0 character-homotopy figure; installed fonts retain their terms."""
from pathlib import Path
from io import BytesIO
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw(output=None):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'none','svg.hashsalt':'ncg-ech-20261011'})
    fig=plt.figure(figsize=(17,10),dpi=100)
    bg=fig.add_axes([0,0,1,1]);bg.set(xlim=(0,17),ylim=(0,10));bg.axis('off');labels=[]
    def text(x,y,s,**kw):
        a=bg.text(x,y,s,ha=kw.pop('ha','center'),va='center',**kw);labels.append(a);return a
    def panel(x,y,w,h,color):
        bg.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.02',facecolor=color,edgecolor='#536a7c'))
    text(8.5,9.60,'A nonzero reduced germ character with zero KK-class',fontsize=25,fontweight='bold')
    text(8.5,9.18,'Actual source fibres; point-norm homotopy; original normal degree and coefficient retained.',fontsize=18)
    panel(.60,6.12,15.80,2.64,'#eef4fc')
    text(.94,8.41,'A. Move the receiving point through actual negative unit fibres — ECH.1–ECH.5',ha='left',fontsize=19,fontweight='bold')
    text(8.5,7.93,r'$x(t)=-t/(1-t):\qquad 0\ \longrightarrow\ -1/3\ \longrightarrow\ -1\ \longrightarrow\ -3\ \longrightarrow\ -\infty$',fontsize=24)
    text(8.5,7.45,'Parameters: t = 0, 1/4, 1/2, 3/4, and the endpoint limit 1. Every negative source fibre has one unit.',fontsize=17)
    text(8.5,6.96,r'$\phi_0=\varepsilon_0,\qquad\phi_t=\lambda_{x(t)}\ (0<t<1),\qquad\phi_1=0,\qquad |\phi_t(a)|\leq\|a\|_A$',fontsize=22)
    text(8.5,6.48,'The distinct zero-source germs remain F2. This representation family does not replace their counting norm.',fontsize=17)
    panel(.60,2.75,7.57,2.97,'#f1f8ef');panel(8.52,2.75,7.88,2.97,'#fff5e9')
    text(.92,5.39,'B. A fixed test and the map norms — ECH.8',ha='left',fontsize=18,fontweight='bold')
    plot=fig.add_axes([.076,.370,.36,.125])
    ts=[i/200 for i in range(201)]
    values=[max((1-2*t)/(1-t),0) if t<1 else 0 for t in ts]
    plot.plot(ts,values,color='#367943',linewidth=2.5,label='fixed v(x) = max(1 - |x|, 0)')
    plot.plot([0,.99],[1,1],color='#b34b37',linestyle='--',linewidth=2,label='map norm 1 for t < 1')
    plot.plot(1,1,'o',mfc='white',mec='#b34b37',ms=7);plot.plot(1,0,'o',color='#b34b37',ms=6)
    plot.set(xlim=(-.02,1.04),ylim=(-.10,1.17));plot.set_xticks([0,.25,.5,.75,1]);plot.tick_params(labelsize=12);plot.grid(alpha=.2)
    plot.legend(fontsize=11,loc='center left');plot.set_xlabel('homotopy parameter t',fontsize=13)
    text(4.35,3.03,'Continuity is for each fixed source element.',fontsize=16)
    text(12.45,5.39,'C. The whole interval cycle — ECH.6–ECH.7',fontsize=18,fontweight='bold')
    text(12.45,4.89,r'$E^+=C([0,1]),\quad E^-=0,\quad F=0$',fontsize=21)
    text(12.45,4.38,r'$\Phi(a)(t)=\phi_t(a),\qquad M_b=\theta_{b,1}\in\mathcal{K}(E)$',fontsize=20)
    text(12.45,3.86,r'$[\varepsilon_0]=0\in KK(A,\mathbb{C})$',fontsize=24,color='#86502c')
    text(12.45,3.27,'The endpoint has zero action and is degenerate.',fontsize=17)
    panel(.60,.59,15.80,1.71,'#edf8f6')
    text(.94,1.98,'D. Keep the original normal requirement — ECH.9–ECH.10',ha='left',fontsize=19,fontweight='bold')
    text(8.5,1.51,r'$q>0:\quad[e_p]=0,\quad b_U[e_p]\kappa=0,\qquad b_U\delta_U=+1\ \mathrm{for\ the\ full\ normal\ inverse}$',fontsize=23)
    text(8.5,1.02,'Finite point actions give zero restriction; a different normal transfer is not presumed to factor through them.',fontsize=17)
    text(8.5,.25,'Vanishing of this scalar class does not exclude a different normally geometric class on the full actual graph.',fontsize=17,color='#354d5c')
    fig.canvas.draw();renderer=fig.canvas.get_renderer();w,h=fig.canvas.get_width_height()
    for a in labels:
        b=a.get_window_extent(renderer)
        assert 8<=b.x0 and b.x1<=w-8 and 8<=b.y0 and b.y1<=h-8,a.get_text()
        assert not b.overlaps(plot.get_tightbbox(renderer)),a.get_text()
    png,svg=BytesIO(),BytesIO()
    fig.savefig(png,format='png',dpi=100,metadata={'Software':'NCG ECH original CC0 generator'})
    fig.savefig(svg,format='svg',metadata={'Date':None,'Creator':'NCG ECH original CC0 generator'})
    result={'png':png.getvalue(),'svg':svg.getvalue()};plt.close(fig)
    if output is not None:
        output.mkdir(parents=True,exist_ok=True)
        for ext,raw in result.items():(output/('actual-character-homotopy.'+ext)).write_bytes(raw)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures');draw(p.parse_args().output)
