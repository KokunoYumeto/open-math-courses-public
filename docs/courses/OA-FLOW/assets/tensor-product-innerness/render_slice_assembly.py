"""Original exact CC0 slice-cancellation and central-assembly diagram."""
from pathlib import Path
import argparse,json
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figure');args=ap.parse_args();args.output.mkdir(parents=True,exist_ok=True)
d=s.diag(1,-1);flip=s.Matrix([[0,1],[1,0]]);u=s.kronecker_product(d,d)
sl1=s.Matrix(2,2,lambda i,j:u[2*i,2*j]);sl2=s.Matrix(2,2,lambda i,j:u[2*i+1,2*j+1]);assert sl1==d and sl2==-d and (sl1+sl2)/2==s.zeros(2)
a1=s.diag(d,s.zeros(2));a2=s.diag(s.zeros(2),flip);w=a1+a2;p1=s.diag(1,1,0,0);p2=s.eye(4)-p1
assert u*u.H==s.eye(4) and a1.H*a1==a1*a1.H==p1 and a2.H*a2==a2*a2.H==p2 and p1*p2==s.zeros(4) and w*w.H==w.H*w==s.eye(4)
for block in range(2):
 for i in range(2):
  for j in range(2):
   x=s.zeros(4);x[2*block+i,2*block+j]=1
   assert a1*x==w*x*w.H*a1 and a2*x==w*x*w.H*a2
data={'d':s.matrix2numpy(d,dtype=int).tolist(),'s':s.matrix2numpy(flip,dtype=int).tolist(),'tensor_unitary':s.matrix2numpy(u,dtype=int).tolist(),'vector_state_slices':[s.matrix2numpy(sl1,dtype=int).tolist(),s.matrix2numpy(sl2,dtype=int).tolist()],'normalized_trace_slice':[[0,0],[0,0]],'central_supports':[s.matrix2numpy(p1,dtype=int).tolist(),s.matrix2numpy(p2,dtype=int).tolist()],'assembled_unitary':s.matrix2numpy(w,dtype=int).tolist(),'eight_block_matrix_units_verified':True,'scope':'Exact finite examples IC5; IC0–IC4 prove the full arbitrary-algebra theorem.'}
(args.output/'slice-assembly-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
plt.rcParams.update({'font.family':'DejaVu Sans','svg.hashsalt':'oa-flow-L123-slice-assembly','mathtext.fontset':'dejavusans'})
blue='#225C7A';teal='#17857F';gold='#A47417';gray='#52636D';bg='#F7FAFC'
fig=plt.figure(figsize=(14,9),dpi=200,facecolor=bg);ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,9));ax.axis('off');texts=[]
def tx(x,y,t,fs=15,c=blue,**kw):texts.append(ax.text(x,y,t,fontsize=fs,color=c,**kw))
def box(x,y,width,height,t,c=blue,fs=16):
 ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.10',facecolor='white',edgecolor=c,lw=1.5));tx(x+width/2,y+height/2,t,fs,c,ha='center',va='center')
def arrow(start,end,c=teal):ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','lw':2,'color':c})
tx(.55,8.48,'Choose separating slices; assemble central supports',23,weight='bold')
tx(.55,8.02,r'Exact examples with $d=\mathrm{diag}(1,-1)$ and $s e_1=e_2,\ s e_2=e_1$.',14,gray)
tx(.55,7.46,'A  Averaging two useful slices can give zero',17,weight='bold')
box(.65,5.65,4.1,1.1,r'$u=d\otimes d$'+'\n'+r'$\mathrm{diag}(1,-1,-1,1)$',fs=17)
box(8.0,6.75,5.1,.6,r'$\omega_{e_1}$ slice $=d$',teal)
box(8.0,5.55,5.1,.6,r'$\omega_{e_2}$ slice $=-d$',teal)
box(8.0,4.35,5.1,.6,r'$\tau=\frac{1}{2}(\omega_{e_1}+\omega_{e_2})$ slice $=0$',gold,15)
arrow((4.95,6.50),(7.75,7.03));arrow((4.95,6.17),(7.75,5.87));arrow((4.95,5.84),(7.75,4.65),gold)
tx(.70,4.75,'The implementer is unitary.\nThe predetermined trace loses it.',14,gray)
tx(.55,3.72,'B  Orthogonal central pieces retain their local implementers',17,weight='bold')
box(.7,2.03,3.3,1.08,r'$a_1=(d,0)$'+'\n'+r'$a_1^*a_1=a_1a_1^*=p_1$',teal,15)
box(5.35,2.03,3.3,1.08,r'$a_2=(0,s)$'+'\n'+r'$a_2^*a_2=a_2a_2^*=p_2$',teal,15)
tx(4.67,2.48,'+',25,teal,ha='center')
arrow((8.9,2.55),(10.05,2.55))
box(10.25,2.03,3.02,1.08,r'$w=(d,s)$'+'\n'+r'$w^*w=ww^*=1$',blue,15)
tx(7,1.35,r'$p_1p_2=0,\quad p_1+p_2=1,\qquad \operatorname{Ad}(w)=\operatorname{Ad}(d)\oplus\operatorname{Ad}(s)$',17,ha='center')
tx(.55,.66,'General proof: IC1 gives central supports; IC2 disjointifies any family and sums its polar parts.',12,gray)
tx(.55,.30,'IC3 constructs separating normal state slices. IC4 proves their supports fill the identity. IC5 checks these examples.',11,gray)
fig.canvas.draw();ren=fig.canvas.get_renderer();width,height=fig.canvas.get_width_height()
for t in texts:
 b=t.get_window_extent(ren);assert 0<=b.x0<=b.x1<=width and 0<=b.y0<=b.y1<=height,(t.get_text(),tuple(b.bounds))
fig.savefig(args.output/'slice-assembly.png',dpi=200,facecolor=bg,metadata={'Software':'L123 exact renderer'})
fig.savefig(args.output/'slice-assembly.svg',facecolor=bg,metadata={'Date':None})
plt.close(fig);print(json.dumps({'passed':True,'pixels':[width,height],'exact_model':True,'labels':len(texts)}))
