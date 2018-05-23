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
