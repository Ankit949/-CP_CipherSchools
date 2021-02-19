def RemoveAllDublicates(head):
    dummy=Node(0)
    current=dummy
    prev=dummy
    while(head):
        if head.data!=head.next.data:
            head=head.next
            prev.next=head
            head=head.next
        head=head.next

    return dummy

#in O(1) extra space

def RemoveAllDublicates1(head):
    if head !=None or head.next!=None:
        return head
    head=current
    while(current.next):
        if current.data==current.next.data:
            current.next=current.next.next
            current=current.next
        else:
            current=current.next
    return head
    