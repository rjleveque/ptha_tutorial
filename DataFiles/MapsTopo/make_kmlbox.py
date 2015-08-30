"""
Code to make the file CCregion.kml.  You can only run this if you have Clawpack installed.
The CCregion.kml file can be opened in Google Earth and should look like the image in
CCregion.png.

Note that longitude must be shifted by 360 degrees to work on GE.
"""

from clawpack.geoclaw import kmltools
kmltools.box2kml((235.79781-360, 235.82087-360, 41.739671,41.762726), fname='CCregion.kml',
        name='Crescent City subset', color='FFFFFF')

