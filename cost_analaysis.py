import math as m
from datetime import date
import datetime

def calc(cost, costPU):
    return m.ceil(cost/costPU)

print ("What is the cost of the item?")
cost = float(input())
print ("What is the normal cost per use of the item?")
costPU = float(input())
totalUses = calc(cost,costPU)
print ("Does this item have a time limit?[y/n]")
answer = input()
if answer == 'y' or answer == 'Y':
    print ("What date will the item expire?")
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    now = date.today()
    days = (date1 - now).days
    print ("You will break even in {} uses".format(totalUses))
    print ("You will need to use {} per day for {} days".format(m.ceil(totalUses/days), days))
else:
    print ("You will break even in {} uses".format(totalUses))
