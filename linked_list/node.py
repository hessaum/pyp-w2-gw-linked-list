class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        if self.next:
            return "Node({0}) > Node({1})".format(self.elem, self.next.elem)
        else:
            return "Node({0}) > /".format(self.elem)
        
    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        return str(self)
