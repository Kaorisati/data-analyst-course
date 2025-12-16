import getpass #hides user's input in terminal.

round = 0
score = [0,0]

def requestOption (player,options):
    while True:
        selectedOption = getpass.getpass(prompt=f"{player}, select and option {options} ").lower()
        if selectedOption in options:
            return selectedOption
        else:
            print ('The option is not valid, please try again.')
 
print("Welcome to rock, paper, scissors")

while max(score)<4 or abs(score[0]-score[1])>2:
    print (f'menor que 4? {max(score)<4}')
    print (f'diferencia mmayor a dos? {abs(score[0]-score[1])>2}')
    print (sum(score) )
    print (abs(score[0]-score[1]))
    round += 1
    print (score)
    validOptions = ["paper", "scissors", "rock"]

    playerOne = requestOption('Player1', validOptions)
    playerTwo = requestOption('Player2', validOptions)

    condition1 = playerOne == "rock" and playerTwo == "scissors"
    condition2 = playerOne == "paper" and playerTwo == "rock"
    condition3 = playerOne == "scissors" and playerTwo == "paper"
    
    print(f"=========Round {round}!=========")
   
    if playerOne == playerTwo:
        print("Draw! Play again") #deberia poder jugarse de nuevo en esta ronda

    elif condition1 or condition2 or condition3:
        score[0] += 1
        print(f"Player 1: {playerOne} \nPlayer 2: {playerTwo}\n   Player 1 wins!")
    else:
        score[1] +=1
        print(f"Player 1: {playerOne} \nPlayer 2: {playerTwo}\n   Player 2 wins!")

print (f'jugador {score.index(max(score))+1}')
#se podria agregar quien es el ganador general