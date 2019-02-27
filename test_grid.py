from grid import PrimeGrid
from nose.tools import assert_equals


def test_prime_grid_edge():
    grid = PrimeGrid(3)
    assert_equals(grid.edge, 4)


def test_prime_grid_size():
    size = 10
    grid = PrimeGrid(size)
    grid.build_grid()
    assert_equals(len(grid.grid), size + 1)
    assert_equals(len(grid.grid[0]), size)
    for item in range(1, size):
        assert_equals(len(grid.grid[item]), size + 1)


def test_prime_grid_prime_generation():
    grid_sizes = [100, 1000, 10000, 100000]
    for size in grid_sizes:
        grid = PrimeGrid(size)
        total_primes_generated = len(grid.sieve.get_results())
        assert (total_primes_generated > grid.grid_size)


def test_find_sieve_input_non_integer():
    grid = PrimeGrid(10)
    try:
        grid.find_sieve_input('hello')
    except (TypeError):
        assert True


def test_find_sieve_input_negative():
    grid = PrimeGrid(10)
    try:
        grid.find_sieve_input(-1)
    except (TypeError):
        assert True


def test_prime_grid_data():
    grid = PrimeGrid(3)
    well_known_grid = [[2, 3, 5], [2, 4, 6, 10], [3, 6, 9, 15],
                       [5, 10, 15, 25]]
    grid.build_grid()
    assert_equals(well_known_grid, grid.grid)


def test_prime_grid_display():
    grid = PrimeGrid(10)
    output = grid.display_grid()
    with open('test-data/output_example') as f:
        well_known_output = f.read()
    assert_equals(well_known_output, output)


def test_prime_grid_input_negative():
    try:
        grid = PrimeGrid(-10)
    except (IndexError):
        assert True
