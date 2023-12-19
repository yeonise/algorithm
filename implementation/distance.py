def euclidean_distance(point1, point2):  # point = [x, y, z]
    distance = 0

    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2

    return distance ** 0.5


def manhattan_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += abs(point1[i] - point2[i])

    return distance


def hamming_distance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        if point1[i] != point2[i]:
            distance += 1

    return distance
