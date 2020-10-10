def main():
    s1 = input("Enter a string s1: ").strip()
    s2 = input("Enter a string s2: ").strip()
    
    index = match(s1, s2);
    if index >= 0:
        print("matched at index " + str(index))
    else:
        print("unmatched")

'''
The worst-case complexity is O(n), where n is s.length()
'''
def match(s, pattern):
    for p in range(len(s)):
        k = 0
        for i in range(p, len(s)):
            if k == len(pattern):
                return i - len(pattern)
            else:
                if s[i] == pattern[k]:
                    k += 1
                else:
                    break
    
        if k == len(pattern):
              return len(s) - len(pattern)

    return -1

main()