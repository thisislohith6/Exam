import sys
from Addition import Addition
from Multiply import Multiply
from Division import Division
from Subtraction import Subtraction

print("Enter the operation to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

inp = input()

if(inp=="1"):
    op = Addition(2,3)
elif(inp=="2"):
    op = Subtraction(2,3)
elif(inp=="3"):
    op = Division(2,3)
elif(inp=="4"):
    op = Multiply(2,3)
else:
    print("Wrong input given")
    sys.exit(0)

    
print(op.operation(a,b))
