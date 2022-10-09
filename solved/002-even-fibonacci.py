sum = 0

fib1 = 1
fib2 = 1

while fib1 < 4000000:
    fibnew = fib1 + fib2
    if fibnew % 2 == 0:
        sum += fibnew
    fib2 = fib1
    fib1 = fibnew 


print(sum)