#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
meal_cost =int
tip_percent = float 
tax_percent = int
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = (meal_cost/100)*tip_percent
    tax_percent = (meal_cost/100)*tax_percent
    total_cost =round(meal_cost+tip_percent+tax_percent)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
