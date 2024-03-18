import random
lives = 3

while True:
    print("You have", lives, "lives left")
    dice_roll = random.randint(1, 6)
    if lives == 0:
        print("You lost all your lives, game over")
        break
        #stop the loop even if the condition of the while is still true
    if dice_roll == 6:
        print("You rolled a 6, you win!")
        break
    print("You rolled a", dice_roll, "try again")
    lives -= 1
#continue = it stops the code there and goes back to the beginning of the loop

num = 0
count = 0
while num <= 19:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3", count)