from project import Truss, Brace, Node
n1 = Node("a",0,1)
n2 = Node("b",1,1)
n3 = Node("c",0,0)
n4 = Node("d",2,0)
b1 = Brace("beam 1",n1,n2)
b2 = Brace("beam 2",n3,n2)
b3 = Brace("beam 3",n3,n4)
b4 = Brace("beam 4",n2,n4)
t = Truss([n1,n2,n3,n4])
answer = t.calculate(upward_force = 1000)
for entry in answer:
    print(entry + " " + str(answer[entry]))
