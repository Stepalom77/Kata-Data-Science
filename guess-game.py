secret = 9
itr = 0
guess_limit = 3
while itr < guess_limit:
    guess = int(input("Guess: "))
    itr += 1
    if guess == secret:
        print("You win!")
        break
    elif itr == guess_limit :
        print("Your lose")
    
    
