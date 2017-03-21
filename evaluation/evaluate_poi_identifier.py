#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn.model_selection import train_test_split

feature_train, feature_test, label_train, label_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(feature_train, label_train)
pred = clf.predict(feature_test)


from sklearn.metrics import confusion_matrix

num = 0
for p in label_test:
    if p == 1.0:
        num += 1

print(num)

print(len(feature_test))
print(confusion_matrix(label_test, pred))

