class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def removezeroes(self,d,s):
        h=d[s[0]]
        m=0
        x=s.split()
        y=int(x[1])
        while(h):
            if h.dataval==0 and m==0:
                n=h
                m+=1
            elif h.dataval==0:
                m+=1
            else:
                m=0
            if m==y:
                for i in range(m):
                    n.dataval=1
                    n=n.nextval
                return True
            h=h.nextval
        return False
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def nodeprint(self,head):
        while(head):
            print(head.dataval,end=",")
            head=head.nextval
        print()
list1 = SLinkedList()
d={'A':[1,1,1,0,1,1,1,1,1,1],
   'B':[1,1,1,1,0,1,1,1,1,1],
   'C':[1,1,1,1,1,0,1,1,1,1],
   'D':[1,1,1,1,1,1,0,1,1,1]}
s=["B 1","C 1","D 1","A 1","A 1","B 1","C 1","D 1"]
for i in d:
    l=d[i]
    m=h=Node(l[0])
    for j in l[1:]:
        h.nextval=Node(j)
        h=h.nextval
    d[i]=m
d2=[]
for i in s:
    d2.append(list1.removezeroes(d,i))
for i in d2:
    print(i,end=" ")