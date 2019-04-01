"""Use a random number generator to devise inputs for your
algorithms for at least four different values of n.
The values of n may need to be different for the two approaches.

(a) n should be large enough so that you can reliably determine
the runtime of your algorithm by using an appropriate
timing function call such as clock() to time your program;
i.e., the minimum run time should be at least 10 times
more than the resolution of your clock function
(the smallest unit of time that it measures).

(b) Also choose n so that you can experimentally verify
the theoretical runtime you derived above.
For each n, determine the run time by taking the
average of three runs on the same input.
This reduces the likelihood of inaccuracies due to system load.
Display your results in a table. Explain your choice of n.
"""

import random
import itertools

minimum = 0
maximum = 200


def rand_input(n, filename):
    with open(filename, "w") as f:
        f.write("{n}\n".format(n=n))
        for _ in itertools.repeat(None, n):
            f.write("{coord0} {coord1}\n".format(coord0=random.randint(minimum, maximum), coord1=random.randint(minimum,maximum)))


# n's for nearest neighbor:
n = 156
rand_input(n, "rand156.txt")

n = 625
rand_input(n, "rand625.txt")

n = 2500
rand_input(n, "rand2500.txt")

n = 10000
rand_input(n, "rand10000.txt")

# n's for exhaustive approach:
n = 6
rand_input(n, "rand6.txt")

n = 8
rand_input(n, "rand8.txt")

n = 9
rand_input(n, "rand9.txt")

n = 10
rand_input(n, "rand10.txt")

n = 11
rand_input(n, "rand11.txt")
