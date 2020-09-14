import math

def getCylinderVolume():
    r = int(input("Please Enter Radius : "))
    h = int(input("Please Enter Height : "))
    return math.pi * (r * r) * h

def getCubeVolume():
    s = int(input("Please Enter Edge Length : "))
    return s * s * s

def getConeVolume():
    r = int(input("Please Enter Radius : "))
    h = int(input("Please Enter Height : "))
    return (1/3) * math.pi * (r * r) * h

functionList = [getCylinderVolume, getCubeVolume, getConeVolume]

print("Volume Calculator ")
print("1. Get Cylinder's Volume")
print("2. Get Cube's Volume")
print("3. Get Cone's Volume")

work = int(input("Please Enter Your Work : "))

print()
print(functionList[work-1]())
