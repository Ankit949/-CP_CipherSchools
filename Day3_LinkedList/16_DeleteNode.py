def deleteNode(node):
    if node.next!=None:
        node.data=node.next.data
        node.next=node.next.next
