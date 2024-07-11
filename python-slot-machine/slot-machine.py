import random #To generate random numbers

MAX_LINES = 5 #global constant
MAX_BET = 1000
MIN_BET = 10

def get_slot_machine_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        columns = []
        current_symbols = all_symbols
        for row in range(rows):
            value = random.choice(all_symbols)


def deposit(): #function
    while True:
        amount = input("What would you like to deposit? Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("amount must be greater than 0")
        else:
            print("Type a number.")
            
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 < lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Type a number.")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs{MIN_BET} - Rs{MAX_BET}.")
        else:
            print("Type a number.")

    return amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
          print(f"You do not have enough to bet that amount. Your current balance is Rs.{balance}")
      else:
          break

    print(f"You are betting Rs.{bet} on {lines} lines. Your total bet is equal to {total_bet}.")

main()