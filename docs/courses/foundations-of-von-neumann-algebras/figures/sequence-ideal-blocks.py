"""Figure 7.1 for Proposition 7.7A. CC0-1.0.

Run with Python and Matplotlib to reproduce sequence-ideal-blocks.svg.
The lower panel is an explicitly labelled finite illustration of the proof.
"""
from pathlib import Path
import argparse
import hashlib
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fractions import Fraction

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--preview', type=Path)
    args = parser.parse_args()
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                         'svg.fonttype':'none','svg.hashsalt':'sequence-ideal-blocks'})
    fig=plt.figure(figsize=(9.3,7.4),facecolor='white')
    fig.text(.07,.95,'Algebraic ideals need not be solid',fontsize=18,weight='bold')
    fig.text(.07,.905,r'$m_k=2^{2^k},\quad a_k=1/m_k,\quad N_k=\sum_{j\leq k}m_j$',fontsize=13)
    ax=fig.add_axes([.07,.64,.86,.21]);ax.axis('off')
    rows=[];total=0
    for k in range(1,5):
        m=2**(2**k)
        rows.append([str(k),f'{m:,}',f'1/{m:,}',f'{total:,}'])
        total+=m
    table=ax.table(cellText=rows,colLabels=['Block k','Length '+r'$m_k$','Height '+r'$a_k$','Earlier coordinates '+r'$N_{k-1}$'],
                   colWidths=[.13,.23,.25,.39],cellLoc='center',loc='center')
    table.auto_set_font_size(False);table.set_fontsize(11);table.scale(1,1.6)
    for (r,c),cell in table.get_celld().items():
        cell.set_edgecolor('#cbd5e1')
        if r==0:cell.set_facecolor('#e8eef6');cell.set_text_props(weight='bold')
    fig.text(.07,.595,r'Within block $B_k$:  $\lambda_n/a_k=1$, while $\mu_{N_{k-1}+j}/a_k=j/m_k$.',fontsize=11)
    ax=fig.add_axes([.10,.19,.80,.34])
    m=256;xs=list(range(1,m+1));ys=[Fraction(j,m) for j in xs]
    ax.scatter(xs,[float(y) for y in ys],s=9,color='#1d4ed8',label=r'Ramp $j/256$',zorder=3)
    levels=[Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(5,6)]
    tolerance=Fraction(1,48)
    for s in levels:
        ax.axhline(float(s),color='#b45309',lw=1,ls='--')
        ax.axhspan(float(s-tolerance),float(s+tolerance),color='#fbbf24',alpha=.22)
    ax.set_xlim(0,256);ax.set_ylim(-.04,1.04)
    ax.set_xticks([0,64,128,192,256]);ax.set_xlabel(r'Coordinate $j$ in the block')
    ax.set_ylabel('Normalized value')
    ax.set_title(r'Illustration: $k=3$, $z_1=1/3$, $z_2=1/2$, $S=\{0,1/3,1/2,5/6\}$',fontsize=11,pad=12)
    ax.spines[['top','right']].set_visible(False);ax.grid(axis='x',alpha=.15)
    ax.legend(loc='upper left',frameon=False)
    fig.text(.07,.095,r'Shaded tolerance: $1/48$. At most $2N_2=40$ of these 256 coordinates can be exceptional.',fontsize=10)
    fig.text(.07,.055,r'In the proof, $rN_{k-1}/m_k\to0$ and the tolerance tends to zero; $S$ stays finite.',fontsize=11)
    out=Path(__file__).with_suffix('.svg')
    fig.savefig(out,metadata={'Date':None,'Title':'Algebraic sequence ideals and the finite-set obstruction'})
    out.write_bytes(b'\n'.join(line.rstrip(b' \t') for line in out.read_bytes().splitlines()) + b'\n')
    stream=BytesIO()
    fig.savefig(stream,format='png',dpi=140,metadata={'Title':'Algebraic sequence ideals and the finite-set obstruction'})
    data=stream.getvalue();digest=hashlib.sha256(data).hexdigest().upper()
    slug='compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies'
    target=Path(__file__).parent.parent/'assets'/slug/('sequence-ideal-blocks-'+digest+'.png')
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(data)
    if args.preview:args.preview.write_bytes(data)
    print(target.relative_to(Path(__file__).parent.parent).as_posix())
    plt.close(fig)

if __name__=='__main__':main()
