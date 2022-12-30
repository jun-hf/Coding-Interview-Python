"""
You just need to move move the fast and slow pointer

"""

def find_middle_node(head):
    slow = head 
    fast = head

    while fast.next != None and fast != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow