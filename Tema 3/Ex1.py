from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('Guest', 'Host'), ('Prize', 'Host')])

cpd_guest = TabularCPD(variable='Guest', variable_card=3, values=[[1/3], [1/3], [1/3]])
cpd_prize = TabularCPD(variable='Prize', variable_card=3, values=[[1/3], [1/3], [1/3]])

cpd_host = TabularCPD(
    variable='Host', variable_card=3,
    values=[
        [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
        [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
        [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]
    ],
    evidence=['Guest', 'Prize'],
    evidence_card=[3, 3]
)

model.add_cpds(cpd_guest, cpd_prize, cpd_host)
