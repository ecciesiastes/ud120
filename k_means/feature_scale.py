

###原值为 200,000 的“salary”特征在尺度变换后的值会是什么，
### 以及原值为 100 万美元的“exercised_stock_options”特征在尺度变换后的值会是什么？


import pickle
import numpy
import sys


sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


feature_1 = "salary"
feature_2 = "exercised_stock_options"
features_list = [feature_1, feature_2]
data = featureFormat(data_dict, features_list)


def maxmin(item):
    min = sys.float_info[0]
    max = 0
    for data in data_dict:
        value = data_dict[data][item]
        if value != 'Nan':
            num = float(value)
            if num < min:
                min = num
            if num > max:
                max = num
    return max, min



max_s, min_s = maxmin('salary')
print((200000. - min_s) / (max_s - min_s))

max_s, min_s = maxmin('exercised_stock_options')
print((1000000. - min_s) / (max_s - min_s))
