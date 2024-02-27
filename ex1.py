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

def arithmetic(expression): 



'''push
top+=1
array[top]=element value

pop
temp = array[top]
top-=1
'''
if __name__=="__main__": 
    if len(sys.argv) != 2:
        print("No expression given.")
        sys.exit(1)
    
    expression = sys.argv[1]
    result = arithmetic(expression)
    print(result)