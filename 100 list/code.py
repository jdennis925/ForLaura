def FactMult(theNumber, theMax):
    result = []
    for i in range(1, theNumber):
        remainder = theNumber % i
        if remainder == 0:
            result.append(i)
    for j in range(1, theMax+1):
        mult = theNumber*j
        if mult <= theMax:
            result.append(mult)
    result.remove(theNumber)
    return result

max = 100
result_new = {}
for k in range(1, max + 1):
    result_new[k] = FactMult(k,max)

print(result_new)

f = open('laura.csv', 'w')

for i in result_new:
    for j in result_new[i]:
        f.write(str(i)+ ',')
        f.write(str(j) + ',\n')

# def FindFunc(curList):
#     lastValue = curList[len(curList)-1]
#     multiplesAndFactors = result_new[lastValue]
#     resultList = []
#     for item in multiplesAndFactors:
#         if item not in curList:
#             newList = list(curList)
#             newList.append(item)
#             resultList.append(newList)
#             otherList = FindFunc(newList)
#             for n in otherList:
#                 resultList.append(n)
#     return resultList


# longestList = []
# for m in range(2, max + 1):
#     x = FindFunc([m])
#     for tempList in x:
#         if (len(tempList) > len(longestList)):
#             longestList = tempList
#             print(longestList)

# print('List Length')
# print(len(longestList))
# print(longestList)

