# import timeit
# def time_function(func):
#     print(timeit.timeit("BinarySearch.binary_search([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 67)", setup="from __main__ import BinarySearch"))
#     print(timeit.timeit("BinarySearch.linear_search([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 67)", setup="from __main__ import BinarySearch"))
#     ...

# Big-Θ (Big-Theta) notation:
# THETA FOR ALL CASES
# Big-O (Big-O) notation:
# FOR WORST CASE (UPPER BOUND)
# Big-Ω (Big-Omega) notation:
# takes min this much iterations
# Θ(1)
# Θ(log2 n)
# Θ(n)
# Θ(n log2 n)
# Θ(n^2)
# Θ(n^2 log2 n)
# Θ(n^3)
# Θ(2^n)
# Θ(n!)

class BinarySearch:
    def linear_search(lst:list, target):
        """
        Returns the index of the given value in the list, returns none if value was not found in the list
        
        O(n)
        
        From: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
        """
        for i, x in enumerate(lst):
            if x == target: return i

        return None
    
    def binary_search(lst:list, target) -> int:
        """
        Returns the index of the given value in the list, returns none if value was not found in the list
        
        O(lg n)
        
        From: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
        """
        min = 0
        max = len(lst) - 1
        guess = (min + max) // 2
        while lst[guess] != target:
            guess = (min + max) // 2
            if lst[guess] < target:
                min = guess + 1
            else:
                max = guess - 1 
        
        return guess
        
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]    
# print(BinarySearch.binary_search(primes, 67))

class Sorting:
    ...