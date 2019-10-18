# File I/O Code
# Chapter 3

"""
file = open("data2.txt", "w")
file.write("Sample file writing\n")
file.write("This is line 2\n")
file.close()

text_lines = [
    "Chapter 3\n",
    "Sample text data file\n",
    "This is the third line of text\n",
    "The fourth line looks like this\n",
    "Edit the file with any text editor\n" ]

file = open("data.txt", "w")
file.writelines(text_lines)
file.close()

file = open("data.txt", "r")
all_data = file.readlines()
print(all_data)
file.close()

print("Lines: ", len(all_data))
for line in all_data:
    print(line.strip())
"""    
    
# binary file code
import struct

file = open("binary.dat", "wb")
for n in range(1000):
    data = struct.pack('i', n)
    file.write(data)
file.close()

file = open("binary.dat", "rb")
size = struct.calcsize("i")
bytes_read = file.read(size)
while bytes_read:
    value = struct.unpack("i", bytes_read)
    value = value[0]
    print(value, end=" ")
    bytes_read = file.read(size)
file.close()

