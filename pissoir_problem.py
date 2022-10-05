import time
import sys
from typing import List

from matplotlib import pyplot as plt


def pissoir_problem(n: int) -> int:
    """
    Calculates the pissoir problem with courtesy distance for a given amount of empty pissoirs n

    :param n: the amount of urinals
    :return: the number of possibilities for the pissoir problem with a given n
    """

    def helper(urinals: List[bool], n: int) -> int:
        """
        recursive helper function

        :param urinals: a list of all urinals, guaranteed to have at least one spot taken
        :param n: number of free urinals left
        :return: the amount of possibilities for a given urinal state
        """
        # check if we need further iterations
        # no urinal left, no choice
        if not n:
            return 0

        # if only 1 urinal is left then we only have 1 choice
        if n == 1:
            return 1

        # calculate distance of each spot to their closest taken spot
        urinal_count: int = len(urinals)  # shorthand since we'll need it a few times
        distances = [0] * urinal_count
        for spot, taken in enumerate(urinals):
            if taken:
                # distances[spot] = 0  # redundant since it's already set to 0
                continue

            x = 1
            while True:  # guaranteed to terminate since there is at least 1 truthy value
                # look towards both sides
                if ((0 <= spot - x < urinal_count) and urinals[spot - x]) \
                        or ((0 <= spot + x < urinal_count) and urinals[spot + x]):
                    distances[spot] = x
                    break  # breaks the 'while True' loop

                x += 1

        # grab only those spots with the maximum distance
        max_distance = max(distances)
        spots_to_choose = (spot for spot, distance in enumerate(distances) if distance == max_distance)
        possibilities = 0
        for spot in spots_to_choose:
            # Mutate the current pissoirs list rather than creating a new one to avoid too much memory consumption
            # and unnecessary copying
            urinals[spot] = True
            possibilities += helper(urinals, n - 1)
            urinals[spot] = False

        return possibilities

    def create_urinals(n: int, spot: int) -> List[bool]:
        """
        Creates a new set of urinals with only 'spot' taken

        :param n: amount of urinals to create
        :param spot: the spot that is initially taken
        :return: A list of
        """
        urinals = [False] * n
        urinals[spot] = True
        return urinals

    if n < 0:
        raise ValueError("amount of urinals can't be negative")

    if n in (0, 1):
        return n

    return sum(helper(create_urinals(n, spot), n - 1) for spot in range(n))


def plot_pissoir_problem(n: int, print_progress=False):
    ns = list(range(n + 1))
    ys: list
    if print_progress:
        def logger(n):
            print(f"Calculating {n=:2}...", end='')
            start_time = time.time()
            sol: int = pissoir_problem(n)
            process_time = time.time() - start_time
            print(f" Took {process_time:.5f}s")  # change the '5' in '.5f' to any precision you like
            return sol

        ys = [logger(n) for n in ns]
        print("\n--------------------------\n")
    else:
        ys = [pissoir_problem(n) for n in ns]

    for n, y in enumerate(ys):
        print(f"Solution for {n=:2}: {y:,}")

    plt.plot(ns, ys)
    plt.show()


if __name__ == "__main__":
    n: int
    log: bool
    try:
        _, n, *optional = sys.argv  # reading command line arguments
        n = int(n)
        log = bool(optional)
    except ValueError as e:
        while True:
            try:
                n = int(input("Please enter your n: "))
                break
            except ValueError:
                print("Failed to convert input to a number")

        log = input("Enter 'y' or '1' if you want to print the progress: ").lower() in ('y', '1', 'yes')

    plot_pissoir_problem(n, log)
