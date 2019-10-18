for i in range(1, 6 + 1):
    # Print leading space
    for j in range(6 - i, 0, -1):
        print("  ", end = "")
      
    for j in range(i, 0, -1):
        print(j, end = " ")

    print()
