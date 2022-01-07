def maxInRange(someList, start, end):
    currentMax = someList[start]
    for i in range(start, end+1):
        if(someList[i] > currentMax):
            currentMax = someList[i]
    return currentMax

def minInRange(someList, start, end):
    currentMin = someList[start]
    for i in range(start, end+1):
        if(someList[i] < currentMin):
            currentMin = someList[i]
    return currentMin

def elementCounter(someList, element):
    count = 0
    for i in range(len(someList)):
        if (someList[i] == element):
            count += 1
    return count

def elementPos(someList, element):
    posCount = []
    for i in range(len(someList)):
        if (someList[i] == element):
            posCount.append(i)
    return posCount

def ranges(sortedList):
    first = 0
    range_list = []
    
    if(len(sortedList) == 0):
        return range_list
    if(len(sortedList) == 1):
        range_list.append((sortedList[0] , sortedList[0]))
        return range_list

    pair = (sortedList[first], sortedList[0])
    
    for i in range(len(sortedList)):
        if(i == len(sortedList)-1):
            pair = (sortedList[first] , sortedList[i])
            range_list.append(pair)
            break
        if(sortedList[i+1] == sortedList[i]+1):
            pair = (sortedList[first] , sortedList[i+1])
        else:
            pair = (sortedList[first] , sortedList[i])
            range_list.append(pair)
            first = i+1

    return range_list


def occupySlot(sequence):
    for i in range(len(sequence)-1):
        if(sequence[i] == 0):
            if(sequence[i-1] == 0 and sequence[i+1] == 0):
                sequence[i] = 1
    
    if(sequence[1] == 0):
        sequence[0] = 1
    if(sequence[len(sequence)-2] == 0):
        sequence[len(sequence)-1] = 1

    return sequence

def setMismatch(someList):
    mismatch = ()
    for i in range(len(someList)-1):
        if(someList[i] + 1 != someList[i+1]):
            mismatch = (someList[i+1],someList[i]+1)
            break
    return mismatch

if __name__ == "__main__":
    print (maxInRange([1,2,3,4,5,6,7,8], 1, 3))         # 4
    print (maxInRange([1,20,3,4,5,6,7,8], 1, 3))        # 20

    print (minInRange([1,2,3,4,5,6,7,8], 1, 3))         # 2
    print (minInRange([1,0,3,4,5,6,7,8], 1, 3))         # 0
    print (minInRange([1,0,3,-1,5,6,7,8], 1, 3))        # -1

    print (elementCounter([1,3,1,4,1,5,1,6,1,7], 1))    # 5
    print (elementPos([1,3,1,4,1,5,1,6,1,7], 1))        # [0, 2, 4, 6, 8]

    print (ranges([0,1,2,4,5,7]))                       # [(0, 2), (4, 5), (7, 7)]
    print (ranges([1,2,3,4,5,6,7,8]))                   # [(1, 8)]
    print (ranges([0,2,3,4,6,8,9]))                     # [(0, 0), (2, 4), (6, 6), (8, 9)]
    print (ranges([]))                                  # []
    print (ranges([4]))                                 # [(4, 4)]

    print (occupySlot([0,1,1,0,0]))                     # [0, 1, 1, 0, 1]
    print (occupySlot([0,0,0,0,0]))                     # [1, 0, 1, 0, 1]
    print (occupySlot([0,1,0,0,0]))                     # [0, 1, 0, 1, 0]

    print (setMismatch([1,1]))                          # (1, 2)
    print (setMismatch([1,2,2,4]))                      # (2, 3)
    print (setMismatch([1,2,3,4,5,9,7,8,9,10]))         # (9, 6)
