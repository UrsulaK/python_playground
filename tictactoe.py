import random
fields = ['A','B','C','D','E','F','G','H','J']
possibleRows = [['A','B','C'],['D','E','F'],['G','H','J'],['A','E','J'],['A','D','G'],['B','E','H'],['C','F','J'],['C','E','G']]
player1 = 'x'
player2 = 'o'
nextTurn = ''
def printField():
    print(fields[0],'|',fields[1],'|',fields[2])
    print('-','|','-','|','-')
    print(fields[3],'|',fields[4],'|',fields[5])
    print('-','|','-','|','-')    
    print(fields[6],'|',fields[7],'|',fields[8])

def removeFromList (itemList, item):
    while item in itemList: 
        itemList.remove(item)
    return itemList

def checkForLastTurn(fields):
    fields_copy = list(fields)
    fields_copy = removeFromList(fields_copy, player1)
    fields_copy = removeFromList(fields_copy, player2)
    return fields_copy

def setTurnToRow (item, player):
    for rowidx in range(len(possibleRows)):
        if(item in possibleRows[rowidx]):
            possibleRows[rowidx][possibleRows[rowidx].index(item)] = player

def findDoubleSets():
    nextTurn = ''
    for rowidx in range(len(possibleRows)):
        row = possibleRows[rowidx]
        if(row.count(player1) == 2 and not player2 in row):
            row_copy = list(row)
            row_copy = removeFromList(row_copy, player1)
            nextTurn = row_copy[0]
            return nextTurn
    return nextTurn

def setNextTurn():
    if( 'E' in fields):
        nextTurn = 'E'
    else: 
        nextTurn = findDoubleSets()
        if not nextTurn:
            fields_copy = list(fields)
            fields_copy = removeFromList(fields_copy, player1)
            if(player2 in fields_copy):
                fields_copy = removeFromList(fields_copy, player2)
            nextTurn = random.choice(fields_copy)
    return nextTurn
    
def doTurn(field):
    if(field in fields):
        fields[fields.index(field)] = player1
        setTurnToRow(field,player1)
        fieldscopy = checkForLastTurn(fields)
        if not fieldscopy:
            printField()
            print('***GAME OVER***')
            return False
        else:    
            nextTurn = setNextTurn()
            fields[fields.index(nextTurn)] = player2
            setTurnToRow(nextTurn, player2)
            return True      
    else:
        print('No possible selection')
        return True  
         
playRuns = True        
while(playRuns):    
    printField()
    field = input('Choose field:')
    playRuns = doTurn(field.upper())