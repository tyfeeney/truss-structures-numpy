import numpy as np
import scipy.linalg as linalg
import math

class Truss():
    def __init__(self, nodeList):
        self.nodeList = nodeList
        self.braceList = []
        for node in self.nodeList:
            for brace in node.braceList:
                if brace not in self.braceList:
                    self.braceList.append(brace)

    def calculate(self, upward_force = None):
        coeffArray = []
        for node in self.nodeList:
            equ_x = []
            equ_y = []
            for brace in self.braceList:
                if brace in node.braceList:
                    if node == brace.node1: sign = -1
                    else: sign = 1
                    equ_x.append(sign * brace.x_comp())
                    equ_y.append(sign * brace.y_comp())
                else:
                    equ_x.append(0)
                    equ_y.append(0)
            coeffArray.append(equ_x)
            coeffArray.append(equ_y)
        matrixCoeff = np.array(coeffArray)
        solutionArray = np.concatenate((matrixCoeff,np.identity(np.size(matrixCoeff,0))),axis=1)
        nullspace = linalg.null_space(solutionArray)
        if upward_force is not None:
            return self.__linearcomb(nullspace, upward_force)
        else:
            return nullspace

    def __linearcomb(self, nullspace, upward_force):
        lhs = []
        rhs = []
        for i in range(len(self.nodeList)):
            if self.nodeList[i].x != 0:
                lhs.append(nullspace[2*i+len(self.braceList)])
                lhs.append(nullspace[2*i+len(self.braceList)+1])
                rhs.append(0)
                rhs.append(upward_force)
        c = linalg.solve(np.array(lhs),np.array(rhs))
        solution = []
        for i in range(len(nullspace)):
            solution.append(0)
        for i in range(len(c)):
            solution = solution + c[i] * nullspace[:,i]
        dict = {}
        counter = 0
        for i in range(len(self.braceList)):
            dict.update({self.braceList[i].name: solution[counter]})
            counter += 1
        for i in range(len(self.nodeList)):
            dict.update({self.nodeList[i].name + " x": solution[counter]})
            dict.update({self.nodeList[i].name + " y": solution[counter+1]})
            counter += 2
        return dict

class Brace():
    def __init__(self, name, node0, node1):
        self.node0 = node0
        self.node1 = node1
        self.name = name
        node0.addBrace(self)
        node1.addBrace(self)
    def length(self):
        return np.sqrt((self.node1.x - self.node0.x)**2 + (self.node1.y-self.node0.y)**2)
    def x_comp(self):
        return (self.node1.x - self.node0.x)/self.length()
    def y_comp(self):
        return (self.node1.y - self.node0.y)/self.length()

class Node():
    def __init__(self, name, x, y):
        self.braceList = []
        self.x = x
        self.y = y
        self.name = name
    def addBrace(self, brace):
        self.braceList.append(brace)
