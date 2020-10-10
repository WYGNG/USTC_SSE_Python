import RandomCharacter

N = 100

count = 1
for i in range(N):
    if count % 10 == 0:
        print(RandomCharacter.getRandomUpperCaseLetter())
    else:
        print(RandomCharacter.getRandomUpperCaseLetter(), end = " ")
    count += 1
    
for i in range(N):
    if count % 10 == 0:
        print(RandomCharacter.getRandomDigitCharacter())
    else:
        print(RandomCharacter.getRandomDigitCharacter(), end = " ")
    count += 1
