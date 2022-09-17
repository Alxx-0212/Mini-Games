import random
import sys
import os

s = [list("- | - | -"),
     list("- | - | -"),
     list("- | - | -")]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = len(s[0])


def move_printval(n):

    total = 1
    y = [0, 4, 8, 0, 4, 8, 0, 4, 8]
    x = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    x_1, y_1 = 0, 0
    for i, j in zip(x, y):
        if n == total:
            x_1, y_1 = i, j
        total += 1

    for i in range(3):

        for j in range(9):

            if s[i][j] == "-" and (i == x_1 and j == y_1):
                s[i][j] = "O"

    return s


def move_printval_user(n):
    total = 1
    y = [0, 4, 8, 0, 4, 8, 0, 4, 8]
    x = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    x_1, y_1 = 0, 0
    for i, j in zip(x, y):
        if n == total:
            x_1, y_1 = i, j
        total += 1

    for i in range(3):

        for j in range(9):

            if s[i][j] == "-" and (i == x_1 and j == y_1):
                s[i][j] = "X"

    return s


def check_radial(s):
    if (s[0][0] == s[0][4] == s[0][8] == "X") or (s[0][0] == s[1][4] == s[2][8] == "X") or (s[1][0] == s[1][4] == s[1][8] == "X") or (s[2][0] == s[2][4] == s[2][8] == "X") or (s[0][0] == s[1][0] == s[2][0] == "X") or (s[0][4] == s[1][4] == s[2][4] == "X") or (s[0][8] == s[1][8] == s[2][8] == "X") or (s[2][0] == s[1][4] == s[0][8] == "X"):
        return "YOU WIN"
    elif (s[0][0] == s[0][4] == s[0][8] == "O") or (s[0][0] == s[1][4] == s[2][8] == "O") or (s[1][0] == s[1][4] == s[1][8] == "O") or (s[2][0] == s[2][4] == s[2][8] == "O") or (s[0][0] == s[1][0] == s[2][0] == "O") or (s[0][4] == s[1][4] == s[2][4] == "O") or (s[0][8] == s[1][8] == s[2][8] == "O") or (s[2][0] == s[1][4] == s[0][8] == "O"):
        return "YOU LOSE"


def user_in():
    a = int(input("Enter a number: "))
    return a


print("\n")

a = ["1 | 2 | 3",
     "4 | 5 | 6",
     "7 | 8 | 9"]
print("\n".join(a))


def control(n):

    if n % 2 == 0:
        print("Your turn !")

        for i in range(5):
            print("\n")
            if check_radial(s) == "YOU WIN":
                for i in s:
                    print("".join(i))
                print("YOU WIN")
                break
            elif check_radial(s) == "YOU LOSE":

                print("YOU LOSE")
                break

            print("\n")
            print(nums)

            z = user_in()
            nums.remove(z)
            move_printval_user(z)

            if check_radial(s) == "YOU WIN":
                for i in s:
                    print("".join(i))
                print("YOU WIN")
                break
            elif check_radial(s) == "YOU LOSE":
                print("YOU LOSE")
                break

            num = random.choice(nums)
            nums.remove(num)
            move_printval(num)
            for i in s:
                print("".join(i))
    elif n % 2 != 0:
        for i in range(5):
            print("\n")
            if check_radial(s) == "YOU WIN":
                for i in s:
                    print("".join(i))
                print("YOU WIN")
                break
            elif check_radial(s) == "YOU LOSE":

                print("YOU LOSE")
                break

            print("\n")
            num = random.choice(nums)
            nums.remove(num)
            move_printval(num)
            print(nums)
            for i in s:
                print("".join(i))
            if check_radial(s) == "YOU WIN":
                for i in s:
                    print("".join(i))
                print("YOU WIN")
                break
            elif check_radial(s) == "YOU LOSE":

                print("YOU LOSE")
                break

            z = user_in()
            nums.remove(z)
            move_printval_user(z)

            for i in s:
                print("".join(i))


control(random.choice([1, 2]))
