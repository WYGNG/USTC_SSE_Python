def main():
    s = input("Enter a string: ").strip()
    print("Maximum consecutive substring is " + maxSubstring(s))

# The worst-case complexity is O(n^2)
def maxSubstring(s):
    # maxLength[i] stores the length of the max substring ending at index i
    maxLength = len(s) * [0]
    # previous[i] stores the index of the previous element in the sequenece
    previous = len(s) * [0]

    for i in range(len(s)):
      previous[i] = -1
      for j in range(i - 1, -1, -1):
        if s[i] > s[j] and maxLength[i] < maxLength[j] + 1:
          maxLength[i] = maxLength[j] + 1
          previous[i] = j

    # Find the largest subsequence length and ending index 
    maxL = maxLength[0]
    index = 0
    for i in range(1, len(s)):
        if maxL < maxLength[i]:
            maxL = maxLength[i]
            index = i


    # Construct the subsequence by tracing through previous 
    chars = (maxL + 1) * [0]
    i = maxL
    while index != -1:
         chars[i] = s[index]
         i -= 1
         index = previous[index]

    return str(chars)

main()