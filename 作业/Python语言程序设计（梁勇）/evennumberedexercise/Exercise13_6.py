import urllib.request

def main():
    infile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
    s = infile.read()

    print("The number of words in the file is " + str(len(s.split())))
main()
