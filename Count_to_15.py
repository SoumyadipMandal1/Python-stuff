'''
This is python program for a game.
In this game, you and your opponent have to choose a number between 1 to 9.
The number choosen should not be repeated.
The goal of the game is have any numbers whose sum becomes equal to 15.
One who achieves the goal first, wins the game.
If both the players can not fulfill this goal and all the numbers from 1 to 9 gets used up, then
it would result in a draw.
The opponent is a bot which is made by simple programming and by machine learning or deep learning.
So, there is a simple Artificial Intelligence in the game.
This game works on the principle of tic-tac-toe and 3 X 3 Magic Square.
A Magic Square is a n x n grid ( n >= 3 ) containing numbers between 1 to n**2 and
the sum of numbers in every row, column and diagonal is same, i.e., (n * (n ** 2 + 1)) / 2.
A 3 X 3 Magic Square is a grid of numbers between 1 to 9 and the sum of numbers in every, row and column is 15.
This is an example of Magic Square :-
                +---+---+---+
                | 6 | 7 | 2 |
                +---+---+---+
                | 1 | 5 | 9 |
                +---+---+---+
                | 8 | 3 | 4 |
                +---+---+---+
As the sum of numbers in every row, column and diagonal is same (15),
so we have to choose numbers in such a way such that
it is in the same row, column or diagonal like in the game of tic-tac-toe,
where we try to match a row, column or diagonal.
'''
#Importing required module(s)
import random
#Creating the magic square and the square of numbers selected by the players
#The zeroes will get replaced by the number selected by the player
#in that position corresponding to the magic square. 
Magic_Square = [[6,7,2],
                [1,5,9],
                [8,3,4]]
def choice_for_playing_the_game_again():
    '''
    This function returns the choice of user whether he/she wants to play the game again or not.
    '''
    #Creating a variable to store the choice
    choice = ''
    #Asking the user for input.
    print('Do you want to play again ? (yes or no)')
    #Taking input from the user.
    choice = input('Enter your choice : ')
    while choice != 'yes' and choice != 'no':
        #This loop will continue until the user have not entered the correct choice.
        #Giving an error response to the user for entering wrong input.
        print('Your choice is wrong.')
        #Again Taking input from the user.
        choice = input('Enter either yes or no as choice : ')
    else:
        #The choice entered is correct and returning the choice
        return choice
def choice_of_who_will_play_first():
    '''
    This function returns the choice of user whether he/she wants to play the first turn or not.
    '''
    #Creating a variable to store the choice
    choice = ''
    #Asking the user for input.
    print('Do you want to play first ? (yes or no)')
    #Taking input from the user.
    choice = input('Enter your choice : ')
    while choice != 'yes' and choice != 'no':
        #This loop will continue until the user have not entered the correct choice.
        #Giving an error response to the user for entering wrong input.
        print('Your choice is wrong.')
        #Again Taking input from the user.
        choice = input('Enter either yes or no as choice : ')
    else:
        #The choice entered is correct and returning the choice
        return choice
def insert_in_sorted_list(Numbers_Selected, Number_to_be_inserted):
    '''
    This function inserts a number in the sorted list in such a way that the list remains sorted.
    '''
    #If the list is empty, then simply inserting the element to the list
    if Numbers_Selected == []:
        Numbers_Selected.append(Number_to_be_inserted)
        return None
    else:
        #Checking if the first element of the list is smaller than the number to be inserted
        if Number_to_be_inserted < Numbers_Selected[0]:
            Numbers_Selected.insert(0, Number_to_be_inserted)
        #Iterating through the whole list with respect to the length of the list
        #if the list is not empty.
        for Each_Position in range(len(Numbers_Selected)):
            #Selecting the number corresponding to the position in the list.
            Number = Numbers_Selected[Each_Position]
            #Checking if the number is less than the number to be selected or not.
            if Number < Number_to_be_inserted:
                #Inserting the number in that position
                Numbers_Selected.insert(Each_Position + 1, Number_to_be_inserted)
                return None
