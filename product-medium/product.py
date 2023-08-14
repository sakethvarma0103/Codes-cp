class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def last(self,head,k):
        z=head
        while(z.nextval):
            z=z.nextval
        z.nextval=head
        x=y=Node()
        a=head.nextval
        m=head.nextval
        f=1
        for i in range(k):
            f*=m.dataval
            m=m.nextval
        y.dataval=f
        while(a!=head):
            m=a.nextval
            f=1
            for i in range(k):
                f*=m.dataval
                m=m.nextval
            y.nextval=Node(f)
            y=y.nextval
            a=a.nextval
        return x
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval, end=" ")
            printval = printval.nextval
        print()
    def nodeprint(self,head):
        while(head):
            print(head.dataval,end=" ")
            head=head.nextval
list1 = SLinkedList()
l=[4, 1, 3, 1, 4, 4, 3, 4, 1, 3, 5, 5, 2, 4, 1, 2, 3, 1, 1, 4, 4, 5, 4, 2, 4, 1, 2, 3, 3, 2, 2, 1, 5, 1, 3, 5, 5, 4, 4, 1, 3, 1, 3, 4, 5, 2, 2, 5, 2, 5, 5, 2, 5, 3, 1, 2, 3, 4, 5, 1, 5, 4, 2, 3, 1, 5, 2, 4, 2, 3, 1, 1, 5, 3, 2, 4, 2, 2, 3, 5, 3, 2, 4, 1, 1, 4, 3, 5, 4, 3, 4, 5, 2, 4, 5, 3, 2, 5]
k=5
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
list2=list1.last(list1.headval,k)
list1.nodeprint(list2)