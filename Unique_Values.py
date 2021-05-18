numbers = [5,2,1,4,5,6]
numbers2 = numbers.copy()
numbers.append(21)
numbers.insert(0,2)

print(numbers)
print(numbers2)

# Get the uniques from the list of numbers. 
print(" \n Get the Uniques from the list of numbers!!")
numbers = [2,2,4,6,4,3,5,4,1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)













