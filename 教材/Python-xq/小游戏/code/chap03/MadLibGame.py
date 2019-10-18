# Mad Lib Game

print("MAD LIB GAME")
print("Enter answers to the following prompts\n")

guy = input("Name of a famous man: ")
girl = input("Name of a famous woman: ")
food = input("Your favorite food (plural): ")
ship = input("Name of a space ship: ")
job = input("Name of a profession (plural): ")
planet = input("Name of a planet: ")
drink = input("Your favorite drink: ")
number = input("A number from 1 to 10: ")

story = "\nA famous married couple, GUY and GIRL, went on\n" +\
        "vacation to the planet PLANET. It took NUMBER\n" +\
        "weeks to get there travelling by SHIP. They\n" +\
        "enjoyed a luxurious candlelight dinner over-\n" +\
        "looking a DRINK ocean while eating FOOD. But,\n" +\
        "since they were both JOB, they had to cut their\n" +\
        "vacation short."

story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)
story = story.replace("JOB", job)
story = story.replace("PLANET", planet)
story = story.replace("DRINK", drink)
story = story.replace("NUMBER", number)

print(story)


