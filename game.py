
#program for Rock Paper Scissor

print("Rock Paper Scissor Game")
Player1=int(input("Enter your choice(stone,paper,scissor): "))
Player2=int(input("Enter your choice(stone,paper,scissor): "))
print("1 for Stone")
print("2 for Paper")
print("3 for Scissor")
if(Player1==Player2):
      print("Both are same! Play Again!")
elif(Player1==1 and Player2==2):
    print("Player2 Wins")
elif(Player1==1 and Player2==3):
    print("Player1 Wins")
elif(Player1==2 and Player2==1):
    print("Player1 Wins")
elif(Player1==2 and Player2==3):
    print("Player2 Wins")
elif(Player1==3 and Player2==1):
    print("Player2 Wins")
elif(Player1==3 and Player2==2):
    print("Player1 Wins")
else:
    print("Invalid Choice")
    
       





