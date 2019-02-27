import math
from eratosthenes import SieveOfEratosthenes


class PrimeGrid():
    # Class that models a prime multiplication table grid
    def __init__(self, grid_size):
        # initializes the table grid
        self.grid_size = grid_size
        self.edge = grid_size + 1
        self.grid = None

        # initializes sieve for this grid after finding the input that is required
        sieve_input = self.find_sieve_input(self.grid_size)
        self.sieve = SieveOfEratosthenes(sieve_input)

    def find_sieve_input(self, total_primes):
        # finds the upper input needed for the sieve to generate a required total number of primes
        # we approximate number of primes generated for a given input using function x/log(x) - 1
        # we test the input in increments of 1000
        primes = 0
        sieve_input = 0
        while (primes < total_primes):
            sieve_input += 1000
            primes = sieve_input / math.log(sieve_input) - 1
        return sieve_input

    def display_grid(self):
        results = [1]
        results.extend(self.sieve.get_results())
        for i in range(0, self.edge):
            li = []
            for j in range(0, self.edge):
                li.append(results[i] * results[j])
            if i==0:
                li[0] = ""
            print('|'.join(['{:^5}'.format(item) for item in li]))
