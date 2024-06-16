# bet characteristics
MAX_LINES = 3
MIN_BET = 5
MAX_BET = 1_500
MAX_DEPOSIT = 1_000_000

# slot machine characteristics
ROWS = 3
COLS = 5
SYMBOLS = { 
    'watermelon':'wa',
    'strawberry':'st',
    'seven':'se',
    'cherry':'ch',
    'crown':'cr',
    'flower':'fl'
} #TODO replace the placeholders with gui refrences

if __name__ == '__main__':
    print(SYMBOLS.values())