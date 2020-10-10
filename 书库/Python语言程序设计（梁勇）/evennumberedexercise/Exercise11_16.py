def sort(points):
    # Swap x- and y-coordinates in each point
    temp = [[y, x] for [x, y] in points]
    temp.sort()
    
    return [[x, y] for [y, x] in temp]
    
points = [[4, 34], [1, 7.5], [4, 8.5], [1, -4.5], [1, 4.5], [4, 6.6]]
print(sort(points))
