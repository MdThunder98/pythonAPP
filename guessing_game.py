secret_word = "mahmoud"
guess = ""
guess_count = 0
guess_limit = 3


while secret_word != guess and guess_count != guess_limit:
    guess = input("enter guess: ")
    guess_count += 1

if secret_word == guess:
    print("You win")
else:
    print("you lose")