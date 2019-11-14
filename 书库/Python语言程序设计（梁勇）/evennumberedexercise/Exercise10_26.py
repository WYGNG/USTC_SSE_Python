def main():
    s = input("Enter list1: ") 
    items = s.split() # Extracts items from the string
    list1 = [ eval(x) for x in items ] # Convert items to numbers

    s = input("Enter list2: ") 
    items = s.split() # Extracts items from the string
    list2 = [ eval(x) for x in items ] # Convert items to numbers
    
    list3 = merge(list1, list2);
    
    print("The merged list is ", end = "")
    for e in list3:
        print(e, end = " ")

def merge(list1, list2):  
    result = []

    current1 = 0 # Current index in list1
    current2 = 0 # Current index in list2

    while current1 < len(list1) and current2 < len(list2):
      if list1[current1] < list2[current2]:
          result.append(list1[current1])
          current1 += 1
      else:
          result.append(list2[current2])
          current2 += 1

    while current1 < len(list1):
        result.append(list1[current1])
        current1 += 1

    while current2 < len(list2):
        result.append(list2[current2])
        current2 += 1

    return result

main()
