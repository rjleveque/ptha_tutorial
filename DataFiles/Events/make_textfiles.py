
"""
Convert each event file `h_eta_small.npy` giving the zeta values for the
event to text form, which are larger files but easier to read by other
software packages.

To run this code, open a terminal, navigate to this directory, and type:
    python make_textfiles.py

"""

import sys, os
import numpy

# read in topography file, which also has x,y locations of all grid points:

fixed_grid_file = '../MapsTopo/fixedgrid_xyB_small.npy'
d = numpy.load(fixed_grid_file)
x = d[:,0]
y = d[:,1]
B = d[:,2]

all_events = ['AASZa', 'AASZb', 'AASZc', 'AASZd', 'CSZa', 'CSZb', 'CSZc',\
              'CSZd', 'CSZe', 'CSZf', 'KmSZa', 'KrSZa', 'SChSZa', 'TOHa']

for event_dir in all_events:
    zeta_file = os.path.join(event_dir, 'h_eta_small.npy')
    zeta = numpy.load(zeta_file)

    fname = os.path.join(event_dir, 'h_eta_small.txt')
    data_array = numpy.vstack((x, y, zeta)).T
    numpy.savetxt(fname, data_array, fmt='%24.10f')
    print "Created file ", os.path.abspath(fname)

