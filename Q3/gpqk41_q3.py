#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################


def good_expression(input_string):

    stack = Stack()

    for character_index in range(0, len(input_string)):

        if input_string[character_index] in ["(", "+", "*"]:
            stack.push(input_string[character_index])

        elif input_string[character_index] is ")":

            flags = [0, 0, 0, 0]

            current_item = ""
            while current_item is not "(":

                current_item = stack.pop()
                if current_item == "+":
                    flags[2] = 1

            if character_index != len(input_string)-1:

                if input_string[character_index + 1] == "*":
                    flags[3] = 1
                elif input_string[character_index + 1] == ")":
                    flags[1] = 1

            if not stack.isEmpty():

                if stack.top() == "(":
                    flags[0] = 1

                if stack.top() == "*":
                    flags[3] = 1

            if flags[0] == 1 and flags[1] == 1:
                return False

            if flags[2] == 0 or flags[3] == 0:
                return False

    return True


class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    
    def push(self, data):
        self.head = Node(data, self.head)

    def top(self):
        return self.head.data


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