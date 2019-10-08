import random

def main():
    list = 100 * [0]
    
    for i in range(len(list)):
        list[i] = random.randint(0, 999)
    
    radixSort(list, 3)
    print(list)
  
''' Sort the int array list. numberOfDigits is the number of digits
    in the largest number in the array 
'''
def radixSort(list, numberOfDigits):
    buckets = []
    for i in range(10):
        buckets.append([0]); 

    for position in range(numberOfDigits + 1):
      # Clear buckets
      for i in range(len(buckets)):
        buckets[i] = []    
      
      # Distribute the elements from list to buckets
      for i in range(len(list)):
        key = getKey(list[i], position)
        buckets[key].append(list[i])

      # Now move the elements from the buckets back to list
      k = 0 # k is an index for list
      for i in range(len(buckets)):
        for j in range(len(buckets[i])):
          list[k] = buckets[i][j]
          k += 1

'''
   Return the digit at the specified position. 
   The last digit's position is 0. 
'''
def getKey(number, position):
    result = 1;
    for i in range(position):
      result *= 10

    return (number // result) % 10

main()
