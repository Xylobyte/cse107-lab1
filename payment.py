# Program to calculate and print the bills needed to sum to a given amount

money = int(input("Enter a dollar ammount: "))
bills = money // 20
money -= 20 * bills
print("$20 bills: " + str(bills))
bills = money // 10
money -= 10 * bills
print("$10 bills: " + str(bills))
bills = money // 5
money -= 5 * bills
print("$5 bills: " + str(bills))
bills = money // 1
money -= 1 * bills
print("$1 bills: " + str(bills))

