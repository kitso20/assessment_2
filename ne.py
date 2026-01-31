def sum_numbers_until_zero(num,length):
    return sum([n for n in range(1,((length+1)*num)) if n % num == 0])

print(sum_numbers_until_zero(3,10))