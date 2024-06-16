# bet characteristics
MAX_LINES = 3
MIN_BET = 5
MAX_BET = 1_500
MAX_DEPOSIT = 1_000_000

# slot machine characteristics
ROWS = 3
COLS = 5
SYMBOLS = ['⓻', '⓺', '💎', '👑', '💲',  '🌼', '🌸', '🍀', '🍒', '🍓', '🍉', '💖', '⭐', '💣']

def get_number_of_lines():
    while True:
        lines = input(f"select lines to bet (1 - {MAX_LINES}): ")
        
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES :
                break
            else:
                print(f"you can bet only on1 1 - {MAX_LINES} lines")
                continue
        else:
            print("please enter a positive whole number")
            continue
    return lines


def get_bet():
    while True:
        bet = input(f"enter your bet on each line $")
        
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET :
                break
            else:
                print(f"you can't bet less than ${MIN_BET} or more than ${MAX_BET}")
                continue
        else:
            print("please enter a positive whole number")
            continue
    return bet


def place_bet(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    while total_bet > balance:
        print(f"your balance is too low for that bet | balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

    balance -= total_bet
    return balance, f"bet succesfully palced\nplaced ${bet} | on {lines} lines | total bet ${total_bet}"


def main():
    print()



if __name__ == "__main__":
    main()