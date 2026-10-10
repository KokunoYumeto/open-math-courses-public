from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
F=Path(__file__).resolve().parents[1]/'figures'
def build():
    plt.rcParams.update({'svg.hashsalt':'YM-GAUGE-F09-differences','svg.fonttype':'none','font.size':11})
    plt.rcParams.update({'font.size':12,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
    fig,axs=plt.subplots(1,2,figsize=(12,5.4),layout='constrained')
    theta=np.linspace(0,2*np.pi,500)
    axs[0].plot(np.cos(theta),np.sin(theta),color='#b9c5cc',lw=1.5)
    a=np.pi/6;b=5*np.pi/6
    x=np.cos([a,b]);y=np.sin([a,b])
    axs[0].plot(x,y,'o-',color='#146b80',lw=3)
    arc=np.linspace(a,b,200)
    axs[0].plot(np.cos(arc),np.sin(arc),color='#aa4c13',lw=3)
    axs[0].text(0,.37,'Chord = √3',ha='center',color='#146b80')
    axs[0].text(0,1.14,'Arc = 2π/3',ha='center',color='#aa4c13')
    axs[0].annotate('exp(iπ/6)',(x[0],y[0]),xytext=(7,-23),textcoords='offset points',ha='center')
    axs[0].annotate('exp(5iπ/6)',(x[1],y[1]),xytext=(-7,-23),textcoords='offset points',ha='center')
    axs[0].axhline(0,color='#c4cbd0',lw=.8);axs[0].axvline(0,color='#c4cbd0',lw=.8)
    axs[0].set(xlim=(-1.35,1.35),ylim=(-1.2,1.35),aspect='equal',xlabel='Real part',ylabel='Imaginary part',title='The exact unitary difference at x = 0')
    delta=np.linspace(0,2*np.pi,500)
    axs[1].plot(delta,2*np.abs(np.sin(delta/2)),color='#146b80',lw=2,label='Exact operator distance  2|sin(δ/2)|')
    axs[1].plot(delta,delta,color='#aa4c13',lw=2,label='Integral bound  |δ|')
    axs[1].scatter([2*np.pi/3],[np.sqrt(3)],color='#146b80')
    axs[1].set(xlabel='Actual phase difference δ (radians)',ylabel='Operator norm of U − U′',title='The bound keeps the full matrix difference')
    axs[1].legend(loc='upper left',fontsize=10)
    axs[1].set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','π/2','π','3π/2','2π'])
    fig.suptitle('Anchored temporal gauge: exact commuting diagnostic (GD.13–GD.14)',fontsize=15)
    for ext in ('svg','png'):fig.savefig(F/('f09-gauge-difference.'+ext),dpi=160,metadata={'Date':None} if ext=='svg' else {'Software':'YM-GAUGE reproducible figure'})
    plt.close(fig)
if __name__=='__main__':build()
