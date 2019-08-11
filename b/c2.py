
# def funcname(parameter_list):
#     pass

import sys
sys.setrecursionlimit(10000)


def add(x,y):
    result = x + y
    return result

def print_code(code):
    print(code)

a = add(1,2)
b = print_code('python')

print(a,b)