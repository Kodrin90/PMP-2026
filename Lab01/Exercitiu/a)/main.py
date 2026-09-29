import random

def simulare():
    zar = random.randint(1, 6)
    
    rosii = 3
    albastre = 4
    negre = 2
    
    if zar in [2, 3, 5]:  
        negre += 1
    elif zar == 6:       
        rosii += 1
    else:                
        albastre += 1
        
    urna = ['rosie'] * rosii + ['albastra'] * albastre + ['neagra'] * negre
    
    bila_extrasa = random.choice(urna)
    return bila_extrasa


print(simulare())
