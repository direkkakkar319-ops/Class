# %%
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)


a.next = b
b.next = c
head = a
# %%
"""Travesring a linked list"""
def traverseList():
    curr = head
    while curr is not None:
        print(curr.data, end="-->")
        curr = curr.next
print(traverseList()) 
# %%
"""Inserting at last of link list"""
newNode = Node(4)
def insertAtLast():
    curr = head 
    while curr.next is not None:
        curr = curr.next 
    curr.next  = newNode

# %%
"""Inserting at front of link list"""
def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    head = newNode
    return head

head = insertAtFront(head, 5)
# %%
"""Inserting element at a given index in a link list"""
def insertAtIndex(head, index, val):
    if index == 0:
        newNode = Node(val)
        newNode.next = head
        return newNode

    curr = head
    count = 0

    while curr is not None and count < index - 1:
        curr = curr.next
        count += 1

    if curr is None:
        return head

    newNode = Node(val)
    newNode.next = curr.next
    curr.next = newNode

    return head
head = insertAtIndex(head, 3, 55)
print(traverseList())
# %%
"""Deleting head of the link list"""
def deleteHead(head):
    if head is None:
        return None

    return head.next
head = deleteHead(head)
print(traverseList())
# %%
"""Deleting last node of a linked list"""
def deleteTail(head):
    curr = head 
    
    while curr.next.next is not None:
        curr = curr.next
    
    curr.next = None 

    return head 
head = deleteTail(head)
print(traverseList()) 
# %%
"""Deleting an element at a given index in a link list"""
def deleteAtIndex(head, index, val):
    curr = head 
    if index == 0:
        head =  curr.next 
        return head 
    
    c = 0

    while c < index -1 and curr is not None:
        curr = curr.next 
        c += 1
    
    if curr is None:
        return head 
    
    newNode = Node(val) 
    newNode.next = curr.next 
    curr.next = newNode
    return head 
head = deleteAtIndex(head, 2, 5555)
print(traverseList())
# %%
"""Reversing a link list"""
def reverseList(head):
    curr = head 
    prev = None 
    nxt = None 

    while curr is not None:
        nxt = curr.next
        curr.next = prev 
        prev = curr 
        curr = nxt 
    
    head = prev 
    curr = head 
    return head 
head = reverseList(head)
print(traverseList())
