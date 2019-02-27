from grid import PrimeGrid
import sys


def process(n):
    try:
        if (int(n) <= 0):
            sys.exit("Input must be a positive number greater than 0")
    except ValueError:
        sys.exit("Please input an integer.")


def main():
    n = input("Enter a grid size:")
    process(n)
    g = PrimeGrid(int(n))
    g.display_grid()


if __name__ == "__main__":
    main()
