propertyPrice = int(input("What is the property price? ") )

print('----------------------')
while True:
  isHelpToBuy = input("Does it include help to buy scheme? 1 - Yes | 2 - No: ")
  if isHelpToBuy == 1:
    helpToBuyPrice = (propertyPrice * 0.2)
    depositAmount = (propertyPrice * 0.05)
    print('Include help to buy scheme')
    break
  elif isHelpToBuy == 2:
    helpToBuyPrice = 0
    print('Exclude help to buy scheme')
    depositAmount = int (input("How much are you putting in deposit? "))
    break
  else:
    print("Please enter y or n.")

print('----------------------')

mortgageRequired = propertyPrice - helpToBuyPrice - depositAmount

print('Property Price: ', propertyPrice)
print('Equity loan: ', helpToBuyPrice)
print('Deposit: ', depositAmount)
print('Mortgage amount required: ', mortgageRequired)