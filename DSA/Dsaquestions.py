def hcf(a,b):
    while b!=0:
        a,b = b,a%b
    return a
print(hcf(12,36))

def lcm(a,b):
    return (a*b)//hcf(a,b)
print(lcm(12,36))

# first occurance
def firstOccurance(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    while low<=high:
        mid = (low + high)//2

        if arr[mid] == target:
            ans = mid
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return ans

t = int(input("enter element to be found"))

nums = [1,2,2,2,3,4]

nn4 = firstOccurance(nums,t)
print(nn4)


# last occurance
def lastOccurance(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    while low<=high:
        mid = (low + high)//2

        if arr[mid] == target:
            ans = mid
            low = mid+1
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return ans

t = int(input("enter element to be found"))

nums = [1,2,2,2,3,4]

nn5 = lastOccurance(nums,t)
print(nn5)


# finding first and last occurance of an element:
class solution:
    # first occurance
    def search(self,arr,target):
        def firstOccurance():
            n = len(arr)
            low = 0
            high = n-1
            ans = -1
            while low<=high:
                mid = (low + high)//2

                if arr[mid] == target:
                    ans = mid
                    high = mid-1
                elif arr[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return ans
        # last occurance
        def lastOccurance():
            n = len(arr)
            low = 0
            high = n-1
            ans = -1
            while low<=high:
                mid = (low + high)//2

                if arr[mid] == target:
                    ans = mid
                    low = mid+1
                elif arr[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
            return ans
        return [firstOccurance(),lastOccurance()]
t = int(input("enter element to be found"))
nums = [1,2,2,2,3,4]
l = solution()
print(l.search(nums,t))


# kadans algorithm
def maxSubarray(arr):
    currentSum = maxSum = arr[0]

    for i in range(1,len(arr)):
        currentSum = max(currentSum,arr[i]+currentSum)
        maxSum = max(currentSum, maxSum)
    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(nums))


# prefix array
def prefixSum(arr):
    n = len(arr)
    pre = [0]*n
    pre[0] = arr[0]

    for i in range(1,n):
        pre[i] = pre[i-1] + arr[i]
        
    return pre 

nums = [1,2,3,4,5,6,7,8,9,10]
nn = prefixSum(nums)
print(nn)




class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertNode(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newNode

    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end="-->")
            curr = curr.next
        print("None")

    def frontNode(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def lastNode(self, val):
        newNode = ListNode(val) 
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newNode

    def anyIndexNode(self,val,k):
        newNode = ListNode(val)

        if k == 0:
            newNode.next = self.head
            self.head = newNode
            return self.head
        
        curr = self.head
        for _ in range(0,k-1):
            if curr is None:
                print("Index out of range")
                return 
            curr = curr.next
            
        if curr is None:
            print("index out of range")
        newNode.next = curr.next
        curr.next = newNode
        return self.head

    def deleteNode(self,k):
        if self.head is None:
            return 
        if k == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(k-1):
            if curr is None:
                return 
            curr = curr.next
        if curr.next is not None:
            curr.next = curr.next.next

    def deleteNodeFastPointer(self,k):
        p1 = self.head
        p2 = self.head
        for _ in range(k):
            if p2 is None:
                return 
            p2 = p2.next
        if p2 == None:
            self.head = self.head.next
            return 
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return 
    
    def findMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def hasCycle(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def hashCyclePos(self):
        slow = self.head
        fast = self.head
        hashCyclevar = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast  = fast.next.next
            if slow == fast:
                hashCyclevar = True
                break
        if not hashCyclevar:
            return None
        lenght = 1
        fast = fast.next
        while slow!=fast:
            fast = fast.next
            lenght+=1
        slow = self.head
        fast = self.head
        for _ in range(lenght):
            fast = fast.next
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return slow 
    
    def rotateList(self,k):
        if self.head is None or self.head.next is None:
            return self.head
        last = self.head
        length = 1
        while last.next is not None:
            last = last.next
            length += 1
        k = k % length
        if k == 0:
            return self.head
        curr = self.head
        for i in range(length-k-1):
            curr = curr.next
        last.next = self.head
        self.head = curr.next
        curr.next = None 

    def deleteNodefront(self):
        if self.head is None:
            return
        self.head = self.head.next

    def deleteNodeLast(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def reverseNode(self):
        prev = None
        nxt = None
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
# taking input of nodes for making linked list
l = LinkedList()
n = int(input("enter number of nodes: "))
for i in range(n):
    val = int(input(f"enter node number {i + 1}: "))
    l.insertNode(val)
print("Original Linked List:")
l.display()
index = int(input("enter index of which node is to be deleted"))
l.deleteNodeFastPointer(index)
l.display()
newNodefront = int(input("enter node to be inserted in front: "))
l.frontNode(newNodefront)
print("\nafter inserting node in front of the linked list")
l.display()
newNodelast = int(input("enter node to be inserted at the last: "))
l.lastNode(newNodelast)
print("\nafter inserting node at the last of the linked list")
l.display()
l.deleteNodefront()
print("\nafter deleting element from front of the linked list")
l.display()
l.deleteNodeLast()
print("\nafter deleting element from last of the linked list")
l.display()
newNodeanyindex = int(input("enter node to be inserted at any index"))
index = int(input("enter index where node is to be inserted"))
l.anyIndexNode(newNodeanyindex,index)
print("\nafter inserting node at the any index of the linked list")
l.display()
l.reverseNode()
print("\nafter reversing a linked list")
l.display()
index = int(input("enter index where node is to be deleted"))
l.deleteNode(index)
print("\nafter deleting element from the given index from a linked list")
l.display()





# maths
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        elif s > target:
            right -= 1

#seive-->tell use the prime numbers in the given range
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes
print(sieve(30))
# kadans algorithm
def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit
# RANGE SUM QUERY
def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

# binary
def mySqrt(x):
    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid - 1

    return right

def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

def subarraySum(nums, k):
    prefix_map = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        count += prefix_map.get(current_sum - k, 0)
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count

def first_unique(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for x in arr:
        if freq[x] == 1:
            return x

    return -1