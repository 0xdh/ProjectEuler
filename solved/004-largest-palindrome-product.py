def is_palindrome(n):
    ns = str(n)
    ns_reversed = ns[::-1]
    return ns == ns_reversed

max_num = 0
for num1 in range(100,1000):
    for num2 in range(num1,1000):
        prod = num1 * num2
        if is_palindrome(prod):
            max_num = max(prod, max_num)

print(max_num)