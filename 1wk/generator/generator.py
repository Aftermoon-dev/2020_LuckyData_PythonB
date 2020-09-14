# 등차수열
print("등차수열 : ")
def getAS(start, diff):
    while True:
        yield start
        start = start + diff

AS = getAS(1, 4)
for i in range(5):
    print(next(AS))

# 등비수열
print("\n등비수열 : ")
def getGS(start, ratio):
    while True:
        yield start
        start = start * ratio

gs = getGS(1, 2)
for i in range(12):
    print(next(gs))


# 계차 수열
print("\n계차 수열 : ")
def getDS(numberList):
    for i in range(len(numberList)):
        yield numberList[i+1] - numberList[i]

numList = [2, 4, 6, 8, 10]
ds = getDS(numList)
while True:
    try: 
        print(next(ds))
    except:
        print("List END")
        break

