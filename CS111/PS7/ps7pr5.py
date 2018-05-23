#
# ps7pr5.py (Problem Set 7, Problem 5)
#
# TT Securities
#
# Computer Science 111    
#

def display_menu():  
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the min price and its day')
    print('(6) Test a threshold')
    print('(7) Your TT investment plan')

    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    ## IMPORTANT: You will need to change this function so
    ## that it prints a table of days and prices.
    print("Day Price")
    print("--- -----")
    for i in range(len(prices)):
        print('%3.0f' %  i, end = ' ')
        print('%5.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your helper functions for options 3-7 below.

def avg_price(prices):
    """ returns the average price """
    sum_price = 0
    for price in prices:
        sum_price += price
    return sum_price / len(prices)

def sd_price(prices):
    """ return the standard deviation of prices """
    avg = avg_price(prices)
    sig_sum = 0
    for price in prices:
        sig_sum += (price - avg)**2
    return (sig_sum / len(prices))**0.5

def min_price(prices):
    """ return the minimum price and the day it occurred """
    min_price = [prices[0], 0]
    for i in range(len(prices)):
        if prices[i] < min_price[0]:
            min_price = [prices[i], i]
    return min_price

def threshold(prices, th):
    """ determine if there are any prices above that threshold, and print an
    appropriate message """
    above = 0
    for price in prices:
        if price > th:
            above += 1
    if above == 0:
        print("There is no price over", th)
    else:
        print("There is at least one price over", th)

def buy_sell(prices):
    """ find the best days on which to buy and sell the stock whose prices
    are given in the list of prices """
    max_tuple = [] # [profit, buy_index, sell_index]
    for i in range(len(prices) - 1):
        diff = [prices[i+1] - prices[i], i, i+1]
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > diff[0]:
                diff = [prices[j] - prices[i], i, j]
        max_tuple += [diff]
    max_profit = max_tuple[0]
    for i in range(len(max_tuple)):
        if max_tuple[i][0] > max_profit[0]:
            max_profit = max_tuple[i]
    print(max_tuple)
    print('Buy on day', max_profit[1], 'at price', prices[max_profit[1]])
    print('Sell on day', max_profit[2], 'at price', prices[max_profit[2]])
    print('Total profit:', max_profit[0])

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print("The average price is", avg_price(prices))
        elif choice == 4:
            print("The standard deviation is", sd_price(prices))
        elif choice == 5:
            min_prices = min_price(prices)
            print("The minimum price is", min_prices[9], "on day", min_prices[1])
        elif choice == 6:
            threshold(prices, int(input("Enter the thershold: ")))
        elif choice == 7:
            buy_sell(prices)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
