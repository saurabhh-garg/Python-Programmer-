name = str(input('Enter Your Name:'))
Total_pushups = 0
for i in range (1,8):
   print("Day", i, ": How many push-ups did you today?")
   Push_up = int(input())
   Total_pushups = Total_pushups + Push_up

AVG_pushup = Total_pushups/7

print("============================\n\tFITNESS REPORT\n============================")

print("Name :", name)
print("Total Push-ups :", Total_pushups)

print("Average :", AVG_pushup)

print("============================")




#  pattern printing

count = 0
for i in range (1, 6):
    print("*"  *i)

count = 5
for i in range(5, 0, -1):
    count -= 1
    print("*" *i)