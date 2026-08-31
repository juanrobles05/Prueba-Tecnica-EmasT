def findTheSingleNumber(items: list):
    result = []
    for item in items:
        if item in result:
            result.remove(item)
        elif item not in result:
            result.append(item)
    return result

def cleanZeros(items: list):
    result = []
    numOfZeros = 0
    for item in items:
        if item == 0:
            numOfZeros += 1
        else:
            result.append(item)

    for zero in range(numOfZeros):
        result.append(0)
    return result

def textCompressor(cadena: list):
    result = ''
    pastItem = ''
    count = 1
    for item in cadena:
        if item == pastItem:
            count += 1
        elif count > 1:
            result = result+str(count)
            count = 1

        if item != pastItem:
            result = result+item
            pastItem = item

    if count > 1:
        result = result+str(count)
    return result

def missingNumber(items: list):
    result = 0
    auxiliar = []
    i = 0
    for item in range(len(items)):
        auxiliar.append(i)
        i += 1

    for x in auxiliar:
        if x not in items:
            result = x

    return result

def main():
    input = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
    input1 = [0,1,-1,9,4,0,5,0,0,14,31]
    input2 = ['a','a','b','c','c','c','c','a','a','a']
    input3 = [1,2,3,5,6,7]
    result = findTheSingleNumber(input)
    result1 = cleanZeros(input1)
    result2 = textCompressor(input2)
    result3 = missingNumber(input3)
    print(result1)
    print(result)
    print(result2)
    print(result3)

if __name__ == "__main__":
    main()
