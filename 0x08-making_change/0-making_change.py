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

    # 0 ways in the following two cases
    if sum < 0 or n == 0:
        return 0

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return countRecur(coins, n, sum - coins[n - 1]) + \
              countRecur(coins, n - 1, sum)

def count(coins, sum):
    return countRecur(coins, len(coins), sum)

if __name__ == "__main__":
    coins = [1, 2, 3]
    sum = 5
    print(count(coins, sum))
