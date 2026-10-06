"""Original CC0 numerical quadrature; decimal approximations, not interval certificates."""
import hashlib,json,math,time
from pathlib import Path
import mpmath as mp
import numpy as np

root=Path(__file__).resolve().parent
started=time.perf_counter()
def integrate(order):
    nodes,weights=np.polynomial.legendre.leggauss(order)
    blocks=[]; result={}
    for k in range(1000):
        block=math.fsum(float(w)*abs(mp.fp.zeta(.5+1j*(k+.5+.5*float(z))))**2 for z,w in zip(nodes,weights))*.5
        blocks.append(block)
        if k+1 in (100,1000):result[k+1]=math.fsum(blocks)
    return result

low=integrate(16); high=integrate(32)
mp.mp.dps=40
samples=[0,1,10,100,500,1000]
sample_errors=[abs(mp.mpc(mp.fp.zeta(.5+1j*t))-mp.zeta(mp.mpc('.5',t))) for t in samples]
assert max(sample_errors)<mp.mpf('1e-10')
assert max(abs(low[t]-high[t]) for t in high)<1e-7
receipt={'method':'Composite Gauss–Legendre quadrature on unit intervals, 16 and 32 nodes; mpmath machine-precision zeta, checked at six points against 40 decimal digits. Approximations, not certified bounds.',
 'software_versions':{'mpmath':mp.__version__,'numpy':np.__version__},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'values':[{'T':t,'integral':high[t],'ratio':high[t]/(t*math.log(t)),'quadrature_change':abs(low[t]-high[t])} for t in (100,1000)],
 'sample_max_absolute_difference':str(max(sample_errors)),'seconds':time.perf_counter()-started}
(root/'mean_square_calculation.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
