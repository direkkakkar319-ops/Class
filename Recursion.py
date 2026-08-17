# %%
def fun1(n):
    print(n)
def fun2(n):
    fun1(n+1)
    print(n)
fun2(5)

# %%
# printing till the nth value is reached
def fun(n):
    if n == 6:
        return
    print(n)
    fun(n+1)
fun(1)

# %%
# printing the sum of n natural numbers
def fun(n)-> int:
    if n<1:
        return 0
    return n + fun(n-1)
    
fun(5)

# %%
# recursion tree
def fun(n):
    if n<=0:
        return 
    print(n)
    fun(n-1)
    fun(n-2)
fun(3)

# %%
# printing fibonacci series using the resursion tree
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter a value"))
for i in range(0, n):
    print(fibonacci(i))

# %%
# printing the nth term of the fibonacci series
def fib(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n+1):
            a, b = b, a+b
        return b
fib(5)

# %%
# printing sum of fibonacci series
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
fibo(3)

# %%
# printing the number from 1 to n
def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n, end=" ")
n = int(input())
print_1_to_n(n)

# %%
# printing the number from n to 1
def print_n_to_1(n):
    if n==0:
        return
    print(n, end=" ")
    print_n_to_1(n-1)
n=int(input())
print_n_to_1(n)

# %%
# Recursive function to find maximum
def find_max(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1], find_max(arr,n-1))

n=int(input("Enter length of array"))
arr=list(map(int,input().split()))
find_max(arr,n)

# %%
# Recursive function to find maximum
def find_max(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1], find_max(arr,n-1))
n=int(input())
arr=list(map(int, input().replace(',', ' ').split()))
print(find_max(arr,n))

# %%
def binary_search(arr, low, high, x):
    if low > high:
       return -1 #element not found
    
    mid = (low + high) // 2
    
    if arr[mid]==x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)

# Input
arr = list(map(int, input().split()))   # Sorted array
x = int(input())                         # Element to search

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

# Output
print(result)
# %%
def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:])+s[0]
s=str(input())
print(reverse_string(s))

# %%
def facgt(n):
    if n<=0:
        return 1
    return n*facgt(n-1)
facgt(5)

# %%
def ss(n):
    if n<=0:
        return 0
    return n%10+ss(n//10)
ss(123)

# %%
def rev(n)->int:
    if n<=0:
        return 0
    return n%10 + rev(n//10)
rev(120)

# %%
# HCF (GCD) using recursion — Euclidean algorithm
def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

# LCM using recursion — lcm(a,b) = a*b // hcf(a,b)
def lcm(a, b):
    return a * b // hcf(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("HCF:", hcf(a, b))
print("LCM:", lcm(a, b))
