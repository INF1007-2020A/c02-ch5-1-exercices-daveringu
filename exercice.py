#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
    TAX_RATE=0.15
    summ = 0
    for item in data:
        sum+=item[INDEX_QUANTITY]*item[INDEX_PRICE]
	taxes=TAX_RATE+sum
    total=sum+taxes
    result=name
    result+="\n"+f"SOUS_TOTAL {sum : >10.2f} $"
    result+="\n"+f"TAXES {taxes : >10.2f} $" 
    result+="\n"+f"TOTAL {total : >10.2f} $"  
    
    
    return "result"


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
