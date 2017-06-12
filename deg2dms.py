# Simple program to convert Decimal Degrees
# to Degrees:Minutes:Seconds
#
# Joseph B. Zambon
# 3 August 2016

# Degrees -> Deg/Min/Sec
inp_dd=raw_input("Decimal Degrees to Convert: ")
inp_dd=float(inp_dd)

def decdeg2dms(dd):
    is_positive = dd >= 0
    dd = abs(dd)
    mnt,sec = divmod(dd*3600,60)
    deg,mnt = divmod(mnt,60)
    deg = deg if is_positive else -deg
    return (deg,mnt,sec)

deg,mnt,sec = decdeg2dms(inp_dd)
print(["Degrees: ", deg])
print(["Minutes: ", mnt])
print(["Seconds: ", sec])
print([deg,mnt,sec])

