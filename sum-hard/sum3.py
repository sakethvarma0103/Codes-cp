class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.prevval= None

class DLinkedList:
    def __init__(self):
        self.headval = None
    def zeronode(self,head):
        l=m=k=head
        c=0
        while(l.nextval):
            a=l.nextval
            while(a):
                if a.dataval<l.dataval:
                    a.dataval,l.dataval=l.dataval,a.dataval
                a=a.nextval
            l=l.nextval
        s=[]
        while(m.nextval):
            m=m.nextval
        while(k):
            x=k.dataval
            i=k.nextval
            z=m
            while(i):
                if i.dataval>z.dataval or i==z:
                    break                
                if i.dataval+z.dataval+x>0:
                    z=z.prevval
                elif i.dataval+z.dataval+x<0:
                    i=i.nextval
                else:
                    if i.dataval==z.dataval:
                        d=0
                        w=i
                        while(w!=z):
                            d+=1
                            w=w.nextval
                        c+=d
                    else:
                        c+=1
                    i=i.nextval
            k=k.nextval
        return c
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval,end=" ")
            head=head.nextval
list1 = DLinkedList()
l=[1,0,-2,1,1,1,1,2]
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
print("-------------------------")
y=list1.zeronode(list1.headval)
print(y)
