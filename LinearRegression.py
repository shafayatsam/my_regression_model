import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def make_prediction(marks):
    df_train = pd.read_csv("train.csv").dropna()

    x_train = np.array(df_train['x'], dtype=np.float64).reshape((-1, 1))
    y_train = np.array(df_train['y'], dtype=np.float64)

    model = LinearRegression()
    model.fit(x_train, y_train)

    x_test = np.array(marks, dtype=np.float64).reshape((-1, 1))

    return model.predict(x_test)
