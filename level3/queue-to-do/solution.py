def xor(n):
 # returns XOR for 1 to n
 if n == 0:
     return(0)
 r = (n-1) % 4
 if r == 0:
     return(n-1)
 elif r == 1:
     return(1)
 elif r == 2:
     return(n)
 return(0)


def solution(start, length):
    cur = start
    total = 0
    i = 0
    while cur <= start+length**2-1:
        total^=xor(cur)^xor(cur+length-i)
        cur+=length
        i+=1
    return(total)

print(solution(17,4))
#print(solution(17,4))
