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

    def build_grid(self):
        results = [1]
        results.extend(self.sieve.get_results())

        self.grid = [[None for x in range(self.edge)]
                     for y in range(self.edge)]
        # to build the grid, start the inner loop from diagonal to reduce computations
        for i in range(0, self.edge):
            for j in range(i, self.edge):
                self.grid[i][j] = self.grid[j][i] = (results[i] * results[j])
        self.grid[0].pop(0)

    def display_grid(self):
        # pretty printing for smaller grids, 5 digit padding and centered
        self.build_grid()
        display_grid = self.grid
        display_grid[0].insert(0, "")
        return '\n'.join([
            '|'.join(['{:^5}'.format(item) for item in row])
            for row in display_grid
        ])
