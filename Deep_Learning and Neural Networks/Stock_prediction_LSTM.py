
# Stock Prices Prediction Using Keras Long Term Short Memory

# Part 1 - Data Preprocessing

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the training set
dataset_train = pd.read_csv('NSE-TATAGLOBAL.csv')
training_set = dataset_train.iloc[:, 1:2].values

