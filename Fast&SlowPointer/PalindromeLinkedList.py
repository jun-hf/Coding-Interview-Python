"""
Given a head of a single linked list, write a function that
determine if the list is a palindrome. 

1. Time complexity o(n)
2. Space complexity o(1)
3. Cannot change the list

Design:
I cannot tranverse to the end and compare, because is a single direction
I cannot store it into a stack also because Space needs to be constant

2 -> 4 -> 8 -> 10 -> 8 -> 4 -> 2 -> null

next_node: 4
curr_node: 4
prev_node: null

none <- 2 

while curr_node != null:
    next_node = curr_node.next
    curr_node.next = prev_node

    prev_node = curr_node
    curr_node = next_node

return prevuoe




Can I just reverse the linked list then compare it?

Design:

  None <-1 <- 2  3 -> null

def reverse_list(head):
    curr_node = 3
    prev_node = 2
    next_node = 3

    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node

    return prev_node


"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

"""

1 -> 2 -> 3 -> 2 -> 1
l1 2

1 -> 2 -> 3 -> 2 -> 1 
l2 2

"""
def is_palindrome(head):

    ll1 = head
    ll2 = reverse_linked_list(head) # space complexity of O(N)
     
    while ll1 != None:

        if ll1.value == ll2.value:
            ll2 = ll2.next
            ll1 = ll1.next
        else:
            return False
    
    return True

def reverse_linked_list(head):
    curr_node = head 
    prev_node = None
    next_node = None

    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node

        prev_node = curr_node
        curr_node = next_node

    return prev_node


"""
Design:


1 -> 2 -> 2 -> 1

How can I reverse the second half part of the array? if the linked list is odd or even cause is diffrent
"""

def test(head):
    original = head
    prev = None

    while head != None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    
    test(original)
    test(head)


def print_all(head):
    
    while head != None:
        print(head.value)
        head = head.next

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(4)


    test(head)
    # print(is_palindrome(head))


main()