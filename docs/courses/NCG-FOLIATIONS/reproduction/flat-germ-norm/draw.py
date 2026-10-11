"""Original CC0 actual-flat-germ figure; installed fonts/software retain terms."""
from pathlib import Path
from io import BytesIO
import argparse,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Rectangle

def draw(output=None):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                         'svg.fonttype':'none','svg.hashsalt':'ncg-fgj-20261011'})
    fig=plt.figure(figsize=(17,11),dpi=100)
    bg=fig.add_axes([0,0,1,1]);bg.set(xlim=(0,17),ylim=(0,11));bg.axis('off')
    labels=[]
    def text(x,y,s,**kw):
        a=bg.text(x,y,s,ha=kw.pop('ha','center'),va='center',**kw);labels.append(a);return a
    def panel(x,y,w,h,color):
        bg.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.02',facecolor=color,edgecolor='#4d6077'))
    text(8.5,10.55,'Flat actual holonomy: jets, neighbouring fibres and the reduced norm',fontsize=24,fontweight='bold')
    text(8.5,10.12,'Original codimension q = 1; all actual germs, source counts and the full positive lift are retained.',fontsize=17)
    panel(.6,5.74,7.55,3.94,'#edf4fc');panel(8.52,5.74,7.88,3.94,'#f1f8f0')
    text(.92,9.32,'A. Actual transverse coordinates — FGJ.1–FGJ.9',ha='left',fontweight='bold',fontsize=18)
    ax=fig.add_axes([.068,.66,.384,.13]);ax.set(xlim=(-.2,.60),ylim=(-.25,.68));ax.spines[['left','right','top']].set_visible(False)
    ax.spines['bottom'].set_position(('data',0));ax.set_yticks([]);ax.set_xticks([-.125,0,.125,.25,.5]);ax.tick_params(axis='x',labelsize=12)
    for n,color in zip(range(1,5),['#286caa','#407bb0','#6294ba','#85adc9']):
        c=2**-n;ell=2**(-n-3)
        ax.add_patch(Rectangle((c-ell,.13),2*ell,.17,facecolor=color,edgecolor='#24445c'))
        ax.text(c,.37,'I'+str(n),ha='center',fontsize=13)
    ax.plot([-.125,-.0625,-.03125],[0,0,0],'o',color='#3c536d',markersize=5)
    ax.plot(0,0,'*',color='#b64527',markersize=13)
    text(4.34,6.72,r'$c_n=2^{-n},\quad\ell_n=2^{-n-3},\quad\epsilon_n=L2^{-n^2}$',fontsize=20)
    text(4.34,6.25,'Four intervals shown; the full flat family approaches zero.',fontsize=16)
    text(12.45,9.32,'B. Exact commutator displacement — FGJ.9',fontweight='bold',fontsize=18)
    plot=fig.add_axes([.555,.655,.372,.17])
    L=sum(10.0**(-math.factorial(k)) for k in range(1,5))
    ns=list(range(1,9))
    logs=[(-n-3)*math.log10(2)+3*(math.log10(L)-n*n*math.log10(2))-math.log10(1-(L*2**(-n*n))**2) for n in ns]
    plot.plot(ns,logs,'o-',color='#367743',linewidth=2,markersize=5)
    plot.set_xticks(ns);plot.set_ylabel('log10 |physical displacement|',fontsize=13);plot.set_xlabel('n (numerical samples)',fontsize=13)
    plot.grid(alpha=.23);plot.tick_params(labelsize=12)
    text(12.45,6.22,r'$f g f^{-1}g^{-1}(c_n)-c_n=-\ell_n\epsilon_n^3/(1-\epsilon_n^2)$',fontsize=18)
    panel(.6,3.01,15.8,2.31,'#fff5e9')
    text(.92,4.99,'C. The actual zero isotropy survives every formal jet — FGJ.5, FGJ.8, FGJ.10',ha='left',fontweight='bold',fontsize=18)
    text(8.5,4.50,r'$\mathcal{H}_0^0=F_2,\qquad j_0^\infty f=j_0^\infty g=j_0^\infty\mathrm{id}$',fontsize=23)
    text(8.5,4.04,'Negative source fibres have one unit arrow. Their unit sequence has two distinct arrow-space limits:',fontsize=17)
    text(8.5,3.63,r'$[\mathrm{id},0]\ \mathrm{and}\ [f,0].\qquad c:\mathcal{H}\to K\ \mathrm{continuous},\ K\ \mathrm{Hausdorff}\ \Longrightarrow\ c(\mathcal{H}_0^0)=\{e\}$',fontsize=20)
    text(8.5,3.24,'The coherent lift is sqrt(Dw), with central phase 1; inverse phase 1 and final right C1 remain.',fontsize=17)
    panel(.6,.53,15.8,2.04,'#edf8f6')
    text(.92,2.23,'D. Two different reduced norms — FGJ.13–FGJ.15',ha='left',fontweight='bold',fontsize=18)
    text(8.5,1.80,r'$\varepsilon_0(k)=\lim_{x\uparrow0}\lambda_x(k),\quad |\varepsilon_0(k)|\leq\|k\|_{C_r^*(\mathcal{H})}$',fontsize=22)
    text(8.5,1.34,r'$C_0(O)\otimes C_r^*F_2:\quad\|v\otimes P\|\leq\sqrt{3}/2<1=\|v\|\quad\mathrm{in}\ C_0(O)$',fontsize=22)
    text(8.5,.89,'Canonical reduced labelled-action collapse would send v tensor P to v and violate contractivity.',fontsize=17)
    text(8.5,.23,'The reduced germ character is even. The original degree-one normal graph class still requires its own proof.',fontsize=17,color='#344c59')
    fig.canvas.draw();renderer=fig.canvas.get_renderer();width,height=fig.canvas.get_width_height()
    for a in labels:
        b=a.get_window_extent(renderer)
        assert 8<=b.x0 and b.x1<=width-8 and 8<=b.y0 and b.y1<=height-8,a.get_text()
        assert not any(b.overlaps(p.get_tightbbox(renderer)) for p in [ax,plot]),a.get_text()
    png,svg=BytesIO(),BytesIO()
    fig.savefig(png,format='png',dpi=100,metadata={'Software':'NCG FGJ original CC0 generator'})
    fig.savefig(svg,format='svg',metadata={'Date':None,'Creator':'NCG FGJ original CC0 generator'})
    result={'png':png.getvalue(),'svg':svg.getvalue()};plt.close(fig)
    if output is not None:
        output.mkdir(parents=True,exist_ok=True)
        for ext,raw in result.items():(output/('flat-actual-germ-norm.'+ext)).write_bytes(raw)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures');draw(p.parse_args().output)
