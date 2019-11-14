def main():  
    N = 10
    s = input("Enter ten integers: ") 
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    
    for i in range(N): 
      for j in range(i + 1, N):
        print(numbers[i], numbers[j])

main()
