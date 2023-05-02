from random import randint

random_pick=randint(0,100)
level = input('Pick "Hard" or "Easy" level' ).lower()

def Guessing(random_pick, pick):
    if pick == random_pick:
        return "You guessed correctly"
    elif pick > random_pick:
        return "Too high"
    else:
        return "Too low"

if level=="hard":
    attempts=5
    for x in range(5):
        print(f"You have {attempts} attempts")
        pick = int(input("Pick number between 1 and 100 \n"))
        print(Guessing(random_pick, pick))
        if Guessing(random_pick, pick)=="You guessed correctly":
            break
        attempts-=1
elif level=="easy":
    attempts=10
    for x in range(10):
        print(f"You have {attempts} attempts")
        pick = int(input("Pick number between 1 and 100 \n"))
        print(Guessing(random_pick, pick))
        if Guessing(random_pick, pick)=="You guessed correctly":
            break
        attempts-=1

else:
    print("Wrong input")
