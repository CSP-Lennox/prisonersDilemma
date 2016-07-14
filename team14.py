####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    prob=calculateProbabilities(my_history, their_history)
    # most recent 
    if len(my_history) < 3:
        return 'c'
    myChoice=my_history[-1]
    theirChoice=their_history[-1]
    # the probability that the opponent will choose C
    temp=0
    if myChoice == 'c':
        if theirChoice == 'c':
            temp=prob[0]
        else:
            temp=prob[1]
    else:
        if theirChoice == 'c':
            temp=prob[2]
        else:
            temp=prob[3]
    if temp > .75:
        return 'c'
    else:
        return 'b'         
def calculateProbabilities(my_history, their_history):
    # numer of opponent choosing C based on previous round
    mCtC_C=.001;
    mCtB_C=.001;
    mBtC_C=.001;
    mBtB_C=.001;
    # numer of opponent choosing B based on previous round
    mCtC_B=.001;
    mCtB_B=.001;
    mBtC_B=.001;
    mBtB_B=.001;
    for i in range(1,len(my_history)):
        myChoice=my_history[i-1]
        theirChoice=their_history[i-1]
        newChoice= their_history[i]
        if myChoice == 'c':
            if theirChoice == 'c':
                if newChoice == 'c':
                    mCtC_C+=1
                else:
                    mCtC_B+=1
            else:
                if newChoice == 'c':
                    mCtB_C+=1
                else:
                    mCtB_B+=1
        else:
            if theirChoice == 'c':
                if newChoice == 'c':
                    mBtC_C+=1
                else:
                    mBtC_B+=1
            else:
                if newChoice == 'c':
                    mBtB_C+=1
                else:
                    mBtB_B+=1
    return (mCtC_C/(mCtC_C+mCtC_B),mCtB_C/(mCtB_C+mCtB_B),
        mBtC_C/(mBtC_C+mBtC_B),mBtB_C/(mBtB_C+mBtB_B))
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             