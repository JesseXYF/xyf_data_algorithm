# 导包
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB

# 读入原始数据
f = open('result/ft_zip2018_non_day1.pkl', 'rb')
data = pickle.load(f)
# print(data[0])
# print(data[1])
# print(len(data[0]))

# 将数据格式从np.ndarray转化成pd.DataFrame方便调用机器学习库
data_frame = pd.DataFrame(data)
# print(data_frame[0:2])

# 用cross_validtion将数据划分为训练集和测试集
X = data_frame.iloc[0:, 0:-1]
y = data_frame.iloc[0:, -1]
# print(X.shape)
# print(y.shape)
# train_test_split随机划分训练集和测试集[交叉验证]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)


# 得出svm的accuracy
def svm_score(x_train, x_test, y_train, y_test):
    # 初始化支持向量机分类器
    lsvc = LinearSVC()
    lsvc.fit(x_train, y_train)
    score = lsvc.score(x_test, y_test)
    return score


# 得出rf的accuracy
def rf_score(x_train, x_test, y_train, y_test):
    fr = RandomForestClassifier()
    fr.fit(x_train, y_train)
    score = fr.score(x_test, y_test)
    return score


# 得出dt的accuracy
def dt_score(x_train, x_test, y_train, y_test):
    dt = DecisionTreeClassifier()
    dt.fit(x_train, y_train)
    score = dt.score(x_test, y_test)
    return score


# 得出gb的accuracy(梯度提升决策树)
def gb_score(x_train, x_test, y_train, y_test):
    gb = GradientBoostingClassifier()
    gb.fit(x_train, y_train)
    score = gb.score(x_test, y_test)
    return score


# 得出bn的accuracy
def bn_score(x_train, x_test, y_train, y_test):
    bn = MultinomialNB()
    bn.fit(x_train, y_train)
    score = bn.score(x_test, y_test)
    return score


# 得出nn的accuracy
def nn_score(x_train, x_test, y_train, y_test):
    pass


print("svm_score= " + str(svm_score(x_train, x_test, y_train, y_test)))
print("rf_score= " + str(rf_score(x_train, x_test, y_train, y_test)))
print("dt_score= " + str(dt_score(x_train, x_test, y_train, y_test)))
print("bn_score= " + str(bn_score(x_train, x_test, y_train, y_test)))
