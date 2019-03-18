bingo = "anqi is beauty"
answer = input("guess please\n")

while True:
    if answer == bingo:
        print("right")
        break
    answer = input("try again please\n")

print("over")
