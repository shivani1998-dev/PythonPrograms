import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
getData=[rock,paper,scissors]

inputData=int(input("Please enter 0 for rock, 1 for paper, and 2 for scissors"))
print(inputData)

if inputData<3 or inputData>=0:
    print(getData[inputData])

print("Computer Generated")
computerGenerated=random.randint(0,2)
print(getData[computerGenerated])

if inputData>3 or inputData<0:
    print("Invalid Input")
elif inputData==0 and computerGenerated==2:
    print("You win")
elif inputData==2 and computerGenerated==0:
     print("You lose")
elif computerGenerated > inputData:
    print("You lose")
elif inputData > computerGenerated:
    print("You win")
elif computerGenerated == inputData:
    print("Its a Draw")

