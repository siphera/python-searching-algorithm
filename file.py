def Binarysearch(mynumbers,element):
    first = 0
    last = len(mynumbers)-1
    index=-1
    while (first<=last) and (index==-1):
        mid=(first + last)//2
        if (mynumbers[mid]) == element:
            index=mid
        else:
            if element<mynumbers[mid]:
                last = mid-1
            else:
                first = mid + 1
    return index

import time
start = time.time()
print(Binarysearch([20, 30, 40, 60, 70, 80, 95, 100], 20))
end = time.time()
print(end - start)