def is_won(Square):
    '''
    This function tells whether a square given to the function parameter
    has fulfilled the necessary winning conditions by returning True or False otherwise.
    '''
    #Checking the rows
    for Each_Row in Square:
        if 0 not in Each_Row:
            return Each_Row
    #Checking the columns
    for Each_Column in range(3):
        column = [Each_Row[Each_Column] for Each_Row in Square]
        if 0 not in column:
            return column
    #Checking the two diagonals
    if 0 not in (Square[0][0], Square[1][1], Square[2][2]):
        return (Square[0][0], Square[1][1], Square[2][2])
    if 0 not in (Square[0][2], Square[1][1], Square[2][0]):
        return (Square[0][2], Square[1][1], Square[2][0])
    #Returning False if the above conditions are not satisfied to win the game.
    return False
def is_going_to_win(Square, Remaining_Numbers):
    '''
    This function returns the number which is remaining to selected by the player
    to win the game and False otherwise.
    '''
    #Checking the rows
    for Each_row_position in range(3):
        #Storing the row in a new variable.
        row = Square[Each_row_position]
        if row.count(0) == 1:
            #In this row, only one number is remaining to be selected,
            #Checking where the number is zero in that row.
            for Each_number_position in range(3):
                if row[Each_number_position] == 0:
                    #Checking if the number is in remaining numbers or not
                    if Magic_Square[Each_row_position][Each_number_position] in Remaining_Numbers:
                        #Returning the number
                        return Magic_Square[Each_row_position][Each_number_position]
    #Checking the columns
    for Each_column_position in range(3):
        #Storing the column in a new variable.
        column = [Each_row[Each_column_position] for Each_row in Square]
        if column.count(0) == 1:
            #In this column, only one number is remaining to be selected,
            #Checking where the number is zero in that column.
            for Each_number_position in range(3):
                if column[Each_number_position] == 0:
                    #Checking if the number is in remaining numbers or not
                    if Magic_Square[Each_number_position][Each_column_position] in Remaining_Numbers:
                        #Returning the number
                        return Magic_Square[Each_number_position][Each_column_position]
    #Checking the diagonals
    if (Square[0][0], Square[1][1], Square[2][2]).count(0) == 1:
        #In this diagonal, only one number is remaining to be selected,
        #Checking where the number is zero in that diagonal and returning that number.
        if Square[0][0] == 0:
            #Checking if the number is in remaining numbers or not
            if 6 in Remaining_Numbers:
                #Returning the number
                return 6
        if Square[1][1] == 0:
            #Checking if the number is in remaining numbers or not
            if 5 in Remaining_Numbers:
                #Returning the number
                return 5
        if Square[2][2] == 0:
            #Checking if the number is in remaining numbers or not
            if 4 in Remaining_Numbers:
                #Returning the number
                return 4
    if (Square[0][2], Square[1][1], Square[2][0]).count(0) == 1:
        #In this diagonal, only one number is remaining to be selected,
        #Checking where the number is zero in that diagonal and returning the number.
        if Square[0][2] == 0:
            #Checking if the number is in remaining numbers or not
            if 2 in Remaining_Numbers:
                #Returning the number
                return 2
        if Square[1][1] == 0:
            #Checking if the number is in remaining numbers or not
            if 5 in Remaining_Numbers:
                #Returning the number
                return 5
        if Square[2][0] == 0:
            #Checking if the number is in remaining numbers or not
            if 8 in Remaining_Numbers:
                #Returning the number
                return 8
    #If none of the above conditions are satisfied
    return False
def place_the_number(number, square):
    '''
    This function places the number in the correct position in the square.
    '''
    #Finding the position of the number in the Magic Square
    for each_row_position in range(3):
        for each_column_position in range(3):
            if Magic_Square[each_row_position][each_column_position] == number:
                #Adding the number in the Square
                #with respect to the position of the number in the Magic Square
                square[each_row_position][each_column_position] = number
