def main():
    s = input("Enter a string: ").strip()
    ch = input("Enter a character: ")[0]
    times = count(s, ch)
    print(ch + " appears " + str(times) + (" times " if times > 1 else " time ") + "in " + s)

def count(s, a):
    result = 0
    if len(s) > 0:
      result = count(s[1:], a) + (1 if (s[0] == a) else 0)

    return result

main()
