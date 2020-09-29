import datetime
def gettime():
    return datetime.datetime.now()
print(" welcome to our Health Management System")


def take(k):
    if k==1:
        c = int(input("type 1 for exercises or 2 for foods "))
        if c == 1:

            d = input("type Here\n")
            with open("anika-ex.txt", "a") as f:

                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")
        if c == 2:

            d = input("type here\n")
            with open("anika-food.txt", "a") as f:

                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")


    if k==2:
        c = int(input("type 1 for exercises or 2 for foods"))
        if c == 1:

            d = input("type here\n")
            with open("jerin-ex.txt", "a") as f:

                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")
        if c == 2:
            d = input("type here\n")
            with open("jerin-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")




    if k==3:
       c=int(input("type 1 for exercises or 2 for foods"))
       if c==1:

            d = input("type here\n")
            with open("joy-ex.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")
       if c==2:

            d = input("type here\n")
            with open("joy-food.txt", "a") as f:
                f.write(str([str(gettime())]) + ": " + d + "\n")
                print("successfully written")

def retrieve(k):

    if k==1:

        c=int(input("type 1 for exercise and 2 for food"))
        if c==1:

            with open("anika-ex.txt") as f:
                a=f.read()
                print(a)
        elif c==2:
            with open("anika-food.txt") as f:
                a=f.read()
                print(a)

    if k == 2:
        c = int(input("type 1 for exercise and 2 for food"))
        if c == 1:
            with open("jerin-ex.txt") as f:
                a = f.read()
                print(a)
        elif c == 2:
            with open("jerin-food.txt") as f:
                a = f.read()
                print(a)
    if k==3:
        c = int(input("type 1 for exercise and 2 for food"))
        if c == 1:
            with open("joy-ex.txt") as f:
                a = f.read()
                print(a)
        elif c == 2:
            with open("joy-food.txt") as f:
                a = f.read()
                print(a)




a=int(input("type 1 to enter info or 2 to retrieve info"))
if a==1:
    b=int(input("type 1 for anika, type 2 for jerin, type 3 for joy"))
    take(b)
else:
    b=int(input("type 1 for anika, type 2 for jerin, type 3 for joy"))
    retrieve(b)