def count_to_15():
    '''
    This is the main function the game.
    '''
    User_Square = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]
    Bot_Square = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    #These lists will store the numbers selected by the player, the bot and the remaining numbers.
    Numbers_Selected_by_User = []             #As no numbers are selected by the two players
    Numbers_Selected_by_Bot = []              #in the start of the game, so these lists are empty.
    #All numbers between 1 to 9 which are to be selected by the players.
    Remaining_Numbers = [1,2,3,4,5,6,7,8,9]
    openings = [6,2,5,8,4]                    #Opening numbers for the bot.
    #Asking the choice of user whether he will play first or the bot
    if choice_of_who_will_play_first() == 'yes':
        #Variable for storing whether it is the first turn of the bot or not
        bot_1st_turn = True
        #Game loop
        while Remaining_Numbers != []:
            #User's turn :
            #Printing the numbers selected by user, bot and the remaining numbers
            print('Numbers selected by you = ', Numbers_Selected_by_User)
            print('Numbers selected by the bot = ', Numbers_Selected_by_Bot)
            print('Remaining numbers = ', Remaining_Numbers)
            #Asking the user which number he wants to select until
            #the number entered by the user is an integer and
            #the number entered by the user is between 1 to 9.
            number_entered = int(input('Enter your number : '))
            while number_entered not in range(1,10) or number_entered not in Remaining_Numbers:
                #If the number entered by the user is not an integer
                if type(number_entered) != int:
                    print('Your input is not a number between 1 to 9.')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
                #If the number entered by the user is not between 1 to 9
                elif number_entered not in range(1,10):
                    print('The number entered should be between 1 to 9')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
                #If number enterd by the user is not in remaining numbers
                elif number_entered not in Remaining_Numbers:
                    print('The number entered should be in remaining numbers. A number can not be selected twice.')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
            else:
                #If the number fulfills all the above conditions,
                #Placing the number in the Magic Square
                place_the_number(number_entered, User_Square)
                #Inserting the number inserted in the list of elements selected by the user
                insert_in_sorted_list(Numbers_Selected_by_User, number_entered)
                #Removing the number selected from the list of remaining numbers
                Remaining_Numbers.remove(number_entered)
            #checking if the user has won the game or not
            is_won_user = is_won(User_Square)
            if is_won_user:
                #Ending the game loop by congratulating the player.
                print('Congratulations! You have won the game.') #Which is obviously not going to happen.
                #Displaying the winning numbers
                print('The required numbers which make you win are : ')
                print(f'{is_won_user[0]} + {is_won_user[1]} + {is_won_user[2]} = 15')
                break
            #Bot's turn :
            #Checking whether it the first turn of the bot
            if bot_1st_turn:
                while True:
                    #Choosing a random number to play at start
                    Bot_number = random.choice(openings)
                    if Bot_number in Remaining_Numbers:
                        #Placing the number in the Magic Square
                        place_the_number(Bot_number, Bot_Square)
                        #Inserting the number inserted in the list of elements selected by the user
                        insert_in_sorted_list(Numbers_Selected_by_Bot, Bot_number)
                        #Removing the number selected from the list of remaining numbers
                        Remaining_Numbers.remove(Bot_number)
                        #Displaying the number selected by bot
                        print('Number selected by bot =', Bot_number)
                        #Making the variable of bot's first turn False
                        bot_1st_turn = False
                        #Leaving the loop
                        break
                    else:
                        #Removing the number from the choice of openings if it is already used by the user
                        openings.remove(Bot_number)
            else:
                #Checking whether the bot is going to win.
                is_going_to_win_Bot = is_going_to_win(Bot_Square, Remaining_Numbers)
                if is_going_to_win_Bot:
                    #Placing the number in the bot Square
                    place_the_number(is_going_to_win_Bot, Bot_Square)
                    #Displaying the number selected by the bot
                    print('Number selected by bot =', is_going_to_win_Bot)
                    #Ending the game loop by displaying a loosing message to the user.
                    print('You are defeated by the bot!')
                    #Displaying the numbers with which the bot has won.
                    is_won_bot = is_won(Bot_Square)
                    print(f'{is_won_bot[0]} + {is_won_bot[1]} + {is_won_bot[2]} = 15')
                    #leaving the game loop
                    break
                #Checking whether the user is going to win.
                is_going_to_win_User = is_going_to_win(User_Square, Remaining_Numbers)
                if is_going_to_win_User:
                    #Placing the number in the bot Square
                    place_the_number(is_going_to_win_User, Bot_Square)
                    #Displaying the number selected by the bot
                    print('Number selected by bot =', is_going_to_win_User)
                    #Inserting the number inserted in the list of elements selected by the bot
                    insert_in_sorted_list(Numbers_Selected_by_Bot, is_going_to_win_User)
                    #Removing the number selected from the list of remaining numbers
                    Remaining_Numbers.remove(is_going_to_win_User)
                    #Checking if the bot has won by entering the number or not
                    is_won_bot = is_won(Bot_Square)
                    if is_won_bot:
                        print('You are defeated by the bot!')
                        #Displaying the numbers with which the bot has won.
                        is_won_bot = is_won(Bot_Square)
                        print(f'{is_won_bot[0]} + {is_won_bot[1]} + {is_won_bot[2]} = 15')
                        #leaving the game loop
                        break
                #If both the bot and the user is not going to win
                else:
                    if 5 in Numbers_Selected_by_Bot:
                        if 6 in Numbers_Selected_by_Bot:
                            if (2 in Numbers_Selected_by_User or 1 in Numbers_Selected_by_User) and (8 in Remaining_Numbers):
                                place_the_number(8, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 8')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(8)
                            elif (7 in Numbers_Selected_by_User or 8 in Numbers_Selected_by_User) and (2 in Remaining_Numbers):
                                place_the_number(2, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 2')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(2)
                        elif 2 in Numbers_Selected_by_Bot:
                            if (9 in Numbers_Selected_by_User or 6 in Numbers_Selected_by_User) and (4 in Remaining_Numbers):
                                place_the_number(4, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 4')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(4)
                            elif (7 in Numbers_Selected_by_User or 4 in Numbers_Selected_by_User) and (6 in Remaining_Numbers):
                                place_the_number(6, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 6')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(6)
                        elif 4 in Numbers_Selected_by_Bot:
                            if (2 in Numbers_Selected_by_User or 3 in Numbers_Selected_by_User) and (8 in Remaining_Numbers):
                                place_the_number(8, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 8')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(8)
                            elif (9 in Numbers_Selected_by_User or 8 in Numbers_Selected_by_User) and (2 in Remaining_Numbers):
                                place_the_number(2, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 2')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(2)
                        elif 8 in Numbers_Selected_by_Bot:
                            if (6 in Numbers_Selected_by_User or 3 in Numbers_Selected_by_User) and (4 in Remaining_Numbers):
                                place_the_number(4, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 4')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(4)
                            elif (1 in Numbers_Selected_by_User or 4 in Numbers_Selected_by_User) and (6 in Remaining_Numbers):
                                place_the_number(6, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 6')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(6)
                        else:
                            if 6 in Numbers_Selected_by_User and 4 in Remaining_Numbers:
                                place_the_number(4, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 4')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(4)
                            elif 4 in Numbers_Selected_by_User and 6 in Remaining_Numbers:
                                place_the_number(6, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 6')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(6)
                            elif 2 in Numbers_Selected_by_User and 8 in Remaining_Numbers:
                                place_the_number(8, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 8')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(8)
                            elif 8 in Numbers_Selected_by_User and 2 in Remaining_Numbers:
                                place_the_number(2, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 2')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(2)
                            else:
                                if {6,2,8,4}.issubset(Remaining_Numbers):
                                    bot_number = random.choice([6,2,8,4])
                                    place_the_number(bot_number, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print(f'Number selected by bot = {bot_number}')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(bot_number)
                                else:
                                    bot_number = random.choice(Remaining_Numbers)
                                    place_the_number(bot_number, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print(f'Number selected by bot = {bot_number}')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(bot_number)
                    else:
                        if 5 in Remaining_Numbers:
                            place_the_number(5, Bot_Square)
                            #Displaying the number selected by the bot
                            print('Number selected by bot = 5')
                            #Inserting the number inserted in the list of elements selected by the bot
                            insert_in_sorted_list(Numbers_Selected_by_Bot, 5)
                            #Removing the number selected from the list of remaining numbers
                            Remaining_Numbers.remove(5)
                        else:
                            if 6 in Numbers_Selected_by_Bot:
                                if 4 in Remaining_Numbers:
                                    place_the_number(4, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 4')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(4)
                            elif 2 in Numbers_Selected_by_Bot:
                                if 8 in Remaining_Numbers:
                                    place_the_number(8, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 8')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(8)
                            elif 4 in Numbers_Selected_by_Bot:
                                if 6 in Remaining_Numbers:
                                    place_the_number(6, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 6')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(6)
                            elif 8 in Numbers_Selected_by_Bot:
                                if 2 in Remaining_Numbers:
                                    place_the_number(2, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 2')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(2)
                            else:
                                if {6,2,8,4}.issubset(Remaining_Numbers):
                                    bot_number = random.choice([6,2,8,4])
                                    place_the_number(bot_number, BotSquare)
                                    #Displaying the number selected by the bot
                                    print(f'Number selected by bot = {bot_number}')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(bot_number)
                                else:
                                    bot_number = random.choice(Remaining_Numbers)
                                    place_the_number(bot_number, BotSquare)
                                    #Displaying the number selected by the bot
                                    print(f'Number selected by bot = {bot_number}')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(bot_number)
        else:
            print('                           DRAW!!!')
    else:
        #Variable for storing whether it is the first turn of the bot or not
        bot_1st_turn = True
        #Game loop
        while Remaining_Numbers != []:
            #Checking whether it the first turn of the bot
            if bot_1st_turn:
                #Choosing a random number to start the game to play
                Bot_number = random.choice(openings)
                #Placing the number in the Magic Square
                place_the_number(Bot_number, Bot_Square)
                #Inserting the number inserted in the list of elements selected by the user
                insert_in_sorted_list(Numbers_Selected_by_Bot, Bot_number)
                #Removing the number selected from the list of remaining numbers
                Remaining_Numbers.remove(Bot_number)
                #Displaying the number selected by bot
                print('Number selected by bot =', Bot_number)
                #Making the variable of bot's first turn False
                bot_1st_turn = False
            else:
                #Checking whether the bot is going to win.
                    is_going_to_win_Bot = is_going_to_win(Bot_Square, Remaining_Numbers)
                    if is_going_to_win_Bot:
                        #Placing the number in the bot Square
                        place_the_number(is_going_to_win_Bot, Bot_Square)
                        #Displaying the number selected by the bot
                        print('Number selected by bot =', is_going_to_win_Bot)
                        #Ending the game loop by displaying a loosing message to the user.
                        print('You are defeated by the bot!')
                        #Displaying the numbers with which the bot has won.
                        is_won_bot = is_won(Bot_Square)
                        print(f'{is_won_bot[0]} + {is_won_bot[1]} + {is_won_bot[2]} = 15')
                        #leaving the loop
                        break
                    #Checking whether the user is going to win.
                    is_going_to_win_User = is_going_to_win(User_Square, Remaining_Numbers)
                    if is_going_to_win_User:
                        #Placing the number in the bot Square
                        place_the_number(is_going_to_win_User, Bot_Square)
                        #Displaying the number selected by the bot
                        print('Number selected by bot =', is_going_to_win_User)
                        #Inserting the number inserted in the list of elements selected by the bot
                        insert_in_sorted_list(Numbers_Selected_by_Bot, is_going_to_win_User)
                        #Removing the number selected from the list of remaining numbers
                        Remaining_Numbers.remove(is_going_to_win_User)
                        #Checking if the bot has won by entering the number or not
                        is_won_bot = is_won(Bot_Square)
                        if is_won_bot:
                            print('You are defeated by the bot!')
                            #Displaying the numbers with which the bot has won.
                            is_won_bot = is_won(Bot_Square)
                            print(f'{is_won_bot[0]} + {is_won_bot[1]} + {is_won_bot[2]} = 15')
                            #leaving the game loop
                            break
                    #If both the bot and the user is not going to win.
                    else:
                        if 5 in Numbers_Selected_by_Bot:
                            if 6 in Numbers_Selected_by_Bot:
                                if (2 in Numbers_Selected_by_User or 1 in Numbers_Selected_by_User) and (8 in Remaining_Numbers):
                                    place_the_number(8, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 8')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(8)
                                elif (7 in Numbers_Selected_by_User or 8 in Numbers_Selected_by_User) and (2 in Remaining_Numbers):
                                    place_the_number(2, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 2')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(2)
                            elif 2 in Numbers_Selected_by_Bot:
                                if (9 in Numbers_Selected_by_User or 6 in Numbers_Selected_by_User) and (4 in Remaining_Numbers):
                                    place_the_number(4, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 4')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(4)
                                elif (7 in Numbers_Selected_by_User or 4 in Numbers_Selected_by_User) and (6 in Remaining_Numbers):
                                    place_the_number(6, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 6')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(6)
                            elif 4 in Numbers_Selected_by_Bot:
                                if (2 in Numbers_Selected_by_User or 3 in Numbers_Selected_by_User) and (8 in Remaining_Numbers):
                                    place_the_number(8, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 8')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(8)
                                elif (9 in Numbers_Selected_by_User or 8 in Numbers_Selected_by_User) and (2 in Remaining_Numbers):
                                    place_the_number(2, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 2')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(2)
                            elif 8 in Numbers_Selected_by_Bot:
                                if (6 in Numbers_Selected_by_User or 3 in Numbers_Selected_by_User) and (4 in Remaining_Numbers):
                                    place_the_number(4, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 4')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(4)
                                elif (1 in Numbers_Selected_by_User or 4 in Numbers_Selected_by_User) and (6 in Remaining_Numbers):
                                    place_the_number(6, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 6')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(6)
                            else:
                                if 6 in Numbers_Selected_by_User and 4 in Remaining_Numbers:
                                    place_the_number(4, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 4')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(4)
                                elif 4 in Numbers_Selected_by_User and 6 in Remaining_Numbers:
                                    place_the_number(6, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 6')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(6)
                                elif 2 in Numbers_Selected_by_User and 8 in Remaining_Numbers:
                                    place_the_number(8, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 8')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(8)
                                elif 8 in Numbers_Selected_by_User and 2 in Remaining_Numbers:
                                    place_the_number(2, Bot_Square)
                                    #Displaying the number selected by the bot
                                    print('Number selected by bot = 2')
                                    #Inserting the number inserted in the list of elements selected by the bot
                                    insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                    #Removing the number selected from the list of remaining numbers
                                    Remaining_Numbers.remove(2)
                                else:
                                    if {6,2,8,4}.issubset(Remaining_Numbers):
                                        bot_number = random.choice([6,2,8,4])
                                        place_the_number(bot_number, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print(f'Number selected by bot = {bot_number}')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(bot_number)
                                    else:
                                        bot_number = random.choice(Remaining_Numbers)
                                        place_the_number(bot_number, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print(f'Number selected by bot = {bot_number}')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(bot_number)
                        else:
                            if 5 in Remaining_Numbers:
                                place_the_number(5, Bot_Square)
                                #Displaying the number selected by the bot
                                print('Number selected by bot = 5')
                                #Inserting the number inserted in the list of elements selected by the bot
                                insert_in_sorted_list(Numbers_Selected_by_Bot, 5)
                                #Removing the number selected from the list of remaining numbers
                                Remaining_Numbers.remove(5)
                            else:
                                if 6 in Numbers_Selected_by_Bot:
                                    if 4 in Remaining_Numbers:
                                        place_the_number(4, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print('Number selected by bot = 4')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, 4)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(4)
                                elif 2 in Numbers_Selected_by_Bot:
                                    if 8 in Remaining_Numbers:
                                        place_the_number(8, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print('Number selected by bot = 8')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, 8)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(8)
                                elif 4 in Numbers_Selected_by_Bot:
                                    if 6 in Remaining_Numbers:
                                        place_the_number(6, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print('Number selected by bot = 6')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, 6)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(6)
                                elif 8 in Numbers_Selected_by_Bot:
                                    if 2 in Remaining_Numbers:
                                        place_the_number(2, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print('Number selected by bot = 2')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, 2)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(2)
                                else:
                                    if {6,2,8,4}.issubset(Remaining_Numbers):
                                        bot_number = random.choice([6,2,8,4])
                                        place_the_number(bot_number, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print(f'Number selected by bot = {bot_number}')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(bot_number)
                                    else:
                                        bot_number = random.choice(Remaining_Numbers)
                                        place_the_number(bot_number, Bot_Square)
                                        #Displaying the number selected by the bot
                                        print(f'Number selected by bot = {bot_number}')
                                        #Inserting the number inserted in the list of elements selected by the bot
                                        insert_in_sorted_list(Numbers_Selected_by_Bot, bot_number)
                                        #Removing the number selected from the list of remaining numbers
                                        Remaining_Numbers.remove(bot_number)
            #User's turn
            #Printing the numbers selected by user, bot and the remaining numbers
            print('Numbers selected by you = ', Numbers_Selected_by_User)
            print('Numbers selected by the bot = ', Numbers_Selected_by_Bot)
            print('Remaining numbers = ', Remaining_Numbers)
            #Asking the user which number he wants to select until
            #the number entered by the user is an integer and
            #the number entered by the user is between 1 to 9.
            number_entered = int(input('Enter your number : '))
            while number_entered not in range(1,10) or number_entered not in Remaining_Numbers:
                #If the number entered by the user is not an integer
                if type(number_entered) != int:
                    print('Your input is not a number between 1 to 9.')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
                #If the number entered by the user is not between 1 to 9
                elif number_entered not in range(1,10):
                    print('The number entered should be between 1 to 9')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
                #If number enterd by the user is not in remaining numbers
                elif number_entered not in Remaining_Numbers:
                    print('The number entered should be in remaining numbers. A number can not be selected twice.')
                    number_entered = int(input('Enter a number between 1 to 9 : '))
            else:
                #If the number fulfills all the above conditions,
                #Placing the number in the Magic Square
                place_the_number(number_entered, User_Square)
                #Inserting the number inserted in the list of elements selected by the user
                insert_in_sorted_list(Numbers_Selected_by_User, number_entered)
                #Removing the number selected from the list of remaining numbers
                Remaining_Numbers.remove(number_entered)
            #checking if the user has won the game or not
            is_won_user = is_won(User_Square)
            if is_won_user:
                #Ending the game loop by congratulating the player.
                print('Congratulations! You have won the game.') #Which is obviously not going to happen.
                #Displaying the winning numbers
                print('The required numbers which make you win are : ')
                print(f'{is_won_user[0]} + {is_won_user[1]} + {is_won_user[2]} = 15')
                break
        else:
            print('                         DRAW!!!')
#Printing the game description to the user.
print("""                                                    COUNT TO 15
Rules :-
1. You and your opponent have to choose any number between 1 to 9 one by one.
2. One whose sum of any numbers choosen becomes equal to 15 after choosing three or more numbers (not two), wins the game.
3. If both you and your opponent is not able to choose numbers such that
   whose sum is equal to 15, then it will be a draw
""")
condition = 'yes'
#game loop
while condition == 'yes':
    #This game loop will continue to iterate until the choice of the user is 'yes'.
    #The Game
    count_to_15()
    #The choice for playing the game again.
    condition = choice_for_playing_the_game_again()
