propertyPrice = float ( input("What is the property price? ") )

print('----------------------')
while True:
  isHelpToBuy = input("Does it include help to buy scheme? 1 - Yes | 2 - No: ")
  if isHelpToBuy == 1:
    helpToBuyPrice = propertyPrice / 0.2
    print('Include help to buy scheme')
    break
  elif isHelpToBuy == 2:
    helpToBuyPrice = 0
    print('Exclude help to buy scheme')
    break
  else:
    print("Please enter y or n.")

print('----------------------')
depositAmount = float (input("How much are you putting in deposit? "))

print(helpToBuyPrice)