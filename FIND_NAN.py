import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import requests
import re
import pandas as pd
pd.options.display.max_rows=999
pd.options.display.max_columns=999
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
from bs4 import BeautifulSoup

source_url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%8C%80%ED%86%B5%EB%A0%B9_%EC%A7%80%EC%A7%80%EC%9C%A8"
req = requests.get(source_url)
html = req.content
soup = BeautifulSoup(html,'lxml')
contents_table = soup.find(name = "table",attrs = {"class":"wikitable"})

table_body = contents_table.find(name = "tbody")
table_data = pd.DataFrame(table_body.text.replace("\n", " ").split("  "))
table_data = table_data.drop(table_data.index[0:300]).reset_index(drop=True)

#행열 수 보정을 위한 NaN(= 미조사) 값 추가.

table_data.loc[0.5] = ["미조사"]
table_data.loc[11.5] = ["미조사"]
table_data.loc[13.5] = ["미조사"]
table_data.loc[40] = ["미조사"]
table_data.sort_index(inplace=True)
data_table = []
def data_index(data):
    for idx in range(0,len(data)):
        if idx%3 ==0:
            k = data.values[idx:idx+3]
            data_table.append(k)
data_index(table_data)

data=str(table_data[0].values)
result=re.findall("미조사", data)
result.count("미조사")
print(result.count("미조사"))
