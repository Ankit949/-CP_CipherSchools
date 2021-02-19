def OddEven(head):
    if head is None:
        return
    if head.next is None or head.next.next is None:
        return head
    dummy=Node(0)
    prev=dummy
    odd=head
    even=head.next
    while(odd and odd.next):
        prev.next=odd
        odd=odd.next.next
    if even.next.next==None:
        prev.next=even
    else:
        while(even and even.next):
            prev.next=even
            even=even.next.next
    return dummy.next
