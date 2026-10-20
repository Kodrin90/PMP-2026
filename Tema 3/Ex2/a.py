from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('B', 'T'), ('B', 'X'), ('B', 'D'), ('T', 'D')])

cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.9], [0.1]]) 

cpd_T = TabularCPD(variable='T', variable_card=2, 
                   values=[[0.7, 0.2],  
                           [0.3, 0.8]], 
                   evidence=['B'], evidence_card=[2])

cpd_X = TabularCPD(variable='X', variable_card=2, 
                   values=[[0.9, 0.1],
                           [0.1, 0.9]], 
                   evidence=['B'], evidence_card=[2])

cpd_D = TabularCPD(variable='D', variable_card=2,
                   values=[[0.9, 0.5, 0.6, 0.1],  
                           [0.1, 0.5, 0.4, 0.9]], 
                   evidence=['B', 'T'], evidence_card=[2, 2])

model.add_cpds(cpd_B, cpd_T, cpd_X, cpd_D)
