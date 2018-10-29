from loadDataset import dataset
#shape
print(dataset.head(20))
if(DEBUG):
    print "Dataset head print success !"
# descriptions
print(dataset.describe())