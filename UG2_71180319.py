import random
import timeit
def generate_list(n):
    batas_atas = n*100
    randomlist = random.sample(range(0,batas_atas),n)
    randomlist.sort()
    return randomlist
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
for i in range(1,10+1):
    data = generate_list(i)
    start = timeit.default_timer()
    hasil = fibo(i)
    end = timeit.default_timer()
    print('Fibonacci Ke - ', i, '= ', hasil,': ', end-start,' second')