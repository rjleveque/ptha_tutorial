#########################################################
#DATAFILE: fixed_xyB_small.npy (bythy.txt is a .txt version)

#This .npy file has 3 columns and 250*250 rows, one row
#per grid point location in Crescent City.  The first 
#250 rows are for the points at the southern most latitude,
#with the first point being the SW corner, and the 250th
#point being the SE corner.  The last set of 250 points
#correspond to the row of points on the northern most
#latitude, with the last point being the NE corner. 

#To read in it in Python:

d=load('fixed_xyB_small.npy')
x=d[:,0]; y=d[:,1]; B=d[:,2];

#To make these into a 2D structures:
Nptsx=250; Nptsy=250;
B=B.reshape((Nptsx,Nptsy),order='F')
x=x.reshape((Nptsx,Nptsy),order='F')
y=y.reshape((Nptsx,Nptsy),order='F')

#Now as the first argument increases, the longitude increases
#and latitude remains fixed.  Likewise, as the second argument
#increases, the latitude increases and the longitude remains fixed.

# To read in and then write out as a text file `xyB.txt` with three
# columns x,y,B, open a terminal and type
#    python make_xyB.py

