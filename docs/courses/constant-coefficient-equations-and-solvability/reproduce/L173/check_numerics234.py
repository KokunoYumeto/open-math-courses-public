"""Supplementary exact domain, reflection, tangent and Fourier-bound probes."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
import mpmath as mp

OWN=Path(__file__).resolve().parent
mp.mp.dps=65
counts={}; maximum=mp.mpf(0)
def test(kind,condition):
    assert condition,kind
    counts[kind]=counts.get(kind,0)+1
def equal(kind,left,right):
    global maximum
    error=abs(left-right); maximum=max(maximum,error)
    test(kind,error<mp.mpf("1e-57"))
def interval_erosion(u,k):
    return (u[0]+k[1],u[1]+k[0])
def interval_difference(u,k):
    return (u[0]-k[1],u[1]-k[0])
def inside(x,u,closed=False):
    return u[0]<=x<=u[1] if closed else u[0]<x<u[1]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def support(vertices,nu):return max(dot(x,nu) for x in vertices)
def norm_fraction_to_mp(x):return mp.mpf(x.numerator)/x.denominator

u=[(F(-3),F(5)),(F(-2),F(4))]
k=[(F(-1),F(2)),(F(-1,2),F(1,2))]
test("rectangle_erosion_endpoints",
     [interval_erosion(a,b) for a,b in zip(u,k)]==[(-1,4),(F(-3,2),F(7,2))])
test("rectangle_difference_endpoints",
     [interval_difference(a,b) for a,b in zip(u,k)]==[(-5,6),(F(-5,2),F(9,2))])
for a in range(-12,15):
    for b in range(-8,11):
        x=[F(a,2),F(b,2)]
        actual=all(inside(xi-ki,ui) for xi,ui,ki_range in zip(x,u,k)
                   for ki in ki_range)
        expected=all(inside(xi,interval_erosion(ui,ki))
                     for xi,ui,ki in zip(x,u,k))
        test("open_rectangle_vertex_containment",actual==expected)

s=[(F(-1),F(2)),(F(0),F(0))]
U=[(F(-2),F(3)),(F(-1),F(2))]
X1=[interval_difference(a,b) for a,b in zip(U,s)]
test("two_atom_unknown_domain",X1==[(-4,4),(-1,2)])
test("two_atom_erosion_recovers_equation",
     [interval_erosion(a,b) for a,b in zip(X1,s)]==U)
C=[(F(-3),F(3)),(F(-1,2),F(3,2))]
receiver=[interval_erosion(a,b) for a,b in zip(C,s)]
test("sharp_closed_receiver",receiver==[(-1,2),(F(-1,2),F(3,2))])
for a in range(-12,13):
    for b in range(-5,10):
        x=[F(a,4),F(b,4)]
        actual=all(inside(x[0]-offset,C[0],True) for offset in s[0]) and inside(x[1],C[1],True)
        expected=all(inside(xi,ri,True) for xi,ri in zip(x,receiver))
        test("closed_two_atom_receiver_sharpness",actual==expected)
test("receiver_compact_margin",
     min(receiver[0][0]-U[0][0],U[0][1]-receiver[0][1],
         receiver[1][0]-U[1][0],U[1][1]-receiver[1][1])==F(1,2))

S=[(F(0),F(0)),(F(0),F(3))]
K0=[(F(0),F(0))]
test("negative_lower_normal_support_gap",
     support(S,(0,1))==3 and support(K0,(0,1))==0)
test("unreflected_lower_normal_misses_gap",
     support(S,(0,-1))==support(K0,(0,-1))==0)
test("point_carrier_allows_outside_point",
     inside(F(-2),(-4,1)) and not inside(F(-2),(-1,1)))
for j in range(1,129):
    gap=F(1,2**j); y=-1+gap; radius=gap/4
    test("escaping_witness_compact_image_bound",F(-1)<y<=0)
    test("actual_witness_support_radius_inside_equation",
         y-radius>-1 and y+radius<1 and radius<2)
    test("witness_distance_to_equation_boundary",min(y+1,1-y,2)==gap)
    test("witness_distance_to_unknown_boundary",min(y+4,1-y,2)==2-gap)
for height in range(13):
    candidate=[(F(0),F(0)),(F(0),F(height,4))]
    test("horizontal_strip_support_values",
         support(candidate,(1,0))==support(candidate,(-1,0))==0)
    shifted=[(F(3,2)-p[0],F(7)-p[1]) for p in candidate]
    test("vertical_carrier_never_changes_strip_first_coordinate",
         all(-2<point[0]<2 for point in shifted))

for a_num in [*range(-8,0),*range(1,9)]:
    a=F(a_num,4); sign=1 if a>0 else -1; slope=sign+2*a
    test("every_regular_tangent_strict_at_corner",a*a>0)
    test("tangent_contact_value",slope*a-a*a==abs(a)+a*a)
    for t_num in range(-24,25):
        t=F(t_num,8)
        gap=abs(t)+t*t-(slope*t-a*a)
        decomposition=(t-a)**2+abs(t)-sign*t
        test("exact_tangent_gap_identity",gap==decomposition and gap>=0)
    ap=norm_fraction_to_mp(a); pp=mp.sign(ap)+2*ap
    normal=(pp/mp.sqrt(1+pp*pp),-1/mp.sqrt(1+pp*pp))
    equal("outward_unit_normal_length",normal[0]**2+normal[1]**2,1)
    test("outward_normal_has_negative_vertical_component",normal[1]<0)
    equal("normal_support_tangent_intercept",
          normal[0]*ap+normal[1]*(abs(ap)+ap*ap),
          ap*ap/mp.sqrt(1+pp*pp))
for p1 in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:
    for p2 in [F(-2),F(-1),F(0),F(1),F(2)]:
        for x1,x2 in [(F(-1,8),F(1,4)),(F(1,2),F(-1,3)),(F(0),F(0))]:
            test("three_dimensional_corner_subgradient_rectangle",
                 abs(x1)+2*abs(x2)+x1*x1+x2*x2>=p1*x1+p2*x2)

sets=[S,[(-1,0),(2,0)],[(F(-1),F(-1,2)),(F(2),F(1,2))]]
for vertices in sets:
    for small in [[vertices[0]],[vertices[-1]],vertices]:
        for nu in [(1,0),(0,-1),(3,4)]:
            full=support(vertices,(-nu[0],-nu[1]))
            one=support(small,(-nu[0],-nu[1])); delta=full-one
            test("halfspace_threshold_shift_nonnegative",delta>=0)
            if delta>0:
                alpha=F(1,3); value=alpha+delta/2
                x=tuple(value*F(v,dot(nu,nu)) for v in nu)
                test("smaller_carrier_admits_outside_halfspace",
                     alpha<dot(x,nu)<alpha+delta)
            else:
                test("shared_normal_gives_identical_halfspace",full==one)

a=(mp.mpf("0.5"),mp.mpf("-0.25"))
for j in range(-3,4):
    p=(mp.mpf(j)/7,mp.mpf(j+2)/9)
    for degree in range(1,6):
        theta=lambda x,y:(1+mp.mpc(".2",".3")*x+mp.mpc("-.1",".4")*y)**degree
        actual=mp.j*theta(p[0]-a[0],p[1]-a[1])
        expected=mp.j*theta(p[0]-mp.mpf("0.5"),p[1]+mp.mpf(".25"))
        equal("complex_bilinear_reflected_point_kernel",actual,expected)
        wrong=-mp.j*theta(p[0]-a[0],p[1]-a[1])
        test("conjugated_coefficient_rejected",abs(actual-wrong)>mp.mpf(".01"))

bump=lambda t:mp.exp(-1/(t*(1-t))) if 0<t<1 else mp.mpf(0)
parts=[0,mp.mpf(".25"),mp.mpf(".5"),mp.mpf(".75"),1]
mass=mp.quad(bump,parts)
test("normalizing_bump_has_positive_finite_mass",0<mass<1)
normalized_mass=mp.quad(lambda t:bump(t)/mass,parts)
equal("normalized_positive_bump_mass",normalized_mass,1)
sampled=[]
for j in range(-10,11):
    xi=mp.mpf(j)/2
    Fg=mp.quad(lambda t:bump(t)*mp.exp(-mp.j*(t+2)*xi),parts)/mass
    Fmu=1+Fg/5
    test("sampled_positive_measure_Fourier_bound",abs(Fg)<=1+mp.mpf("1e-57"))
    test("sampled_kernel_real_lower_bound",abs(Fmu)>=mp.mpf(".8")-mp.mpf("1e-57"))
    sampled.append({"frequency":mp.nstr(xi,12),
                    "kernel_modulus":mp.nstr(abs(Fmu),25)})
report={"scope":"Supplementary finite exact geometry and 65-digit numerical checks; full universal statements are proved in the chapters.",
    "status":"PASS","decimal_precision":65,"probe_count":sum(counts.values()),
    "probe_counts":counts,"maximum_numerical_identity_error":mp.nstr(maximum,25),
    "sampled_real_Fourier_values":sampled,
    "source_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
    "not_an_enumeration_of_the_entire_profile_family":True,
    "proofs_not_replaced_by_probes":True}
(OWN/"supplementary-example-probes234.json").write_text(
    json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:report[k] for k in ("status","probe_count","decimal_precision",
                                     "maximum_numerical_identity_error")}))
