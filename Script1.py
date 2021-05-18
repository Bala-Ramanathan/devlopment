print ("This is a sample line!! \n")

# If commands 
the_world_is_flat = True
if the_world_is_flat:
    print("The world is flat \n")

s = 'First Line. \n Second Line.'
print (s)

# If commands more 
x = int(input("Please enter an Integer :"))
if x < 0:
    x = 0 
    print ("Negative changed to Zero \n")
elif x == 0:
    print("Zero \n")
elif x == 1:
    print ("One \n")
else:
    print("More Values \n" )


# for Statements 
words = ['CAT','window','Sanadana Dharma \n \n']
for w in words:
    print(w,len(w))
    
# Python List 

nums = []

#append to a list

nums.append (21)
nums.append("Bala")
nums.append(33.3)
print(nums)


# Python Input 

num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter number 2:"))
prd = num1 * num2
print("Product is  :",prd)