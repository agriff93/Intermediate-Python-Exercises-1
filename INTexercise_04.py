x = int(1)
inputtedSum = int(0)
while 5 >= x:
    inputtedInt = input("Enter int #" + str(x) + ": ")
    try:
        inputtedCheck = int(inputtedInt)
        x = x + 1
        inputtedSum = inputtedSum + int(inputtedInt)
    except ValueError:
       print("Invalid Input. Please enter an int.")
print(inputtedSum)