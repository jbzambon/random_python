# Simple program to convert Degrees:Minutes
# to Decimal Degrees.
#
# Joseph B. Zambon
# 3 August 2016

import numpy as np
# Deg/Min -> Degrees
# Put however much data you want into this.
# Pair off degrees/minutes into sub-arrays.
inp_dm = [[-69,6.158448],[56,20.726100],[84,27.466920],[23,14.040000],[53,20.725800]]

def dm2decdeg(deg,mnt):
    is_positive = deg >= 0
    dd = abs(deg)
    dd_int = int(deg)
    dd_dec = (mnt)/60
    dd = dd_int+dd_dec if is_positive else -dd_int-dd_dec
    return(dd)

for x in range(len(inp_dm[:,0])):
    dd = dm2decdeg(inp_dm[x,0],inp_dm[x,1])
    print "%08f" % (dm)
