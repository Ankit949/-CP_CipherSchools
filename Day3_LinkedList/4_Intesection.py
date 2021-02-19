def Intersection(head1,head2):
    current1=head1
    current2=head2
    count1=0
    count2=0
    while(current1):
        count1=count1+1
        current1=current1.next
    while(cufrent2):
        count2= count2+1
        current2=current2.next

    c=abs(count1-count2)
    count=0
    while(head1 or head2):
        count=count+1
        if count1 >count2 and count<=c:
            head1=head1.next
        if count2>count1 and count<=c:
            head2=head2.next

        if count > c:
            if head1.data==head2.data:
                return head1.data
            head1=head1.next
            head2=head2.next



    