import math
import time

start = time.time()


def open_file(filename):
    with open(filename, "r"):
        lines = [p.split() for p in [line.rstrip('\n') for line in open(filename)]]
        return lines


def nearest_point(curr_point, route):
    closest_dist = float("inf")

    for next_point in route:
        dist = math.sqrt((int(curr_point[0]) - int(next_point[0]))**2 + (int(curr_point[1]) - int(next_point[1]))**2)

        if dist < closest_dist:
            closest_dist = dist
            closest_point = next_point

    return closest_point, closest_dist


def nearest_neighbor(tsp_file):
    """Nearest neighbor approach to the TSP problem"""
    input_data = open_file(tsp_file)
    num_of_points = int(input_data[0][0])
    start_point = input_data[1]
    visit = input_data[2:]

    tour = [start_point]
    tour_len = 0

    # Visit the unvisited points (but don't include the starting point)
    while (num_of_points - 1) >= 1:
        nearest, distance = nearest_point(tour[-1], visit)
        tour.append(nearest)
        visit.remove(nearest)
        tour_len += distance
        num_of_points -= 1

    # End at the starting point
    nearest, distance = nearest_point(tour[-1], [start_point])
    tour.append(nearest)
    tour_len += distance

    return tour, tour_len


nn_tour, nn_len = nearest_neighbor("input75.txt")
print("Nearest Neighbor Tour: " + str(nn_tour) + "\n" + "Nearest Neighbor Length: " + str(nn_len))
print("Time: " + str(time.time() - start) + " " + "seconds")
