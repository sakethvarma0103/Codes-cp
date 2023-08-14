class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def last(self,head,l):
        if len(l)==0:
            return head
        m=head
        x=l.count(1)
        for i in range(x):
            if i==0:
                head.dataval=1
            else:
                head.nextval=Node(1)
                head=head.nextval
        if x==0:
            head.dataval=l[0]
        for i in range(1,len(l)):
            if l[i]==0:
                temp=Node(0)
                temp.nextval=m
                m=temp
            elif l[i]==2:
                head.nextval=Node(2)
                head=head.nextval
        return m
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval,end=" ")
            head=head.nextval
list1 = SLinkedList()
l=[2,2,2,2]
list1.headval=Node()
print("-------------------------")
x=list1.last(list1.headval,l)
list1.nodeprint(x)
