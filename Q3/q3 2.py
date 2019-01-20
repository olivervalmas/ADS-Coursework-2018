#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################

def good_expression(aString):
    expStack = Stack()
    expStack.__init__()
    redundant = False
    for i in range(0, len(aString)):
        if aString[i] == ')':
            #initialise flags
            cb = False
            ob = False
            mult = False
            add = False
            #if current char being examined is not the last char of expressions
            if i != len(aString)-1:
                #if char after is a closed bracket too, set flag to true
                if aString[i+1] == ')':
                    cb = True
                elif aString[i+1] == '*':
                #if char after is a multiplication sign, set flag to true
                    mult = True
            stackItem = '-'
            #keep popping items until beginning of bracketed expression is reached
            while stackItem != '('
                stackItem = expStack.pop(expStack)
                if stackItem = '+':
                    add = True
            #the whole bracket expression has been popped off
            if expStack.isEmpty(expStack) == False:
                #peek at the item before the bracket
                if expStack.top(expStack) == '*':
                    mult = True
                elif expStack.top(expStack) == '(':
                    ob = True
            expStack.push(expStack, 'a') #push arbitrary char to replace bracket result
            if (cb == True) and (ob == True):
                redundant = True
            if (add = False) or (mult = False):
                redundant = True
        else: #if ')' has not been reached, just push onto stack
            expStack.push(expStack, chara)
        if redundant == True:
            break
    if redundant == True:
        return False #False means not a good expression
    else:
        return True #True means good expression

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after
    
#####################################################
            

def testq3():
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)") 
    print ("all tests passed")
    
#####################################################

