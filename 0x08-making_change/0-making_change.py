#!/usr/bin/python3
"""
Python program for coin change problem using recursion
"""

def makeChange(coins, total):
    """ 
    This function returns the fewest number of coins needed to make up the given total.
    If the total cannot be made up with the given coins, it returns -1.
    
    Arguments:
    coins: a list of integers representing the available coin denominations
    total: the total value we want to make with the fewest number of coins
    
    Returns:
    int: the fewest number of coins needed to form the total, or -1 if it's not possible
    """
    if total <= 0:
        return 0

   elif total > 0:
    newList = sorted(coins[:])
    newList = list(reversed(newList))
    count = 0
    value = total + 0
    index = 0
    
    while value >= 0 and (index < len(newList)):
        if value >= newList[index]:
            value = value - newList[index]
            count += 1
        elif value < newList[index]:
            index += 1
    
    if index == len(newList):
        if value != 0:
            return -1
        elif value == 0:
            return count
