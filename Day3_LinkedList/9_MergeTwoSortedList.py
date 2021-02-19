def MergeSortedList(head1,head2):
    dummy=Node(0)
    prev=dummy

    while(head1 and head2):
        if head1.data<=head2.data:
            prev.next=head1
            head1=head1.next
        if head1.data>head2.data:
            prev.next=head2
            head2=head2.next
        
    while(head1):
        prev.next=head1
        head1=head1.next
    while(head2):
        prev.next=head2
        head2=head2.next
    return dummy.next
