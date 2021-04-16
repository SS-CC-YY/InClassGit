import string

def calc_sum(a,b):
    print (a+b)

def calc_diff(a,b):
    print (a-b)

def calc_mul(a,b):
    print (a*b)

def calc_div(a,b):
    print (a/b)

operator = {'+':calc_sum,'-':calc_diff,'*':calc_mul,'/':calc_div}

def calc(a,o,b):
    operator.get(o)(a,b)

a = int (input("Please enter the first number: "))
b = int (input("Please enter the second number: "))
o = input("Please enter the operator: ")
calc(a,o,b)