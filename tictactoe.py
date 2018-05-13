import random
fields = ['A','B','C','D','E','F','G','H','J']
possibleRows = [['A','B','C'],['D','E','F'],['G','H','J'],['A','E','J'],['A','D','G'],['B','E','H'],['C','F','J'],['C','E','G']]
player1 = 'x'
player2 = 'o'
nextTurn = ''
# prints the playing field
def printField():
    print(fields[0],'|',fields[1],'|',fields[2])
    print('-','|','-','|','-')
    print(fields[3],'|',fields[4],'|',fields[5])
    print('-','|','-','|','-')    
    print(fields[6],'|',fields[7],'|',fields[8])
# removes item from a list
def removeFromList (itemList, item):
    while item in itemList: 
        itemList.remove(item)
    return itemList
# checks if there are possible turns or last turn
def checkIfLastTurn(fields):
    fields_copy = list(fields)
    fields_copy = removeFromList(fields_copy, player1)
    fields_copy = removeFromList(fields_copy, player2)
    return fields_copy
# checks if there are a winning row
def checkIfWinner(player):
    for rowidx in range(len(possibleRows)):
        row = possibleRows[rowidx]
        if(row.count(player) == 3): 
            return True
    return False
# setting the turn of one player to the possible rows
def setTurnToRow (item, player):
    for rowidx in range(len(possibleRows)):
        if(item in possibleRows[rowidx]):
            possibleRows[rowidx][possibleRows[rowidx].index(item)] = player

# finds double settings of one player in one row and returns the item which is left in the row
def findDoubleSetsForPlayer(firstPlayer, secondPlayer):
    nextTurn = ''
    for rowidx in range(len(possibleRows)):
        row = possibleRows[rowidx]
        if(row.count(firstPlayer) == 2 and not secondPlayer in row):
            row_copy = list(row)
            row_copy = removeFromList(row_copy, firstPlayer)
            nextTurn = row_copy[0]
            return nextTurn
    return nextTurn
# sets the next turn of player 2 (the system)
def setNextTurn():
    if( 'E' in fields):
        nextTurn = 'E'
    else: 
        nextTurn = findDoubleSetsForPlayer(player2, player1)
        if not nextTurn:
            nextTurn = findDoubleSetsForPlayer(player1, player2)
        if not nextTurn:
            fields_copy = list(fields)
            fields_copy = removeFromList(fields_copy, player1)
            if(player2 in fields_copy):
                fields_copy = removeFromList(fields_copy, player2)
            nextTurn = random.choice(fields_copy)
    return nextTurn
# doing a whole play turn for both player   
def doTurn(field):
    if(field in fields):
        fields[fields.index(field)] = player1
        setTurnToRow(field,player1)
        wonPlayer1 = checkIfWinner(player1)
        if wonPlayer1:
            printField()
            print('***CONGRATULATION YOU WON***')
            print('***GAME OVER***')
            return False
        fieldscopy = checkIfLastTurn(fields)
        if not fieldscopy:
            printField()
            print('***THE GAME IS UNDECIDED***')
            print('***GAME OVER***')
            return False
        else:    
            nextTurn = setNextTurn()
            fields[fields.index(nextTurn)] = player2
            setTurnToRow(nextTurn, player2)
            wonPlayer2 = checkIfWinner(player2)
            if wonPlayer2:
                printField()
                print('***THE SYSTEM WON***')
                print('***GAME OVER***')
                return False
            return True      
    else:
        print('No possible selection')
        return True  
# the game starts         
playRuns = True        
while(playRuns):    
    printField()
    field = input('Choose field:')
    playRuns = doTurn(field.upper())