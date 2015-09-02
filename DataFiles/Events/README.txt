
Each event directory, e.g. AASZa, contains a file h_eta_small.npy
with the value of zeta at each grid point on the 250 x 250 grid covering a
portion of Crescent City.

These are binary files that can be read from Python using the `numpy.load`
function.

To convert them all to text files named `h_eta_small.txt` (with columns
x,y,zeta) open a terminal, navigate to this directory, and type:

    python make_textfiles.py

