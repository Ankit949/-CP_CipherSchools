def AddingNumber(head1,head2):
    carry=0
    res=0
    prev=None
    while(head1 and head2):
        sum1=(head1.data+head2.data+carry)
        res=sum1%10
        carry=sum1//10
        head1=head1.next
        head2=head2.next
        #Adding node 
        dummy=Node(res)
        if prev==None:
            temp=dummy
            prev=dummy
            prev.next=None
            continue
        dummy.next=None
        prev.next=dummy
        prev=dummy
    while(head1):
        sum1=head1.data+carry
        res=sum1%10
        carry=sum1//10
        dummy=Node(res)
        dummy.next=None
        prev.next=dummy
        prev=dummy
    while(head2):
        sum1=head2.data+carry
        res=sum1%10
        carry=sum1//10
        dummy=Node(res)
        dummy.next=None
        prev.next=dummy
        prev=dummy


    return temp
        