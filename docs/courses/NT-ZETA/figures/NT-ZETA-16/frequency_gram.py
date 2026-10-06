"""Original CC0 figure of the exact normalized frequency Gram matrix."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':24,'axes.titlesize':28,'axes.labelsize':26})
indices=np.arange(1,17,dtype=float)
logratio=np.log(indices[:,None]/indices[None,:])
fig,axes=plt.subplots(1,2,figsize=(12,5.6),layout='constrained')
for ax,T in zip(axes,(10,100)):
    gram=np.abs(np.sinc(T*logratio/(2*np.pi)))
    assert np.all(np.diag(gram)==1)
    im=ax.imshow(gram,origin='lower',extent=(.5,16.5,.5,16.5),vmin=0,vmax=1,cmap='viridis',interpolation='nearest')
    ax.set(title=f'T = {T}',xlabel='n',ylabel='m',xticks=[1,4,8,12,16],yticks=[1,4,8,12,16])
fig.colorbar(im,ax=axes,shrink=.82,label='Absolute correlation',ticks=[0,.5,1])
fig.savefig(root/'frequency_gram.png',dpi=180)
plt.close(fig)
