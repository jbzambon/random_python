# Simple program to convert Degrees:Minutes
# to Decimal Degrees.
#
# Joseph B. Zambon
# 3 August 2016

import numpy as np
# Deg/Min -> Degrees
# Put however much data you want into this.
# Pair off degrees/minutes into sub-arrays.
#inp_dm = [[-69,6.158448],[56,20.726100],[84,27.466920],[23,14.040000],[53,20.725800]]
#inp_dm = [[40,0.178],[-69,6.154],[40,0.224],[69,6.161],[40,0.239],[69,6.162],[40,0.325],[69,6.074],[40,0.332],[69,6.057],[40,0.336],[69,6.05],[40,0.347],[69,6.011],[40,0.396],[69,5.959],[40,0.402],[69,5.954],[40,0.435],[69,5.937],[40,0.538],[69,5.879],[40,0.542],[69,5.877],[40,0.546],[69,5.876]]
inp_dm = [[34,57.306],[-74,25.002],[34,57.306],[-74,25.002],[34,48.000],[-74,42.600],[34,54.000],[-74,49.500],[35,0.000],[-74,57.000],[35,4.200],[-75,1.500],[35,6.000],[-75,3.900]]
inp_dm=np.asarray(inp_dm)

def dm2decdeg(deg,mnt):
    is_positive = deg >= 0
    dd = abs(deg)
    dd_int = int(deg)
    dd_dec = (mnt)/60
    dd = dd_int+dd_dec if is_positive else -dd-dd_dec
    return(dd)

for x in range(len(inp_dm)):
    dd = dm2decdeg(inp_dm[x,0],inp_dm[x,1])
    print "%08f" % (dd)
