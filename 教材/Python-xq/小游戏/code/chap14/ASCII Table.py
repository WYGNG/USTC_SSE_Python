# ASCII Table Printer
# Chapter 14

cols = 8
rows = 256//cols
table = list("" for n in range(rows+1))
char = 0

#create strings filled with table data
for col in range(1,cols+1):
    for row in range(1,rows+1):
        table[row] += '{:3.0f}'.format(char) + ' '
        if char not in (9,10,13): 
            table[row] += chr(char)
        table[row] += '\t'
        char += 1

#print the ASCII table
for row in table:  print(row)



   
                                                        


