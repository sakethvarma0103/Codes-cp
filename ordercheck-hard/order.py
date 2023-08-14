class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def order(self,head,order):
        if len(order)==0:
            return True
        m=max(order)
        l=[0]*m
        k=head
        i=0
        while(head):
            l[order[i]-1]=head.dataval
            head=head.nextval
        for i in range(1,m-1):
            if l[i]>l[i-1] and l[i]<l[i+1]:
                continue
            else:
                return False
        return True

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval)
            head=head.nextval
list1 = SLinkedList()
l=[]
months=[]
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
x=list1.order(list1.headval,months)
print(x)