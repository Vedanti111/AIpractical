import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Define the structure of the Bayesian network
model = BayesianNetwork([('Pollution', 'Cancer'), ('Smoker', 'Cancer'), ('Cancer', 'Xray'), ('Cancer', 'Dyspnoea')])

# Define the conditional probability distributions (CPDs) for each node
cpd_pollution = TabularCPD(variable='Pollution', variable_card=3, values=[[0.1], [0.3], [0.6]])
cpd_smoker = TabularCPD(variable='Smoker', variable_card=2, values=[[0.2], [0.8]])
cpd_cancer = TabularCPD(variable='Cancer', variable_card=2,
                        values=[[0.7, 0.3, 0.6, 0.4, 0.1, 0.9], [0.3, 0.7, 0.4, 0.6, 0.9, 0.1]],
                        evidence=['Pollution', 'Smoker'], evidence_card=[3, 2])
cpd_xray = TabularCPD(variable='Xray', variable_card=2, values=[[0.8, 0.3], [0.2, 0.7]], evidence=['Cancer'], evidence_card=[2])
cpd_dyspnoea = TabularCPD(variable='Dyspnoea', variable_card=2, values=[[0.7, 0.2], [0.3, 0.8]], evidence=['Cancer'], evidence_card=[2])

# Add the CPDs to the model
model.add_cpds(cpd_pollution, cpd_smoker, cpd_cancer, cpd_xray, cpd_dyspnoea)

# Check the model for consistency
model.check_model()

# Display CPDs in tabular form
print("CPD for Pollution:")
print(cpd_pollution)
print("\nCPD for Smoker:")
print(cpd_smoker)
print("\nCPD for Cancer:")
print(cpd_cancer)
print("\nCPD for Xray:")
print(cpd_xray)
print("\nCPD for Dyspnoea:")
print(cpd_dyspnoea)
