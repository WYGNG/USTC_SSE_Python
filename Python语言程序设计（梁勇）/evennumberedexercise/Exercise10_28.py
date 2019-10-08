def main():
    s = input("Enter a list: ") 
    items = s.split() # Extracts items from the string
    list = [ eval(x) for x in items ] # Convert items to numbers   
    
    partition(list)
    
    print("After the partition, the list is ", end = "")
    for e in list:
        print(e, end = " ")

def partition(list):
    pivot = list[0]  # Choose the first element as the pivot
    low = 1  # Index for forward search
    high = len(list) - 1  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and list[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and list[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            list[high], list[low] = list[low], list[high]

    while high > 1 and list[high] >= pivot:
        high -= 1

    # Swap pivot with list[high]
    if pivot > list[high]:
        list[0] = list[high]
        list[high] = pivot

main()
