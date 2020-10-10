def main():
    number = input("Enter the first 12 digits of an ISBN as a string: ").strip()

    # Calculate checksum
    sum = 0
    for i in range(12):
        sum += int(number[i]) * (1 if i % 2 == 0 else 3) 

    checksum = 10 - sum % 10
    if checksum == 10: checksum = 0
    
    print("The ISBN-13 number is " + number + str(checksum))
    
main()