class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def last(self,head,x):
        m=k=head
        c=12
        y=0
        while(m):
            if x>c:
                m.dataval=0
                m=m.nextval
                continue
            elif y==c-x:
                m.dataval=0
                m=m.nextval
                continue
            m=m.nextval
            y+=1
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval,end=" ")
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval,end=" ")
            head=head.nextval
list1 = SLinkedList()
l=[0,0,1,1,2,2,3,3,1,2,3,4]
months=14
if len(l)==0:
    list1.headval=Node()
else:
    list1.headval=Node(l[0])
    h=list1.headval
    for i in l[1:]:
        h.nextval=Node(i)
        h=h.nextval
list1.listprint()
print("-------------------------")
list1.last(list1.headval,months)
list1.listprint()