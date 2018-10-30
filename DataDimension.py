from loadDataset import dataset
from loadDataset import DEBUG
#shape
print(dataset.head(20))
if(DEBUG):
    print "Dataset head print success !"
# descriptions
print(dataset.describe())

#Class Distributions
print(dataset.groupby('class').size())

