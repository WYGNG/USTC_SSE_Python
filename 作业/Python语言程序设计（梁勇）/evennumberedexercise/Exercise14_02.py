def main():
    s = input("Enter the numbers: ").strip()
    numbers = [eval(x) for x in s.split()]

    dictionary = {} # Create an empty dictionary
    
    for number in numbers:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    
    maxCount = max(dictionary.values())

    pairs = list(dictionary.items())
    
    items = [[x, y] for (x, y) in pairs] # Reverse pairs in the list

    print("The numbers with the most occurrence are ", end = "")
    for (x, y) in items:
        if y == maxCount:
            print(x, end = " ")

main()
