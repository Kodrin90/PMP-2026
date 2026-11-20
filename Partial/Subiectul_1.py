import numpy as np
from hmmlearn.hmm import CategoricalHMM

emisii = np.array([
    [0.7, 0.2, 0.1],  
    [0.2, 0.6, 0.2],  
    [0.1, 0.3, 0.6], 
    [0.5, 0.2, 0.3],  
])

secventa_obs = np.array([[0], [1], [2], [2], [0]])

tranz_a = np.array([
    [0.2, 0.4, 0.0, 0.4],
    [0.4, 0.2, 0.4, 0.0],
    [0.0, 0.4, 0.2, 0.4],
    [0.4, 0.0, 0.4, 0.2],
])

tranz_b = np.array([
    [0.0, 0.5, 0.0, 0.5],
    [0.5, 0.0, 0.5, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.5, 0.0, 0.5, 0.0],
])

for p, A in [("a", tranz_a), ("b", tranz_b)]:
    hmm = CategoricalHMM(n_components=4)
    hmm.startprob_ = np.array([0.25, 0.25, 0.25, 0.25])
    hmm.transmat_ = A
    hmm.emissionprob_ = emisii

    log_prob, camere = hmm.decode(secventa_obs, algorithm="viterbi")
    traseu = [int(c) + 1 for c in camere]
    prob = np.exp(log_prob)

    print(f"({p}) camere: {traseu}, prob comuna: {prob:.10f}")

    
    # (a) secventa: [1, 2, 3, 4, 1] probabilitate: 0.000338688
    # (b) secventa: [1, 2, 3, 4, 1] probabilitate: 0.0008268749999999998
    # Comparatia rezultatelor:
    # Secventa ramane identica ([1, 2, 3, 4, 1])
    # Probabilitatea creste semnificativ la b)
