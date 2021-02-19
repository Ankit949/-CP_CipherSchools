def copyRandomList(self, head: 'Node') -> 'Node':
        copy = preroot = Node(-1, head, None)
		
        while head:
            orig_next = head.next
            head.next = copy.next = Node(head.val, None, head.random)
            head, copy = orig_next, copy.next
        
        copy = preroot.next
        while copy:
            copy.random = copy.random.next if copy.random else None
            copy = copy.next
            
        return preroot.next