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
        limit = 0
        x = 0
        while (limit < total_primes):
            x += 1000
            limit = x / math.log(x) - 1
        return x

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
        displaygrid = self.grid
        displaygrid[0].insert(0, "")
        return '\n'.join([
            '|'.join(['{:^5}'.format(item) for item in row])
            for row in displaygrid
        ])
