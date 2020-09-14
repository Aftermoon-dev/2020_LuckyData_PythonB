import math

# Get Percentage Function
def getPercentage(x, y):
    return (x/y) * 100

per = lambda x,y:(x/y)*100

# Get Squared Function
def getSquared(x):
    return x * x

sqd = lambda x:x*x

# Get Cylinder's Volume
def getCylinderVolume(r, h):
    return math.pi * getSquared(r) * h

cyvol = lambda r,h: math.pi * sqd(r) * h

print("Get Percentage :")
print("Normal Function :", getPercentage(123, 653))
print("Lambda Function :", per(123, 653))
print()
print("Get Squared :")
print("Normal Function :", getSquared(8))
print("Lambda Function :", sqd(8))
print()
print("Get Cylinder's Volume :")
print("Normal Function :", getCylinderVolume(9, 10))
print("Lambda Function :", cyvol(9, 10))
