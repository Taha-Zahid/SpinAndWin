# Welcome to the Slot Machine Game!

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# The more rare the symbol ==> The bigger the multiplier is
# A (2 of them) is the most rare, D (8 of them) is the least rare
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines= []
    for line in range(lines):  # Checking all lines the user is betting on
        symbol = columns[0][line] # Checking the symmbol in the first column of the row
        for column in columns:    # Looping through every column to check for that symbol mentioned above
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # If the symbol in one column is not equal to the others in the row --> 
                break                     # break and check the next line
        else:
            winnings += values[symbol] * bet  # Multiplier of each symbol * their bet on the line
            winning_lines.append(line + 1) # The lines the winner has won on

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Getting the symbols and symbol amounts from the symbol dictionarie
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # Counting through symbol amounts
            all_symbols.append(symbol) # Adding one or more symbol amounts of the symbol into the List

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # Copying all_symbols into a new object
        for _ in range(rows):
            value = random.choice(current_symbols) # Choosing a random value from the Symbols list
            current_symbols.remove(value)  # This then removes the random value that is chosen
            column.append(value) # Adds the random value into the column

        columns.append(column)

    return columns
        
# This function transposes our array
def print_slot_machine(columns):
    for row in range(len(columns[0])): # Iterates over the each row
        for i, column in enumerate(columns): # Iterating over columns and providing the index and as well as the item
            if i != len(columns) -1: # Checking for the last column
                print(column[row], end=" | ") # Prints this if it's not the last item
            else:
                print(column[row], end="") # Prints this if it's the last item
        
        print()
            



# This function gets the total amount the user would like to use for the Slot Machine
def deposit():
    # User will keep entering an amount until there is a value, hence we have a while loop
    while True:
        amount = input("How much would you like to deposit today? $")
        if amount.isdigit(): # Checking if we have a digit returned
            amount = int(amount) # Converting number into an integer
            if amount > 0:
                break  # If amount is valid, we then break
            else:
                print("Amount has to be greater than 0!")
        else:
            print("Please enter a valid number.")       

    return amount        

# This function gets the number of lines the user would like to bet on
def get_number_of_line():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") # Converted MAX_LINES to a str
        if lines.isdigit(): 
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES:   # Checking the correct bounds for value entered ('lines')
                break  
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")       

    return lines     

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break  
            else:
                print(f"Amount has to be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")       

    return amount    

def spin(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        # Checking if the user has sufficient funds to bet by checking total_bet and user balance
        if total_bet > balance:
            print(f"You do not have enough to bet that amount! Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots) # Printing the "slot" values in our slot machine function
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines) # Using the splat operator to split the number of lines won when printed
    return winnings - total_bet


def main():

    print("🎰 Welcome to the Slot Machine Game!")
    print("Place your deposit, choose your lines, and spin the reels to see if luck is on your side!")

    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Thank you for playing!")
    print(f"You left with ${balance}")
    


main()


