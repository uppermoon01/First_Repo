from constants_store import *


def return_discount(trip, price, discount):
    if (trip % TWO == 0):
      discount += (trip/TWO) * (price/TWO)
    return discount



def return_cash(price,fastag):
    return price - fastag
    
    
def addDiscount(total, discount): 
    total -= discount
    return (total, discount)


def calculateTax(total):
    total += total
    return total
