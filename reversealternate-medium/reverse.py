class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval= None

class DLinkedList:
    def __init__(self):
        self.headval = None
    def removezeroes(self,head):
        m=head
        e1=e2=o2=head
        o1=e1.nextval
        c=0
        while(m.nextval):
            m=m.nextval
            c+=1
        c+=1
        if c%2!=0:
            e2=m
            o2=m.prevval
        else:
            e2=m.prevval
            o2=m
        while(True):
            if e1==e2:
                break
            e1.dataval,e2.dataval=e2.dataval,e1.dataval
            e1=e1.nextval.nextval
            if e1==e2:
                break
            else:
                e2=e2.prevval.prevval
        while(True):
            if o1==o2:
                break
            o1.dataval,o2.dataval=o2.dataval,o1.dataval
            o1=o1.nextval.nextval
            if o1==o2:
                break
            else:
                o2=o2.prevval.prevval
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
l=[1,2,3,4,5,6,7,8]
if len(l)==0:
    list1.headval=Node()
else:
    list1.headval=Node(l[0])
    h=list1.headval
    k=h
    for i in l[1:]:
        h.nextval=Node(i)
        h=h.nextval
        h.prevval=k
        k=h
print(list1)
list1.listprint()
print("-------------------------")
list1.removezeroes(list1.headval)
list1.listprint()
