def main():
    stateCapital = [
      ["Alabama", "Montgomery"],
      ["Alaska", "Juneau"],
      ["Arizona", "Phoenix"],
      ["Arkansas", "Little Rock"],
      ["California", "Sacramento"],
      ["Colorado", "Denver"],
      ["Connecticut", "Hartford"],
      ["Delaware", "Dover"],
      ["Florida", "Tallahassee"],
      ["Georgia", "Atlanta"],
      ["Hawaii", "Honolulu"],
      ["Idaho", "Boise"],
      ["Illinois", "Springfield"],
      ["Indiana", "Indianapolis"],
      ["Iowa", "Des Moines"],
      ["Kansas", "Topeka"],
      ["Kentucky", "Frankfort"],
      ["Louisiana", "Baton Rouge"],
      ["Maine", "Augusta"],
      ["Maryland", "Annapolis"],
      ["Massachusettes", "Boston"],
      ["Michigan", "Lansing"],
      ["Minnesota", "Saint Paul"],
      ["Mississippi", "Jackson"],
      ["Missouri", "Jefferson City"],
      ["Montana", "Helena"],
      ["Nebraska", "Lincoln"],
      ["Nevada", "Carson City"],
      ["New Hampshire", "Concord"],
      ["New Jersey", "Trenton"],
      ["New York", "Albany"],
      ["New Mexico", "Santa Fe"],
      ["North Carolina", "Raleigh"],
      ["North Dakota", "Bismark"],
      ["Ohio", "Columbus"],
      ["Oklahoma", "Oklahoma City"],
      ["Oregon", "Salem"],
      ["Pennslyvania", "Harrisburg"],
      ["Rhode Island", "Providence"],
      ["South Carolina", "Columbia"],
      ["South Dakota", "Pierre"],
      ["Tennessee", "Nashville"],
      ["Texas", "Austin"],
      ["Utah", "Salt Lake City"],
      ["Vermont", "Montpelier"],
      ["Virginia", "Richmond"],
      ["Washington", "Olympia"],
      ["West Virginia", "Charleston"],
      ["Wisconsin", "Madison"],
      ["Wyoming", "Cheyenne"]
    ]
    
    correctCount = 0

    for i in range(len(stateCapital)):
        capital = input("What is the capital of " + stateCapital[i][0] + "? ").strip()
      
        if capital.lower() == stateCapital[i][1].lower():
            print("Your answer is correct");
            correctCount += 1
        else:
            print("The correct answer should be " + stateCapital[i][1])

    println("The correct count is " + correctCount)
    
main()
