from functools import cmp_to_key

def compare(a, b):
    print("a = ",a,"b = ",b,",b-a = ",b-a)
    return b - a

nums = [3,1,4,2]

sorted_nums = sorted(nums, key=cmp_to_key(compare))
print(sorted_nums)

'''
KeyWrapper(1) < KeyWrapper(3)
compare(1, 3)
compare(4, 1)
compare(4, 3)
compare(2, 3)
compare(2, 1)
Returns positive (> 0) → a should come after b.
Returns negative (< 0) → a should come before b.
'''
