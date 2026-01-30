def sum_numbers_until_zero(nums: list):
    joined = "".join(str(item) for item in nums)
    splied = joined.split('0')    
    return sum([int(item) for item in list(splied[0])])


print(sum_numbers_until_zero([1, 2, 3, 0]))