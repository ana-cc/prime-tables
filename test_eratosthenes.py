from eratosthenes import SieveOfEratosthenes
from nose.tools import assert_equals


def test_sieve_of_eratosthenes():
    # compares results returned by the sieve to the known primes under 100
    sieve = SieveOfEratosthenes(100)
    known_primes_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97
    ]
    assert_equals(known_primes_100, sieve.get_results())


def test_sieve_of_eratosthenes_large():
    # tests the sieve with a limit of 2 million
    # compares number of results returned by the sieve to the known number of primes under 1M
    sieve = SieveOfEratosthenes(1000000)
    known_number = 78498
    assert_equals(known_number, len(sieve.get_results()))
