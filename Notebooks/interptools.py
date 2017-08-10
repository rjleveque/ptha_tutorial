from __future__ import print_function
from numpy import ma
import os, glob, re
import matplotlib.pyplot as plt
import numpy as np
from pylab import find

def interp(xi,yi,x,y,z):
    """
    Given 2d arrays x,y,z of data (on rectangular grid with uniform spacing),
    Interpolate to points specified by xi,yi and return zi.
    Uses bilinear interpolation, extrapolating if xi,yi outside limits of data

    If xi and yi are both floats, returns a float.
    If xi is a float and yi a 1-dimensional array (or vice versa), 
        returns a 1-d array
    If xi and yi both have the same shape (1-d or 2-d arrays), returns
        an array of the same shape.
    """

    X = x; Y = y; Z = z;
    if y[1,0] == y[0,0]:
        X = X.T
        Y = Y.T
        Z = Z.T
    if Y[1,0] < Y[0,0]:
        Y = np.flipud(Y)
        Z = np.flipud(Z)
    my,mx = X.shape
    xlow,ylow = X[0,0], Y[0,0]
    dx = X[0,1]-X[0,0]
    dy = Y[1,0]-Y[0,0]
    
    xoff = (xi-xlow)/dx
    yoff = (yi-ylow)/dy

    ii = xoff.astype(int)
    ii = np.where(ii > 0, ii, 0)
    ii = np.where(ii < mx-1, ii, mx-1)

    ji = yoff.astype(int)
    ji = np.where(ji > 0, ji, 0)
    ji = np.where(ji < my-1, ji, my-1)
    
    alphax = (xi - X[ji,ii]) / dx
    alphay = (yi - Y[ji,ii]) / dy
    w00 = (1-alphax)*(1-alphay)
    w01 = alphax*(1-alphay)
    w10 = (1-alphax)*alphay
    w11 = alphax*alphay
    zi = w00*Z[ji,ii] + w01*Z[ji,ii+1] + w10*Z[ji+1,ii] + w11*Z[ji+1,ii+1]
        
    return zi


def transect(xy1,xy2,x,y,z,npts=1001):
    xi = np.linspace(xy1[0], xy2[0], npts)
    yi = np.linspace(xy1[1], xy2[1], npts)
    zi = np.array([interp(xii,yii,x,y,z) for xii,yii in zip(xi,yi)])
    zi = interp(xi,yi,x,y,z)
    return xi,yi,zi

def query_transect(x,y,z,ax=None,ax2=None):
    """
    Given 2d arrays x,y,z do a contourf plot of z and then prompt 
    user to click on end points of a transect.

    """

    if ax is None:
        plt.figure()
        ax = plt.axes()
        cplot = ax.contourf(x,y,z)
        ax.ticklabel_format(format='plain',useOffset=False)
        plt.xticks(rotation=20)
        y0 = 0.5*(y[0,0]+y[-1,-1])
        ax.set_aspect(1./(np.cos(y0*np.pi/180.)))
        plt.colorbar(cplot, ax=ax)

    print("Click transect end points on map... ")
    xy1 = ax.figure.ginput(1,timeout=0)[0]
    ax.plot([xy1[0]],[xy1[1]],'r+',markersize=12)
    xy2 = ax.figure.ginput(1,timeout=0)[0]
    ax.plot([xy2[0]],[xy2[1]],'r+',markersize=12)
    ax.plot([xy1[0],xy2[0]], [xy1[1],xy2[1]], 'r-')
    plt.show()

    xi,yi,zi = transect(xy1,xy2,x,y,z)
    if ax2 is None:
        plot_transect_zi(xi,yi,zi,fill_below=0)
    else:
        plot_transect_zi(xi,yi,zi,ax=ax2,fill_below=0)
    return xi,yi,zi

def plot_transect_zi(xi,yi,zi,ax=None,clear=True,fill_below=None):

    if (abs(xi[-1]-xi[0]) > 0.5*abs(yi[-1]-yi[0])):
        ti = xi
        xtext = 'longitude'
    else:
        ti = yi
        xtext = 'latitude'

    if ax is None:
        fig = plt.figure()
        ax = plt.axes()
    if clear:
        ax.cla()
    ax.plot(ti,zi)
    plt.xlabel(xtext)
    ax.ticklabel_format(format='plain',useOffset=False)
    plt.xticks(rotation=20)
    plt.ylabel('meters')
    plt.title('Elevation vs. %s' % xtext)
    if fill_below is not None:
        ax.fill_between(ti, zi, fill_below, (zi<fill_below), 
                interpolate=True, color='b')

def query_point(X,Y,Z,axes):
    print("Click point on map... ")
    xy = plt.ginput(1,timeout=0)[0]
    xi = [xy[0]]
    yi = [xy[1]]
    axes.plot(xi,yi,'k+',markersize=12)
    zi = interp(xi,yi,X,Y,Z)
    return xi,yi,zi
    
def query_points(X,Y,Z,axes):
    while True:
        print("Click point on map... ")
        xy = plt.ginput(1,timeout=0)[0]
        xi = [xy[0]]
        yi = [xy[1]]
        axes.plot(xi,yi,'k+',markersize=12)
        zi = interp(xi,yi,X,Y,Z)
        print("x = %g, y = %g, z = %g" % (xy[0],xy[1],zi))
    
def query_transect2(x,y,z,axes):
    """
    Given 2d arrays x,y,z do a contourf plot of z and then prompt 
    user to click on end points of a transect.

    """

    print("Click transect end points on map... ")
    xy1 = plt.ginput(1,timeout=0)[0]
    axes.plot([xy1[0]],[xy1[1]],'r+',markersize=12)
    xy2 = plt.ginput(1,timeout=0)[0]
    axes.plot([xy2[0]],[xy2[1]],'r+',markersize=12)
    axes.plot([xy1[0],xy2[0]], [xy1[1],xy2[1]], 'r-')
    plt.show()

    xi,yi,zi = transect(xy1,xy2,x,y,z)
    #plt.figure()
    ax2 = plt.axes((.05,.7,.2,.2))
    plot_transect_zi(xi,yi,zi,axes=ax2)
    return xi,yi,zi

