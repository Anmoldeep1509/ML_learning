import importFiles
from importFiles import DEBUG
import pandas
# Load dataset
url = "C:\\Users\\Anmoldeep\\Documents\\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
if DEBUG:
    print "Data set load success!"