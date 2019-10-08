def main():
    for i in range(1, 10 + 1):
        print(m(i))

def m(i):
    if i == 1:
        return 1
    else:
        return m(i - 1) + 1.0 / i

main()
