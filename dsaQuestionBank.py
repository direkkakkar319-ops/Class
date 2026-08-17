# %%
"""Reversing a String using Recursion"""
def reverseString(str, n):
    if n <= 0:
        return ""
    return  str[n-1] + reverseString(str, n-1)
print(reverseString("Direk", 5))

# %%
"""1. Print 1 to N Using Recursion"""
def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)
print_1_to_n(10)

#%%
"""2. Check Palindrome String"""
def checkPalindrome(s,n):
    if len(s)<1:
        return "Yes"
    if s[0]!=s[-1]:
        return "No"
    return checkPalindrome(s[-1:1],n)
print(checkPalindrome("tenent",6))

#%%
"""3. Fibonacci Series"""
# the nth term
def fibo(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print("="*40)
print(f"5thTerm = {fibo(5)}")
print("="*40)

# printing the nth term
def print_fibo(n):
    a,b=0,1

    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b 
print("="*40)
print(print_fibo(5)) 
print("="*40)
print() 

# sum of nth term
def sum_fibo(n):
    a,b=0,1
    sum_fib=0

    for i in range(n):
        sum_fib += a
        a,b=b,a+b 

    return sum_fib

print("="*40)
print("SUM = ",sum_fibo(5))
print("="*40)
print()
#%%
"""4. Recurring Digit Sum"""
def recurring(n):
    if n<10:
        return n

    total = 0
    while n>0:
        total += n%10
        n //= 10
    else:
        return recurring(total)
print("="*40)
print(f"Sum of Number to Single Digit is = {recurring(38)}")
print("="*40)
#%%
"""5. Tower of Hanoi"""
def tower_of_hanoi(n, source, auxiliary, destination):
    if n==1:
        print(f"Move disk 1 from Rod {source} to Rod {destination}")
        return tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from Rod {source} to Rod {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

n = int(input())
tower_of_hanoi(n, 'A', 'B', 'C')
#%%
"""
6. Merge Sort
    It is a divide and conquer algorithm with O(n log n) time complexity.
    
    Steps Involed are:-
        1. Splitting the array
        2. Merging the array
"""
def merge(nums, l, mid, r):
    """
    Merging the left and right array
    
    Parameters:
        nums - array 
        mid - middle index of array
        l - left array length 
        r - right array length
    """
    left = nums[l: mid + 1]
    right = nums[mid + 1: r + 1]

    i = j = 0
    k = l 

    while i<len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i+=1
        else:       #right[j]<left[i]
            nums[k] = right[j]
            j += 1
        k += 1
    
    # if left array elements are remaining
    while i<len(left):
        nums[k]=left[i]
        i += 1
        k += 1
    
    # if right array elements are remaining
    while j<len(right):
        nums[k]=right[j]
        j += 1
        k += 1

def split(nums, l, r):
    """
    Splitting the array into left and right

    Parameters:
        nums - array
        l - length of left array
        r - length of right array
    """
    if l >= r:
        return 
    mid = (l+r)//2
    split(nums, l, mid) 
    split(nums, mid+1, r)
    merge(nums, l, mid, r) 

def sortArray(nums):
    """
    Main sorting function
    Here the sort and merge happenes

    Parameter:
        nums - array
    """ 
    split(nums, 0,  len(nums)-1)
    return nums 

nums = [324, 342, 324, 4, 23432, 4, 32, 34]
sorted_nums = sortArray(nums)
print(sorted_nums)

#%%
"""7. Quick Sort"""

#%%
"""8. Next Smaller Element"""
def nextSmallerElememt(nums, n):
    """
    Parameters
        nums - array of numbers
        n - length of array
    """
    arr2 = []
    for i in range(0,n):
        count = i + 1
        found = False 

        while count<n:
            if nums[i]>nums[count]:
                arr2.append(nums[count])
                found = True
                break

            count += 1
        
        if not found:
            arr2.append(-1) 
    return arr2
# n = int(input("Enter length of nums"))
# nums = list(map(int, input("Enter numbers in nums").split()))
next = nextSmallerElememt([4, 2, 14, 7, 1, 9], 6)
# print(*next)
print(next)

#%%
"""9. Push and Pop (Stack)"""
MAX_SIZE = 100
a = [0]*100
top=-1

def push(ele):
    global top 
    if top<=MAX_SIZE:
        top+=1
        a[top] = ele 
        print(f"Element{ele} inserted at{top}")
    else:
        print(f"Element{ele} Cannot be inserted, Stack is full")

def pop(ele):
    global top
    if top>=0:
        ele = a[top]
        top-=1
        print(f"Popped element{ele}")
        return ele
    else:
        print(f"Stack is empty,element cannot be popped")

#%%
"""10. Peek, isEmpty, isFull"""
MAX_SIZE = 100
a = [0]*MAX_SIZE
top=-1

def peek():
    global top 
    if top>=0:
        ele = a[top]
        print("Peeked: {ele}")
        return a[top] 
    else:
        print("Stack is empty")
        return -1

def isFull():
    return top == MAX_SIZE

def isEmpty():
    return top == 0 
#%%
"""11. Evaluate Expression"""
def evaluate(s):
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+': stack.append(a + b)
            elif ch == '-': stack.append(a - b)
            elif ch == '*': stack.append(a * b)
    return stack[0]

#%%
"""12. Valid Parenthesis"""
def is_valid(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

T = int(input())
for _ in range(T):
    s = input().strip()
    result = "true" if is_valid(s) else "false"
    print(f"{s} : {result}")

#%%
"""13. isEmpty, isFull, functions of Queue"""
MAX_SIZE = 100
a = [0]*MAX_SIZE
front = 0
rear = -1
currentSize = 0 

def isEmpty():
    return currentSize == 0

def isFull():
    if currentSize == MAX_SIZE:
        return True
    else:
        return False

def size():
    return currentSize
#%%
"""14. Sliding Window Maximum"""
from collections import deque
import queue

t = int(input())

for _ in range(t):

    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    dq = deque()

    for i in range(n):
        # remove indexes outside window
        while dq and dq[0] <= i - x:
            dq.popleft()
        # remove smaller elements
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)
        
        # print answer when first window completed
        if i >= x - 1:
            print(arr[dq[0]], end=" ")
    print()
#%%
"""15. Enqueue and Dequeue Functions (Queues)"""
MAX_SIZE = 100
a = [0]*MAX_SIZE
front = 0
rear = -1
currentSize = 0 

def isEmpty():
    return currentSize == 0

def isFull():
    return currentSize == MAX_SIZE 

def size():
    return currentSize

def enqueue(item):
    if isFull():
        return "Queue is full"
    rear = (rear + 1) % MAX_SIZE
    arr[rear] = item
    currentSize += 1 

def dequeue():
    if isEmpty():
        return "Queue is empty"
    removed_item = a[front]
    front = (front+1)%MAX_SIZE
    currentSize -= 1
    return f"Item removed from Queue is {removed_item}" 

# %% 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four  = TreeNode(4)
five  = TreeNode(5)
six  = TreeNode(6)
eight  = TreeNode(8)
nine  = TreeNode(9)
ten  = TreeNode(10)

three.left = two 
three.right = nine 
eight.left = one 
eight.right = six 
four.left = eight
four.right = ten
five.left = three 
five.right = four 


root = five 
#%%
"""
16. PreOrder Traversal
Root-->Left-->Right
"""
def preOrder(node):
    if node is None:
        return 
    
    print(node.val, end = " ")
    preOrder(node.left)
    preOrder(node.right)

preOrder(root)
#%%
"""
17. PostOrder Traversal
Left-->Right-->Root
"""
def postOrder(node):
    if node is None:
        return 

    postOrder(node.left)
    postOrder(node.right)
    print(node.val, end=" ")

print(postOrder(root))

#%%
"""
18. InOrder Traversal
Left-->Root-->Right
"""
def inOrder(node):
    if node is None:
        return 
    
    inOrder(node.left)
    print(node.val, end=" ")
    inOrder(node.right)

print(inOrder(root))

#%%
"""19. Level Order Traversal"""
from collections import deque
def levelOrder(node):
    result = []
    queue = deque([])
    queue.append(node)

    while len(queue)!=0:
        e = queue.popleft()
        result.append(e.val)

        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
    
    return result

result = levelOrder(root)
print(*result)
#%%
"""20. Minimum Depth of Binary Tree"""
from collections import deque
def minimumDepth(node):
    if node is None:
        return 0
    
    queue = deque([(node, 1)])

    while len(queue)!=0:
        e, depth = queue.popleft()

        if e.left is None and e.right is None:
            return depth
        else:
            if e.left:
                queue.append((e.left, depth+1))
            else:
                if e.right:
                    queue.append((e.right, depth+1))

result = minimumDepth(root)
print(result)

#%%
"""21. Check for BST"""
def isBST(root):
    def check(node, low, high):
        if node is None:
            return True
        if not (low<node.val<high):
            return False 
        return(check(node.left, low, node.val) and check(node.right, node.val, high))
        
    if check(root , float("-inf") , float("inf")):
        print("YES")
    else:
        print("NO")

#%%
"""22. ZigZag Traversal"""
from collections import deque
def zigZagTraversal(node):

    if node is None:
        return

    result = []
    queue = deque([node])
    left_to_right = True

    while queue:
        level = []

        for i in range(len(queue)):
            root = queue.popleft()
            level.append(root.val)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        if not left_to_right:
            level.reverse()

        result.append(level)
        left_to_right = not left_to_right

    return result
print(zigZagTraversal(root))
#%%
"""23. Top view of the Binary Tree"""
from collections import deque

def top_view_input():
    n = int(input())
    children = set()
    tree = {}  # node -> {'L': child, 'R': child}

    for _ in range(n - 1):
        p, c, direction = input().split()
        p, c = int(p), int(c)
        if p not in tree:
            tree[p] = {}
        tree[p][direction] = c
        children.add(c)

    # Root = node that never appears as a child
    all_nodes = set(tree.keys()) | children
    root = (all_nodes - children).pop()

    # BFS with horizontal distance
    hd_map = {}
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()
        if hd not in hd_map:
            hd_map[hd] = node
        if node in tree:
            if 'L' in tree[node]:
                queue.append((tree[node]['L'], hd - 1))
            if 'R' in tree[node]:
                queue.append((tree[node]['R'], hd + 1))

    print(*[hd_map[hd] for hd in sorted(hd_map)])

top_view_input()
#%%
"""24. left side view of Binary tree"""
from collections import deque

def left_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == 0:              # first node of each level = leftmost
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

print(left_side_view(root))  # Output: [5, 3, 2, 1]
#%%
"""25. Search in BST"""
# If target < node → search left, if target > node → search right

def search_bst(root, target):
    if root is None:        # not found
        return False
    if root.val == target:
        return True
    if target < root.val:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

# Uses bst_root defined in Q26 — run Q26 cell first
print(search_bst(bst_root, 6))   # Output: True
print(search_bst(bst_root, 11))  # Output: False

#%%
"""26. Find maximum node in BST"""
# BST sample:
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#        / \   /
#       4   7 13

bst_root = TreeNode(8)
bst_root.left = TreeNode(3)
bst_root.right = TreeNode(10)
bst_root.left.left = TreeNode(1)
bst_root.left.right = TreeNode(6)
bst_root.left.right.left = TreeNode(4)
bst_root.left.right.right = TreeNode(7)
bst_root.right.right = TreeNode(14)
bst_root.right.right.left = TreeNode(13)

# In a BST, the maximum is always the rightmost node
def find_max_bst(root):
    if root.right is None:
        return root.val
    return find_max_bst(root.right)

print(find_max_bst(bst_root))  # Output: 14
#%%
"""27. Kth Largest Node in BST"""
# Reverse in-order (Right -> Root -> Left) gives descending order in BST.
# The kth node visited is the kth largest.

def kth_largest(root, k):
    count = [0]
    result = [None]

    def reverse_inorder(node):
        if not node or result[0] is not None:
            return
        reverse_inorder(node.right)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        reverse_inorder(node.left)

    reverse_inorder(root)
    return result[0]

print(kth_largest(bst_root, 1))  # Output: 14 (1st largest)
print(kth_largest(bst_root, 3))  # Output: 10 (3rd largest)

#%%
"""28. Implementation - Create BST"""
# Insert into BST: smaller values go left, larger go right.

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def inorder(self, node, result=[]):
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result

bst = BST()
for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(val)

print(bst.inorder(bst.root, []))  # Output: [1, 3, 4, 6, 7, 8, 10, 13, 14]

# %%
"""29. Next greater Element"""
def nextGreaterElememt(nums, n):
    """
    Parameters
        nums - array of numbers
        n - length of array
    """
    arr2 = []
    for i in range(0,n):
        count = i + 1
        found = False 

        while count<n:
            if nums[i]<nums[count]:
                arr2.append(nums[count])
                found = True
                break

            count += 1
        
        if not found:
            arr2.append(-1) 
    return arr2
# n = int(input("Enter length of nums"))
# nums = list(map(int, input("Enter numbers in nums").split()))
next = nextGreaterElememt([4, 2, 14, 7, 1,9], 6)
# print(*next)
print(next)
# %%
