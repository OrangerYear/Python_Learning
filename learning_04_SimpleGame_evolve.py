import random
secret = random.randint(1,10)

print("--------simple game-------")
temp = input ("guess please\n") #打印并要求输入
guess=int(temp)
if guess==8:
    print("right")
else:
    if guess > 8 :
        print("too big")
    else:
        print("too small")
    print("wrong")
print("game over")
