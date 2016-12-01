import sys
import math

#Binary operation functions
def add(a, b):
        return a + b

def minus(a, b):
        return b - a

def multiply(a, b):
        return a * b

def divide(a, b):
        return b / a

def power(a, b):
        return b ** a

#Unary operation functions
def negate(a):
        return -a

def square(a):
        return a ** 2

def square_root(a):
        return math.sqrt(a)

def log(a):
        return math.log(a)

#dictionary of binary operators
binary_ops = {
        "+": add,
        "-": minus,
        "*": multiply,
        "/": divide,
        "**": power,
}

#dictionary of unary operators
unary_ops = {
        "n": negate,
        "s": square,
        "r": square_root,
        "l": log,
}

def process(stack, token):
        if token in binary_ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(binary_ops[token](a, b))
        elif token in unary_ops:
                a = stack.pop()
                stack.append(unary_ops[token](a))
        elif token == "p":
                print stack[-1]
        else:
                stack.append(float(token))


def main():
        line = sys.stdin.readline()
        stack = []
        while line:
                tokens = line.split()
                i = 0
                while i < len(tokens):
                        token = tokens[i]
                        process(stack, token)
                        i += 1
                line = sys.stdin.readline()

if __name__ == "__main__":
        main()
