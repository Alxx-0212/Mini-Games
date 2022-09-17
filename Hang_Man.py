import random
import os
import math

list_pic = ["------------|\n |\n o\n/|\\\n/ \\", "------------|\n |\n  \n/|\\\n/ \\", "------------|\n |\n  \n |\\\n/ \\",
            "------------|\n |\n  \n | \n/ \\", "------------|\n |\n  \n | \n  \\", "------------|\n |\n  \n | \n   "]
a = len(list_pic)


def randomizer(name, str_len):
    x = math.floor(str_len/2)
    l = []
    for i in range(x):
        num = random.randint(0, str_len-1)
        while name[num] == " ":
            num = random.randint(0, str_len-1)
        l.append(num)
        name[num] = " "

    return name, l


game = "DIS IS HANG MAN".lower()  # Goal, change anytime u like
name = list(game)
n = len(name)

x, y = randomizer(name, n)

missing = [game[i] for i in y]
lose = ["\u2661"]*5

while True:
    print("Guess the name !!"+" "*30+"Lives {}".format(" ".join(lose)))
    print(list_pic[a-1])
    print("".join(x))
    for i in range(len(game)):
        if game[i] != " ":
            print("-", end="")
        else:
            print(" ", end="")
    print()
    s = str(input("Enter a letter : ")).lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if s in missing:
        idx = missing.index(s)
        x[y[idx]] = s
        y.pop(idx)
        missing.remove(s)
    else:
        lose.pop()
        a -= 1

    if len(lose) == 0 or len(missing) == 0:
        print("Game Over")
        if len(missing) == 0:
            print("WIN")
        else:
            print(list_pic[0])
            print("LOSE")
        print(game)
        for i in range(len(game)):
            if game[i] != " ":
                print("-", end="")
            else:
                print(" ", end="")

        break
