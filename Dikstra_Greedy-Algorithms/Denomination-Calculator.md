```python
# Name: Ayan Tuladhar

# The following program give changes for the least number of bills and coins using greedy algorithm.


# Program to count the number of denominations for any specified amount.
# Demonstrate the condition where it makes greedy algorithm fail.

number_of_bills_and_coins = [100, 50, 20, 15, 10, 5, 1, 0.50, 0.25, 0.10, 0.5, 0.01]
# currency = [25, 15, 1]
assumption_denominations = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# no_of_used_cur = [0, 0, 0]
print("")
print("Welcome to the Money Exchange at Denver International Airport\n")
print("Please exchange your Currency in USD\n")
print("Number of Bills and Coins are distributed in the list shown below:\n")
print("$100")
print("$50")
print("$20")
print("$10")
print("$5")
print("$1")
print("0.50c")
print("0.25c")
print("0.10c")
print("0.005c")
print("0.001c\n")
print("We accept any kinds of Foreign currency. For example, AUD, CAD, NRS etc.")
money = float(input("Please input the currency you want to exchange: "))
print("")
change = float(0)
for a in range(11):
    while money >= change:
        if (change + number_of_bills_and_coins[a]) <= money:
            change += number_of_bills_and_coins[a]
            assumption_denominations[a] += 1
        else:
            break
    if change == money:
        break

for b in range(11):
    print("{0}: {1}".format(number_of_bills_and_coins[b], assumption_denominations[b]))
print("")
print("Thanks for using Money Exchange Service at Denver Internation Airport")
print("Hope you have a Wonderful Trip.")
print("'SOMETIMES WHAT WE SEE IS NOT HAPPENING AND WHAT'S HAPPENING IS NOT SEEN'.")
print("To ensure best customer service you can use our 'Premium Money Exchange Service'.")
print("to provide you with the best service during your travel.")
print("Premium service comes with SPECIAL algorithm which counts the total number of ways to give the change.")
print("This service uses Dynamic Programming")
print("Please use our free trail by entering an amount below:")
print("For example, To exchange $30 DP algorithm will provide you two $15 or one $20 and one $10 instead of one $25 and five $1 bills.")


# Program to solve failed greedy algorithm case using DP by calculating the best optimal solution.
# Counts and Finds number of combinations.


def premium_service(DP):
    number_of_bills = [100, 50, 20, 15, 10, 5, 1]
    count_best_case = [0, 0, 0, 0, 0, 0, 0, 0]
    print("Accurate Count of the currency:")
    for x, y in zip(number_of_bills, count_best_case):
        if DP >= x:
            y = DP // x
            DP = DP - y * x
            print(x, " : ", y)

    possibilities = [0 for i in range(amount + 1)]
    possibilities[0] = 1
    for c in range(len(number_of_bills)):
        for d in range(number_of_bills[c], amount+1):
            possibilities[d] += possibilities[d - number_of_bills[c]]
    print("The total number of comparison for best optimal solution: ", possibilities[amount])


print("")
amount = int(input("Please input the currency you want to exchange to count: "))
premium_service(amount)
print("Congratulation '1000' points has been added towards your membership points. Have a great Trip!")

```

    
    Welcome to the Money Exchange at Denver International Airport
    
    Please exchange your Currency in USD
    
    Number of Bills and Coins are distributed in the list shown below:
    
    $100
    $50
    $20
    $10
    $5
    $1
    0.50c
    0.25c
    0.10c
    0.005c
    0.001c
    
    We accept any kinds of Foreign currency. For example, AUD, CAD, NRS etc.
    Please input the currency you want to exchange: 269.63
    
    100: 2
    50: 1
    20: 0
    15: 1
    10: 0
    5: 0
    1: 4
    0.5: 1
    0.25: 0
    0.1: 1
    0.5: 0
    
    Thanks for using Money Exchange Service at Denver Internation Airport
    Hope you have a Wonderful Trip.
    'SOMETIMES WHAT WE SEE IS NOT HAPPENING AND WHAT'S HAPPENING IS NOT SEEN'.
    To ensure best customer service you can use our 'Premium Money Exchange Service'.
    to provide you with the best service during your travel.
    Premium service comes with SPECIAL algorithm which counts the total number of ways to give the change.
    This service uses Dynamic Programming
    Please use our free trail by entering an amount below:
    For example, To exchange $30 DP algorithm will provide you two $15 or one $20 and one $10 instead of one $25 and five $1 bills.
    
    Please input the currency you want to exchange to count: 30
    Accurate Count of the currency:
    20  :  1
    10  :  1
    The total number of comparison for best optimal solution:  27
    Congratulation '1000' points has been added towards your membership points. Have a great Trip!
    


```python

```
