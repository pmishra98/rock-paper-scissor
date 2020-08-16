import random

computer = ["rock", "paper", "scissor"]
u = 0
c = 0  # n and m is for initializing counter
i = 1
while i <= 10:
    print("Lets start", i, "round",)
    user = input("enter user's choice")

    comp = random.choice(computer)

    if user == "rock":

        if comp == user:
            print("the game is tie b/w u and computer")
        elif comp == "paper":
            print("winner of this game is computer")
            c = c + 1
        elif comp == "scissor":
            print("user is winner")
            u = u + 1
        i = i + 1
    elif user == "paper":

        if comp == user:
            print("the game is tie b/w u and computer")
        elif comp == "rock":
            print("winner of this game is user")
            u = u + 1
        elif comp == "scissor":
            print("computer is winner")
            c = c + 1
        i = i + 1
    elif user == "scissor":

        if comp == user:
            print("the game is tie b/w u and computer")
        elif comp == "rock":
            print("winner of this game is computer")
            c = c + 1
        elif comp == "paper":
            print("user is winner")
            u = u + 1
        i = i + 1
    elif user not in computer:
        print("please enter valid input")
    print("user", u, "computer", c)
if u < c:
    print("overall winner of the game is computer")
elif u > c:
    print("overall winner of the game is user")
elif u == c:
    print("the game is tied b/w the user")

