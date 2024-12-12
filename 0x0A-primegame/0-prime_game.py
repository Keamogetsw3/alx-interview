#!/usr/bin/python3
"""
Prime Game Problem
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after a specified number of rounds.

    Parameters:
        x (int): The number of rounds to be played.
        nums (list of int): A list of integers.

    Returns:
        str: The name of the player who wins more rounds ("Maria" or "Ben"),
             or None if there is a tie.
    """

    if x < 1 or not nums:
        return None

    maria_chances = 0
    ben_chances = 0

    n = max(nums)

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    for num in nums:
        prime_count = sum(primes[2:num + 1])
        if prime_count % 2 == 0:
            ben_chances += 1
        else:
            maria_chances += 1

    if maria_chances == ben_chances:
        return None  # Tie
    return "Maria" if maria_chances > ben_chances else "Ben"
