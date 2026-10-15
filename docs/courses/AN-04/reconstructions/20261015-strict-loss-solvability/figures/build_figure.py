"""Reproduce exact loss coordinates and discrete logarithmic majorants."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans','svg.hashsalt':'AN04-SLS-exact'})
fig,axes=plt.subplots(2,1,figsize=(11,7.6),gridspec_kw={'height_ratios':[1,1.3]})
ax=axes[0];threshold=F(-1,6);target=F(-5,12)
ax.axvspan(-.85,float(threshold),color='#e1f1eb')
ax.plot([-.85,.3],[.85,-.3],color='#196576',label=r'adjoint measuring order $r=-t$')
ax.axvline(float(threshold),color='#a63e30',linestyle='--')
ax.plot([float(threshold)],[-float(threshold)],'o',mfc='white',mec='#a63e30',ms=8,zorder=4)
ax.plot([float(target)],[-float(target)],'o',color='#196576')
ax.annotate('target t = -5/12\nr = 5/12',xy=(float(target),-float(target)),xytext=(-.77,.15),arrowprops={'arrowstyle':'->','color':'#196576'})
ax.annotate('excluded threshold t = -1/6',xy=(float(threshold),-.15),xytext=(-.1,.72),arrowprops={'arrowstyle':'->','color':'#a63e30'})
ax.annotate('',xy=(float(target),-.2),xytext=(float(threshold),-.2),arrowprops={'arrowstyle':'<->'})
ax.text(float((target+threshold)/2),-.28,'gap = 1/4',ha='center',fontsize=10)
ax.set(xlim=(-.85,.3),ylim=(-.36,.9),xlabel='solution order t',ylabel='adjoint order r',
 title='Exact orders for m = 3/2, s = -2/3; admissible targets are shaded')
ax.grid(alpha=.16)
ax.text(-.78,.59,'r = -t',color='#196576',fontsize=10)
ax=axes[1];js=list(range(1,10))
ax.plot(js,[-j*j+2*j for j in js],'o-',color='#196576',label=r'second-derivative bound for $h_j$: $-j^2+2j$')
ax.plot(js,[-j for j in js],'s-',color='#759233',label=r'uniform bound for $g_j$: $-j$')
ax.plot(js,[j-1 for j in js],'^-',color='#a63e30',label=r'tested derivative Fourier coefficient: $j-1$')
ax.set(xlabel='integer j',ylabel='base-two logarithm',title='Exact discrete formulas: smooth summability needs derivative control')
ax.set_xticks(js);ax.grid(alpha=.16);ax.legend(loc='lower left',fontsize=9)
fig.tight_layout(pad=1.4)
out=root/'strict-loss-solvability.svg'
fig.savefig(out,metadata={'Date':None,'Title':'Strict loss, reciprocal orders and derivative tails','Creator':'Independent CC0 programme figure'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root.parent/'figure-check.json').write_text(json.dumps({
 'svg':'figures/strict-loss-solvability.svg','svg_sha256':sha(out),
 'generator_sha256':sha(Path(__file__)),'actually_inspected':False,
 'coordinates':{'m':'3/2','s':'-2/3','threshold':'-1/6','target':'-5/12','gap':'1/4','adjoint_order':'5/12'},
 'sequence_formulas':['-j*j+2*j','-j','j-1'],'sample_indices':js,
 'scope':'Exact rational coordinates and discrete logarithmic formulas; proof is in SLS:X1 and SLS:X3.',
 'independent_expression_licence':'CC0-1.0'},indent=2)+'\n',encoding='utf-8')
print('Wrote reproducible SVG with exact coordinates and formula checks.')
