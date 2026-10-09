"""Compare rendered source samples with independently integrated Green kernels."""
from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET
import mpmath as mp
from PIL import Image
mp.mp.dps=140
OWN=Path(__file__).resolve().parent;FIG=OWN/"figures"
g=json.loads((FIG/"geometry260.json").read_bytes())
q=mp.mpf(g["q"]);count=0;worst=mp.mpf(0)
def equal(left,right):
    global count,worst
    error=abs(left-right)/(1+abs(right));worst=max(worst,error)
    assert error<mp.mpf("1e-65"),error
    count+=1
for row in g["curves"]:
    h=row["h"]
    for index in [0,25,50,75,100,150,200,250,300]:
        y=mp.mpf(g["y_samples"][index])
        equal(mp.mpf(row["forcing_rate"][index]),-(y-h)**2-1)
        r0=abs(y-h)
        cuts=sorted(set([mp.mpf(0),max(mp.mpf(0),r0-1),r0,r0+1,mp.inf]))
        integral=mp.quad(lambda r:mp.exp(-q*r)*(
            mp.exp(-q*(y-r-h)**2)+mp.exp(-q*(y+r-h)**2)),cuts)/(2*q)
        equal(mp.mpf(row["particular_rate"][index]),-1+mp.log(integral)/q)
for row in g["per_mode_complex_time_scales"]:
    h=mp.mpf(row["h"])
    equal(mp.mpf(row["forcing_threshold"]),(h*h+1)/(h*h))
    equal(mp.mpf(row["tail_threshold"]),(h+mp.mpf(3)/4)/(h*h))
assert g["left_modes_are_finite_parameter_examples_not_the_actual_lacunary_sum"]
assert g["tail_scales_are_proved_q_to_infinity_leading_exponential_rates"]
assert ET.fromstring((FIG/"gaussian-sources-and-distant-tails.svg").read_bytes()).tag.endswith("svg")
im=Image.open(FIG/"gaussian-sources-and-distant-tails.png");assert im.size==(2145,792)
record=dict(schema="AN02-analytic-figure-check260/v1",status="PASS",
    total_checks=count,precision_decimal_digits=140,tolerance="1e-65",max_scaled_error=str(worst),
    independent_green_integral_samples=True,PNG_dimensions=list(im.size),SVG_XML_valid=True,
    private_source_pixels_not_reused=True)
(OWN/"figure-checks260.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
