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

numar_simulari = 100000
numar_rosii = 0

for i in range(numar_simulari):
    rezultat = simulare()
    if rezultat == 'rosie':
        numar_rosii += 1

prob_estimata = numar_rosii / numar_simulari

print(f"Probabilitatea : {prob_estimata}")
