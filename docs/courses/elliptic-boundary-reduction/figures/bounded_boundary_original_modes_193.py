"""CC0 figure of exact original roots and bounded components; no coordinate substitution."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
A=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
ax=axes[0];ax.axhline(0,color='#555555',lw=.8);ax.axvline(0,color='#555555',lw=.8)
ax.scatter([0],[0],s=85,color='#24659e',zorder=5);ax.scatter([1],[-1],s=85,color='#b75030',marker='x',zorder=5)
ax.annotate('Original root 0\nAlgebraic multiplicity 2\nBounded dimension 1',(0,0),xytext=(-.86,.4),fontsize=11,arrowprops=dict(arrowstyle='-',color='#24659e'))
ax.annotate('Auxiliary root 1 − i\nAlgebraic multiplicity 2\nBounded dimension 0',(1,-1),xytext=(.12,-1.85),fontsize=11,arrowprops=dict(arrowstyle='-',color='#b75030'))
ax.set(xlim=(-1,1.9),ylim=(-2.05,1.1),xlabel='Re z',ylabel='Im z',title='Full determinant: 3 z² (z + iλ)²');ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.15)
ax=axes[1];t=np.linspace(0,4,101)
ax.plot(t,np.ones_like(t),color='#24659e',lw=2,label='Re U₀ = 1')
ax.plot(t,-np.ones_like(t),color='#b75030',lw=2,label='Im U₁ = −1')
ax.plot(t,np.zeros_like(t),color='#555555',lw=1.6,ls='--',label='Im U₀ = Re U₁ = 0')
ax.set(xlim=(0,4),ylim=(-1.5,1.5),xlabel='Original time t',ylabel='Exact component value',title='Bounded lift U = (1, −i)');ax.grid(alpha=.18);ax.legend(loc='center right',fontsize=10)
fig.suptitle('Original p(z) = 3 z²;  λ = 1 + i;  τ = i',fontsize=15)
fig.savefig(A/'bounded-boundary-original-modes.png',dpi=175)
(A/'bounded-boundary-original-modes-parameters.json').write_text(json.dumps(dict(license='CC0-1.0',original_polynomial='3 z^2',leading_coefficient=3,lambda_real=1,lambda_imag=1,tau_real=0,tau_imag=1,root_coordinates=[[0,0],[1,-1]],root_algebraic_multiplicities=[2,2],bounded_dimensions=[1,0],exact_U0=[1,0],exact_U1=[0,-1],time_interval=[0,4],proof_locators=['SB4','SB19','SB21','SB28'],numerical_proof_claim=False),indent=2)+'\n',encoding='utf-8')
plt.close(fig)
