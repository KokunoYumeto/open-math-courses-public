"""Original CC0 figure for the proved occupancy envelope, Lesson 7 (7.61).

The family adapts Gouillon's rounded construction (2003), thesis §§5.1 and5.3.2.
Samples illustrate the function; logarithmic convexity and rational
endpoint certificates in the lesson establish the full interval bound.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent.parent
C=3**(1/3)+1350**(-1/3)
def envelope(c):
    r=c**(1/6)
    return 2*(C+.452/r+.151/r**4)**2*(C+.00642*r*r)
cs=[math.exp(math.log(300)+j*(math.log(5000)-math.log(300))/200) for j in range(201)]
fig,ax=plt.subplots(figsize=(10,5.6),facecolor='white')
fig.subplots_adjust(left=.10,right=.965,bottom=.28,top=.82)
ax.plot(cs,[envelope(c) for c in cs],lw=2.6,color='#137875',label='Explicit upper envelope (7.61)')
ax.axhline(9.224,lw=1.5,color='#202936',ls='--',label='Certified bound: 9.224')
ax.axhline(250/27,lw=1.5,color='#b63b4a',ls=':',label=r'Occupancy threshold $250/27$')
ax.scatter([300,5000],[envelope(300),envelope(5000)],color='#137875',s=45,zorder=4)
ax.annotate('9.2236397…',(300,envelope(300)),xytext=(8,-25),textcoords='offset points',fontsize=10)
ax.annotate('8.8629166…',(5000,envelope(5000)),xytext=(-8,-25),textcoords='offset points',ha='right',fontsize=10)
ax.set_xscale('log')
ax.set_xticks([300,500,1000,2000,5000],[300,500,1000,2000,5000])
ax.set(xlim=(280,5400),ylim=(8.55,9.32),xlabel=r'Parameter $c_0$ (logarithmic axis)',ylabel=r'Upper bound for $(R+1)(S+1)(T+1)/N$')
ax.grid(alpha=.15)
ax.legend(loc='lower left',fontsize=9,frameon=True,facecolor='white')
fig.suptitle('Rounded boxes stay below the occupancy threshold',x=.10,y=.965,ha='left',fontsize=17,fontweight='bold',color='#202936')
fig.text(.10,.875,r'$C_*=\sqrt[3]{3}+1350^{-1/3},\quad r=c_0^{1/6},\quad F(r)=2(C_*+0.452/r+0.151/r^4)^2(C_*+0.00642r^2)$',fontsize=10.5)
fig.text(.10,.155,r'Positive Laurent coefficients make $F(e^u)$ convex. Its maximum on the interval is at an endpoint.',fontsize=10)
fig.text(.10,.105,'The certified bound implies g < 0.241 and ω < 0.946.\nAdapted from Nicolas Gouillon (2003), thesis §§5.1, 5.3.2. Full proof: Lesson 7, (7.59)–(7.62).\nCurve: numerical samples; proof: exact rational interval endpoint bounds and logarithmic convexity.',fontsize=9,color='#4e5865',linespacing=1.5,va='top')
target=root/'figures/gouillon-occupancy-envelope.png'
fig.savefig(target,dpi=160)
plt.close(fig)
print(str(target))
