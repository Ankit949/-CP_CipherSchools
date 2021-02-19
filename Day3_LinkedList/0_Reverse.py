#Given pointer to the head node of a linked list, the task is to reverse the linked list. We need to reverse the list by changing the links between nodes.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    #adding element in a linkedList at begining
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printt(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


    def ReverseList(self):
        temp=self.head
        if temp==None:
            return
        dummy=None
        while(temp):
            next_node=temp.next
            temp.next=dummy
            dummy=temp
            temp=next_node
        self.head=dummy

if __name__=='__main__':
    list1=LinkedList()
    list1.push(20)
    list1.push(4)
    list1.push(15)
    list1.push(85)
    list1.ReverseList()
    list1.printt()


