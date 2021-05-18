#Guess the Value - Game 1 

initial_value = 9
counter_value = 0 
counter_max = 3
while counter_value < counter_max:
    value = int(input("Guess the Value: "))
    counter_value = counter_value + 1
    if value == initial_value:
        print("You have guessed right. ")
        break
else:
    print("You have tried maximum time. Better luck next time")

