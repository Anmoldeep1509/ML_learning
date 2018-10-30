# Load libraries
# block 1
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
DEBUG = True

if DEBUG:
    print "Import Success!"

# block 2
# Load dataset
url = "C:\\Users\\Anmoldeep\\Documents\\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
if DEBUG:
    print "Data set load success!"

# block 3
#shape
print(dataset.head(20))
if(DEBUG):
    print "Dataset head print success !"
# descriptions
print(dataset.describe())
if(DEBUG):
    print "Dataset describe print success !"

#Class Distributions
print(dataset.groupby('class').size())
if(DEBUG):
    print "Dataset class group success !"

#box and whisker plots
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False)
plt.show()
if(DEBUG):
    print "Dataset plot success !"

#histograms
dataset.hist()
plt.show()
if(DEBUG):
    print "Dataset histogram success !"


