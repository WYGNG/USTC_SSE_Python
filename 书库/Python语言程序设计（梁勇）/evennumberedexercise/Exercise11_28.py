def main():
    SIZE = 3
    m1 = input("Enter list1: ").split()
    m2 = input("Enter list2: ").split()
    
    if equals(m1, m2):
        print("Two lists are strictly identical")
    else:
        print("Two lists are not strictly identical")

def equals(m1, m2):
    for i in range(len(m1)):
        if m1[i] != m2[i]: return False
    
    return True

main()
