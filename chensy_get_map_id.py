import pandas as pd

# 读取excel文件
# data = pd.read_csv("feature_dict_BDAI_20181103(2).xlsx")
# pirnt(data)
'''将DataFrame转成字典，这种实现方法不好，放弃
#print(data)
data = data.loc[55:,['F_ID','VAR_IDX']]
data.set_index('VAR_IDX',drop=True,inplace=True)
dictionary = data.to_dict(orient='index')
print(data)
lab = 'AKI_label'
print(data.loc[lab].values[0])

print(dictionary)
print(dictionary['lab1']['F_ID'])
lab = 'lab2'
print(dictionary[lab]['F_ID'])
print(dictionary['days']['F_ID'])
'''
data = pd.read_excel("D:/Pydataproject/xyf_data_algorithm/Raw_Data/feature_dict_BDAI_20181103.xlsx", sheetname=0)
data1 = data.loc[:54, ['F_ID', 'VAR_IDX', 'VALUESET_ITEM']]
data1.set_index(['VAR_IDX', 'VALUESET_ITEM'], drop=True, inplace=True)
# print(data1)
# temp = data1.loc['demo4',"'A'"].values[0]
data2 = data.loc[55:, ['F_ID', 'VAR_IDX']]
data2.set_index('VAR_IDX', drop=True, inplace=True)
print(data2)


def map_demo_vitals(location1, location2):
    location2 = "'" + location2 + "'"
    return data1.loc[location1, location2].values[0]


def map_lab_css_px_med_days_AKI_label(location):
    return data2.loc[location].values[0]


print("--------------------------------------------")
print(map_lab_css_px_med_days_AKI_label('med9997'))
print(map_demo_vitals('vital8', 'BP_DIASTOLIC'))
