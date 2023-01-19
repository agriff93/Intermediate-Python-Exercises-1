inputtedText = input('Enter a string: ')
inputtedText = inputtedText.lower()
def dictLetterCount(inputString):
    functionDict = {}
    for j in inputString:
        functionDict[j] = functionDict.get(j, 0) + 1
    return(functionDict)
print(dictLetterCount(inputtedText))