import random

secret_number = random.randint(0,100)
guessed = False
max_attempts = 6
attempts = 0 

print ('Welcome to the game: Guess the secret number!!!')

while not guessed:
    if not attempts < max_attempts:
        print ("Game Over!! You couldn't guess within the "+max_attempts+" attempts.")
        break
    entered_number = int(input("Enter a number from 1 to 99: "))

    if entered_number == secret_number:
        print ("Congrats! You guessed the secret number!!!")
        guessed = True
    elif entered_number < secret_number:
        print ("The number is higher than "+entered_number)
    else:
        print ("The number is lower than "+entered_number)

attempts += 1
