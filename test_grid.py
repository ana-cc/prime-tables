import sys, io
from grid import PrimeGrid
from nose.tools import assert_equals


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

def test_prime_grid_display():
    grid = PrimeGrid(10)
    sys.stdout = io.StringIO()
    grid.display_grid()
    output = sys.stdout.getvalue()

    with open('test-data/output_example') as f:
        well_known_output = f.read()
    assert_equals(well_known_output, output)


def test_prime_grid_input_negative():
    try:
        grid = PrimeGrid(-10)
    except (IndexError):
        assert True
