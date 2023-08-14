class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def shift(self,head):
        k=Node()
        m=k
        # l=[0,0,1,0,2,0,0,3,0,0,0]
        while(head):
            x=head.dataval
            if x==None:
                return m.nextval
            if x>0:
                for i in range(x+1):
                    if head.nextval==None:
                        return m.nextval
                    head=head.nextval
                continue
            k.nextval=Node(head.dataval)
            k=k.nextval
            if x==0:
                head=head.nextval
        return m.nextval
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
l=[0,0,1,1,2,2,3,3]
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
list2=list1.shift(list1.headval)
list1.nodeprint(list2)