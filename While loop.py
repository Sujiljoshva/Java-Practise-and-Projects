import random

top_of_range = input("Type a number ? ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print("Enter a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time !!")

random_number = random.randint(0,top_of_range)
print(random_number)

while True:
    user_guess = input("Guess a number!!")
    
