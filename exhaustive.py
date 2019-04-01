import math
import itertools
import time

start = time.time()


def open_file(filename):
    with open(filename, "r"):
        lines = [p.split() for p in [line.rstrip('\n') for line in open(filename)]]
        return lines


def exhaustive_tsp(tsp_file):
    """Exhaustive approach to the TSP problem"""
    input_data = open_file(tsp_file)
    points = input_data[1:]

    # Try all possible orderings of the points, starting at the start point
    distance = float("inf")
    for route in itertools.permutations(points):
        # End at starting point
        route += tuple([route[0]])

        # Calculate cost of route
        route_list = list(route)
        cost = 0
        while len(route_list) > 1:
            curr_point, *route_list = route_list
            cost += math.sqrt(
                (int(curr_point[0]) - int(route_list[0][0])) ** 2 + (int(curr_point[1]) - int(route_list[0][1])) ** 2)

        # Select the one which minimizes the total length
        if cost <= distance:
            distance = cost
            opt_route = route

    # Return guaranteed optimal tour
    return opt_route, distance


exh_tour, exh_len = exhaustive_tsp("input.txt")
print("Optimal Tour: " + str(exh_tour) + "\n " + "Optimal Length: " + str(exh_len))
print("Time: " + str(time.time() - start) + " " + "seconds")
