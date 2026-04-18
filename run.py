import MAFIA1

try:
    MAFIA1.main() 
except AttributeError:
    try:
        MAFIA1.menu()
    except:
        pass
      
