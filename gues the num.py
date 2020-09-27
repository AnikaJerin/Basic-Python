n=1
while(n<=9):
    i=int(input("enter a number \n"))
    if i>18:
        print("please enter a smaller number")
    elif i<18:
        print("enter a bigger number")
    elif i==18:
        print("congrats!")
        print("took",n,"guesses to finish")
        break

    print(9-n,"guesses left")
    n=n+1
    if n>9:
        print("you are out of guess")