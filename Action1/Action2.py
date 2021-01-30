# 统计全班5名同学成绩：三科中的平均成绩、最小成绩、最大成绩、方差、标准差，然后把总成绩排序，得出名次进行成绩输出。

import pandas as pd

# 录入成绩
data = {'语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'])
print(df1)

# 求三科中的平均成绩、最小成绩、最大成绩、方差、标准差

print(df1.describe())
print(df1.var())

# 把总成绩排序，得出名次进行成绩输出。
# 先算出总成绩

i = df1.index.values.tolist()
# print(i)
s=[]
for ii in i:
    s.append(df1.loc[ii].sum())
df1['总成绩'] = s
# print(df1)

#排序输出
df2 = df1.sort_values(by=['总成绩'],ascending=False)
print(df2)
