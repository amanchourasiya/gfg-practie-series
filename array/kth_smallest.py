# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

import heapq

def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    h = []
    heapq.heapify(h)

    for i in range(k):
        heapq.heappush(h, arr[i] * -1)
    #print(h)

    for i in range(k, r+1):
        #print(h)
        if -1*h[0] > arr[i]:
            heapq.heappop(h)
            heapq.heappush(h, -1 * arr[i])
        
    
    return -1 * h[0]


print(kthSmallest([7,10,4,3,20,15], 0, 5, 3))

