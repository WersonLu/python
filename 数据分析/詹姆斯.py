#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/18 12:37
 
'''
# 詹姆斯生涯数据
import pandas as pd
import matplotlib.pyplot as plt
import numba as np

data = pd.read_csv('zms.csv')
# print(data.shape)  # (15, 30)
# print(data.describe()) 结果如截图

# 总得分
total_points = (data.PTS * data.G).sum()
# 平均得分
avg_points = total_points / data.G.sum()
print(total_points, avg_points)  # 29622.8 27.151970669110906

# 巅峰赛季
max_point = data.PTS.max()
# print(data[data.PTS == max_point])

#     Season  Age   Tm   Lg Pos   G  GS    MP    FG   FGA  ...     FT%  ORB  \
# 2  2005-06   21  CLE  NBA  SF  79  79  42.5  11.1  23.1  ...   0.738  0.9
#
#    DRB  TRB  AST  STL  BLK  TOV   PF   PTS
# 2  6.1  7.0  6.6  1.6  0.8  3.3  2.3  31.4

# 每项最强数据
max_data = {
    '得分': data.PTS.max(),
    '篮板': data.TRB.max(),
    '助攻': data.AST.max(),
    '抢断': data.STL.max(),
    '盖帽': data.BLK.max(),
    '失误': data.TOV.min(),
    '犯规': data.PF.min()
}
best_zms = pd.Series(max_data)
# print(best_zms)
# 助攻     9.1
# 失误     3.0
# 得分    31.4
# 抢断     2.2
# 犯规     1.4
# 盖帽     1.1
# 篮板     8.6

# 可视化

# x = pd.data_range('2003', '2017', freq='365D')
x=pd.date_range('2003', '2017', freq='365D')
y = data.PTS
plt.xlabel('session')
plt.ylabel('point')
plt.plot(x, y)
plt.show()
