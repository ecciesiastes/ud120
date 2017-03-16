from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

learning_rate = 1
n_estimators = 22

clf = tree.DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
clf.fit(features_train, labels_train)

ada_real = AdaBoostClassifier(base_estimator=clf, learning_rate=learning_rate,
                              n_estimators=n_estimators, algorithm='SAMME.R')
ada_real.fit(features_train, labels_train)

pred = ada_real.predict(features_test)
acc = accuracy_score(labels_test, pred)
print(acc)