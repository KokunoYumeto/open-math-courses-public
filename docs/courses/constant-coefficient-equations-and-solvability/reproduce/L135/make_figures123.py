"""Exact half-space Green kernels and ball inversion diagrams (original CC0)."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'mathtext.fontset':'dejavusans','svg.fonttype':'none',
                     'svg.hashsalt':'AN02-L135-Green-Riesz',
                     'axes.spines.top':False,'axes.spines.right':False})
BLUE,PURPLE,ORANGE,GREEN='#2166ac','#7b3294','#c56c12','#16815c'

def green2(z,t,eta=.6,s=1.2):
    numerator=(np.asarray(z)-eta)**2+(np.asarray(t)-s)**2
    denominator=(np.asarray(z)-eta)**2+(np.asarray(t)+s)**2
    with np.errstate(divide='ignore'):
        return np.log(numerator/denominator)/(4*np.pi)
def poisson2(z,t,eta=0.):
    return np.asarray(t)/(np.pi*((np.asarray(z)-eta)**2+np.asarray(t)**2))
def inversion(y):
    v=np.asarray(y,dtype=float)+np.array([0.,1.])
    return -np.array([0.,1.])+2*v/np.dot(v,v)

geometry={
 'dimension':2,'kernel_convention':'Delta E_2 = delta_0; E_2=log(r)/(2*pi)',
 'source':[.6,1.2],'reflected_source':[.6,-1.2],'observation':[-.8,1.6],
 'source_distance_squared':2.12,'reflected_distance_squared':9.8,
 'green_formula':'log(((z-.6)^2+(t-1.2)^2)/((z-.6)^2+(t+1.2)^2))/(4*pi)',
 'green_sample_domain':{'z':[-3,3],'t':[0,3.6]},'green_color_lower_clip':-.55,
 'poisson_sample':'P((0,1),eta)=1/(pi*(1+eta^2)); whole-line integral=1',
 'poisson_plot_window':[-5,5],
 'ball_inversion':'T(y)=-e+2*(y+e)/|y+e|^2, e=(0,1)',
 'sphere_atoms':[{'point':[0,1],'mass':1,'boundary_point':0,'boundary_mass':.5},
                 {'point':[1,0],'mass':1,'boundary_point':1,'boundary_mass':1},
                 {'point':[0,-1],'mass':'pi/2','image':'infinity','height_coefficient':.25}],
 'positive_harmonic_example':'u=P(x,0)/2+P(x,1)+t/4; v=-u satisfies the source upper bound',
 'harmonic_slice_height':1,'height_coefficient':.25,
 'proof_locators':['GR3','GR8','GR10','GR11 Examples 1-2']}
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')

fig=plt.figure(figsize=(15,6.2),layout='constrained')
grid=fig.add_gridspec(1,3,width_ratios=[1.05,1.25,1])
ax=fig.add_subplot(grid[0,0]);field=fig.add_subplot(grid[0,1]);density=fig.add_subplot(grid[0,2])
ax.set_aspect('equal');ax.set_xlim(-2.1,2.0);ax.set_ylim(-1.85,2.35)
ax.axhspan(0,2.35,color='#edf4fa');ax.axhline(0,color='#333333',linewidth=1.5)
x=np.array([-.8,1.6]);y=np.array([.6,1.2]);ystar=np.array([.6,-1.2])
ax.plot([x[0],y[0]],[x[1],y[1]],color=BLUE,linewidth=2)
ax.plot([x[0],ystar[0]],[x[1],ystar[1]],color=PURPLE,linewidth=2,linestyle='--')
ax.scatter(*x,s=65,c=GREEN,zorder=5)
ax.scatter(*y,s=95,c=BLUE,zorder=5);ax.scatter(*ystar,s=95,c=PURPLE,zorder=5)
ax.annotate(r'$x=(-0.8,1.6)$',x,(-1.9,2.0),fontsize=11,
            arrowprops={'arrowstyle':'-','color':GREEN})
ax.annotate(r'$y=(0.6,1.2)$'+'\npositive interior mass',y,(.76,1.48),fontsize=10,ha='left',color=BLUE)
ax.annotate(r'$y^*=(0.6,-1.2)$'+'\nreflected negative mass',ystar,(.68,-1.70),fontsize=10,ha='left',color=PURPLE)
ax.text(-.15,1.82,r'$r_-^2=2.12$',color=BLUE,fontsize=11)
ax.text(-1.7,.35,r'$r_+^2=9.8$',color=PURPLE,fontsize=11)
ax.text(-1.9,-.18,'boundary: t=0, G=0',fontsize=10)
ax.set_xlabel('horizontal coordinate z');ax.set_ylabel('height t')
ax.set_title('Source and reflected pole',fontsize=13);ax.grid(alpha=.12)

zz=np.linspace(-3,3,230);tt=np.linspace(0,3.6,220)
Z,T=np.meshgrid(zz,tt);values=green2(Z,T)
im=field.imshow(np.maximum(values,-.55),origin='lower',extent=[-3,3,0,3.6],
                aspect='equal',cmap='Blues_r',vmin=-.55,vmax=0,interpolation='bilinear')
levels=[-.4,-.2,-.1,-.05,-.01]
contours=field.contour(Z,T,values,levels=levels,colors='#40596b',linewidths=.7)
field.clabel(contours,fontsize=8,fmt='%g')
field.scatter(.6,1.2,s=55,c=ORANGE,edgecolors='white',linewidths=.8,zorder=5)
field.annotate('pole: G → −∞',(.6,1.2),(-1.8,2.7),fontsize=10,
               arrowprops={'arrowstyle':'->','color':ORANGE},
               bbox={'facecolor':'white','edgecolor':'none','alpha':.85})
field.axhline(0,color='#333333',linewidth=1.5)
field.set_xlabel('z');field.set_ylabel('t');field.set_title('Exact Green kernel samples',fontsize=13)
bar=fig.colorbar(im,ax=field,shrink=.75,pad=.025);bar.set_label('G (colors clipped below −0.55)',fontsize=10)
eta=np.linspace(-5,5,900);p=1/(np.pi*(1+eta*eta))
density.plot(eta,p,color=GREEN,linewidth=2.4)
density.fill_between(eta,p,color=GREEN,alpha=.14)
density.set_xlim(-5,5);density.set_ylim(0,.37)
density.set_xlabel('boundary coordinate η');density.set_ylabel('Poisson density')
density.set_title('Boundary kernel at (0,1)',fontsize=13)
density.text(0,.348,r'$P=1/[\pi(1+\eta^2)]$',ha='center',fontsize=11)
density.text(1.25,.24,'Whole-line integral: 1\nWindow: −5 ≤ η ≤ 5',ha='left',fontsize=9,
             bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
density.grid(alpha=.14)
fig.suptitle('A reflected Green source and its boundary Poisson kernel (GR2–GR12)',fontsize=15)
for ext in ['png','svg']:
    fig.savefig(OUT/f'reflected-green.{ext}',dpi=160,
                metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 1.0',**({'Date':None} if ext=='svg' else {})})
plt.close(fig)

fig=plt.figure(figsize=(14.8,8.1),layout='constrained')
grid=fig.add_gridspec(2,2,height_ratios=[1,1.1])
ball=fig.add_subplot(grid[0,0]);half=fig.add_subplot(grid[0,1]);sliceax=fig.add_subplot(grid[1,:])
ball.set_aspect('equal');ball.set_xlim(-1.52,1.60);ball.set_ylim(-1.48,1.48)
ball.add_patch(Circle((0,0),1,facecolor='#edf4fa',edgecolor='#333333',linewidth=1.5))
ball.scatter(0,0,s=45,c=GREEN);ball.text(-.33,.12,'center 0',fontsize=10,color=GREEN)
for point,color,label,where in [((0,1),BLUE,'mass 1 → boundary mass 1/2',(-1.38,1.2)),
                               ((1,0),ORANGE,'mass 1 → boundary mass 1',(.10,.42)),
                               ((0,-1),PURPLE,'mass π/2 → coefficient 1/4',(-1.38,-1.3))]:
    ball.scatter(*point,s=100,c=color,zorder=4)
    ball.annotate(label,point,where,fontsize=10,color=color,
                  arrowprops={'arrowstyle':'-','color':color})
ball.text(-1.38,-.48,'T(y) = −e + 2(y+e)/|y+e|²',fontsize=10)
ball.set_xticks([-1,0,1]);ball.set_yticks([-1,0,1]);ball.set_xlabel('ball horizontal coordinate');ball.set_ylabel('ball vertical coordinate')
ball.set_title('Finite sphere measure',fontsize=13)
half.set_xlim(-2.4,3.1);half.set_ylim(-.28,2.35)
half.axhspan(0,2.35,color='#edf4fa');half.axhline(0,color='#333333',linewidth=1.5)
half.scatter(0,0,s=95,c=BLUE);half.scatter(1,0,s=95,c=ORANGE);half.scatter(0,1,s=45,c=GREEN)
half.annotate('boundary atom 1/2',(0,0),(-2.20,.55),fontsize=10,color=BLUE,
              arrowprops={'arrowstyle':'-','color':BLUE})
half.annotate('boundary atom 1',(1,0),(1.22,.55),fontsize=10,color=ORANGE,
              arrowprops={'arrowstyle':'-','color':ORANGE})
half.annotate('T(0)=(0,1)',(0,1),(-2.20,1.28),fontsize=10,color=GREEN,
              arrowprops={'arrowstyle':'-','color':GREEN})
half.annotate('pole −e corresponds to infinity\nlinear term: t/4',xy=(2.48,1.85),xytext=(-.7,1.95),ha='center',fontsize=11,color=PURPLE,
              arrowprops={'arrowstyle':'->','color':PURPLE})
half.set_xlabel('half-space horizontal coordinate z');half.set_ylabel('height t');half.set_title('Boundary measure + linear height',fontsize=13)
z=np.linspace(-4,5,1100);term0=.5*poisson2(z,1,0);term1=poisson2(z,1,1);linear=np.full_like(z,.25)
sliceax.plot(z,term0,color=BLUE,linewidth=1.8,label='P(x,0)/2')
sliceax.plot(z,term1,color=ORANGE,linewidth=1.8,label='P(x,1)')
sliceax.plot(z,linear,color=PURPLE,linewidth=1.8,linestyle='--',label='t/4')
sliceax.plot(z,term0+term1+linear,color=GREEN,linewidth=2.8,label='u = sum of the three terms')
sliceax.set_xlim(-4,5);sliceax.set_ylim(0,.69);sliceax.set_xlabel('horizontal coordinate z, at height t=1')
sliceax.set_ylabel('positive harmonic function and terms')
sliceax.set_title('Exact harmonic slice: u=P(x,0)/2+P(x,1)+t/4; v=−u satisfies the upper bound',fontsize=12)
sliceax.legend(loc='upper right',fontsize=10,frameon=False);sliceax.grid(alpha=.13)
fig.suptitle('Inversion turns one sphere atom into the linear term (GR21–GR28)',fontsize=15)
for ext in ['png','svg']:
    fig.savefig(OUT/f'ball-to-half-space.{ext}',dpi=160,
                metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 1.0',**({'Date':None} if ext=='svg' else {})})
plt.close(fig)
print(json.dumps({'figures':['reflected-green.png','reflected-green.svg','ball-to-half-space.png','ball-to-half-space.svg'],
                  'marked_green_value':float(green2(-.8,1.6))},indent=2))
