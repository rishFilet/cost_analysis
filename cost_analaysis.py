import math as m

def calc(cost, costPU):
    return m.ceil(cost/costPU)

print ("What is the cost of the item?")
cost = float(input())
print ("What is the normal cost per use of the item?")
costPU = float(input())
print ("You will break even in {} uses".format(calc(cost,costPU)))
