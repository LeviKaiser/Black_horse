# 对汽车质量数据进行统计，对数据进行探索：品牌投诉总数，车型投诉总数，哪个品牌的平均车型投诉最多
# 数据集：car_complain.csv

import pandas as pd
# Step1，数据加载
df = pd.read_csv('../car_data_analyze/car_complain.csv')

# Step2，数据预处理
# 将问题列拆分降为，便于统计
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))

# 数据清洗
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x

df['brand'] = df['brand'].apply(f)

# Step3，数据统计

# 品牌投诉总数
result1 = df.groupby(['brand'])['id'].agg(['count'])
result1 = result1.sort_values(by=['count'], ascending=False)
print(result1)

# 车型投诉总数
result2 = df.groupby(['car_model'])['id'].agg(['count'])
result2 = result2.sort_values(by=['count'], ascending=False)
print(result2)

# 哪个品牌的平均车型投诉最多
result3 = df.groupby(['brand', 'car_model'])['id'].agg(['count'])
result3 = result3.groupby(['brand'])['count'].agg('mean')
result3 = pd.DataFrame(result3)
result3 = result3.sort_values(by=['count'], ascending=False)
print(result3)