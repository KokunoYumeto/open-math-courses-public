# Reproducing the single-scale obstruction diagram

Run python reproduce.py with Python 3.13 and Pillow 12.2.0. The outputs are figures/plaque-single-scale-obstruction.png and figures/plaque-single-scale-obstruction.svg. Use --output with a directory to select another output directory.

The generator draws the actual circle with physical circumference four, the ordinary chart (0,1), the exact smooth profiles at epsilon 1/32, the duality/interpolation maps and the proved cross-boundary integral lower bound. It does not calculate operator spectra or assign a numerical value to an unspecified proof constant.

The smooth transition used in the sampled profile is s(z)=exp(-1/z)/(exp(-1/z)+exp(-1/(1-z))) for 0<z<1, extended by zero and one outside that interval. The proof cutoff is eta(t)=s(t-1). The fixed reflection cutoff is s(4(t+3/4))s(4(7/4-t)), supported in [-3/4,7/4] and equal to one on [-1/2,3/2].

The unmodified bundled DejaVu Sans is used for every raster label and is embedded in the SVG. Complete font terms and [component terms](COMPONENT-TERMS.md) accompany the generator. Python and Pillow are external software requirements; their full retained licence texts are in software-notices/.
