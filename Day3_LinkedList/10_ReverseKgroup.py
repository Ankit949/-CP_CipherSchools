def ReverseIngroup(head,k):
     # step 1: exit of recursion: when less than k elements left, return head directly
        if not head or not head.next:
            return head
        currNode = head
        for _ in range(k - 1):
            currNode = currNode.next
            if not currNode:
                return head
            
        # step 2: revursivey find the new head of the reversed list
        nextGroupHead = self.reverseKGroup(currNode.next, k)
        
        # step 3: reverse the first k elements
        dummyNode = ListNode(0)
        dummyNode.next = head
        prev, curr = None, head
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # step 4: hook up the reversedNewHead with head
        head.next = nextGroupHead
        
        return prev