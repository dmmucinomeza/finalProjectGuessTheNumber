'''
Created on Mar 7, 2020

@author: Desteny M Mucino Meza
'''
import random 
  
print("Welcome to the Random Number Guessing game") 
print("press 'q' if you would like to quit")
print("What is your name?")
name = input()
    
print("Hello\n" + str(name.capitalize()))

number = random.randint(1, 20) 
        
chances = 0
  
print("Guess a number (between 1 and 20):")  
  
while chances < 5: 
    guess = int(input()) 
    if guess == number: 
        print("Congratulations YOU WON!!!") 
        break
    elif guess < number: 
        print("Your guess was too low: Guess a number higher than", guess) 
    else: 
        print("Your guess was too high: Guess a number lower than", guess) 
    chances += 1
if not chances < 5: 
    print("No sorry, you LOST!!! The number is", number) 