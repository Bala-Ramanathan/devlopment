# Defining a basic function 
def greet_user():
    print("Hi there!! ")
    print("Wlecome to Python!!")

print("Start")
greet_user()
print("Finish")

# Define a function with a parameter.

def greet_user1(first_name,last_name):
    print(f'Hi {first_name}{last_name}!')
    print('Wlecome to python!!')


print('Start')
greet_user1(first_name = "John",last_name = " Smith") 
print('Finish')