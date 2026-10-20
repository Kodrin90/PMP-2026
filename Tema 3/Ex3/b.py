import numpy as np
from scipy.stats import binom

model_joc = BayesianNetwork([('S', 'M'), ('N', 'M')])

cpd_S = TabularCPD(variable='S', variable_card=2, values=[[0.5], [0.5]])

cpd_N = TabularCPD(variable='N', variable_card=6, 
                   values=[[1/6], [1/6], [1/6], [1/6], [1/6], [1/6]])

m_values = []
for m in range(13):
    row = []
    for s in [0, 1]:
        for n_idx in range(6):
            n = n_idx + 1
            if m > 2 * n:
                prob = 0
            else:
                p_stema = 4/7 if s == 0 else 1/2
                prob = binom.pmf(m, 2 * n, p_stema)
            row.append(prob)
    m_values.append(row)

cpd_M = TabularCPD(variable='M', variable_card=13, values=m_values,
                   evidence=['S', 'N'], evidence_card=[2, 6])

model_joc.add_cpds(cpd_S, cpd_N, cpd_M)
