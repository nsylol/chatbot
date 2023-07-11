from .menu import SetupMenu
from .Game import setup_Game

def SetupHandlers(dp):
    SetupMenu(dp)
    setup_Game(dp)