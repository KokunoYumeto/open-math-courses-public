"""Exact two-order rotation diagram for YM-F03, equations F3.21--F3.23."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def build():
    out=Path(__file__).resolve().parents[1]/'figures'
    out.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                         'svg.hashsalt':'YM-F03-rotation-order-v1'})
    q3=np.array([[0,-1,0],[1,0,0],[0,0,1]])
    q1=np.array([[1,0,0],[0,0,-1],[0,1,0]])
    v=np.array([1,2,3])
    paths=[(v,q1@v,q3@q1@v),(v,q3@v,q1@q3@v)]
    assert all(int(w@w)==14 for path in paths for w in path)
    fig=plt.figure(figsize=(14,7.8),facecolor='#fffef9')
    fig.text(.04,.94,'The order of rotations changes the result',
             fontsize=23,weight='bold',color='#163e4b')
    fig.text(.04,.894,'Same initial vector, exact matrix products, common coordinate scales',
             fontsize=14,color='#354e55')
    colors=['#00786a','#bb6500','#6b3fa0']
    names=[['v',r'$Q_1v$',r'$Q_3Q_1v$'],['v',r'$Q_3v$',r'$Q_1Q_3v$']]
    r=np.sqrt(14)
    theta=np.linspace(0,2*np.pi,65)
    phi=np.linspace(0,np.pi,17)
    sphere=(r*np.outer(np.sin(phi),np.cos(theta)),
            r*np.outer(np.sin(phi),np.sin(theta)),
            r*np.outer(np.cos(phi),np.ones_like(theta)))
    for j,vs in enumerate(paths):
        ax=fig.add_axes([.025+.50*j,.205,.45,.61],projection='3d',facecolor='#fffef9')
        ax.set_title([r'$Q_1$ first, then $Q_3$',r'$Q_3$ first, then $Q_1$'][j],
                     fontsize=17,color='#163e4b',pad=6)
        ax.plot_wireframe(*sphere,rstride=2,cstride=8,color='#aebfc0',alpha=.35,linewidth=.55)
        for w,name,col in zip(vs,names[j],colors):
            ax.quiver(0,0,0,*w,color=col,linewidth=3,arrow_length_ratio=.13,normalize=False)
            ax.scatter(*w,color=col,s=27,depthshade=False)
            ax.text(*(w+np.array([.10,.10,.17])),name,color=col,fontsize=12)
        ax.scatter(0,0,0,color='#163e4b',s=20,depthshade=False)
        ax.set(xlim=(-4,4),ylim=(-4,4),zlim=(-4,4),
               xticks=[-3,0,3],yticks=[-3,0,3],zticks=[-3,0,3])
        ax.set_xlabel(r'$x^1$',labelpad=4)
        ax.set_ylabel(r'$x^2$',labelpad=4)
        ax.set_zlabel(r'$x^3$',labelpad=4)
        ax.set_box_aspect((1,1,1))
        ax.view_init(elev=22,azim=-56)
        ax.tick_params(labelsize=9,pad=0)
        for axis in (ax.xaxis,ax.yaxis,ax.zaxis):
            axis.pane.fill=False
            axis._axinfo['grid']['color']=(.6,.65,.65,.13)
        for k,(w,name,col) in enumerate(zip(vs,names[j],colors)):
            tup='('+', '.join(str(int(x)) for x in w)+')'
            fig.text(.07+.50*j,.186-.031*k,name+' = '+tup,color=col,fontsize=13)
    fig.text(.04,.052,r'All squared lengths are 14. The wire sphere has radius $\sqrt{14}$; arrows show the full vectors.',
             fontsize=12,color='#354e55')
    fig.text(.04,.019,'Coordinate projections of three-dimensional vectors. Source and proof: YM-F03, equations (F3.21)–(F3.23).',
             fontsize=11,color='#354e55')
    fig.savefig(out/'f03-rotation-order.svg',metadata={'Date':None,'Creator':'YM-GAUGE CC0 figure source'})
    fig.savefig(out/'f03-rotation-order.png',dpi=150,metadata={'Software':'YM-GAUGE CC0 figure source'})
    plt.close(fig)
    svg=out/'f03-rotation-order.svg'
    s=svg.read_text(encoding='utf-8')
    start=s.index('<svg ');end=s.index('>',start)
    s=s[:end]+' role="img" aria-labelledby="f03-title f03-desc"'+s[end:]
    end=s.index('>',start)
    s=s[:end+1]+'''\n<title id="f03-title">Two orders of orthogonal rotations on one vector</title>
<desc id="f03-desc">Left: (1,2,3) maps under Q1 to (1,-3,2), then under Q3 to (3,1,2). Right: (1,2,3) maps under Q3 to (-2,1,3), then under Q1 to (-2,-3,1). Arrows run from the origin to these exact vectors. Both projections use equal coordinate scales and the same view. The sphere radius is square root of 14.</desc>'''+s[end+1:]
    svg.write_text(s,encoding='utf-8')

if __name__=='__main__':
    build()
