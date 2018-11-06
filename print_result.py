import pickle

f = open('result/ft_zip2018.pkl', 'rb')
info = pickle.load(f)
print(info)  # show file
# print(list(info).index("vital1"))
# print(list(info).index("vital402"))
# print(len(info))
