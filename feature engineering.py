# 卡方检验

import numpy as np
import pandas as pd
from scipy import special

# X为输入，是一个feature的样本情况，左边{}为label=0的样本，右边{}为label=1的样本
X = [{1 : 50, 2 : 30, 5 : 60, 7 : 20, 13 : 10}, {1 : 20, 2 : 10, 7 : 10, 13 : 50}]
# X = pd.DataFrame([label0.values(), label1.values()], columns = label0.keys())
X = pd.DataFrame(X)
X = X.fillna(0)
observed = np.array(X)
feature_count = observed.sum(axis = 0).reshape(1, -1)
label_count = observed.sum(axis = 1)
label_percent = np.true_divide(label_count, sum(label_count)).reshape(-1, 1)
expected = np.dot(label_percent, feature_count)
chi2 = np.true_divide((observed - expected)**2, expected).sum(axis = 1).sum(axis = 0)
F = len(observed[0]) - 1
p_score = special.chdtrc(F, chi2)
print(p_score)

# 互信息

X = [{1 : 50, 2 : 30, 5 : 60, 7 : 20, 13 : 10}, {1 : 20, 2 : 10, 7 : 10, 13 : 50}]
X = pd.DataFrame(X)
# 缺失值补0
X = X.fillna(0)
X = np.array(X)

label0SampleNumbers = sum(X[0])
label1SampleNumbers = sum(X[1])
sampleNumbers = label0SampleNumbers + label1SampleNumbers

array0 = X[0]
array1 = X[1]

label1_everyFeatureValue_prob = np.true_divide(array1, sampleNumbers)
label0_everyFeatureValue_prob = np.true_divide(array0, sampleNumbers)

everyFeatureValue_prob = np.true_divide((array0 + array1), sampleNumbers)
label1_prob = np.true_divide(label1SampleNumbers, sampleNumbers)
label0_prob = np.true_divide(label0SampleNumbers, sampleNumbers)

# 对于label为1：
temp = np.true_divide(np.true_divide(label1_everyFeatureValue_prob, everyFeatureValue_prob), label1_prob)
temp = np.where(temp != 0, np.log2(temp), 0)
temp *= label1_everyFeatureValue_prob
I_label1 = sum(temp)
# print('I_label1:', I_label1)

# 对于label为0：
temp = np.true_divide(np.true_divide(label0_everyFeatureValue_prob, everyFeatureValue_prob), label0_prob)
temp = np.where(temp != 0, np.log2(temp), 0)
temp *= label0_everyFeatureValue_prob
I_label0 = sum(temp)
# print('I_label0:', I_label0)

I = I_label1 + I_label0
print(I)

import numpy as np
import pandas as pd
import xgboost as xgb
import operator
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectFromModel

# 数据预处理
train = pd.read_csv("/home/aistudio/data/data98852/train-winequality-white.csv")
# train = pd.DataFrame(train)
y = train['quality']
X = train.drop(['quality'], 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

# 训练参数
model = XGBClassifier(learning_rate=1,
                    n_estimators=1,         # 树的个数--1000棵树建立xgboost
                    max_depth=3,               # 树的深度
                    min_child_weight = 1,      # 叶子节点最小权重
                    gamma=0.2,                  # 惩罚项中叶子结点个数前的参数
                    subsample=0.8,             # 随机选择80%样本建立决策树
                    colsample_btree=0.8,       # 随机选择80%特征建立决策树
                    objective='multi:softmax', # 指定损失函数
                    num_class=7,
                    scale_pos_weight=1,        # 解决样本个数不平衡的问题
                    random_state=27            # 随机数
                    )

# 模型训练
model.fit(X_train,
          y_train,
        #   eval_set = [(x_test,y_test)],
          eval_metric = "mlogloss",
        #   early_stopping_rounds = 3,
        #   verbose = True
          )

# 当前模型下测试集精确度
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

# 绘制特征重要性排序直方图
fig,ax = plt.subplots(figsize=(15,15))
plot_importance(model, height=0.5, ax=ax, max_num_features=64)
plt.show()

# 不同importance_type取值情况下，特征重要性打分情况
# print('weight:', model.get_booster().get_score(importance_type='weight'))
# print('gain:', model.get_booster().get_score(importance_type='gain'))
# print('cover:', model.get_booster().get_score(importance_type='cover'))

# 不同重要性阈值设置的情况下，结果准确率
thresholds = sorted(model.feature_importances_)
for thresh in thresholds:
 # select features using threshold
 selection = SelectFromModel(model, threshold=thresh, prefit=True)
 select_X_train = selection.transform(X_train)
 # train model
model = XGBClassifier(learning_rate=1,
                    n_estimators=1,         # 树的个数--1000棵树建立xgboost
                    max_depth=3,               # 树的深度
                    min_child_weight = 1,      # 叶子节点最小权重
                    gamma=0.2,                  # 惩罚项中叶子结点个数前的参数
                    subsample=0.8,             # 随机选择80%样本建立决策树
                    colsample_btree=0.8,       # 随机选择80%特征建立决策树
                    objective='multi:softmax', # 指定损失函数
                    num_class=7,
                    scale_pos_weight=1,        # 解决样本个数不平衡的问题
                    random_state=27            # 随机数
                    )
model.fit(select_X_train, y_train)
# eval model
select_X_test = selection.transform(X_test)
y_pred = model.predict(select_X_test)
predictions = [round(value) for value in y_pred]
accuracy = accuracy_score(y_test, predictions)
print("Thresh=%.3f, n=%d, Accuracy: %.2f%%" % (thresh, select_X_train.shape[1], accuracy*100.0))