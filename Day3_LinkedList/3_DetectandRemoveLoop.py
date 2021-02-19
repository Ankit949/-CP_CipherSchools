def DetectandRemoveLoop(head):
    slow=head
    fast=head
    flag=False
    while(slow and fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            flag=True
            break
    fast=head
    if flag==False:
        return False
    else:
        while(fast):
            if slow==fast:
                slow.next=None
                break
            slow=slow.next
            fast=fast.next

    