#
# Lab 7, Task 2
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('0) Input new goal lists')
    print('1) Get the latest score')
    print('2) Print the results')
    print('3) Find the number of wins')
    print('4) Find the max number of goals')
    print("5) Find the full record")
    
    ## Add any new menu options here.


    print('7) Quit')
    print()

def latest_score(bruins, opponents):
    """ returns the score of the latest (i.e., most recent) game
        inputs: bruins - a list of goals scored by the Bruins in a 
                  set of games
                opponents - a list of goals scored by their opponents
        We assume that both lists contain the same number of integers,
        and that they each contain at least one integer.
    """
    score = str(bruins[-1]) + '-' + str(opponents[-1])
    return score

## Add your helper functions for the remaining options below.

def full_record(bruins, opponents):
    """ return the full record of the whole game """
    record = [0, 0, 0]
    for i in range(len(bruins)):
        if bruins[i] > opponents[i]:
            record[0] += 1
        elif bruins[i] == opponents[i]:
            record[2] += 1
        else:
            record[1] += 1
    return record

def find_max_goals(goals):
    """ returns the largest number of goals in the specified 
        list of goals, which we assume contains at least one integer
    """
    maxg = goals[0]
    for g in goals:
        if g >= maxg:
            maxg = g
    return maxg

def find_num_wins(bruins, opponents):
    ''' returns the number of games that the Bruins won '''
    win = 0
    for i in range(len(bruins)):
        if bruins[i] > opponents[i]:
            win += 1
    return win

def print_results(bruins, opponents):
    ''' prints the results of each game in the format shown below '''
    for i in range(len(bruins)):
        if bruins[i] > opponents[i]:
            print("win", str(bruins[i]) + "-" + str(opponents[i]))
        elif bruins[i] == opponents[i]:
            print("tie", str(bruins[i]) + "-" + str(opponents[i]))
        else:
            print("loss", str(bruins[i]) + "-" + str(opponents[i]))
            

def main():
    """ the main user-interaction loop
    """
    bruins = []
    opponents = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            bruins = eval(input('Enter the Bruins list of goals: '))
            opponents = eval(input('Enter their opponents list of goals: '))
            if len(bruins) != len(opponents):
                print('The lists must have the same length.')
                print('Please select menu option 0 to try again.')
                bruins = []
                opponents = []
        elif choice == 7:
            break
        elif choice < 7 and len(bruins) == 0:
            print('You need to first enter the goal lists.')
            print('Please select menu option 0 to do so.')
        elif choice == 1:
            score = latest_score(bruins, opponents)
            print('The score of the latest game was', score)
        ## add code to process the other choices here
        elif choice == 2:
            print_results(bruins, opponents)
        elif choice == 3:
            print("The Bruins have won", find_num_wins(bruins, opponents),"games.")
        elif choice == 4:
            print("The largest number of goals by the Bruins is", find_max_goals(bruins))
        elif choice == 5:
            record = full_record(bruins, opponents)
            print(record[0], "win(s)")
            print(record[1], "loss(es)")
            print(record[2], "tie(s)")
        else:
            print('Invalid choice. Please try again.')

    print('Goodbye!')
