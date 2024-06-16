from globals import SYMBOLS
import gui

class Symbol:
    def __init__(self, id) -> None:
        self.id = id
    
    def show_symbol(self):
        gui.show(SYMBOLS[id]) #TODO: implement show in gui.py

    def __eq__(self, Symbol: object) -> bool:
        if type(Symbol) == type(self):
            if Symbol.id == self.id:
                return True
        return False