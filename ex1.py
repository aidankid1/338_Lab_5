'''We are going to use a stack to build a primitive parser for arithmetic
S-expressions. Such an expression consists of either:
• An atom x, consisting of an integer number
• An expression of the form (o e1 e2), where o is an operand and e1, e2 are S-
expressions
• Possible operands are +, -, *, /
• Examples:
• 1
• (+15)
• (*(+15)2)
• (-(*13)(/4(+12)))

Your code must:
1. Receive a string representing an expression as a command line parameter
[0.3 pts]
2. Implement a stack data structure as discussed in lab and class [0.4 pts]
3. Using the stack, compute the overall result of an expression [0.8 pts]
• For example: python ex1.py '(+ 1 5)'
6
python ex1.py '(* (+ 1 5) 2)'
12
python ex1.py '(- (* 1 3) (/ 6 (+ 1 2)))'
1
'''
import sys

class MyStack:
    def __init__(self):
        self.elements = []
        
    def push(self, element):
        self.elements.append(element)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from empty stack.")
        else:
            return self.elements.pop()
            
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.elements[-1]
        
    def is_empty(self):
        return len(self.elements) == 0

def evaluate_expression(expression):
    stack = MyStack()
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char == '(':
            continue
        elif char in ['+', '-', '*', '/']:
            stack.push(char)
        elif char == ')':
            element1 = stack.pop()
            element2 = stack.pop()
            op = stack.pop()
            if op == '+':
                stack.push(element2 + element1)
            elif op == '-':
                stack.push(element2 - element1)
            elif op == '*':
                stack.push(element2 * element1)
            elif op == '/':
                stack.push(element2 // element1)
    return stack.pop()    
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No expression given.")
        sys.exit(1)

    expression = sys.argv[1]
    try:
        result = evaluate_expression(expression)
        print(result)
    except ValueError as e:
        print("Error:", e)


    
