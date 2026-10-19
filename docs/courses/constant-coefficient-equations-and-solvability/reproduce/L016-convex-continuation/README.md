# Rounded hulls and characteristic faces

Figure 0.1 of *Lorentz cones and domain solvability* illustrates the compact-seed argument in Theorem 0.1, equations (CC9)–(CC13). For the symbol R(xi)=xi_1, the only characteristic unit normals are vertical. The seed rectangle has a strictly larger vertical support function than the target disk. Consequently every characteristic supporting face of every rounded hull remains inside the known zero strip.

The same resource set includes Figure 4.1 of *Planar domains and directional solvability*. Its upper half disk of radius three and two unit disks centered at (+/-2,0) give a circular example of the failure of locality. Equations (CG1)–(CG4) prove the exact horizontal and vertical slice assertions and both support-convex truncations.

The JSON file gives all coordinates, parameters and support functions. The Python source uses NumPy and Matplotlib to sample the exact support-point formulas at 4096 normal directions and the parametric circle boundaries. The PNGs are the reader images; the SVGs keep editable text. The marked rightmost point in Figure 0.1 illustrates a noncharacteristic normal and does not represent the support of a particular solution.

Run `python -B rounded-hulls-and-characteristic-faces.py` in this directory to reproduce the image and data files. The original diagram, data and source are dedicated to the public domain under CC0 1.0 Universal. The lesson contains the full proof and the precise continuation hypotheses.
