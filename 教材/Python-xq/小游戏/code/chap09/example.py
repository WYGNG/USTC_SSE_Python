# example code for list

ages = [16, 91, 29, 38, 14, 22]
print(ages)
print(ages[1])

ages.append(100)
print(ages)

ages.append(20)
ages.append(20)
ages.append(20)
print(ages)
print(ages.count(20))

print(ages.index(20))

ages.insert(1, 50)
print(ages)
ages.insert(1, 60)
print(ages)

ages.remove(20)
print(ages)

ages.reverse()
print(ages)
ages.reverse()

ages.sort()
print(ages)
ages.reverse()
print(ages)

# example code for a stack
stack = []
for i in range(10):
    stack.append(i)
print(stack)
stack.append(10)
print(stack)
n = stack.pop()
m = stack.pop()
print(stack)

# example code for a queue
queue = []
for l in range(10):
    queue.append(l)
print(queue)
queue.append(50)
queue.append(60)
queue.append(70)
print(queue)
n = queue[0]
queue.remove(n)
print(queue)

# example code for a grid
grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
print(grid)
print(grid[0])
print(len(grid[0]))

for n in grid[0]: print(n)

grid[0][0] = 100
grid[0][1] = 200
grid[0][2] = 300
print(grid[0])

grid = [
    [10 for col in range(10)]
        for row in range(10)]

for row in grid: print(row)

# representing a 2D list with 1D    
level = [
    1,1,1,1,1,1,1,1,1,1,1,1, 
    2,2,2,2,2,2,2,2,2,2,2,2, 
    3,3,3,3,3,3,3,3,3,3,3,3, 
    1,1,1,1,1,1,1,1,1,1,1,1, 
    1,1,1,1,1,0,0,1,1,1,1,1, 
    1,1,1,1,1,0,0,1,1,1,1,1, 
    1,1,1,1,1,1,1,1,1,1,1,1, 
    3,3,3,3,3,3,3,3,3,3,3,3, 
    2,2,2,2,2,2,2,2,2,2,2,2, 
    1,1,1,1,1,1,1,1,1,1,1,1]

print(grid)

for row in range(10):
    s = ""
    for col in range(12):
        s += str(level[row*10+col]) + " "
    print(s)

# a 2D list
level = [
    [1,1,1,1,1,1,1,1,1,1,1,1], 
    [2,2,2,2,2,2,2,2,2,2,2,2], 
    [3,3,3,3,3,3,3,3,3,3,3,3], 
    [1,1,1,1,1,1,1,1,1,1,1,1], 
    [1,1,1,1,1,0,0,1,1,1,1,1], 
    [1,1,1,1,1,0,0,1,1,1,1,1], 
    [1,1,1,1,1,1,1,1,1,1,1,1], 
    [3,3,3,3,3,3,3,3,3,3,3,3], 
    [2,2,2,2,2,2,2,2,2,2,2,2], 
    [1,1,1,1,1,1,1,1,1,1,1,1]]

for row in level: print(row)


# working with tuples
tuple1 = (1,2,3,4,5)
print(tuple1)
a,b,c,d,e = tuple1
print(a,b,c,d,e)

data = (100 for n in range(10))
for n in data: print(n)


level = (
    (1,1,1,1,1,1,1,1,1,1,1,1), 
    (2,2,2,2,2,2,2,2,2,2,2,2), 
    (3,3,3,3,3,3,3,3,3,3,3,3), 
    (1,1,1,1,1,1,1,1,1,1,1,1), 
    (1,1,1,1,1,0,0,1,1,1,1,1), 
    (1,1,1,1,1,0,0,1,1,1,1,1), 
    (1,1,1,1,1,1,1,1,1,1,1,1), 
    (3,3,3,3,3,3,3,3,3,3,3,3), 
    (2,2,2,2,2,2,2,2,2,2,2,2), 
    (1,1,1,1,1,1,1,1,1,1,1,1))

for row in level: print(row)

names = ("john","jane","dave","robert","andrea","susan")
print(names)
print(names.index("dave"))
print("jane" in names)
print("bob" in names)
print(names.count("susan"))
print(len(names))


