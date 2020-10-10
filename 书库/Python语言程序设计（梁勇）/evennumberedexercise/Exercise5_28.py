e = 1
item = 1

for i in range(1, 100000 + 1):
    item = item / i
    e += item

    if i == 10000 or i == 20000 or i == 30000 or i == 40000 or \
          i == 50000 or i == 60000 or i == 70000 or i == 80000 or \
          i == 90000 or i == 100000:
        print("The e is " + str(e) + " for i = " + str(i))