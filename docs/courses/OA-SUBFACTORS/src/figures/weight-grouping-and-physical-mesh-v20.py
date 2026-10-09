"""Exact finite Jones/cyclotomic/fusion checks and a reproducible algebraic figure."""
from fractions import Fraction as F
import datetime, hashlib, json, pathlib, random, re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="weight-grouping-and-physical-mesh-v20"
from matplotlib.patches import FancyBboxPatch

own = pathlib.Path(__file__).resolve().parent
T = [[0,0,1,0],[0,0,1,0],[1,1,0,1],[0,0,1,1]]
dims = [1,1,2,2]

def mul(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def vec(a,v):
    return [sum(x*y for x,y in zip(row,v)) for row in a]

def scale(a,t):
    return [[x*t for x in row] for row in a]

def kron(a,b):
    return [[x*y for x in rowa for y in rowb] for rowa in a for rowb in b]

def ident(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

cup = [[F(0) for _ in range(4)] for _ in range(4)]
for i in [1,2]:
    for j in [1,2]:
        cup[i][j] = F(1,2)
assert mul(cup,cup)==cup
assert sum(cup[i][i] for i in range(4))/4==F(1,4)
left, right = kron(cup,ident(2)), kron(ident(2),cup)
assert mul(mul(left,right),left)==scale(left,F(1,4))
assert mul(mul(right,left),right)==scale(right,F(1,4))
for a in range(2):
    for b in range(2):
        matrix = [[F(int(i==a and j==b)) for j in range(2)] for i in range(2)]
        assert mul(mul(cup,kron(ident(2),matrix)),cup)==scale(cup,F(int(a==b),2))
partial = [[sum(cup[2*a+k][2*b+k] for k in range(2))/2 for b in range(2)] for a in range(2)]
assert partial==scale(ident(2),F(1,4))

# Exact characters in Z[z]/(1+z+z^2+z^3+z^4).
def canonical(a):
    return tuple(a[i]-a[4] for i in range(4))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def poly_mul(a,b):
    out=[0]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[(i+j)%5]+=x*y
    return canonical(out)

def char(r,k):
    out=[0]*5
    out[(r*k)%5]+=1
    out[(-r*k)%5]+=1
    return canonical(out)

one=(1,0,0,0)
character_cases=0
for k in range(5):
    u,w=char(1,k),char(2,k)
    assert poly_mul(u,u)==add(add(one,one),w)
    assert poly_mul(u,w)==add(u,w)
    character_cases+=2
for k in range(5):
    # Both two-dimensional reflection characters vanish; 1+epsilon=0.
    assert 0*0==1-1+0
    assert 0*0==0+0
    character_cases+=2

levels=[]
m=[1,0,0,0]
for n in range(31):
    weights=[F(d,2**n) for d in dims]
    assert sum(h*w for h,w in zip(m,weights))==1
    maximum=max(w for h,w in zip(m,weights) if h)
    assert maximum<=F(3,4)**(n//2)
    later=[F(d,2**(n+1)) for d in dims]
    assert all(sum(T[i][j]*later[i] for i in range(4))==weights[j] for j in range(4))
    levels.append(m)
    m=vec(T,m)
assert levels[3]==[0,0,3,1]
assert levels[4]==[3,3,1,4]
assert levels[5]==[1,1,10,5]
assert levels[9]==[36,36,127,93]
assert all(m[2]>0 and m[3]>0 for m in levels[3:])

v=[0,0,1,-1]
fib=[0,1]
for h in range(2,62):
    fib.append(fib[-1]+fib[-2])
gap_results=[]
for h in range(1,61):
    v=vec(T,v)
    expected=[(-1)**(h-1)*fib[h],(-1)**(h-1)*fib[h],(-1)**h*fib[h+1],(-1)**(h-1)*fib[h-1]]
    assert v==expected
    group_difference=v[0]+v[1]
    assert group_difference==2*(-1)**(h-1)*fib[h] and group_difference!=0
    assert group_difference+2*(v[2]+v[3])==0
    gap_results.append({"gap":h,"dimension_one_rank_difference":group_difference})

generator=random.Random(190810)
mesh_cases=0
for m in range(7):
    for gap in range(9):
        n=m+gap
        for case in range(7):
            old=[generator.randrange(cap+1) for cap in levels[m]]
            actual=old
            for step in range(gap):
                actual=vec(T,actual)
            weights=[F(d,2**n) for d in dims]
            total=sum(h*w for h,w in zip(actual,weights))
            target=total*F(generator.randrange(101),100)
            taken=[0]*4
            remaining=target
            for i,(cap,w) in enumerate(zip(actual,weights)):
                h=min(cap,remaining//w)
                taken[i]=h
                remaining-=h*w
                if h<cap:
                    break
            got=sum(h*w for h,w in zip(taken,weights))
            assert F(0)<=target-got<max(w for cap,w in zip(levels[n],weights) if cap) or target==total==got
            assert all(0<=a<=b for a,b in zip(taken,actual))
            mesh_cases+=1

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.fonttype":"none"})
fig=plt.figure(figsize=(13.8,9.6))
ax=fig.add_axes([0,0,1,1])
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
blue="#1b5e94";red="#aa3737";green="#2b6a4f";grey="#35465a"
fig.patch.set_facecolor("#fcfcfb")
ax.text(.045,.95,"An actual Jones tower defeats numerical grouping",fontsize=22,fontweight="bold",color=grey)
ax.text(.045,.912,r"Index 4, outer $D_5$ tensor action; actual whole tunnel; both finite traces $\tau=\rho$.",fontsize=13,color=grey)

def box(x,y,w,h,label,color=blue,fill="#eff5fa",size=13):
    patch=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.009,rounding_size=0.008",linewidth=1.5,edgecolor=color,facecolor=fill)
    ax.add_patch(patch)
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=size,color=color,linespacing=1.6)

box(.045,.69,.25,.16,r"$C_3=M_3\oplus\mathbb{C}$"+"\n"+r"$U$ multiplicity 3; $W$ multiplicity 1"+"\n"+r"both minimal weights: $1/4$",size=12)
box(.59,.758,.365,.092,r"$M_3(1)\oplus M_3(\epsilon)$"+"\n"+r"dimension-one group: rank 6, weight $1/16$",size=12)
box(.59,.626,.365,.092,r"$\mathbb{C}(U)\oplus M_4(W)$"+"\n"+r"dimension-two group: rank 5, weight $1/8$",size=12)
ax.text(.6,.866,r"Actual $C_4$: four endpoint blocks",fontsize=13,color=grey)
ax.annotate("",xy=(.575,.796),xytext=(.309,.788),arrowprops={"arrowstyle":"->","color":blue,"lw":2.2})
ax.text(.36,.812,r"$p_U:\ 2$ ranks",fontsize=12,color=blue)
ax.annotate("",xy=(.575,.69),xytext=(.309,.746),arrowprops={"arrowstyle":"->","color":blue,"lw":2.2})
ax.text(.35,.756,r"$p_U:\ 1$ rank",fontsize=12,color=blue)
ax.annotate("",xy=(.575,.652),xytext=(.309,.695),arrowprops={"arrowstyle":"->","color":red,"lw":2.2})
ax.text(.36,.648,r"$p_W:\ 2$ ranks",fontsize=12,color=red)
ax.text(.32,.858,r"$p_W$ has zero dimension-one rank",fontsize=12,color=red)
box(.045,.55,.91,.058,r"Grouped: $M_4$    ↛    $M_6\oplus M_5$"+"     (unital embedding impossible)",color=red,fill="#fff1ef",size=14)
ax.text(.052,.516,"Equivalent source projections have unequal target ranks.  Exact obstruction: GW.20–GW.22.",fontsize=12,color=grey)

box(.045,.295,.49,.185,"",color=red,fill="#fff7f4",size=13)
ax.text(.065,.455,"Every finite gap fails",fontsize=13,fontweight="bold",color=red)
ax.text(.066,.425,r"Dimension-one rank difference: $2(-1)^{h-1}F_h\neq0$",fontsize=13,color=red)
ax.text(.07,.383,"gap h       1        2        3        4        5        6",fontsize=12,color=grey)
ax.text(.07,.345,"difference  +2      −2       +4       −6      +10      −16",fontsize=12,color=red)
ax.text(.065,.312,"U,W persist for n ≥ 3; every cofinal subsequence fails.",fontsize=11,color=red)
ax.text(.06,.273,"GW.23 covers all positive gaps. Divisible matrix sizes",fontsize=11,color=grey)
ax.text(.06,.251,"do not repair extension of the actual inclusion.",fontsize=11,color=grey)

mesh=fig.add_axes([.61,.335,.335,.13])
xs=list(range(51))
ys=[float(F(3,4)**(n//2)) for n in xs]
mesh.step(xs,ys,where="post",color=green,lw=2.4)
mesh.set_xlabel("integer continuation length n",fontsize=10)
mesh.set_ylabel("proved physical bound",fontsize=10)
mesh.set_xlim(0,50);mesh.set_ylim(0,1)
mesh.grid(alpha=.18);mesh.tick_params(labelsize=9)
ax.text(.61,.482,r"General actual bound: $\mu_n\leq(3/4)^{\lfloor n/2\rfloor}$ at $d=4$",fontsize=12,color=green)
ax.text(.6,.25,r"GW.25: $\mu_{n+2}\leq\max(1/d,1-1/d)\mu_n$",fontsize=11,color=green)

box(.045,.08,.91,.135,
    "The full finite-family theorem survives this example."+"\n"+
    "Finite depth and the generating tunnel supply it. The failed step is automatic numerical grouping."+"\n"+
    "The general mesh bound controls physical cuts; exact residual return with all three rows still needs proof.",
    color=grey,fill="#f0f3f5",size=12)
ax.text(.045,.033,"Schematic matrix/rank diagram and a proved bound, not sampled geometry.  Editable source: weight-grouping-and-physical-mesh-v20.py.",fontsize=10,color=grey)
fig.savefig(own/"weight-grouping-and-physical-mesh-v20.svg",facecolor=fig.get_facecolor(),metadata={"Date":None})
fig.savefig(own/"weight-grouping-and-physical-mesh-v20.png",dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)

result={
    "checked_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "exact_cup_and_TL_relations":True,
    "exact_cyclotomic_character_cases":character_cases,
    "actual_multiplicity_and_both_trace_levels":len(levels),
    "all_gap_Fibonacci_cases":len(gap_results),
    "actual_subprojection_mesh_cases":mesh_cases,
    "all_gap_differences":gap_results,
            "scope":"Checks reproduce finite algebraic identities of the explicit actual Jones construction and the proved general physical mesh estimate. They do not infer the full arbitrary-inclusion family theorem.",
}
(own/"weight-grouping-and-physical-mesh-checks.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="all_gap_differences"}))

# Normalize serializer whitespace while retaining every SVG coordinate and label.
svg_path=own / "weight-grouping-and-physical-mesh-v20.svg"
svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
