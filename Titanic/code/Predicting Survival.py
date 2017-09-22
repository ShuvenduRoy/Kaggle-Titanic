import warnings
warnings.filterwarnings('ignore')

# Handling table like data and matrices
import numpy as np
import pandas as pd

# Modeling algorithm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier

# Modelling Helpers
from sklearn.preprocessing import Imputer , Normalizer , scale
from sklearn.model_selection import train_test_split , StratifiedKFold
from sklearn.feature_selection import RFECV

# Visualisation
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

mpl.style.use( 'ggplot' )
sns.set_style( 'white' )
pylab.rcParams[ 'figure.figsize' ] = 8 , 6




"""Helpepr functions"""
def plot_correlation_map(df, cat, target, **kwargs):
    pass



# Loading data
train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")

full = train.append(test, ignore_index = True)
titanic=full[:891]
del train, test



"""Statistical symmaries and viasualisations"""
# Show first few rows of data
titanic.head()

# show statistical summary
titanic.describe()