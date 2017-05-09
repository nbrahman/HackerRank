"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head:
        n_node = head
        nn_node = head
        while n_node and nn_node and nn_node.next:
            n_node = n_node.next
            nn_node = nn_node.next.next
            if n_node == nn_node:
                return True
        return False