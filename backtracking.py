import random

cards = [["El/la mejor amigo(a)","Pistola", "Venganza","Cabeza", "Sala"],
         ["El/la novio(a)","Cuchillo", "Celos", "Pecho", ""]]

solution = ["El/la mejor amigo(a)","Cuchillo","Venganza","Cabeza", "Sala"]

restringedCards = []
restrictedPairs = []

def generateRestrictedPairs(pairAmount):
    """Generates the restricted pairs

    Args:
        pairAmount: Amount of restricted pairs
    """
    counter = 0
    while(counter < pairAmount):
        firstMid = cards[random.randint(0,len(cards) -1)][random.randint(0, len(cards[0]) -1)]
        secondMid = cards[random.randint(0,len(cards) -1)][random.randint(0, len(cards[0]) -1)] 
        if (checkPair(firstMid, secondMid)):
            restrictedPairs.append([firstMid, secondMid])
            counter += 1

def checkPair(firstMid, secondMid):
    """
    Check if a generated pair is unique and does not belong to the 
    solution set

    Args:
        firstMid: First pair value
        secondMid: Second pair value
    
    Returns:
        True if the pair meets the requeriments, false otherwise
    """
    return (firstMid != secondMid and firstMid not in solution and
        secondMid not in solution and firstMid != "" and
        secondMid != "" and [firstMid, secondMid] not in restrictedPairs and
        [secondMid, firstMid] not in restrictedPairs)

def checkRestriction(resultArray):
    """
    Check if the solution list contains a restriction

    Args:
        resultArray: list that contains the actual problem solution
    
    Returns:
        True if the solution list contains a restriction, False otherwise.
    """
    for pair in range(0, len(restrictedPairs)):
        if (restrictedPairs[pair][0] in resultArray and restrictedPairs[pair][1] in resultArray):
            return True
    return False

def restrictCard(wrongSolution):
    """
    Choose a card from the wrong solution and add it to the restricted cards set

    Args:
        wrongSolution: list with the deeper backtracking solution
    """
    wrongSolution = difference(wrongSolution, solution)
    card = random.randint(0, len(wrongSolution) -1)
    if (wrongSolution[card] not in restringedCards):
        restringedCards.append(wrongSolution[card])

def goBack(resultArray):
    """
    Check if it is necesary to go back in the search
    
    Args:
        resultArray: list with the actual problem solution
    
    Returns: True if it is necesary to go back, False otherwise
    """
    for card in range(0 , len(restringedCards)):
        if (restringedCards[card] in resultArray):
            return True

def backtracking(isFound, index, column, resultArray):
    """
    Perfomrms the backtracking search

    Args:
        isFound: list with a unique value. Used to know if the solution was reached
        index: actual row of the cards matrix
        column: acutal column of the cards matrix
        resultArray: acutal problem solution
    """
    if(isFound[0] == True):
        return
    if (column >= len(cards[index]) ):
        restrictCard(resultArray)
        resultArray[column - 1] = ""
        return
    for row in range(0, len(cards)):
        if (isFound[0] == True):
            break
        if (cards[row][column] == "" ):
            return
        checkSol = resultArray
        checkSol[column] = ""
        if (goBack(checkSol)):
            resultArray[column] = ""
            return
        if (checkRestriction(resultArray)):
            resultArray[column] = ""
            return
        resultArray[column] = cards[row][column]
        print(resultArray)
        if (resultArray == solution):
            print("Solucion:", resultArray)
            isFound[0] = True
            return
        else:
            backtracking(isFound, row, column + 1, resultArray)

def difference(listA, listB):
    """
    Make the difference between list
    Used to know the wrong values in the actual solution

    Args:
        listA: minuend list
        listB: substrahend list

    Returns: listC the differece between lists
    """
    listC = []
    for element in listA:
        if element not in listB:
            listC.append(element)
    return listC

def main():
    generateRestrictedPairs(4)
    backtracking([False], 0, 0, ["", "", "", "", ""])
main()