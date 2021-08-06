import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(20,10)})

TRAIN_DATA = 'D:\\new begin\money\zhfintech\\train_v2.csv'
TEST_DATA1 = 'D:\\new begin\money\zhfintech\\test_v2_day.csv'
TEST_DATA2 = 'D:\\new begin\money\zhfintech\\test_v2_periods.csv'
HOLIDAY = 'D:\\new begin\money\zhfintech\\wkd_v1.csv'

holiday = pd.read_csv(HOLIDAY)
train = pd.read_csv(TRAIN_DATA)
test1 = pd.read_csv(TEST_DATA1)
test2 = pd.read_csv(TEST_DATA2)

train_A1 = train.loc[train.biz_type == 'A1']
train_A2 = train.loc[train.biz_type == 'A2']
train_A3 = train.loc[train.biz_type == 'A3']
train_A4 = train.loc[train.biz_type == 'A4']
train_A5 = train.loc[train.biz_type == 'A5']
train_A6 = train.loc[train.biz_type == 'A6']
train_A7 = train.loc[train.biz_type == 'A7']
train_A8 = train.loc[train.biz_type == 'A8']
train_A9 = train.loc[train.biz_type == 'A9']
train_A10 = train.loc[train.biz_type == 'A10']
train_A11 = train.loc[train.biz_type == 'A11']
train_A12 = train.loc[train.biz_type == 'A12']
train_A13 = train.loc[train.biz_type == 'A13']
train_B = train.loc[train.post_id == 'B']


train_A1_day = train_A1.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A2_day = train_A2.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A3_day = train_A3.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A4_day = train_A4.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A5_day = train_A5.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A6_day = train_A6.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A7_day = train_A7.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A8_day = train_A8.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A9_day = train_A9.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A10_day = train_A10.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A11_day = train_A11.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A12_day = train_A12.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_A13_day = train_A13.groupby(['date'], sort=False)['amount'].sum().to_frame()
train_B_day = train_B.groupby('date', sort=False)['amount'].sum().to_frame()

real_test = holiday[1065:1065+31]
real_test = pd.concat([real_test, pd.get_dummies(real_test['type'])], axis = 1)
real_test['year'] = pd.to_datetime(real_test.date).apply(lambda x: x.year).to_frame()-2018
real_test['month'] = pd.to_datetime(real_test.date).apply(lambda x: x.month).to_frame()
real_test['day'] = pd.to_datetime(real_test.date).apply(lambda x: x.day).to_frame()
real_test['step'] = real_test.index.to_frame()

res_a = model2.predict(m11)
res_b = model.predict(m11)
with open('res.txt', 'w') as f:
    f.write('date,post_id,amount\n')
    i = 1
    for a, b in zip(res_a, res_b):
        f.write('2020/12/'+str(i)+',A,'+str(int(a))+'\n')
        f.write('2020/12/'+str(i)+',B,'+str(int(b))+'\n')
        i += 1

m11 = pd.DataFrame({'NH':0}, index =range(1065,1096))
m11['SN'] = real_test['SN']
m11['SS'] = 0
m11['WN'] = real_test['WN']
m11['WS'] = 0
m11[['year', 'month', 'day','step']] = real_test[['year', 'month', 'day','step']]

plt.figure(figsize=(80,50))
plt.plot(train_A1_day[-305:])
plt.plot(train_A2_day[-305:])
plt.plot(train_A3_day[-305:])
plt.plot(train_A4_day[-305:])
plt.plot(train_A5_day[-305:])
plt.plot(train_A6_day[-305:])
plt.plot(train_A7_day[-305:])
plt.plot(train_A8_day[-305:])
plt.plot(train_A9_day[-305:])
plt.plot(train_A10_day[-305:])
plt.plot(train_A11_day[-305:])
plt.plot(train_A12_day[-305:])
plt.plot(train_A13_day[-305:])
plt.show()