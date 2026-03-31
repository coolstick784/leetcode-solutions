class Solution(object):
    def findPrimePairs(self, n):
        prime = [True] * (n + 1)  # List to store whether a number is prime or not
        ans = []  # List to store the pairs of prime numbers
        
        # Initializing all numbers as prime
        for i in range(2, n + 1):
            prime[i] = True
        
        prime[1] = False  # 1 is not a prime number
        prime[0] = False  # 0 is not a prime number
        
        # Finding prime numbers using the Sieve of Eratosthenes algorithm
        p = 2
        while p * p <= n:
            if prime[p]:
                # Marking multiples of p as non-prime
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        
        for i in range(2, n):
            j = n - i  # Finding the complement of i to make the sum n
            if prime[i] and prime[j] and i <= j:
                temp = [i, j]  # Creating a pair of prime numbers
                ans.append(temp)  # Adding the pair to the result list
        
        return ans  # Returning the list of prime pairs


