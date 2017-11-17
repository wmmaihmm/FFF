


def _odd_iter():
    n = 1
    while n<1001 :
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x:x % n > 0
def primes():
    it = _odd_iter()
    n=3
    while n<997:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)


print (len (list(n for n in primes())))

    

