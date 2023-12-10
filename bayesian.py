from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Define the structure of the Bayesian Network
model = BayesianNetwork([('Pollution', 'Cancer'), ('Smoker', 'Cancer'), ('Cancer', 'Xray'), ('Cancer', 'Dyspnoea')])

# Creating a sample dataset
data = pd.DataFrame(data={
    'Pollution': [0, 1, 1, 2, 2, 0, 1, 2, 0, 2],
    'Smoker': [0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    'Cancer': [0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    'Xray': [0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    'Dyspnoea': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
})

# Learning CPD using Maximum Likelihood Estimators
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Inferencing with Bayesian Network
infer = VariableElimination(model)

# 1. Probability of Cancer given evidence of Dyspnoea
q1 = infer.query(variables=['Cancer'], evidence={'Dyspnoea': 1})
print(q1)

# 2. Probability of Xray given evidence of Pollution
q2 = infer.query(variables=['Xray'], evidence={'Pollution': 2})
print(q2)

