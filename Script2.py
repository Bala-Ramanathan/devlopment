
import math
# Python function to illustrate with Main()

def getInteger():
    result = int(input("Enter integer :"))
    return result

def main():
    print("Started")
    num = -85

#Calling the getInteger function and 
# Storing its returned value in the putput variable
    output = getInteger()
    print("The value enter is : ",output)
    num = math.fabs(num)
    print("Absolute value is:" , num)

# We are required to tell python for main() function existence
if __name__=="__main__":
    main()


print (0==None)
print(True or False)
print(False or True)
print(False and True)


assert 5 <3 , "5 Less than 3."


file1 = open('/Users/bala/DataDeck/test1.txt')
mytxt = file1.read()
file1.close()

a = input("Please type a wrod: ")
print((a+' ')* 5)

type(42.0)