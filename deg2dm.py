# Simple program to convert Decimal Degrees
# to Degrees:Minutes.
#
# Joseph B. Zambon
# 3 August 2016

import numpy as np
# Degrees -> Deg/Min
# Put however much data you want into this.
#inp_dd = [-69.5901602,39.81040012,-69.5898,39.81056,-69.59009012,39.81127385,-69.58976309,39.81124346,-69.5895,39.81141]
inp_dd=[69.28504170633249,39.86742112361463,-69.28502201520864,39.87578439929273]

def decdeg2dm(dd):
    is_positive = dd >= 0
    dd = abs(dd)
    dd_int = int(dd)
    mnt = (dd-dd_int)*60
    deg = dd_int if is_positive else -dd_int
    return(deg,mnt)

for x in range(len(inp_dd)):
    deg,mnt = decdeg2dm(inp_dd[x])
    print " %d %08f " % (deg, mnt)

