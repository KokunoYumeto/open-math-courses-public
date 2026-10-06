from pathlib import Path
import json,argparse,os
os.environ['MPLBACKEND']='Agg'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'L120-first-corner-v1'})
E=Path(__file__).resolve().parent
def build(out):
 out.mkdir(parents=True,exist_ok=True)
 h=[0,1,3,7]; labels=[[h[j]-h[i] for j in range(4)] for i in range(4)]
 spectrum=sorted({x for r in labels for x in r})
 # Integer matrices prove the finite partial-isometry identities exactly.
 p=np.diag([int(i==0) for i in range(4) for j in range(4)])
 q=np.diag([int(j==0) for i in range(4) for j in range(4)])
 r=np.diag([int(i==0 and j==0) for i in range(4) for j in range(4)])
 v=np.zeros((16,16),dtype=int)
 for i in range(4):v[4*i, i]=1
 assert np.array_equal(v.T@v,p) and np.array_equal(v@v.T,q)
 assert np.array_equal(v@r,r) and np.array_equal(r@v,r)
 data={'model':'finite coordinate restriction of B(ell2(I)); not a proof of unrestricted cardinal classification','basis_order':[[i,j] for i in range(4) for j in range(4)],'frequencies':h,'negative_label_matrix_hj_minus_hi':labels,'before_action_spectrum':spectrum,'after_action_spectrum':[0],'p_support':[[0,i] for i in range(4)],'q_support':[[i,0] for i in range(4)],'r_support':[[0,0]],'v_exact_integer_matrix':v.tolist(),'checks':{'v_star_v_equals_p':True,'v_v_star_equals_q':True,'vr_equals_rv_equals_r':True},'arbitrary_cardinal_statement':'The same basis rule on arbitrary infinite I extends by Hilbert completion; |I minus {0}|=|I|. See CI2 and PC0.'}
 (out/'first-corner-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
 fig,axs=plt.subplots(2,2,figsize=(16,11),dpi=180)
 fig.patch.set_facecolor('#f6f8fa')
 fig.suptitle('The amplification must fix its first corner',fontsize=23,fontweight='bold',y=.985)
 def grid(ax,title,active):
  ax.set_title(title,fontsize=15,fontweight='bold',pad=14)
  for i in range(4):
   for j in range(4):
    col='#c8e9f2' if (i,j) in active else '#ffffff'
    if i==j==0:col='#ffe09a'
    ax.add_patch(Rectangle((j,3-i),1,1,facecolor=col,edgecolor='#536474',linewidth=1.5))
    ax.text(j+.5,3-i+.5,f'({i},{j})',ha='center',va='center',fontsize=13,fontweight='bold' if i==j==0 else 'normal')
  ax.set_xlim(-.7,4.3);ax.set_ylim(-.8,4.5);ax.set_aspect('equal');ax.axis('off')
  ax.text(2,4.18,'second coordinate j',ha='center',fontsize=11)
  ax.text(-.42,2,'first coordinate i',rotation=90,ha='center',va='center',fontsize=11)
 grid(axs[0,0],'Initial projection p = a ⊗ 1',set(map(tuple,data['p_support'])))
 grid(axs[0,1],'Final projection q = 1 ⊗ a',set(map(tuple,data['q_support'])))
 axs[0,0].text(1.8,-.52,'p−r: (0,1), (0,2), (0,3)',ha='center',fontsize=12,color='#19566e')
 axs[0,1].text(1.8,-.52,'q−r: (1,0), (2,0), (3,0)',ha='center',fontsize=12,color='#19566e')
 fig.text(.50,.56,'v : (0,i) ↦ (i,0)     •     r = (0,0) is fixed exactly',ha='center',fontsize=16,fontweight='bold',bbox=dict(boxstyle='round,pad=.45',facecolor='#fff2cd',edgecolor='#bb9437'))
 ax=axs[1,0];ax.set_title('Exact negative labels: hⱼ − hᵢ',fontsize=15,fontweight='bold',pad=12)
 for i in range(4):
  for j in range(4):
   ax.add_patch(Rectangle((j,3-i),1,1,facecolor='#ffe09a' if i==j else '#e2edf3',edgecolor='#536474'))
   ax.text(j+.5,3-i+.5,str(labels[i][j]),ha='center',va='center',fontsize=17)
 for i,x in enumerate(h):
  ax.text(-.15,3-i+.5,str(x),ha='right',va='center');ax.text(i+.5,4.1,str(x),ha='center')
 ax.set_xlim(-.7,4.3);ax.set_ylim(-.7,4.6);ax.set_aspect('equal');ax.axis('off')
 ax.text(2,-.4,'Eigenphase of Eᵢⱼ: exp(it(hᵢ−hⱼ))',ha='center',fontsize=12)
 ax=axs[1,1];ax.set_title('Cancel Uₜ with the cocycle uₜ = Uₜ*',fontsize=15,fontweight='bold',pad=12)
 ax.axhline(1,color='#50677a',linewidth=1);ax.axhline(0,color='#50677a',linewidth=1)
 ax.scatter(spectrum,[1]*len(spectrum),s=75,color='#206e88',zorder=3)
 ax.scatter([0],[0],s=110,color='#a77400',zorder=3)
 ax.text(0,1.33,'Sp(α) in the four-coordinate model',ha='center',fontsize=12)
 ax.text(0,-.32,'Sp(αᵘ) = Sp(αᵃ) = Γ(α) = {0}',ha='center',fontsize=13,fontweight='bold')
 ax.set_xlim(-8,8);ax.set_ylim(-.7,1.7);ax.set_xticks(range(-7,8));ax.set_yticks([])
 ax.set_xlabel('character label for G = ℝ',labelpad=8)
 for spine in ax.spines.values():spine.set_visible(False)
 fig.subplots_adjust(top=.91,bottom=.12,left=.06,right=.97,hspace=.42,wspace=.22)
 fig.text(.5,.055,'Four coordinates illustrate the exact maps. For arbitrary infinite I, finite-vector approximation proves continuity;',ha='center',fontsize=12)
 fig.text(.5,.028,'the local sigma-finite-center covering bound and central assembly prove the cardinal comparison.  TR1–2 • CA/HF • LC1–4 • FC4–5 • CI1–3',ha='center',fontsize=11)
 # Check visible text boxes against the canvas after real font/layout rendering.
 fig.canvas.draw();renderer=fig.canvas.get_renderer();w,H=fig.canvas.get_width_height()
 boxes=[]
 for text in fig.findobj(matplotlib.text.Text):
  if text.get_visible() and text.get_text():
   b=text.get_window_extent(renderer);assert b.x0>=-1 and b.y0>=-1 and b.x1<=w+1 and b.y1<=H+1,(text.get_text(),b,w,H)
   boxes.append({'text':text.get_text(),'bounds_pixels':[round(x,3) for x in [b.x0,b.y0,b.x1,b.y1]]})
 (out/'figure-layout-check.json').write_text(json.dumps({'all_visible_text_within_canvas':True,'canvas':[w,H],'text_bounds':boxes},indent=2)+'\n',encoding='utf8')
 fig.savefig(out/'first-corner.png',dpi=180,metadata={'Software':'L120 exact renderer'})
 fig.savefig(out/'first-corner.svg',metadata={'Date':None,'Creator':'L120 exact renderer'})
 plt.close(fig)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=E/'assets');build(p.parse_args().output)
