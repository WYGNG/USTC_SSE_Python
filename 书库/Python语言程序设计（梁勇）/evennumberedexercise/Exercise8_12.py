def main():
    genome = input("Enter a genome string: ")
    
    found = False
    start = -1
    for i in range(len(genome) - 2):
        triplet = genome[i : i + 3]
        if triplet == "ATG":
            start = i + 3
        elif (triplet == "TAG" or triplet == "TAA" or triplet == "TGA") and start != -1:
            # A possible gene is found
            gene = genome[start : i]
            if len(gene) % 3 == 0:
                # A gene is found and display the gene
                found = True
                print(gene)  
                start = -1 # Start to find the next gene in the genome
    
    if not found:
        print("no gene is found")

main()