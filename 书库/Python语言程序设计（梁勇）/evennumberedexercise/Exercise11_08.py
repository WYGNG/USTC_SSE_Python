import math

def main():
    points = [[0, 0, 0], [9, 9, 9], [-1, 0, 3], [-1, -1, -1], [4, 1, 1], [4, 1, 2], [4, 1, 0],
      [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2],
      [5.5, 4, -0.5]]

    # p1 and p2 are the indices in the points list
    p1 = 0
    p2 = 1 
    list1 = [[p1, p2]]
    shortestDistances = distance(
      points[p1][0], points[p1][1], points[p1][2],
      points[p2][0], points[p2][1], points[p2][2]) # Initialize shortestDistances

    # Compute distance for every two points
    for i in range(len(points)):
      for j in range(i + 1, len(points)):
        currentDistance = distance(
          points[i][0], points[i][1], points[i][2],
          points[j][0], points[j][1], points[j][2])

        if shortestDistances > currentDistance:
            list1 = [[i, j]]
            shortestDistances = currentDistance # Update shortestDistances
        elif shortestDistances == currentDistance:
            list1.append([i, j])

    # Display result
    for pair in list1:
        print("The closest two points are " +
            "(" + str(points[pair[0]]) + ", " + str(points[pair[1]]) + ")")

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))

main()
