class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def checkl(l1,l2,a):
        for i in range(a):
            if l1.dataval!=l2.dataval:
                return False
            l1=l1.nextval
            l2=l2.nextval
        return True
    def last(self,head,k):
        a=l=0
        m=z=head
        n=k
        x=False
        while(m.nextval):
            m=m.nextval
            n=n.nextval
            a+=1
        a+=1
        m.nextval=head
        n.nextval=k
        y=head
        for i in range(a):
            if y.dataval==k.dataval:
                x=SLinkedList.checkl(y,k,a)
            if x:
                head=y
                break
            y=y.nextval
        while(head!=z):
            head=head.nextval
            l+=1
        print(x)
        if x==False:
            return -1
        return l
list1 = SLinkedList()
list2= SLinkedList()
l=[1,2,3]
o=[1,2,1]
if len(l)==0:
    list1.headval=Node()
    list2.headval=Node()
else:
    list1.headval=Node(l[0])
    list2.headval=Node(o[0])
    h=list1.headval
    h2=list2.headval
    for i in l[1:]:
        h.nextval=Node(i)
        h=h.nextval
    for i in o[1:]:
        h2.nextval=Node(i)
        h2=h2.nextval
print("-------------------------")
x=list1.last(list1.headval,list2.headval)
print(x)