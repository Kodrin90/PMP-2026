import random

def simuleaza_joc():
    start = random.choice([0, 1])
    n = random.randint(1, 6)
    
    if start == 0:
        m = sum(1 for _ in range(2 * n) if random.random() < 4/7)
        return 'J0' if n >= m else 'J1'
    else:
        m = sum(1 for _ in range(2 * n) if random.random() < 1/2)
        return 'J1' if n >= m else 'J0'

victorii_J0 = 0
victorii_J1 = 0

for _ in range(10000):
    castigator = simuleaza_joc()
    if castigator == 'J0':
        victorii_J0 += 1
    else:
        victorii_J1 += 1

print(f"J0: {victorii_J0}, J1: {victorii_J1}")
