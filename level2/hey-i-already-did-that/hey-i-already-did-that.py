def n2b(digits,b):
    val = 0
    for i,item in enumerate(digits):
        val+=int(item)*b**(len(digits)-i-1)
    return(val)

def b2n(n,b):
    d=[]
    while n>0:
        r=n%b
        n=n/b
        d.append(r)
    return(d)

def compute(n,b,seen):
    asc = n2b(sorted(n),b)
    dsc = n2b(sorted(n,reverse=True),b)
    val = b2n((dsc - asc),b)
    if (val not in seen):
        seen.append(val)
    else:
        return(str(len(seen)-seen.index(val)))
    return compute(val,b,seen)

def solution(n,b):
    return(compute(n,b,[]))
