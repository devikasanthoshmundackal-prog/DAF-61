import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    attempts -= 1

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)

#2 Multiplication table
number = int(input("Enter the number for which you want the multiplication table: 5"))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    # BMI calculator
    def calculate_bmi(weight, height):
    return weight / (height ** 2)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")