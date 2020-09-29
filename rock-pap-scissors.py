import random
lst=['rock','paper','scissor']
chance=10
cp=0
hp=0
i=0
print("LeT's PlAy Rock, PapeR, SciSSoR")
print("r=rock,p=paper,s=scisor")
while i<chance:
    inp=input("enter r,p or s \n ")
    ci=random.choice(lst) #ci=computer input
    if inp == ci:
        print("It's a tie")
        print(f"your score is {hp} and computer scores {cp}")
    if inp=="r" and ci=="paper":
        cp=cp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you lose. computer wins 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    elif inp=="r" and ci=="scissor":
        hp=hp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you win. you get 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    elif inp=="p" and ci=="rock":
        hp=hp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you win. you get 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    elif inp=="p" and ci=="scissor":
        cp=cp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you lose. Copmuter wins 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    elif inp=="s" and ci=="rock":
        cp=cp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you lose. computer wins 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    elif inp=="s" and ci=="paper":
        hp=hp+1
        print(f"your guess is {inp} and computer's guess is {ci}")
        print("you win. you get 1 point")
        print(f"your score is {hp} and computer scores {cp}")
    else:
        print("wrong input")
        print(f"your score is {hp} and computer scores {cp}")
    i=i+1
    print(f"{chance-i} is left out of {chance}")
print("Game Over")
print(f"your score is {hp} and computer scores {cp}")
if hp>cp:
    print("you won")
elif hp<cp:
    print("you lost the game")
elif hp+cp:
    print("It's a tie")
