print("Decimal to Binary")
dec = int(input("Please Enter Decimal Number : "))
deccopy = dec
binarylist = []

while True:
    # if number is 1 or 0, break 
    if dec == 1 or dec == 0:
        binarylist.append(dec)
        break
    else:
        binarylist.append(dec % 2)
        dec = (int) (dec / 2)

print("Binary Number : ", end='')
for i in range(len(binarylist)-1, -1, -1):
    print(binarylist[i], end='')

print("\nPython bin() function : ", end='')
print(bin(deccopy))

