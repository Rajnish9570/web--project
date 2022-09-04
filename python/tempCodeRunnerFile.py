
import random
print('''
Enter the 1 or 2 or 3 only.
1 for Rock
2 for Paper
3 for  Scissor
''')
print()
print("first player")
uc1=input("Enter 1st player ")
value1=input("Enter the Your choice. ")
uc2="Computer"
list2=["Rock","Scissor","Paper"]
value2=random.choice(list2)
print()
print("Result")
print(uc2, "choose", value2)

if value1=="1" and value2=="Paper":
  print(uc1," choose Rock")
  print("winner is ",uc2)
elif value1=="1" and value2=="Scissor":
  print(uc1," choose Rock")
  print("winner is ",uc1)
elif value1=="1" and value2=="Rock":
  print(uc1," choose Rock")
  print("Game is Tie. ")
elif value2=="1" and value1=="Paper":
  print(uc1," choose Rock")
  print("winner is ",uc1)
elif value2=="1" and value1=="Scissor":
  print(uc1," choose Rock")
  print("winner is ",uc2)
elif value2=="1" and value1=="Rock":
  print(uc1," choose Rock")
  print("Game is Tie. ")
elif value1=="2" and value2=="Scissor":
  print(uc1," choose Paper")
  print("winner is ",uc2)
elif value1=="2" and value2=="Rock":
  print(uc1," choose Paper")
  print("winner is ",uc1)
elif value1=="2" and value2=="Paper":
  print(uc1," choose Paper")
  print("Game is Tie. ")
elif value2=="2" and value1=="Scissor":
  print(uc1," choose Paper")
  print("winner is ",uc1)
elif value2=="2" and value1=="Rock":
  print(uc1," choose Paper")
  print("winner is ",uc2)
elif value2=="2" and value1=="Paper":
  print(uc1," choose Paper")
  print("Game is Tie. ")

elif value1=="3" and value2=="Rock":
  print(uc1," choose Scissor")
  print("winner is ",uc2)
elif value1=="3" and value2=="Paper":
  print(uc1," choose Scissor")
  print("winner is ",uc1)
elif value1=="3" and value2=="Scissor":
  print(uc1," choose Scissor")
  print("Game is Tie. ")

elif value2=="3" and value1=="Rock":
  print(uc1," choose Scissor")
  print("winner is ",uc1)
elif value2=="3" and value1=="Paper":
  print(uc1," choose Scissor")
  print("winner is ",uc2)
elif value2=="3" and value1=="Scissor":
  print(uc1," choose Scissor")
  print("Game is Tie. ")
else:
  ("Invalid Choice. ")
