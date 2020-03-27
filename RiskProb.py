import random

def attack(numAttackers, numDefenders):
    if numAttackers > 3 or numAttackers < 1 or numDefenders > 3 or numDefenders < 1:
        raise ValueError('The parameters must be between 1 and 3, inclusive.')
    attackRolls = []
    defenseRolls = []
    attackDeaths = 0
    defenseDeaths = 0
    for i in range(numAttackers):
        attackRolls.append(random.randint(1, 6))
    for i in range(numDefenders):
        defenseRolls.append(random.randint(1, 6))
    attackRolls.sort(reverse=True)
    defenseRolls.sort(reverse=True)
    for i in range(min(numAttackers, numDefenders)):
        if attackRolls[i] > defenseRolls[i]:
            defenseDeaths += 1
        else:
            attackDeaths += 1
    return attackDeaths, defenseDeaths
    
def playRound(totalAttackers, totalDefenders):
    if totalAttackers <= 1 or totalDefenders < 1:
        raise ValueError('You must have at least 2 attackers and 1 defender.') 
    while totalAttackers > 1 and totalDefenders > 0:
        numAttackers = min(3, totalAttackers - 1)
        numDefenders = min(3, totalDefenders)
        deaths = attack(numAttackers, numDefenders)
        totalAttackers -= deaths[0]
        totalDefenders -= deaths[1]
    if totalDefenders == 0:
        return True
    else:
        return False
    
def simulate(totalAttackers, totalDefenders, totalSims = 10000):
    winCount = 0
    for i in range(totalSims):
        win = playRound(totalAttackers, totalDefenders)
        if win:
            winCount += 1
    return str(100 * (winCount/float(totalSims))) + '%'