player = 1
for i in range(1,6):
    score = int(input("Enter the Score of player " + str(i)+ ": "))
    player += 1
    if score <= -999:
        print("Tournament Stopped!")
        break
    elif score <= -1:
        print("Invalid score, skipping player...")
        continue
    elif score == 0:
        print("No score")
        pass
    else:
        pass
    if score >= 90:
        print("player", i, ": Excellent")
    elif score >=70:
        print("player", i, ": Good")
    elif score >= 50:
        print("player", i, ": Average")
    elif score > 0:
        print("player", i, ": Needs Improvement")
    else:
        pass

