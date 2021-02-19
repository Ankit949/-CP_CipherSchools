def Pallindrome(head):
    if head is None:return True
    slow=head
    fast=head

    while(fast or fast.next):
        slow=slow.next
        fast=fast.next.next

    fast=None
    while(head.next!=slow):
        next_node=head.next
        head.next=fast
        fast=head
        head=next_node
    while(slow and fast):
        if slow.data==fast.data:
            slow=slow.next
            fast=fast.next
        else:
            return False
    return True

def Pallindrome2(head):
    if head is None:
        return
    temp=head
    Pallindrome2(temp.next)
    if head.data!=temp.data:
        return False
    return True





