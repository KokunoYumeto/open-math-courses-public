"""Exact finite central-ergodic decomposition, OA-FLOW L42, E1--E6.

Original diagram, code and data: CC0-1.0.
Run with Python and matplotlib to reproduce PNG/SVG/data beside this script.
DejaVu font terms are retained in FONT_LICENSE_DEJAVU.txt.
All dimension checks below are integer counts of explicit matrix-unit orbits.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent
blocks = [(0, 1), (2, 3), (4, 5, 6)]
permutation = (2, 3, 0, 1, 4, 5, 6)
assert all(permutation[permutation[i]] == i for i in range(7))
matrix_units = {(i, j) for block in blocks for i in block for j in block}
assert len(matrix_units) == 17
orbits = {tuple(sorted({(i, j), (permutation[i], permutation[j])}))
          for i, j in matrix_units}
assert len(orbits) == 13
assert all(set(orbit) <= matrix_units for orbit in orbits)
central_orbits = ((0, 1), (2,))
assert len(central_orbits) == 2
first_units = {(i,j) for block in blocks[:2] for i in block for j in block}
first_orbits = {tuple(sorted({(i,j),(permutation[i],permutation[j])}))
                for i,j in first_units}
assert len(first_units) == 8 and len(first_orbits) == 4
e = [[int(i in block) for i in range(7)] for block in blocks]
d_a = [e[0][i]+e[1][i] for i in range(7)]
d_b = e[2]
assert all(d_a[i]+d_b[i] == 1 and d_a[i]*d_b[i] == 0 for i in range(7))
assert all(d_a[permutation[i]] == d_a[i] and d_b[permutation[i]] == d_b[i]
           for i in range(7))
data = {
    "license": "CC0-1.0",
    "proof_locator": "OA-FLOW-L42.md#oa-flow.centerg.example; E1-E6",
    "group": "C2={e,s}, s^2=e",
    "matrix_blocks": [2,2,3],
    "implementing_unitary_basis_permutation_zero_based": permutation,
    "minimal_full_centre_projection_diagonals": e,
    "invariant_centre_projection_diagonals": {"a": d_a, "b": d_b},
    "base": {"a": "1/2", "b": "1/2"},
    "whole_algebra_complex_dimension": len(matrix_units),
    "whole_centre_complex_dimension": 3,
    "invariant_centre_complex_dimension": 2,
    "fixed_algebra_complex_dimension": len(orbits),
    "matrix_unit_orbits_in_fixed_algebra": sorted(orbits),
    "components": {
        "a": {"algebra":"M2 + M2", "action":"swap", "centre":"C2",
              "fixed_centre":"C", "fixed_algebra":"M2", "fixed_dimension":4,
              "factor":False, "centrally_ergodic":True, "ergodic":False},
        "b": {"algebra":"M3", "action":"identity", "centre":"C",
              "fixed_centre":"C", "fixed_algebra":"M3", "fixed_dimension":9,
              "factor":True, "centrally_ergodic":True, "ergodic":False}},
    "one_point_original": {"algebra":"M2 + M2", "centre_dimension":2,
                           "invariant_centre_dimension":1,"fixed_dimension":4}
}
(OUT/'fixed-centre-exact-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":15,
                    "mathtext.fontset":"dejavusans", "svg.fonttype":"path",
                    "svg.hashsalt":"oa-flow-central-ergodic-components-20261006"})
fig=plt.figure(figsize=(15,10),facecolor="#f7fafc")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink,muted,blue,green,orange="#192e3b","#536b7a","#176b9d","#177a66","#b65b20"
ax.text(.055,.965,"The invariant centre chooses the components",fontsize=25,
        color=ink,weight='bold',va='top')
ax.text(.055,.895,r"$\widetilde M=M_2\oplus M_2\oplus M_3$,   $s(A,B,C)=(B,A,C)$",
        fontsize=21,color=muted)
ax.text(.055,.846,"Full centre: three independent scalar coordinates",fontsize=16,
        weight='bold',color=blue)

def box(x,y,w,h,face,edge=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.007',
                             fc=face,ec=edge if edge else 'none',lw=1.2))

for x,label,centre,proj in [(.07,r"$M_2$",r"$\lambda I_2$",r"$e_1$"),
                            (.35,r"$M_2$",r"$\gamma I_2$",r"$e_2$"),
                            (.72,r"$M_3$",r"$\delta I_3$",r"$e_3$")]:
    box(x,.679,.21,.13,'#e6f0f7')
    ax.text(x+.105,.772,label,ha='center',fontsize=23,color=ink)
    ax.text(x+.105,.724,centre,ha='center',fontsize=19,color=blue)
    ax.text(x+.105,.692,proj,ha='center',fontsize=13,color=muted)
ax.add_patch(FancyArrowPatch((.288,.748),(.343,.748),arrowstyle='<->',
                            mutation_scale=16,color=orange,lw=2))
ax.text(.3155,.782,r"$s$",ha='center',color=orange,fontsize=18)
ax.text(.825,.823,"fixed by s",ha='center',fontsize=12,color=muted)

for start,end in [((.175,.669),(.33,.603)),((.455,.669),(.33,.603)),
                  ((.825,.669),(.825,.603))]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='->',mutation_scale=17,
                                color=muted,lw=1.6))
ax.text(.515,.624,"invariant sums",fontsize=13,color=muted,ha='center')

box(.055,.243,.555,.35,'#eef4f6','#b4c7d2')
box(.665,.243,.28,.35,'#eef4f6','#b4c7d2')
ax.text(.080,.555,r"Base point $a$:  $d_a=e_1+e_2$",fontsize=19,color=green,
        weight='bold')
ax.text(.690,.555,r"Base point $b$:  $d_b=e_3$",fontsize=17,color=green,
        weight='bold')
ax.text(.080,.505,r"$M_a=M_2\oplus M_2$; action swaps the summands",fontsize=16,color=ink)
ax.text(.690,.505,r"$M_b=M_3$; identity action",fontsize=15,color=ink)
ax.plot([.08,.585],[.482,.482],color='#c7d4dc',lw=1)
ax.plot([.69,.92],[.482,.482],color='#c7d4dc',lw=1)
labels=[(.435,"Full centre",r"$\mathbb{C}^2$",r"$\mathbb{C}$",blue),
        (.365,"Fixed centre",r"$\mathbb{C}$",r"$\mathbb{C}$",green),
        (.295,"Fixed algebra",r"$\{(A,A)\}\cong M_2$",r"$M_3$",orange)]
for y,label,left,right,color in labels:
    ax.text(.08,y,label,fontsize=16,color=color)
    ax.text(.305,y,left,fontsize=21,color=color)
    ax.text(.69,y,label,fontsize=14,color=color)
    ax.text(.884,y,right,fontsize=20,color=color,ha='center')

ax.text(.055,.19,r"Invariant centre: $\widetilde D\cong\mathbb{C}^2$  |  Fixed algebra: $M_2\oplus M_3$ (dimension $13$)",
        fontsize=18,color=ink)
ax.text(.055,.135,"Each component has scalar fixed centre. Neither has scalar fixed algebra.",
        fontsize=18,color=green,weight='bold')
ax.text(.055,.083,r"Remove $M_3$: one base point, full centre $\mathbb{C}^2$, fixed centre $\mathbb{C}$, fixed algebra $M_2$.",
        fontsize=16,color=muted)
ax.text(.055,.025,"Exact matrix calculation · OA-FLOW L42 · equations (E1)–(E6)",
        fontsize=11,color=muted)
fig.savefig(OUT/'fixed-centre-components.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(OUT/'fixed-centre-components.svg',facecolor=fig.get_facecolor(),
            metadata={'Date':None})
plt.close(fig)
print(json.dumps({'exact_matrix_unit_orbit_checks':'passed','png_dimensions':[2700,1800]}))
