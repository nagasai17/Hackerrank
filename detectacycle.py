"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    h=[]
    i=0
    s=0
    if(head==None):
        return True
    while(head!=None):
        s=s+1
        if  h.count(head)==0:
            h.append(head)
        if(s>len(h)):
            break
        head=head.next
    if(s>len(h)):
        return True
    else:
        return False
    pass
