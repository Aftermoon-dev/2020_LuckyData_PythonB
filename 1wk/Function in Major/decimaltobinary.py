# 10진수 숫자를 2진수로 변환하기

def decimaltobinary(dec):
    binarylist = []
    while True:
        # if number is 1 or 0, break 
        if dec == 1 or dec == 0:
            binarylist.append(dec)
            break
        else:
            binarylist.append(dec % 2)
            dec = (int) (dec / 2)

    # Print List Element (Reverse)
    print("Binary Number : ", end='')
    for i in range(len(binarylist)-1, -1, -1):
        print(binarylist[i], end='')


print("Decimal to Binary")
num = int(input("Please Enter Decimal Number : "))
decimaltobinary(num)

# 파이썬 내장 함수와 비교
print("\nPython bin() function : ", end='')
print(bin(num))