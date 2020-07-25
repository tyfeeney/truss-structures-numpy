# truss-structures-numpy

This repo calculates forces in a truss structure by using linear algebra features of the numpy package. The code creates a few simple classes:
=======
> `Node n1 = new Node("n1",0,0)` creates a new node at position (0,0) named "n1"

> `Node n2 = new Node("n2",1,1)` creates a new node at position (1,1) named "n2"

> `Brace b1 = new Brace("b1",n1,n2)` creates a brace that connects node 1 and node 2 named "n3"

> `Truss t = new Truss([n1,n2])` creates a truss structure including n1, n2. and b1
