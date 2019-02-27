class SieveOfEratosthenes():
    # generates primes up to given limit
    def __init__(self, limit):
        self.limit = limit
        # intitializes all items in sieve to True, i.e marks them all as prime
        self.sieve = [True for i in range(limit)]
        # 0 and 1 are not primes
        self.sieve[0] = False
        self.sieve[1] = False
        self.sieve_primes()

    def sieve_primes(self):
        # for every True item in sieve, mark all its multiples in the sieve as False
        for item in range(self.limit):
            if self.sieve[item]:
                for multiple in range(item + item, self.limit, item):
                    self.sieve[multiple] = False

    def get_results(self):
        # returns a list of all primes
        return [x for x in range(self.limit) if self.sieve[x] is True]
