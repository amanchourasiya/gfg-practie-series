# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

def min_max(l):
    mx = -2 ** 31
    mn = 2 ** 31 -1
    for i in l:
        if i>mx:
            mx = i
        elif i < mn:
            mn = i
    
    return mn, mx
            

print(min_max([4,2,1,4,5,6,8,2]))