def sum_to(n):
    # Gives the result of the sum from 1 to the number n given
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum


print(sum_to(10))
