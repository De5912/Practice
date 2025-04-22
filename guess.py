import random
number_to_guess = random.randint(1,100)

attempts = 0  # Initialize the attempt counter
 max_attempts = 7  # Set the maximum number of attempts

 while attempts < max_attempts:
     try:
         guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
         attempts += 1

         if guess < number_to_guess:
             print("Too low.")
         elif guess > number_to_guess:
             print("Too high.")
         else:
             print(f"🎉 You guessed it in {attempts} attempts!")
             break
         if attempts == 3:
             if number_to_guess % 2 == 0:
                 print("Hint: The number is even!")
             else:
                 pritn("Hint: The number is odd!")



       except ValueError:
         print("Invalid input. Please enter a number.")

 if attempts == max_attempts and guess != number_to_guess:
     print(f"❌ You've used all {max_attempts} attempts. The number was {number_to_guess}.")

