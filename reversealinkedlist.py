

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    q = None
    p = head
    while p != None:
        r = p.next
        p.next = q
        q = p
        p = r
    return q

