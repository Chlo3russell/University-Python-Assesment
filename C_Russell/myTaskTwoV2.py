import time, sys, random, numpy as np
""" This is my (27954016) connect four, I created the class FourInARow, which creates an object (the board), which updates depending on the function.
    After the board it generated, It uses two functions to print the board (displayBoard) and create the board with obstacles (boardWithObstacles).
    Then it uses three functions to update the board (updateBoard, specialMoveRemove, and specialMovePop) based on the move type.
    To check whether the game has finished, I created a function (gameChecker) that iterates through all of the cells and returns True when all of the cells are full
    The remaining functions I used to count the scores (pointCounter), and I used getTimedTurn to get the users input and time it!
"""
# I had to create this because no matter what I did, I couldn't get the obstacle generator to work
def rangeLogical(start, end):
     return range(start, end+1)

class FourInARow():

    columns, rows = (7, 6)
    # I specified these in the class as they need to be accessed by the functions, but not in the functions as they would be reset everytime they are called.
    specialMovePopT1,specialMovePopT2 = 1, 1
    specialMoveRemoveT1, specialMoveRemoveT2  = 1, 1

    def __init__(self):
        # Generates the array, instead of having one already printed
        self.board = [[' ' for i in range(FourInARow.columns)] for j in range(FourInARow.rows)] 

    def displayBoard(self):
        # This shows a formatted version of my board
        emptyCell = ''
        for row in self.board:
            for cell in row:
                emptyCell += f'|{cell}' # this creates the formatted cell
            emptyCell += '|\n'
        print(" 1 2 3 4 5 6 7 ")
        print(emptyCell)

    def boardWithObstacles(self, board, obstacleSize):
        #This updates the object to have a randomised obstacle with what the user
        obstacleCol = int(obstacleSize[0])  
        obstacleRow = int(obstacleSize[1]) 
        # This gets the random integer where the corner of the obstacle will be 
        randInt = random.randint(0, (7 - obstacleCol))
        # This is where I had to use range locical as I just couln't get it to work properly without adding this. 
        # For row in range -obstacle row, going to - 1, then for cell in range -obstacle column minus the random integer, ending at - 1 minus the random integer
        for row in rangeLogical(-obstacleRow , -1):
            for cell in rangeLogical(-obstacleCol - randInt, -1 - randInt):
                self.board[row][cell] = "X"
        return self.board

    def updateBoard(self, col, team: str ):
        # This function checks for special moves, catches any erronous inputs and updates the board
        # If any of the special moves are used, it takes the point of the local variable
        if col == "R":
            if team == team1 and FourInARow.specialMoveRemoveT1 == 1:
                FourInARow.specialMoveRemoveT1 -= 1 
                board.specialMoveRemove(team)
            elif team == team2 and FourInARow.specialMoveRemoveT2 == 1:
                FourInARow.specialMoveRemoveT2 -= 1
                board.specialMoveRemove(team)
            else:
                print("You have already used your special move. Lose a turn")
        elif col == "P":
            if team == team1 and FourInARow.specialMovePopT1 == 1:
                FourInARow.specialMovePopT1 -= 1
                board.specialMovePop(team)
            elif team == team2 and FourInARow.specialMovePopT2 == 1:
                FourInARow.specialMovePopT2 -= 1
                board.specialMovePop(team)
            else: # If you have already used your special move, it stops here
                print("You have already used your special move. Lose a turn")
        else:
            # After the special moves, it moves on to updating regular turns, checking for integer errors and ensuring that there is an input        
            try:
                if col:
                    col = int(col)
            except (ValueError, TypeError):
                print("Please only Integers OR special moves. Lose your turn")      
            else:
                if col:        
                    if col <= 7 and col >= 1 or col: # Checking the column is actaully in the board, instead of getting an index error
                        col -= 1
                        # This checks the "column" is full
                        if self.board[0][col] == ' ':
                            # This goes through checks all of the rows until it finds an empty cell and then updates the cell
                            for row in range(5, -1, -1):
                                if self.board[row][col] == ' ':
                                    self.board[row][col] = team # Changes the boards cell to team
                                    break
                        else:
                            print("That column is full. You\'ve lost your turn")
                    else:
                        print("1 to 7. You\'ve lost your turn")
                else:
                    print("You need to enter something, lose your turn")
                
    def specialMoveRemove(self, team):
        # This special move worked perfectly... until I found out it wasn't just the wto adjacent cells it was removing
        # This of course made it a lot harder.
        print("For special move Remove, you piece cannot be touching the sides or the bottom or top.\nIf you try and place a piece there you will loose your turn")
        col = input("Where would you like to put your special piece: ")
        try:
            if col:
                col = int(col)
        except (ValueError, TypeError):
            print("Please only Integers. Lose your turn and lose your special move")
        else:
            try:
                if col: 
                    # Checks that the columns aren't 1 or 7 because I didn't have to time to write conitions for all for the sides
                    if 1 < col < 7 and self.board[0][col - 1] == ' ':
                        col -= 1
                        # Finding the empty cell, starting at the bottom and working its way down (in numbers but up in the lists)
                        for row in range(5, -1, -1):
                                if self.board[row][col] == ' ':
                                    # it replaces the i and j in the below board to try and remove all of the surrounding cells
                                    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                                        self.board[row + i][col + j] = ' '
                                    self.board[row + 1][col] = ' '  
                    elif col == 1 or col == 7:
                        print("No Removing columns 1 or 7 pieces, lose your turn!")                    
                else:
                        print("1-7 please in an empty column! Lose your turn, and special move") 
            except IndexError:
                print("You tried to put the move somewhere you shouldn't didn't you?")

    def specialMovePop(self, team):
        # This function removes the players piece in the last "row" and moves all of the other pieces down
        col = input("Where would you like to put your special piece: ")
        try:
            if col:
                col = int(col)
        except (ValueError, TypeError):
            print("Please only Integers. Lose your turn and lose your special move!")
        else:
            # This nestest if and for statement, first checking that their is an input and then that it means the conditions
            if col:        
                if col <= 7 and col >= 1:
                    col -= 1
                    # Then checks that the bottom column piece is the team's piece and removes it
                    if self.board[5][col] == team:
                        self.board[5][col] = ' '
                        # For loop loops through the "rows" and moves down the pieces
                        for row in range(5, -1, -1):
                            self.board[row][col] = self.board[row - 1][col]
                        self.board[0][col] = ' '
                    else:
                        print("That was not your piece to Pop Out, lose your turn and special move!")
                else:
                    print("invalid input, lose your turn and special move")
            else:
                print("You need to enter something, lose your turn")
            
    def getTimedTurn(self, team):
        #  This times the turn and gets the initial input to update the board
        startTime = time.time()
        userInput = False
        finishTime = startTime + 5
        # A while not user input, I orginally thought I needed to interupt the input, but it worked this way so I kept it
        while not userInput:
            print(f"Team {team}, for Pop-out write P, for Removing two adajacent discs write R ")
            if time.time() >= finishTime:
                break
            else:
                column = input("Please input a column or special move: ")
                userInput = True
        # If the user takes longer than 5 seconds the turn is invalid
        if time.time() >= finishTime:
            print("Turn took too long, lose turn")
        else:
            board.updateBoard(column, team)
            board.displayBoard()


    def pointCounter(self, team):
        # This function iterates through all of the lists and checks for points, it checks every possible combination before moving on
        teamscore = 0
        #Checking HORIZONTAL points
        for row in range(0, 6):
            for cell in range(4):
                if self.board[row][cell] == team and self.board[row][cell + 1] == team and self.board[row][cell + 2] == team and self.board[row][cell + 3] == team:
                 teamscore += 1
        #Checking for VERTICAL points
        for row in range(0, 3):
            for cell in range(7):
                if self.board[row][cell] == team and self.board[row + 1][cell] == team and self.board[row + 2][cell] == team and self.board[row + 3][cell] == team:
                    teamscore += 1
        #Checking for RIGHT DIAGANOL points
        for row in range(3):
            for cell in range(4):
                if self.board[row][cell] == team and self.board[row+1][cell+1] == team and self.board[row+2][cell+2] == team and self.board[row+3][cell+3] == team:
                    teamscore += 1
        #Checking for LEFT DIAGANOL points
        for row in range(3):
            for cell in range(4):
                if self.board[row][cell] == team and self.board[row+1][cell-1] == team and self.board[row+2][cell-2] == team and self.board[row+3][cell-3] == team:
                    teamscore += 1
        
        print(f"Team {team}'s score is", teamscore)
        return teamscore


    def gameChecker(self):
        # This iterates through all the empty slots in the board, and returns True if it is full and ends the loop
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
# Initaiting the code
if __name__ == '__main__':
    # Rules here
    print("Welcome to Chloe's Four in a Row. \n The rules are as follows;\n-If you take longer than 5 seconds your turn is ended\n-Use R for special move Remove\n And P for special move Pop\n-The game ends when the board is full")
    # Creating the object
    board = FourInARow()
    board.displayBoard()
    # Creating a boolean to loop over to try and get the correct obstacle size
    isThereAnObstacle = False

    while isThereAnObstacle == False:
        obstacle = input("Please enter your obstacle size (ColumnRow): ")
        # Try catch to check that if someone enters any letters it won't break
        try:
            obstacle = int(obstacle)
            if obstacle > 10 and obstacle <67: # If its bigger than the board it won't allow it
                obstacle = str(obstacle)
                isThereAnObstacle = True    
        except (ValueError, TypeError):
            print("Wrong format please enter in the formart (ColumnRow)")
            isThereAnObstacle = False
        else: 
            print("Obstacle to large or too small")
    # Once there is an obstacle, we create an obstacle board 
    board.boardWithObstacles(board.displayBoard, obstacle)
    board.displayBoard()

    team1, team2 = 'a', 'b'

while board.gameChecker() == False:
    # While game checker returns false, it continues looping through the two teams, whilst displaying the up to date scores
    board.getTimedTurn(team1)
    team1Score = board.pointCounter(team1)
    team2Score = board.pointCounter(team2)
    board.getTimedTurn(team2)
    team1Score = board.pointCounter(team1)
    team2Score = board.pointCounter(team2)

# Displaying the winner, compares the two teams scores
if team1Score > team2Score:
    print(f"Congrats to team 1! You win with {team1Score} points")
elif team1Score == team2Score:
    print(f"Congrats... Oh. You have both got {team2Score} points, you draw.")
else:
    print(f"Congrats to team 2! You win with {team2Score} points")
