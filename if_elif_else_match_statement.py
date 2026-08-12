print("=====================================\n\tAI CAREER ADVISOR\n=====================================")
Name = str(input("Enter Your Name:"))
Age = int(input("Enter Your Age:"))
Current_Percentage = float(input("Enter Your Percentage:"))
Fav_Subject = str(input("Enter Subject Name:"))

if(Current_Percentage >= 90):
    performance = "Excellent Performance"
elif(Current_Percentage >= 75 and Current_Percentage <= 89):
    performance = "Very Good"
elif(Current_Percentage >= 60 and Current_Percentage <= 74):
    performance = "Good"
elif(Current_Percentage >= 40 and Current_Percentage <= 59):
    performance = "Needs Improvement"
else:
    performance = "Work Hard"

Study_Hrs = int(input("Hours Studied Per Day:"))
if(Study_Hrs >= 8):
    study_habit = "Excellent Discipline"
elif(Study_Hrs >= 5 and Study_Hrs <= 7):
    study_habit = "Good Consistency"
elif(Study_Hrs >= 3 and Study_Hrs <= 4):
    study_habit = "Can Improve"
else:
    study_habit = "Not Enough Practice"

print("1 → Data Scientist\n2 → AI Engineer\n3 → Cyber Security")
Career = int(input("choose a career from above:"))

match Career:
    case 1:
        career = "You selected Data Scientist."
        print("You selected Data Scientist.")
        print("Recommended Skills:")
        print("\tPython")
        print("\tMachine Learning")
        print("\tstatics")
        print("\tSQL")
        print("\tGit")
    case 2:
        career = "You selected AI Engineer."
        print("You selected AI Engineer.")
        print("Recommended Skills:")
        print("\tPython")
        print("\tMachine Learning")
        print("\tDeep Learning")
        print("\tSQL")
        print("\tGit")
    case 3:
        career = "You selected cyber security."
        print("You selected cyber security.")
        print("Recommended Skills:")
        print("\tPython")
        print("\tLinux")
        print("\tServer")
        print("\tNetwork")
        print("\CMD")

print("1 → INDIA\n2 → USA\n3 → JAPAN")
Country = int(input("choose a country from above:"))

match Country:
    case 1:
        country = "INDIA"
        print("You selected INDIA.")
        print("\tTop salary: 45LPA")
        print("\tTop Company: FAANG")
        print("\tDemand: HIGH")
    case 2:
        country = "USA"
        print("You selected USA.")
        print("\tTop salary: 45LPA")
        print("\tTop Company: FAANG")
        print("\tDemand: HIGH")
    case 3:
        country = "JAPAN"
        print("You selected JAPAN.")
        print("\tTop salary: 45LPA")
        print("\tTop Company: FAANG")
        print("\tDemand: HIGH")

print("============================\n  Career Analysis Report")

print("Name:", Name)
print("Age:", Age)
print("Percentage:", Current_Percentage)
print("Performance:", performance)
print("Study Habit:", study_habit)
print("Career Selected:", Career)
print("Preferred Country:", country)

print("============================")