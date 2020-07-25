# truss-structures-numpy

project.py provides the constructors and methods, while client.py provides example code for the 4 joint and 4 beam problem.

## This repo calculates forces in a truss structure by using linear algebra features of the numpy package. The code creates a few simple classes:

> `Node n1 = new Node("n1",0,0)` creates a new node at position (0,0) named "n1".

> `Node n2 = new Node("n2",1,1)` creates a new node at position (1,1) named "n2".

> `Brace b1 = new Brace("b1",n1,n2)` creates a brace that connects node 1 and node 2 named "n3".

> `Truss t = new Truss([n1,n2])` creates a truss structure including n1, n2, and b1.

## The truss class also has a non-static calculate() method.

The calculate method takes an optional `upward_force` parameter. When you do not include the parameter, the program returns a basis for the vector subspace that includes all of the possible forces that the structure may have. When you do include the numeric `upward_force` parameter, the program assumes, for all joints not located on the y-axis, that the upward force is the `upward_force` numeric parameter and the horizontal forces are zero. It then provides a python dictionary that includes the name of the beam or joint, a direction of the force (if applicable), and the calculated force. 

If you include the upward force parameter, make sure that the truss structure has exactly one solution. Python will throw unhelpful error messages at you if you provide a structure with multiple or no solutions.

## Disclaimers

* Since this repo is a quick production, no helpful error checking is provided. If you get a "non-square matrix" numpy error, some of the node or brace connections may be missing or incorrect.

* Also, this code may not be very efficent for solving large structures. It uses a lot of different numpy linear algebra functions, and the mathematical functions are not collapsed for maximum efficency.


