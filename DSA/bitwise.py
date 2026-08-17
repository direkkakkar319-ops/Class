"""
BITWISE OPERATIONS
"""
a=12
b=13

"""Implementing AND gate"""
print("="*40)
print(a & b)
print("="*40)
print(format(a&b, '04b'));
print()

"""Implementing OR gate"""
print("="*40)
print(a | b)
print(format(a | b), '04b')
print("="*40)
print()

"""Implementing NOT gate"""
print("="*40)
print(~b)
print(~a)
print("="*40)
print()

"""Implementing XOR gate"""
print("="*40)
print(a ^ b)
print(format(a ^ b, '04b'))
print("="*40)
print()

"""Implementing left shift"""
print("="*40)
print(a << 1) #adding one zero to the  of right the number
print(a << 2)
print("="*40)
print()

"""Implementing right shift"""
print("="*40)
print(a >> 1) #adding one zero to the left of number
print(a >> 2)
print("="*40)
print()

"""Implementing the count bit function"""
def count_bits(n):
    count=0
    while n>0:
        if n&1:
            count+=1
        n=n>>1
    return count
print("="*40)
print(count_bits(a))
print("="*40)
print()

"""Implementing the reverse bitwise counting"""
def reverse_bits(n):
    rev = 0
    while n > 0:
        rev = (rev << 1) | (n & 1)
        n = n >> 1
    return rev
print("="*40)
print(reverse_bits(a))
print(12 & 1)
print("="*40)
print()

"""check if the number is of power of 2"""
def pow_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
print("="*40)
print(pow_of_two(12))
print(pow_of_two(8)) 
print("="*40)
print()