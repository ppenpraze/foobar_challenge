def solution(n):  
    i=0
    primes = ""
    while len(primes)<n+6:
        i+=1
        isPrime = True
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                isPrime = False
                break
        if isPrime:
            primes+=str(i)
    return(primes[n+1:n+6])
