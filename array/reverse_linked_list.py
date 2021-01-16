# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

def reverseWord(s):
    #your code here
    l = []
    l[:0] = s
    #l = s.split('')
    #print(l)
    
    start = 0
    end = len(l) -1
    while start < end:
        l[start], l[end] = l[end], l[start]
        #print('swapping')
        start+=1
        end-=1
    #print(l)
    return ''.join(l)

print(reverseWord('Geeks'))