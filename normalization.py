# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
import pandas
import numpy

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv("../Desktop/datasci/Final/Data Preprocessing/diabetes.csv")
array = dataframe.values

# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(normalizedX[0:6,:])