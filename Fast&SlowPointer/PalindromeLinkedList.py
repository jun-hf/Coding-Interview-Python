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

