from grid import PrimeGrid
from nose.tools import assert_equals

def test_prime_grid_size():
    grid = PrimeGrid(2)
    assert_equals(grid.edge, 3)

def test_prime_grid_prime_generation():
    grid_sizes = [100, 1000, 10000]  
    for size in grid_sizes:
        grid = PrimeGrid(size)
        total_primes_generated = grid.sieve.get_results()
        assert(total_primes_generated > grid.grid_size)

def test_prime_grid_data():
    grid = PrimeGrid(2)
    well_known_grid = [ [2, 3, 5], [2,4,6,10], [3,6,9,15], [5,10,15,25] ]
    assert_equals(well_known_grid, grid.grid)
