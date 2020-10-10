def main():
    print("{0:15s}{1:20s}".format("i", "m(i)"))
    for i in range(1, 1000, 100):
        print("{0:<15d}{1:<20.4f}".format(i, m(i)))

def m(i):
    pi = 0
    sign = 1
    for i in range(1, i + 1, 1):
        pi += sign / (2 * i - 1) 
        sign = -1 * sign

    return 4 * pi

main()