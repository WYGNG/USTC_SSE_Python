import urllib.request

def main():
    url = input("Enter a URL: ").strip()
    wrod = input("Enter a word to search: ").strip()
    crawler(url, word) # Traverse the Web from the a starting url

def crawler(startingURL, word):
    listOfPendingURLs = []
    listOfTraversedURLs = []
    
    listOfPendingURLs.append(startingURL)
    while len(listOfPendingURLs) > 0 and \
            len(listOfTraversedURLs) <= 100:
        urlString = listOfPendingURLs[0]
        del listOfPendingURLs[0]
        if urlString not in listOfTraversedURLs:
            listOfTraversedURLs.append(urlString)
            print("Craw", urlString)
            if contains(urlString, word):
                print("The URL", urlString, "contains the word", word)
                print("The number of pages been searched is", len(listOfTraversedURLs))
                break
            
            for s in getSubURLs(urlString):
                if s not in listOfTraversedURLs:
                    listOfPendingURLs.append(s)

def getSubURLs(urlString):
    list = []
    
    try:
        infile = urllib.request.urlopen(urlString)
        text = infile.read().decode() 
        current = 0
        current = text.find("http:", current)
        while current > 0:
            endIndex = text.find("\"", current)
            if endIndex > 0: # Ensure that a correct URL is found
                list.append(text[current : endIndex]) 
                current = text.find("http:", endIndex)
            else:
                current = -1
    except Exception as ex:
        print("Error:", ex)
    
    return list

main()