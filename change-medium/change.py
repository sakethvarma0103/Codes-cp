class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class DLinkedList:
    def __init__(self):
        self.headval = None
    def reverse(self,head):
        k=head
        x=head.dataval
        while(head):
            y=head
            while(y):
                y.dataval,x=x,y.dataval
                y=y.nextval
            head.dataval=x
            if head and head.nextval:
                head=head.nextval.nextval
            else:
                break
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval,end=" ")
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval)
            head=head.nextval
list1 = DLinkedList()
l=[10,20]
if len(l)==0:
    list1.headval=Node()
else:
    list1.headval=Node(l[0])
    h=list1.headval
    k=h
    for i in l[1:]:
        h.nextval=Node(i)
        h=h.nextval
        k=h
list1.listprint()
print("-------------------------")
list1.reverse(list1.headval)
list1.listprint()
