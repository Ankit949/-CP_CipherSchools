def MergeSort(head1,head2):
    res=None
    if head1 is None:
        return head2
    else:
        return head1
    if head1.data<=head2.data:
        res=head1.data
        res.next=MergeSort(head1.next,head2)
    else:
        res=head2.data
        res.next=MergeSort(head1,head2.next)
    return res

def KList(arr,k-1):
    while(k!=0):
        i=0
        j=k
        while(i<j):
            arr[i]=MergeSort(arr[i],arr[j])
            i=i+1
            j=j-1
            #update K
            if i>=j:
                k=j
    return arr[0]
                
    

        
