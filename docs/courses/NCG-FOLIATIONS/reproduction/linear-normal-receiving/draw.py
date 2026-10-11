"""Original CC0 receiving correspondence; fonts/software retain their terms."""
from pathlib import Path
import argparse
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw(output=None):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,
                         'svg.fonttype':'none','svg.hashsalt':'ncg-linr-20261011'})
    fig, ax=plt.subplots(figsize=(17,10),dpi=100)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.set(xlim=(0,17),ylim=(0,10));ax.axis('off')
    labels=[]
    def text(x,y,s,**kw):
        artist=ax.text(x,y,s,ha=kw.pop('ha','center'),va='center',**kw)
        labels.append(artist);return artist
    def box(x,y,w,h,color):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02',
                                   facecolor=color,edgecolor='#46617a',linewidth=1.2))
    def arrow(a,b,label,above=.28):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':2.1,'color':'#24485f'})
        text((a[0]+b[0])/2,(a[1]+b[1])/2+above,label,fontsize=18)
    text(8.5,9.52,'The original linear normal class: an exact receiving correspondence',fontsize=24,fontweight='bold')
    text(8.5,9.08,'Faithful orthogonal action with the entire supplied spin-c lift; original degree q',fontsize=18)
    box(.65,6.10,15.7,2.48,'#eef4fb')
    text(.96,8.24,'A. Both full inverse products — LINR.2–LINR.4',ha='left',fontweight='bold')
    box(1.12,6.72,4.30,.85,'#ffffff');box(6.70,6.72,3.60,.85,'#ffffff');box(11.56,6.72,4.30,.85,'#ffffff')
    text(3.27,7.15,r'$R\,\widehat\otimes\,C_q$',fontsize=24)
    text(8.50,7.15,r'$A_r$',fontsize=25)
    text(13.71,7.15,r'$R\,\widehat\otimes\,C_q$',fontsize=24)
    arrow((5.50,7.15),(6.62,7.15),r'$\eta_r$')
    arrow((10.38,7.15),(11.48,7.15),r'$\delta_r$')
    text(8.5,6.38,r'$\eta_r\delta_r=1_{R\widehat\otimes C_q}\qquad\delta_r\eta_r=1_{A_r}$',fontsize=20)
    box(.65,3.20,15.7,2.52,'#eef8f1')
    text(.96,5.38,'B. All scalar classes and the original positive disk — LINR.5–LINR.11',ha='left',fontweight='bold')
    text(8.5,4.80,r'$\xi=\delta_r(\kappa\widehat\otimes1_{C_q})\quad\longleftrightarrow\quad\eta_r\xi=\kappa\widehat\otimes1_{C_q}$',fontsize=23)
    text(8.5,4.25,r'$b\xi=1_{C_q}\quad\Longleftrightarrow\quad [i]\xi=\delta\quad\Longleftrightarrow\quad [u]\kappa=1$',fontsize=22)
    text(8.5,3.70,r'$\Pi(a u_g)=(\pi(a)U_g)\widehat\otimes V_g,\qquad\|\Pi(f)\|\leq\|f\|_r$',fontsize=22)
    text(8.5,3.39,'The product phase supplies scalar compact defects on the whole balanced carrier.',fontsize=17)
    box(.65,.68,15.7,2.13,'#fff4e7')
    text(.96,2.49,'C. The full inverse line remains — Theorem 7.17 and LINR.12',ha='left',fontweight='bold')
    text(8.5,1.99,r'$k_q=q(q-1)/2,\quad c_{\mathrm{phys}}(e_j)=(-1)^{k_q+1}L_{t_j},\quad zs\mapsto z^{-1}\rho_t(s)$',fontsize=21)
    text(8.5,1.51,'Rank-two character twist: z = i becomes −i; the inverse phase −i becomes i.',fontsize=19)
    text(8.5,1.05,'Both inverse determinant phases equal −1. They miss the full character twist.',fontsize=19)
    text(8.5,.26,'Exact linear-model test. Arbitrary original holonomy and its graph construction remain unfinished.',fontsize=17,color='#33495a')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer();width,height=fig.canvas.get_width_height()
    for label in labels:
        b=label.get_window_extent(renderer)
        assert 8<=b.x0 and b.x1<=width-8 and 8<=b.y0 and b.y1<=height-8,label.get_text()
    png,svg=BytesIO(),BytesIO()
    fig.savefig(png,format='png',dpi=100,metadata={'Software':'NCG LINR original CC0 generator'})
    fig.savefig(svg,format='svg',metadata={'Date':None,'Creator':'NCG LINR original CC0 generator'})
    result={'png':png.getvalue(),'svg':svg.getvalue()}
    if output is not None:
        output.mkdir(parents=True,exist_ok=True)
        for ext,raw in result.items():
            (output/('linear-normal-receiving-equivalence.'+ext)).write_bytes(raw)
    plt.close(fig)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures')
    draw(parser.parse_args().output)
