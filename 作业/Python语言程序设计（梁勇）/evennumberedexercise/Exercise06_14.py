def main():
    print(format("i", "<15s"), format("m(i)", "<20s"))
    for i in range(1, 1000, 100):
        print(format(i, "<15d"), format(m(i), "<20.4f"))

def m(i):
    pi = 0
    sign = 1
    for i in range(1, i + 1, 1):
        pi += sign / (2 * i - 1) 
        sign = -1 * sign

    return 4 * pi

main()
