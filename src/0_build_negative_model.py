import numpy as np
import pandas as pd

from read_data import read_data
from evaluate_model import evaluate_model, print_evaluation

df = read_data()
print(df.head())

actuals = df["HEQ010"]
predictions = np.zeros_like(actuals)

print_evaluation(evaluate_model(actuals, predictions))
