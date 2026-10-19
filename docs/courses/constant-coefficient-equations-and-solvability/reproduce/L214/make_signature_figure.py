"""Exact normalized cone source coefficients. Original code/data/figure, CC0.

GPT-6.1 Sol (OpenAI), October2026.
https://creativecommons.org/publicdomain/zero/1.0/
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap,BoundaryNorm
from matplotlib.patches import Rectangle
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
CYCLE=[0,1,0,-1]
def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'quadratic-signature-L214'})
    plus=np.ma.masked_all((9,9));minus=np.ma.masked_all((9,9));rows=[]
    for p in range(9):
        for q in range(9):
            if 3<=p+q<=8:
                plus[p,q]=CYCLE[p%4];minus[p,q]=-CYCLE[q%4]
                rows.append({'n':p+q,'positive_squares':p,'negative_squares':q,
                  'positive_cone_source_normalized':CYCLE[p%4],
                  'negative_cone_source_normalized':-CYCLE[q%4],
                  'upper_boundary_phase':['1','-i','-1','i'][q%4],
                  'lower_boundary_phase':['1','i','-1','-i'][q%4]})
    cmap=ListedColormap(['#6794b4','#e5eaed','#d7a16b']);cmap.set_bad('white')
    norm=BoundaryNorm([-1.5,-.5,.5,1.5],3)
    fig,axes=plt.subplots(1,2,figsize=(12.5,6.2))
    for ax,data,title in [(axes[0],plus,r'Positive sign cone: $\sin(\pi p/2)$'),
      (axes[1],minus,r'Negative sign cone: $-\sin(\pi q/2)$')]:
        ax.imshow(data,origin='lower',cmap=cmap,norm=norm,interpolation='nearest')
        for p in range(9):
            for q in range(9):
                if not data.mask[p,q]:
                    v=int(data[p,q]);ax.text(q,p,'+1' if v==1 else str(v),ha='center',va='center',fontsize=11)
        ax.add_patch(Rectangle((1.5,1.5),1,1,fill=False,edgecolor='#222222',linewidth=2))
        ax.set_xticks(range(9));ax.set_yticks(range(9))
        ax.set(xlabel=r'Negative squares $q$',ylabel=r'Positive squares $p$',title=title)
        ax.set_xticks(np.arange(-.5,9,1),minor=True);ax.set_yticks(np.arange(-.5,9,1),minor=True)
        ax.grid(which='minor',color='white',linewidth=1);ax.tick_params(which='minor',bottom=False,left=False)
    fig.text(.5,.055,r'Multiply by $4\pi^{(n-2)/2}|\det A|^{-1/2}$;  $n=p+q$.  Displayed dimensions: $3\leq n\leq8$.',
      ha='center',fontsize=11)
    fig.text(.5,.012,'Outlined signature (2,2): both cone layers have zero source; boundary-value inverses still exist.',
      ha='center',fontsize=10)
    fig.subplots_adjust(left=.07,right=.985,top=.88,bottom=.18,wspace=.25)
    fig.savefig(OUT/'signature-and-cone-source-coefficients.png',dpi=160,
      metadata={'Software':'Exact quadratic signature source coefficients'})
    path=OUT/'signature-and-cone-source-coefficients.svg'
    fig.savefig(path,metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI),October2026;CC0 1.0'})
    path.write_bytes(('\n'.join(x.rstrip() for x in path.read_text(encoding='utf-8').splitlines())+'\n').encode())
    plt.close(fig)
    data={'chapter':'Quadratic boundary kernels and signature phases','creator':'GPT-6.1 Sol (OpenAI),October2026',
      'license':'CC0-1.0','proof_locators':['Theorem1.1,equation1.5','Theorem4.1,equation4.5','Example7.2'],
      'normalization':'4*pi^((n-2)/2)*abs(det(A))^(-1/2)',
      'positive_cone_source':'sin(pi*p/2)','negative_cone_source':'-sin(pi*q/2)',
      'integers_generated_by_exact_cycle':[0,1,0,-1],
      'dimensions_included':[3,4,5,6,7,8],'all_signatures_for_these_dimensions_included':True,
      'entries':rows,'scope':'Exact coefficient tables,not pointwise kernel plots. Zero sine coefficients do not mean that the always nonzero boundary-value source coefficient vanishes.'}
    (HERE/'signature-coefficients.json').write_bytes((json.dumps(data,indent=2)+'\n').encode())
    print(json.dumps({'status':'FIGURE_GENERATED','PNG':1,'SVG':1,'exact_signature_pairs':len(rows)}))
if __name__=='__main__':main()
