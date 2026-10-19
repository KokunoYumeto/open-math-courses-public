"""Radial kernels and dilation defects. Original code/data/figure, CC0 1.0.

GPT-6.1 Sol (OpenAI), October2026.
https://creativecommons.org/publicdomain/zero/1.0/
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
def main():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'homogeneous-elliptic-L213'})
    u=np.linspace(-1.5,1.5,1001)
    fig,axes=plt.subplots(1,2,figsize=(12.5,5.5))
    axes[0].plot(u,-u,color='#357da5',lw=2.2,label=r'$2\pi E_2(re_1)=-u$')
    axes[0].plot(u,np.exp(-u),color='#3d8b64',lw=2.2,label=r'$4\pi E_3(re_1)=e^{-u}$')
    axes[0].set(title='Normalized radial profiles',xlabel=r'$u=\log r$',ylabel='Normalized kernel value',ylim=(-1.8,4.8))
    axes[1].plot(u,-u,color='#357da5',lw=2.2,label=r'$2\pi(E_2(te_1)-E_2(e_1))=-u$')
    axes[1].plot(u,np.zeros_like(u),color='#3d8b64',lw=2.2,label=r'$4\pi(tE_3(te_1)-E_3(e_1))=0$')
    axes[1].set(title='Defect after the homogeneous rescaling',xlabel=r'$u=\log t$',ylabel='Normalized dilation defect',ylim=(-1.8,1.8))
    for a in axes:
        a.set_xlim(-1.5,1.5);a.grid(alpha=.15);a.legend(fontsize=9,loc='upper right')
        a.axvline(0,color='#aaaaaa',lw=.7,zorder=0)
    fig.text(.5,.025,r'$E_2(x)=-\log|x|/(2\pi)$ in two dimensions;  $E_3(x)=1/(4\pi|x|)$ in three dimensions.',
      ha='center',fontsize=11)
    fig.subplots_adjust(left=.07,right=.985,bottom=.18,top=.88,wspace=.25)
    fig.savefig(OUT/'radial-kernels-and-dilation-defect.png',dpi=160,metadata={'Software':'Radial elliptic kernels and exact dilation formulas'})
    p=OUT/'radial-kernels-and-dilation-defect.svg'
    fig.savefig(p,metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI),October2026;CC0 1.0'})
    p.write_bytes(('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n').encode())
    plt.close(fig)
    data={'chapter':'Homogeneous elliptic kernels and logarithmic scaling','creator':'GPT-6.1 Sol (OpenAI),October2026',
      'license':'CC0-1.0','proof_locators':['Theorem3.1','Example4.1','equations4.1-4.2'],
      'operators':'Minus the Laplacian, in two and three dimensions respectively',
      'kernels':{'E2':'-log(|x|)/(2*pi)','E3':'1/(4*pi*|x|)'},
      'left':{'horizontal':'u=log(r)','curves':['2*pi*E2(r*e1)=-u','4*pi*E3(r*e1)=exp(-u)']},
      'right':{'horizontal':'u=log(t)','curves':['2*pi*(E2(t*e1)-E2(e1))=-u','4*pi*(t*E3(t*e1)-E3(e1))=0']},
      'horizontal_range_exact':['-3/2','3/2'],'samples':1001,
      'scope':'Curves sample the exact displayed formulas; the two kernels act in different dimensions. The all-symbol scaling theorem is proved in the chapter,not inferred from this picture.'}
    (HERE/'dilation-data.json').write_bytes((json.dumps(data,indent=2)+'\n').encode())
    print(json.dumps({'status':'FIGURE_GENERATED','PNG':1,'SVG':1,'panels':2}))
if __name__=='__main__':main()
